"""Version published stylesheet URLs using the CSS content hash."""
import hashlib
from pathlib import Path
import re
import sys
import shutil

site = Path(sys.argv[1])
# This script is called by both Pages workflows after collecting public files.
source_root = Path(__file__).resolve().parent.parent
for filename in ('robots.txt', 'sitemap.xml', 'nivilog.html'):
    shutil.copyfile(source_root / filename, site / filename)
version = hashlib.sha256((site / 'styles.css').read_bytes()).hexdigest()[:12]
for page in site.glob('*.html'):
    source = page.read_text()
    updated = re.sub(r'href="styles\.css(?:\?[^"\s]*)?"',
                     f'href="styles.css?v={version}"', source)
    page.write_text(updated)
print(f'Published stylesheet version: {version}')
