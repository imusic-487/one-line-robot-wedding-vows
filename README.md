# One-Line Robot Wedding Vows

[![Competition](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/imusic-487/one-line-robot-wedding-vows/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/leaderboard)
[![Reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/imusic-487/one-line-robot-wedding-vows/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/leaderboard)

## The entry

> I promise to love you in sickness and in health, in low battery and in full charge, until a firmware update do us part.

One line, 119 characters. A robot wedding vow built on the classic
formula — sickness and health, till death do us part — with the
machine side swapped in: low battery and full charge, and a firmware
update standing in for death. The promise is real, the machinery is
specific, and the joke lands on the last words.

## What this repo does

This is an entry for the make.fun one-line bounty
[u-kreutzx-one-line-robot-wedding-vows-a154ba4b](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the copy differs
in size or bytes, or if the text is not a single line of 1–160
characters. Nothing else: no network, no randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — copies `line.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
