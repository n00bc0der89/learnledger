# LearnLedger website

Static site: `index.html` (landing page), `privacy.html` (the privacy policy the Web Store needs), `goodbye.html` (the uninstall-feedback page).

## Publish free on GitHub Pages
1. Create a public GitHub repo, e.g. `learnledger`.
2. Upload `index.html`, `privacy.html`, `goodbye.html` and the `assets/` folder to the repo root.
3. Repo → **Settings → Pages** → Source: *Deploy from a branch* → `main` / root → Save.
4. After about a minute the site is live at `https://<username>.github.io/learnledger/`.
5. Use that address for:
   - `learnledger/src/config.js` → `SITE_URL` (no trailing slash)
   - Web Store listing → homepage and privacy policy URL (`…/privacy.html`)
6. Optional: add a custom domain under Settings → Pages.

## Editing
Edit `landing.src.html`, then run `python3 build.py` to regenerate `index.html`.
Once the listing is live, set `STORE_URL` near the bottom of `landing.src.html` and rebuild. Until then, the install buttons open a Web Store search for "LearnLedger".
In `goodbye.html`, set `EMAIL` to your support address.
