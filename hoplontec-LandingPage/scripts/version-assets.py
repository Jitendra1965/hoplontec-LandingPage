"""Version published stylesheet URLs using the CSS content hash."""
import hashlib
from pathlib import Path
import re
import sys
import shutil

site = Path(sys.argv[1])
# This script is called by both Pages workflows after collecting public files.
source_root = Path(__file__).resolve().parent.parent
for filename in ('robots.txt', 'sitemap.xml', 'nivilog.html', 'nivilog-privacy.html', 'nivilog-terms.html', 'nivilog-privacy-es.html', 'nivilog-terms-es.html', 'nivilog-feedback.html', 'nivilog-feedback-es.html', 'nivilog-feedback-thanks.html', 'nivilog-feedback-thanks-es.html', 'feedback.css', 'feedback.js'):
    shutil.copyfile(source_root / filename, site / filename)
version = hashlib.sha256((site / 'styles.css').read_bytes()).hexdigest()[:12]
for page in site.glob('*.html'):
    source = page.read_text()
    updated = re.sub(r'href="styles\.css(?:\?[^"\s]*)?"',
                     f'href="styles.css?v={version}"', source)
    page.write_text(updated)
print(f'Published stylesheet version: {version}')

# Apply public opaque recipient configuration after copying page templates.
import runpy
configure = runpy.run_path(str(source_root / 'scripts/configure-feedback.py'))['configure']
configure(site, source_root)
# Version feedback assets independently; both languages always use the same code.
for filename in ('feedback.css', 'feedback.js'):
    version = hashlib.sha256((site / filename).read_bytes()).hexdigest()[:12]
    for page in site.glob('nivilog-*.html'):
        page.write_text(page.read_text().replace(f'"{filename}"', f'"{filename}?v={version}"'))
