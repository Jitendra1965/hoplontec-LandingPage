"""Validate bilingual feedback packaging without sending any email or request."""
from html.parser import HTMLParser
import json
from pathlib import Path
import runpy
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
configure = runpy.run_path(str(ROOT / 'scripts/configure-feedback.py'))['configure']

class Tags(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.tags = []; self.feed(text)
    def handle_starttag(self, name, attributes):
        self.tags.append((name, dict(attributes)))
    def find(self, tag, **attrs):
        return [item for name, item in self.tags if name == tag and all(item.get(k) == v for k,v in attrs.items())]

class FeedbackTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.site = self.root / 'site'; self.site.mkdir()
        for name in ('nivilog-feedback.html','nivilog-feedback-es.html','contact.html','careers.html'):
            shutil.copyfile(ROOT / name, self.site / name)
    def config(self, value):
        (self.root / 'feedback-config.json').write_text(json.dumps({'formId': value}))
        configure(self.site, self.root)
    def test_blank_id_cannot_send(self):
        self.config('')
        for name in ('nivilog-feedback.html','nivilog-feedback-es.html'):
            tags=Tags((self.site/name).read_text())
            self.assertEqual(tags.find('form')[0]['action'],'')
            self.assertIn('disabled',tags.find('fieldset',id='feedback-fields')[0])
    def test_opaque_id_enables_both_languages_and_replaces_other_form_destinations(self):
        self.config('testOnlyOpaqueId123456789')
        for name in ('nivilog-feedback.html','nivilog-feedback-es.html','contact.html','careers.html'):
            tags=Tags((self.site/name).read_text())
            self.assertEqual(tags.find('form')[0]['action'],'https://formsubmit.co/testOnlyOpaqueId123456789')
        for name in ('nivilog-feedback.html','nivilog-feedback-es.html'):
            self.assertNotIn('disabled',Tags((self.site/name).read_text()).find('fieldset',id='feedback-fields')[0])
    def test_email_and_url_configuration_rejected(self):
        for value in ('person@example.com','https://formsubmit.co/identifier','too-short',123):
            with self.assertRaises(ValueError): self.config(value)
    def test_data_minimization_native_validation_and_locale_parity(self):
        allowed={'satisfaction','topic','comment','language','product','reference','_url','_subject','_template','_next','_honey'}
        options=[]
        for language,name in [('en','nivilog-feedback.html'),('es','nivilog-feedback-es.html')]:
            text=(ROOT/name).read_text(); tags=Tags(text)
            self.assertEqual(tags.find('html')[0]['lang'],language)
            fields=[item for tag,item in tags.tags if tag in ('input','textarea','select')]
            self.assertEqual({item['name'] for item in fields},allowed)
            self.assertEqual({x['value'] for x in tags.find('input',type='radio')},{'1','2','3','4','5'})
            self.assertTrue(all('required' in x for x in tags.find('input',type='radio')))
            self.assertEqual(tags.find('textarea')[0]['maxlength'],'1000')
            self.assertEqual(tags.find('input',name='language')[0]['value'],language)
            self.assertFalse(tags.find('input',type='email'))
            self.assertFalse(tags.find('input',type='file'))
            self.assertNotIn('googletagmanager',text);self.assertNotIn('mailto:',text)
            self.assertTrue(all(not x.get('src','').startswith('http') for x in tags.find('script')))
            options.append([x.get('value') for x in tags.find('option')])
        self.assertEqual(*options)
    def test_formsubmit_receives_fixed_source_url_without_browser_referrer(self):
        self.config('testOnlyOpaqueId123456789')
        for suffix in ('', '-es'):
            name = f'nivilog-feedback{suffix}.html'
            tags = Tags((self.site / name).read_text())
            self.assertEqual(tags.find('meta', name='referrer')[0]['content'], 'no-referrer')
            self.assertEqual(tags.find('input', name='_url')[0]['value'],
                             f'https://hoplontec.io/{name}')
            self.assertEqual(tags.find('input', name='_url')[0]['type'], 'hidden')
            self.assertEqual(tags.find('form')[0]['method'].upper(), 'POST')

    def test_local_links_and_privacy_languages_exist(self):
        for name in ROOT.glob('nivilog-feedback*.html'):
            for tag,attrs in Tags(name.read_text()).tags:
                url=attrs.get('href',attrs.get('src',''))
                if url and not url.startswith(('http','#','data:')):
                    self.assertTrue((ROOT/url.split('?')[0]).exists(),(name,url))
        for suffix,language in [('', 'en'),('-es','es')]:
            text=(ROOT/f'nivilog-privacy{suffix}.html').read_text()
            self.assertEqual(Tags(text).find('html')[0]['lang'],language)
            self.assertIn('FormSubmit',text)
            self.assertNotIn('{{',text)

if __name__=='__main__': unittest.main()
