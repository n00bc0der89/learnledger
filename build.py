"""Builds index.html (static site) and an inlined single-file preview from landing.src.html."""
import base64, re, pathlib, sys
here = pathlib.Path(__file__).parent
src = (here / 'landing.src.html').read_text()
title = re.search(r'<title>.*?</title>', src).group(0)
body = src.replace(title, '')
head_extra = '''<meta name="description" content="Free Chrome extension for CBSE Class 10 Social Science: tracks the chapters you study on YouTube and NCERT sites, checks what you remember with 90-second recall tests, and plans your revision.">
<meta property="og:title" content="LearnLedger — Class 10 SST revision tracker">
<meta property="og:description" content="All 22 chapters of CBSE Class 10 Social Science. Track what you study, find out what you remember, revise what you forget. Free, no login.">
<meta property="og:image" content="https://learnledger.site/assets/og-image.png">
<meta property="og:url" content="https://learnledger.site/">
<link rel="canonical" href="https://learnledger.site/">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.png">'''
site = f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<title>LearnLedger — CBSE Class 10 Social Science revision tracker</title>\n{head_extra}\n</head>\n<body>\n' + re.sub(r'\{\{asset:([^}]+)\}\}', r'assets/\1', body) + '\n</body>\n</html>\n'
(here / 'index.html').write_text(site)
def datauri(m):
    f = here / 'assets' / m.group(1)
    mime = 'image/png' if f.suffix == '.png' else 'image/jpeg'
    return f'data:{mime};base64,' + base64.b64encode(f.read_bytes()).decode()
inline = title + '\n' + re.sub(r'\{\{asset:([^}]+)\}\}', datauri, body).replace('href="privacy.html"', 'href="#privacy"')
out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else here / 'preview.html'
out.write_text(inline)
print('site', len(site), 'inline', len(inline))
