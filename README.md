# ARC — Ancient Roots Circle

Community website for the Persian diaspora.

- **Live site:** https://ancientrootscircle.com
- **GitHub Pages URL:** https://elnaz-es.github.io/arc-website/
- **Repo:** https://github.com/Elnaz-ES/arc-website

## How it works

A **static site** — no build step. `index.html` holds the page (markup + a
`<script data-dc-script>` data model); `support.js` is the runtime that loads
React from a CDN and renders it in the browser. Images live in `photos/` and
`illustrations/`. Hosted free on **GitHub Pages**, which redeploys automatically
on every push to `main`.

## Updating the site (it goes live automatically)

**Easiest — edit online in GitHub:**
1. Open the repo: https://github.com/Elnaz-ES/arc-website
2. Click the file you want to change (e.g. `index.html`), then the ✏️ pencil.
3. Make your edit → **Commit changes**.
4. Wait ~30–60s — the change is live at ancientrootscircle.com. (Hard-refresh:
   `Cmd+Shift+R`.)

**Adding/replacing an image:** upload it into `photos/` (or `illustrations/`)
in GitHub with the **same filename** it replaces, or add a new file and
reference it in `index.html`.

**From your Mac (local):**
```bash
cd ~/Workarea/arc-website
# ...make edits...
git add -A
git commit -m "describe the change"
git push
```

## Preview locally before pushing

```bash
cd ~/Workarea/arc-website
npm run website     # or: python3 serve.py
# open http://localhost:4173/
```
(`serve.py` sends no-cache headers so image swaps show immediately.)

## Notes

- Content/data (roadmap, pricing tiers, FAQs, founders, etc.) all live in the
  `<script data-dc-script>` block near the bottom of `index.html`.
- Props with defaults (editable in that script's `data-props`): `careerCadence`
  (`Bi-weekly`/`Weekly`), `basicPrice` (35), `premiumPrice` (55).
- Full-resolution image originals are kept locally in `originals/` (git-ignored,
  not deployed). Stray files from earlier drops are parked in `_unused/`.
