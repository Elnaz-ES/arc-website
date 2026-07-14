# ARC — Ancient Roots Circle (website)

Implemented from the Claude Design project `ARC.dc.html`
(project: *AncientRootsCircle Website (Remix)*).

## What this is

- **`ARC.dc.html`** — the page: template markup + a `<script data-dc-script>` state/data model.
- **`support.js`** — the design runtime. It loads React 18 + Babel from unpkg at runtime,
  parses the `<x-dc>` template, and renders the component. No build step.
- **`photos/`, `illustrations/`, `*.jpg/png`** — image assets.

It's a single-page app with client-side routing (Home / Community / Membership),
a mobile menu, billing toggle, FAQ accordion, and an EN/FA cooking-language toggle —
all driven by the data model in `ARC.dc.html`.

## Run it

Any static server works (an internet connection is required so `support.js` can pull
React/Babel from unpkg):

```bash
cd arc-website
python3 -m http.server 4173
# open http://localhost:4173/ARC.dc.html
```

## ⚠️ Placeholder images (replace these)

9 originals exceeded the design tool's 256 KiB transfer cap and could not be pulled
intact, so they are currently **on-brand placeholders** (dark-green with a gold diamond
and an "ARC placeholder" tag). Drop the real files in at the same paths to replace them:

| File | Intended content |
|------|------------------|
| `logo.png` | ARC logo mark |
| `hero-couple.jpg` | Hero photo (Hoda & Shervin) |
| `illustrations/conversations.png` | Community "conversations" illustration |
| `photos/family-three.jpg` | Family photo |
| `photos/hoda-shervin-2.jpg` | Hoda & Shervin |
| `photos/hoda-child-2.jpg` | Hoda as a child (founder) |
| `photos/shervin-child.jpg` | Shervin as a child (founder) |
| `photos/wedding.jpg` | Wedding photo |
| `photos/recipe-ghormeh.jpg` | Ghormeh Sabzi recipe |

The other 9 images are the real originals pulled from the design project.

## Props (defaults, editable in the `data-props` attribute of `ARC.dc.html`)

- `careerCadence`: `"Bi-weekly"` (or `"Weekly"`)
- `basicPrice`: `35`
- `premiumPrice`: `55`
