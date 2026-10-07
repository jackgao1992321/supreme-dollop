# Roth IRA Plan: Core + Trend Satellites

Benchmark: **S&P 500 (VOO)**. Goal: keep up with it in rising markets and lose less in falling ones.
Account on 2026-10-07: **$10,361**, of which **$3,644 (35%) is uninvested cash**.

## What was wrong with the old portfolio

| Problem | Why it matters | Fix |
|---|---|---|
| 35% sitting in cash | With the S&P at record highs, a third of the account earns nothing. Losing ground to an index usually starts here. | Invest it in the core and SGOV |
| SQQQ (3x inverse Nasdaq) | Loses value every day it's held, even when the market is flat. It's a day-trading tool, not something to hold. | Sell |
| EWJ + BBJP | Both hold the same Japan stocks; BBJP costs 0.19% a year vs 0.50% for EWJ | Combine into BBJP |
| 7 positions each under 3% (MP, RKLB, HOOD, NOK, B, DUK, SQQQ) | Too small to move the result, but each still needs watching | Sell; QQQM and MTUM already cover these themes |
| GIS (-21.6%, near its 52-week low) | Its price is still falling, and packaged-food sales are shrinking | Sell |
| XOM about 12% and SPCX about 10% | Two single stocks are about 22% of the account, and SPCX is a new IPO that swings a lot | Cut each to 6% |

## Target allocation

| Group | Holding | Target | Role |
|---|---|---|---|
| Core 49% | VOO | 29% | The S&P 500 itself |
| | QQQM | 10% | Nasdaq-100: growth and AI |
| | MTUM | 10% | Momentum fund: buys whatever is trending, reshuffles itself |
| Defense 28% | ALLW | 9% | All Weather mix of stocks, bonds, gold and commodities |
| | BRK.B | 9% | Steady, high-quality company that swings less than the market |
| | BBJP | 4% | Japan |
| | GLDM | 3.5% | Gold, as a hedge |
| | JNJ | 2.5% | Healthcare, defensive |
| Satellites 18% | XOM | 6% | Energy, while oil keeps rising |
| | SPCX | 6% | SpaceX |
| | MU | 6% | AI memory chips |
| Cash 5% | SGOV | 5% | Treasury bills: cash for dips and a place to park money when the market turns down |

## Weekly routine (Friday after close, trade on Monday)

Most weeks you won't need to trade. Rules, in order:

1. **Market trend check.** If VOO closes a week below its 40-week (about 200-day) moving average for **2 weeks in a row**, switch to risk-off:
   move all satellites (XOM, SPCX, MU) and half of QQQM into SGOV.
   Switch back when VOO closes 2 weeks in a row above that average.
2. **Single-stock stop.** Sell a satellite into SGOV if it closes a week **20% below its highest weekly close since you bought it**
   or below its own 40-week average. Replace it only with a stock that is above its 40-week average. Otherwise put the money in VOO.
3. **Drift check.** Run `python3 rebalance.py` after updating `holdings.csv`. Trade only positions that are **more than 2 percentage points** away from target.
4. **Size limits.** No single stock above 8%. Satellites above 20% combined get trimmed back to 18%.
5. **New contributions** go to whatever is furthest below its target. No timing needed.

Roth IRA notes: selling inside the account has no tax cost, so rebalancing is free. Tax-loss harvesting does nothing here.
Use limit orders, and avoid the first 15 minutes after the open.

## What to expect, honestly

- About half the account (VOO, QQQM, MTUM) will move with the market almost exactly. Nothing in this plan can fall far behind the index.
- The plan tries to beat the index in three ways:
  - **Momentum.** Owning stocks that are already trending (through MTUM) has historically earned more than the market over time.
  - **Losing less in big drops.** A portfolio that falls 20% when the market falls 30% finishes ahead even if it only matches the market's gains.
  - **No more drag.** The 35% cash and SQQQ were holding the account back.
- When the market rises steadily, the defense group and SGOV will trail VOO by roughly 1–3 points a year. That's the price of the protection.
- **No strategy guarantees beating the index.** Most professional funds fail to beat the S&P 500 over 10 or more years. Judge this plan over full market cycles, not individual weeks.
