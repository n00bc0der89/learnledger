"""Fails if any page links to a local file that doesn't exist."""
import pathlib, re, sys
root = pathlib.Path(__file__).resolve().parent.parent
bad = []
for page in sorted(root.glob('*.html')):
    if page.name in ('preview.html', 'landing.src.html'):
        continue
    for ref in re.findall(r'(?:href|src)="([^"#?]+)', page.read_text()):
        if re.match(r'^(https?:|mailto:|data:|//|\$\{)', ref):
            continue
        if not (root / ref.lstrip('/')).exists():
            bad.append(f'{page.name}: {ref}')
print('\n'.join(bad) or 'all local links resolve')
sys.exit(1 if bad else 0)
