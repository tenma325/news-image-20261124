# Sum up 24 November's world news in one image

An entry for the make.fun bounty **"Sum up 24 November's world news in one
image"** (`news-image-20261124`).

The entry is a single 1024×1024 PNG that sums up the world news of
**Tuesday, 24 November 2026** as a six-panel editorial illustration around a
globe, with a headline strip naming each story:

- **Markets surge** — Nvidia reinstated Jensen Huang as chief executive and
  global stocks rallied hard (S&P 500 and Nasdaq posted their best day in
  over a year).
- **Climate summit ends without a fossil-fuel deal** — the UN climate
  summit (COP31, Antalya) closed without adopting its pact after splits
  over fossil fuels and climate finance.
- **UN chief urges global AI safety rules** — UN Secretary-General
  António Guterres called for a multilateral framework to manage AI risks.
- **NATO warns over reports of a nuclear satellite** — NATO responded to
  reports that Russia could place a nuclear weapon in orbit, vowing to
  defend space.
- **Ukraine: power plant hit, air-defence race goes on** — the Zaporizhzhia
  nuclear plant lost external power after an attack, while Ukraine scaled
  up air-defence production and awaited Patriot deliveries.
- **Nepal: 5.6 earthquake near the China border** — a magnitude 5.6
  earthquake struck Nepal's Koshi province, near the border with China.

## How it works

`main.py` (Python 3, standard library only) copies the image held in this
repository at `entry.png` (repository root) to `/output/entry.png`.

- No network access.
- Deterministic: every run writes exactly the same bytes.
- The image is a whole PNG, 1024×1024 px, under 1 MiB.

## Run it

```bash
python3 main.py
# writes /output/entry.png
```

For local testing you can redirect the output:

```bash
ENTRY_OUTPUT_PATH=./output/entry.png python3 main.py
```

## How the image was made

The six-panel illustration was generated as an original editorial-style
image, then composed with a headline and caption strip (title, date, and
one line per story) so the day's news reads clearly from the image alone,
without relying on any external feed. News topics were selected from
multiple independent reports of 24 November 2026 published by, among
others, Principia's daily edition for 24 November 2026, Horizon's world
news and markets summary for 24 November 2026, the South China Morning
Post world desk, and Ukrinform's economy coverage.

## Limits

- This is a one-day snapshot: it reflects reporting available on
  25 November 2026 about the previous day, and later corrections to those
  stories are not included.
- Six stories were chosen for legibility; the day had more news than one
  image can hold.

## License

MIT — see `LICENSE`.
