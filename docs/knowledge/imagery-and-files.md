# Imagery: Sources and Rules

## Rules

- Minimalist and premium: cream or beige backgrounds, soft daylight, one subject, no baked-in text, no saturated orange backdrops (D-021).
- Every image gets a title or caption. Retina: serve 2x to 3x.
- Check AI images' labels at full resolution; multi-product AI shots usually have garbled print (L-051).
- No hard health claims in imagery (cholesterol figures, medication testimonials, dementia statistics): they break the UK claims rule.
- The UK store does not sell the Cellnergy hydration bottle or the diffuser; do not use them on UK pages.
- Generating new AI images costs credits: ask first.

## Sources

| Source | What it is | Notes |
|---|---|---|
| Dropbox "Branding Resources" | Style guide PDF, fonts, logos, "ICONS 2024" orange circle icons, Soona photography (~1 GB) | Icons cut as `lp-benefit-*.png` |
| Dropbox "Social Media" (Letisha) | Marketing posts 2018 to 2026 | Mostly baked-in text; few clean photos per month; fetch one month at a time (L-052) |
| Kive (LifePharm workspace) | AI product and lifestyle images | Read through the Kive MCP; page it in a subagent (verbose) |
| Higgsfield | AI images and videos | Higgsfield MCP; scan videos by pulling one frame with ffmpeg |
| Soona shoot | Real product lifestyle photos | Used for hover photos |
| Client uploads | e.g. `ProductPageHeaderImage.jpg` | Kept in repo root, not committed |

## Known gaps

- No clean LAMININE bottle-plus-box packshot; no tidy group of 3+ nutritionals.
- No lifestyle photo of the CELLNERGY WELLNESS STAND (only PNGs on black).
- About timeline icons were cut from a mockup JPG; originals (XD) not received.

## Compositing notes

- Strip baked shadows from transparent PNGs before compositing (L-050).
- Crop and upload helpers lived in scratchpads; reuse `tools/store-audit/files_upload.py` and `replace_file.py`.
