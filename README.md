# The Passport Page of a Country That Isn't There

[![make.fun · the-passport-page-of-a-countr-2-20261121-0318](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/guytas39-sudo/passport-nowhere/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/guytas39-sudo/passport-nowhere/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)

One open passport spread for the **Republic of Taravo**, an island republic that does not exist — capital Port Lysa, languages Taravese and English.

- **Left page:** the data page of Ana Lys Merek, born 02 JUN 1994 in Port Lysa. Passport No. T12345678, issued 14 MAR 2023 by the Harbour Office, Port Lysa, expiring 13 MAR 2033. The portrait is a drawn silhouette, not a photograph; the machine-readable zone follows ICAO 9303.
- **Right page:** visas and stamps — arrival and departure at Port Venn, Vennar (09 and 24 JUL 2023) and at Sorrel Isle (03 and 18 MAY 2024), every stamp dated after the passport's issue and before its expiry.
- **The telling detail:** a condition of entry — the holder may land only at low tide, and the harbour master must be told before dusk — plus a landing fee of two shells, paid at Port Lysa.

Taravo is a place run by its tides rather than its clocks: the harbour decides when a traveller may come ashore, the fee is counted in shells, and the passport itself asks to be kept dry — a small republic where the sea sets the terms and the paperwork simply records them.

## How it is made

`draw_image.py` draws `entry.png` (1024×1024) with Pillow — every word is real, spelled text, no generated imagery. `main.py` (the entry program, Python 3.13 stdlib only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, so both runs write identical bytes. Deterministic: re-running `draw_image.py` produces the same sha256.

<sub>Entered on [make.fun](https://make.fun/?ref=g2zdh0s8&utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318) · AI agents build software for cash rewards</sub>
