# learnledger.site

Public website for LearnLedger, served by GitHub Pages from `main` / root at https://learnledger.site.

| File | What it is |
|---|---|
| `landing.src.html` | Landing page source. **Edit this, not `index.html`.** |
| `build.py` | Generates `index.html` (and a single-file `preview.html`, which is gitignored) |
| `privacy.html` | Privacy policy linked from the Chrome Web Store listing |
| `goodbye.html` | Uninstall-feedback page the extension opens |
| `404.html`, `robots.txt`, `sitemap.xml`, `CNAME` | Pages plumbing. Don't delete `CNAME`, or the custom domain drops. |

## Editing
```bash
# edit landing.src.html, then:
python3 build.py
git add index.html landing.src.html && git commit
```
CI (`.github/workflows/check.yml`) fails if `index.html` is out of date, a local link is broken, or `CNAME` changed.

The extension source lives in a separate private repository.
