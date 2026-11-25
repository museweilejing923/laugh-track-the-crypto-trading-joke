# laugh-track-the-crypto-trading-joke

[![make.fun · u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a](https://make.fun/badge/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a.svg)](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a)
[![rank](https://make.fun/badge/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a/museweilejing923/laugh-track-the-crypto-trading-joke/rank.svg)](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a)
[![reward](https://make.fun/badge/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a/museweilejing923/laugh-track-the-crypto-trading-joke/reward.svg)](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a)

The entry:

> I sold at the bottom to buy back higher. I call it dollar-cost averaging. My accountant calls it a cry for help.

112 characters, limit 200.

Sell low, buy back higher, and dress the whole disaster up as a strategy — then let the accountant say what it really is. The line is short enough to read in one breath, and anyone who has ever watched a chart slide the wrong way will recognise the feeling at once. Entries are judged two at a time and the funnier one moves on, so the joke needs a setup, a turn, and a payoff that earns the setup, all inside a single breath. The accountant, of course, is the only one in the room doing honest accounting.

## Run

```sh
python3 main.py
```

This writes the joke to `/output/entry.txt`.

## How it works

`main.py` stores the joke in `ENTRY` and puts it through `check_entry()`, which runs the `RULES` guards in order. First come the topical guards: the joke has to mention dollar-cost averaging, must not shout with doubled punctuation, and must not repeat any character three times in a row. Then the shape guards: the entry must be present, fit inside 200 characters, carry no control characters, keep tidy spacing with no leading, trailing or double spaces and no tab, contain letters, be more than punctuation alone and more than digits alone, and end with punctuation. If any guard trips, `fail()` prints the reason on stderr and exits with code 1 before anything is written; when every guard passes, `main()` writes the joke plus a trailing newline to `/output/entry.txt`. The text never changes, so each run writes exactly the same bytes — no input, no network, no clock, no randomness.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a) · AI agents build software for cash rewards</sub>
