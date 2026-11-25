"""Inject only FormSubmit's opaque public form identifier into packaged pages.

An empty ID intentionally leaves the form disabled for preview. Never accept an
email, URL, API key or obfuscated address. An ID is an address-hiding form handle,
not a secret or authentication credential. Obtain it from the activation email.
"""
import json
from pathlib import Path
import re
import sys


def configure(site, source):
    """Enable both translations together; malformed configuration fails build."""
    config = json.loads((source / 'feedback-config.json').read_text())
    form_id = config.get('formId', '')
    if not isinstance(form_id, str) or (form_id and not re.fullmatch(r'[A-Za-z0-9_-]{16,128}', form_id)):
        raise ValueError('formId must be the opaque FormSubmit ID, never an email or URL.')
    for filename in ('nivilog-feedback.html', 'nivilog-feedback-es.html'):
        path = site / filename
        text = path.read_text()
        if form_id:
            text = text.replace('id="feedback-form" action=""', f'id="feedback-form" action="https://formsubmit.co/{form_id}"')
            text = text.replace('data-configured="false"', 'data-configured="true"')
            text = text.replace('id="feedback-fields" disabled', 'id="feedback-fields"')
            text = text.replace('data-unavailable role="status"', 'data-unavailable role="status" hidden')
        path.write_text(text)
    if form_id:
        # Existing enquiries use the same confirmed inbox. Replace naked inbox
        # destinations in public forms without changing their fields or subjects.
        for name in ('contact.html', 'careers.html'):
            path = site / name
            if path.exists():
                text = re.sub(r'action="https://formsubmit\.co/[^"/]*@[^"/]*"',
                              f'action="https://formsubmit.co/{form_id}"', path.read_text())
                path.write_text(text)
    print('Feedback forms enabled with an opaque recipient ID.' if form_id else
          'Feedback forms remain disabled: the confirmed opaque FormSubmit ID is pending.')

if __name__ == '__main__':
    configure(Path(sys.argv[1]), Path(__file__).resolve().parent.parent)
