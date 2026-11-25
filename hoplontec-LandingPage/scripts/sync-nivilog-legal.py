"""Render the app's English/Spanish legal sources as offline-readable site pages.

Run manually with the NiviLog assets/legal directory after a policy update.
No receiving email is published: the public privacy contact is the contact form.
"""
from pathlib import Path
from html import escape
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
PRIVACY_VERSION = '2026-11-25.5'
TERMS_VERSION = '2026-11-25.2'


def inline(text):
    """Render the limited Markdown used by reviewed legal sources, escaping HTML."""
    text = escape(text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', r'<a href="\2">\1</a>', text)
    return re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)


def markdown(text):
    """Convert headings, paragraphs and simple bullet lists without remote code."""
    result, paragraph, bullets = [], [], []
    def flush():
        if paragraph:
            result.append('<p>' + inline(' '.join(paragraph)) + '</p>')
            paragraph.clear()
        if bullets:
            result.append('<ul>' + ''.join('<li>' + inline(item) + '</li>' for item in bullets) + '</ul>')
            bullets.clear()
    for line in text.splitlines():
        if not line.strip():
            flush()
        elif line.startswith('#'):
            flush()
            level = min(3, len(line) - len(line.lstrip('#')))
            result.append(f'<h{level}>' + inline(line[level:].strip()) + f'</h{level}>')
        elif line.startswith('- '):
            if paragraph: flush()
            bullets.append(line[2:])
        else:
            if bullets: flush()
            paragraph.append(line)
    flush()
    return '\n'.join(result)


def sync(source):
    """Publish current facts in both languages with the same applicability notice as the app."""
    for language in ('en', 'es'):
        es = language == 'es'
        suffix = '-es' if es else ''
        for kind in ('privacy', 'terms'):
            filename = 'privacy-policy.md' if kind == 'privacy' else 'terms-of-use.md'
            body = (source / ('es' if es else '') / filename).read_text()
            values = {
                'PUBLISHER': 'Hoplontec Inc', 'ADDRESS': '1111B S Governors Ave #87194, Dover, DE 19904, USA',
                'CONTACT': '[Formulario de contacto](https://hoplontec.io/contact.html)' if es else '[Contact form](https://hoplontec.io/contact.html)',
                'POLICY_LINK': f'[hoplontec.io](https://hoplontec.io/nivilog-privacy{suffix}.html)',
                'PRIVACY_REFERENCE': f'https://hoplontec.io/nivilog-privacy{suffix}.html',
                'PRIVACY_VERSION': PRIVACY_VERSION, 'TERMS_VERSION': TERMS_VERSION,
                'PUBLICATION_STATUS': 'Esta versión se aplica cuando la aceptas en NiviLog.' if es else 'This version applies when you accept it in NiviLog.',
            }
            for key, value in values.items():
                body = body.replace('{{' + key + '}}', value)
            if '{{' in body:
                raise ValueError('Unresolved legal placeholder')
            (ROOT / 'assets/legal' / f'nivilog-{filename[:-3]}{suffix}.md').write_text(body)
            title = ('Política de privacidad' if kind == 'privacy' else 'Condiciones de uso') if es else ('Privacy Policy' if kind == 'privacy' else 'Terms of Use')
            page = f'nivilog-{kind}{suffix}.html'
            public = f'''<!doctype html><html lang="{language}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="referrer" content="no-referrer"><title>NiviLog {title} | Hoplontec Inc.</title><link rel="canonical" href="https://hoplontec.io/{page}"><link rel="alternate" hreflang="en" href="https://hoplontec.io/nivilog-{kind}.html"><link rel="alternate" hreflang="es" href="https://hoplontec.io/nivilog-{kind}-es.html"><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="feedback.css"></head><body class="feedback-page"><div class="page-shell"><header class="header feedback-header"><a class="wordmark" href="./" aria-label="Hoplontec">hoplontec<span class="inc">inc.</span></a><nav class="language-switch" aria-label="{'Idioma' if es else 'Language'}"><a href="nivilog-{kind}.html" lang="en" {'aria-current="page"' if not es else ''}>English</a><a href="nivilog-{kind}-es.html" lang="es" {'aria-current="page"' if es else ''}>Español</a></nav></header><main class="inner-page"><article class="legal-document">{markdown(body)}</article><nav class="nivi-legal-links" aria-label="NiviLog"><a href="nivilog-feedback{suffix}.html">{'Ayuda a mejorar NiviLog' if es else 'Help improve NiviLog'}</a><a href="nivilog-privacy{suffix}.html">{'Política de privacidad' if es else 'Privacy Policy'}</a><a href="nivilog-terms{suffix}.html">{'Condiciones de uso' if es else 'Terms of Use'}</a></nav><p><a href="assets/legal/nivilog-{filename[:-3]}{suffix}.md" download>{'Descargar una copia' if es else 'Download a text copy'}</a></p></main><footer class="footer feedback-footer"><span>Hoplontec Inc.</span><a href="nivilog.html">NiviLog</a></footer></div></body></html>'''
            (ROOT / page).write_text(public + '\n')
    print('Rendered current NiviLog legal sources in English and Spanish.')

if __name__ == '__main__':
    sync(Path(sys.argv[1]))
