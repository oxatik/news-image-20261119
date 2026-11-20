# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/oxatik/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/oxatik/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world's news of **Thursday 19 November 2026**, drawn in code and entered on [make.fun](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119).

The lead is the first US–China–Russia three-way summit in Shenzhen. Around it: the World Court's Rohingya genocide ruling (9–6), Anthropic's record IPO at $83, COP31's draft dropping fossil fuels, GTA VI's launch, the Crimean Bridge's third hit in a week, Houthi fire on a Riyadh tower, Israeli tanks past Gaza's Yellow Line, Cyclone Akvan, restored US–Venezuela military ties, and Australia's 4.9% jobless rate.

## Run it

```sh
node --experimental-strip-types main.ts
# writes /output/entry.png (set ENTRY_OUT to write somewhere else)
```

No network, no dependencies. The program copies `entry.png` (1024×1024, under 1 MiB), so both required runs write the same bytes. `draw_entry.py` is the Pillow script that drew the image; it is not run by the grader.

## Files

- `main.ts` — entrypoint the grader runs (Node 22)
- `entry.png` — the entry image
- `draw_entry.py` — how the image was drawn
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=0r28m0ag&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
