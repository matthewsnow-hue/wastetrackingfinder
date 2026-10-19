# Waste Tracking Finder (D-010): build status
Updated Mon 19 Oct 2026 ~23:30 BST by Tel's executor. Local only: git init, no remote, no push, no domain/DNS, no analytics.

## Build
- `python3 tools/build.py` (re-runnable; reads data/dataset.csv = copy of research/dwt/D-010-dataset.csv FINAL, 219 rows). Env: WTF_SITE (default https://wastetrackingfinder.co.uk placeholder), WTF_PREVIEW=1 (noindex + robots Disallow + preview bar; set 0 at go-live), WTF_EMAIL (blank = "[contact email to be confirmed]").
- `python3 tools/check.py` (needs `python3 -m http.server 8765` in repo root): every sitemap URL at 390 and 1366, HTTP 200, JSON-LD parses, no horizontal overflow, no console/page errors, filter counts, screenshots to shots/.
- Styles: MTD Finder assets/style.css copied + assets/wtf.css; JS assets/wtf.js (menu, search, filters). No Google Fonts (falls back to system fonts).
- Sponsors: data/sponsors.json (absent = none). Rendered only in a separate "Sponsored" box, rel=sponsored, never reorders lists.

## Data rules applied (README-D-010-dataset.md)
- Names exactly as GOV.UK (incl. "(exempt for certain PAT scenarios)" suffixes in names; slug strips it only).
- URL shown only if url_basis starts "hand-checked" (94); else link to GOV.UK list.
- Price shown only if verified (31; 28 "hand-checked", 3 "read from pricing page") with "price checked 19 Oct 2026".
- 72 unclear -> /other-not-yet-categorised/, in no type filter.
- PAT 23 from GOV.UK.

## Pages: 242 in sitemap + 404.html
home, /software/ A–Z, 8 type pages + other, 219 vendor pages, 4 deadline guides (Oct 2027 worded exactly "is a plan, not a legal duty yet" in title, meta, badge, warning, timeline), penalties, about-methodology, sponsor, newsletter, disclaimer, contact, privacy, terms.
Regulatory quotes are verbatim from GOV.UK content API copies in research/dwt/*.json (read 19 Oct).

## Last check: 242 pages × 2 widths, 0 errors, 0 bad, JSON-LD valid. Skip hire filter 13; +price 2.

## Open (blockers before go-live)
- Contact email for the new site (not invented). Stripe payment link, Kit newsletter form: placeholders marked [to be confirmed]. Sponsor price now shown (sponsor + terms): £29/mo first 5 listings, then £49.
- Privacy: add newsletter + stats sections when connected.
- Type pages differ from plan v1.1 slugs (no /transfer-stations-recycling/ or /hazardous-waste/: no data for them).
- Repo creation / github.io URL / domain: needs Matthew via Snowman.

## Snowman QA fixes (preview 68615d5) — applied Mon 19 Oct 2026 ~22:45 BST
1. Oct 2027 wording -> "is a plan, not a legal duty yet" everywhere (0 "not yet law" left).
2. Sponsor test: test sponsor (WasteMatrix) in data/sponsors.json -> "Sponsored" badge, rel="sponsored noopener", list order identical to no-sponsor build (home 219, type page 94, diffed). Shots: shots/sponsor-test-390.png, shots/sponsor-test-1366.png. Test sponsor removed and rebuilt (no sponsors.json).
3. LoadSnap free/£25 tier: NOT added. Dataset/README only give "£39/mo Pro; £169 Business". The £25 figure exists only as an unverified search summary in niche-log.md. Needs Sam to verify and add to dataset.
4. Favicon: assets/favicon.svg + favicon-32.png + apple-touch-icon.png (replaces data:,).
5. Sponsor offer on /sponsor/ and /terms/.
Sam: 31 prices all show "price checked 19 Oct 2026"; no transfer-stations/hazardous pages.
Check: 242 pages x 390/1366, 0 bad, 0 errors, JSON-LD valid; skip 13, +price 2.
