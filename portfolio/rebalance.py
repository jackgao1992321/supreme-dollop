#!/usr/bin/env python3
"""Weekly rebalance calculator for the Roth IRA.

Usage:
    python3 rebalance.py [holdings.csv] [targets.csv] [--band 2.0]

Update `shares` and `price` in holdings.csv from the Robinhood app, then run.
A trade is only suggested when a position is more than `band` percentage
points away from its target (or is not in the target list at all), so most
weeks this prints "no trades".
"""
import csv
import sys


def load(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    band = 2.0
    if "--band" in argv:
        band = float(argv[argv.index("--band") + 1])
        args.remove(argv[argv.index("--band") + 1])
    holdings_path = args[0] if args else "holdings.csv"
    targets_path = args[1] if len(args) > 1 else "targets.csv"

    holdings = {r["symbol"]: float(r["shares"]) * float(r["price"]) for r in load(holdings_path)}
    prices = {r["symbol"]: float(r["price"]) for r in load(holdings_path)}
    targets = {r["symbol"]: float(r["target_pct"]) for r in load(targets_path)}
    total = sum(holdings.values())
    cash = holdings.pop("CASH", 0.0)

    print(f"Account value: ${total:,.2f}   (cash ${cash:,.2f} = {cash / total:.1%})\n")
    rows = []
    for sym in sorted(set(holdings) | set(targets), key=lambda s: -targets.get(s, -1)):
        now = holdings.get(sym, 0.0)
        tgt_pct = targets.get(sym, 0.0)
        drift = now / total * 100 - tgt_pct
        trade = tgt_pct / 100 * total - now
        if sym in targets and abs(drift) <= band and now > 0:
            trade = 0.0
        rows.append([sym, now, tgt_pct, trade])

    # Positions held inside their band keep their drift, so scale buys to the
    # cash actually available (sell proceeds + existing cash).
    sells = sum(-r[3] for r in rows if r[3] < 0)
    buys = sum(r[3] for r in rows if r[3] > 0)
    scale = min(1.0, (sells + cash) / buys) if buys else 1.0
    for r in rows:
        if r[3] > 0:
            r[3] *= scale

    print(f"{'Symbol':<7}{'Now $':>10}{'Now %':>8}{'Target %':>10}{'Trade $':>11}  Action")
    for sym, now, tgt_pct, trade in rows:
        if sym not in targets:
            action = "SELL ALL"
        elif trade == 0:
            action = "hold (inside band)"
        else:
            action = "BUY" if trade > 0 else "SELL"
            if sym in prices:
                action += f" ~{abs(trade) / prices[sym]:.2f} sh"
        print(f"{sym:<7}{now:>10,.0f}{now / total * 100:>7.1f}%{tgt_pct:>9.1f}%{trade:>+11,.0f}  {action}")
    print(f"\nSell proceeds ${sells:,.0f} + cash ${cash:,.0f} -> buys ${buys * scale:,.0f}")
    print(f"Targets sum to {sum(targets.values()):.1f}%")

if __name__ == "__main__":
    main(sys.argv[1:])
