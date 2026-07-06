#!/usr/bin/env python3
"""Market Map — June 26, 2026.
The Hormuz Unwind: Iran MoU signed, oil -19%, two stops hit, Warsh signals October hike.
Fresh marks + Shark Tank two-column format (render_v2.py).
"""
import os, sys, json, html as _html
from datetime import date, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import book, charts

TODAY = "2026-06-26"
NOW   = "08:45"
HERE  = os.path.dirname(os.path.abspath(__file__))

def e(s):
    return _html.escape(str(s)) if s is not None else ""

# ── CSS — Shark Tank / render_v2.py flat-white spec ──────────────────────────
CSS = """
:root {
  --bg:#ffffff; --surface:#f7f7f5; --ink:#1a1a1a; --ink-soft:#6b6b6b;
  --ink-mute:#9a9a9a; --gold:#b8960c; --red:#c0392b; --green:#1a7a45;
  --line:rgba(0,0,0,0.1); --radius-md:8px; --radius-lg:12px;
  --font:-apple-system,"Helvetica Neue",sans-serif;
  --serif:Georgia,"Times New Roman",serif;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font-family:var(--font);font-size:15px;line-height:1.65;padding:0}
.page{max-width:1400px;margin:0 auto;padding:2rem 2rem 4rem}
.two-col{display:grid;grid-template-columns:1fr 380px;gap:2.5rem;align-items:start}
@media(max-width:960px){.two-col{grid-template-columns:1fr}}
.lhs{min-width:0}
.rhs{min-width:0;position:sticky;top:1rem}
.masthead{border-bottom:0.5px solid var(--line);padding-bottom:1rem;margin-bottom:1.5rem}
.article-title{font-family:var(--serif);font-size:2rem;font-weight:400;line-height:1.25;color:var(--ink);margin:0 0 0.4rem}
.meta{font-size:11px;color:var(--ink-mute);letter-spacing:0.08em;text-transform:uppercase;margin-top:0.35rem}
.regime-tag{display:inline-block;font-size:10px;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;color:var(--gold);border:0.5px solid var(--gold);border-radius:20px;padding:2px 10px;margin-bottom:0.75rem}
.gold-rule{border:none;border-top:1px solid var(--gold);margin:1rem 0 0;opacity:0.4}
.section-label{font-size:10px;font-weight:500;letter-spacing:0.14em;text-transform:uppercase;color:var(--ink-mute);margin:1.75rem 0 0.75rem}
.section-label:first-child{margin-top:0}
.dash-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:5px;margin-bottom:1rem}
.dash-tile{background:var(--surface);border-radius:var(--radius-md);padding:0.5rem 0.75rem;border:0.5px solid var(--line)}
.dash-tile .dlabel{font-size:10px;color:var(--ink-mute);margin-bottom:2px}
.dash-tile .dval{font-size:13px;font-weight:500;color:var(--ink);font-variant-numeric:tabular-nums}
.dash-tile .dchg{font-size:11px}
.chg-up{color:var(--green)}.chg-dn{color:var(--red)}.chg-flat{color:var(--ink-mute)}
.theme-line{border-left:2px solid var(--gold);padding:0.5rem 0.85rem;background:var(--surface);border-radius:0 var(--radius-md) var(--radius-md) 0;margin:1rem 0;font-size:13px;font-weight:500;line-height:1.5}
.tile{background:var(--bg);border:0.5px solid var(--line);border-radius:var(--radius-lg);padding:1rem 1.1rem;margin-bottom:8px}
.tile-head{font-size:10px;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;color:var(--ink-mute);margin-bottom:0.4rem}
.tile-claim{font-size:13px;font-weight:500;color:var(--ink);line-height:1.5;margin-bottom:0.4rem}
.tile-body{font-size:12px;color:var(--ink-soft);line-height:1.6}
.tile-gold{border-top:2px solid var(--gold)}.tile-green{border-top:2px solid var(--green)}.tile-red{border-top:2px solid var(--red)}.tile-muted{border-top:2px solid var(--line)}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:8px}
.grid-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-bottom:8px}
@media(max-width:600px){.grid-2,.grid-3{grid-template-columns:1fr}}
.trade-card{background:var(--bg);border:0.5px solid var(--line);border-radius:var(--radius-lg);padding:1rem 1.1rem;margin-bottom:8px}
.trade-card.warn{border-color:rgba(192,57,43,0.35);background:#fff8f8}
.tc-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:0.75rem}
.tc-name{font-size:13px;font-weight:500;color:var(--ink)}
.tc-class{font-size:10px;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink-mute);margin-top:2px}
.conv-badge{font-size:11px;font-weight:500;background:var(--surface);border:0.5px solid var(--line);border-radius:20px;padding:2px 10px;color:var(--ink);white-space:nowrap}
.tc-row{display:flex;justify-content:space-between;font-size:12px;padding:4px 0;border-bottom:0.5px solid var(--line)}
.tc-row:last-of-type{border-bottom:none}
.tc-k{color:var(--ink-mute)}.tc-v{font-weight:500;color:var(--ink)}
.conv-bar{display:flex;gap:3px;align-items:center;margin:0.5rem 0}
.pip{width:18px;height:4px;border-radius:2px;background:var(--line)}
.pip.on{background:var(--gold)}
.conv-detail{font-size:10px;color:var(--ink-mute);margin-left:6px}
.tc-thesis{font-size:12px;color:var(--ink-soft);line-height:1.6;margin-top:0.6rem;padding-top:0.6rem;border-top:0.5px solid var(--line)}
.score-row{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:10px}
.score-tile{background:var(--surface);border-radius:var(--radius-md);padding:0.5rem 0.6rem;text-align:center}
.sval{font-size:18px;font-weight:500;color:var(--ink)}
.sval.pos{color:var(--green)}.sval.neg{color:var(--red)}
.slabel{font-size:10px;color:var(--ink-mute);margin-top:2px}
.live-table{width:100%;font-size:12px;border-collapse:collapse}
.live-table th{font-size:10px;text-transform:uppercase;letter-spacing:0.1em;color:var(--ink-mute);font-weight:500;padding:0 0 6px;text-align:left;border-bottom:0.5px solid var(--line)}
.live-table td{padding:6px 0;border-bottom:0.5px solid var(--line);color:var(--ink);vertical-align:middle}
.live-table tr:last-child td{border-bottom:none}
.pnl-pos{color:var(--green);font-weight:500}.pnl-neg{color:var(--red);font-weight:500}
.pill{font-size:10px;padding:2px 8px;border-radius:20px;background:var(--surface);color:var(--ink-mute);border:0.5px solid var(--line)}
.prog-bar{height:4px;background:var(--line);border-radius:2px;overflow:hidden;min-width:48px;margin-top:3px}
.prog-bar>span{display:block;height:100%;background:var(--gold)}
.canary{padding:0.55rem 0;border-bottom:0.5px solid var(--line);display:flex;gap:10px;align-items:flex-start}
.canary:last-child{border-bottom:none}
.cdot{width:6px;height:6px;border-radius:50%;background:var(--gold);flex-shrink:0;margin-top:5px}
.ctext{font-size:12px;color:var(--ink-soft);line-height:1.6}
.ctext strong{color:var(--ink);font-weight:500}
.ammo{padding:0.55rem 0;border-bottom:0.5px solid var(--line)}
.ammo:last-child{border-bottom:none}
.ammo-q{font-size:12px;font-weight:500;color:var(--ink);margin-bottom:3px}
.ammo-a{font-size:12px;color:var(--ink-soft);line-height:1.5}
.yesterday{background:var(--surface);border-radius:var(--radius-md);padding:0.75rem 1rem;margin-bottom:1rem}
.yest-item{font-size:12px;color:var(--ink-soft);padding:4px 0;display:flex;gap:8px;align-items:flex-start;border-bottom:0.5px solid var(--line)}
.yest-item:last-child{border-bottom:none}
.tick-g{color:var(--green);flex-shrink:0;font-weight:600}
.tick-r{color:var(--red);flex-shrink:0;font-weight:600}
.tick-n{color:var(--ink-mute);flex-shrink:0}
.cal-table{width:100%;font-size:12px;border-collapse:collapse}
.cal-table th{font-size:10px;text-transform:uppercase;letter-spacing:0.1em;color:var(--ink-mute);font-weight:500;padding:0 6px 6px 0;text-align:left;border-bottom:0.5px solid var(--line)}
.cal-table td{padding:7px 6px 7px 0;border-bottom:0.5px solid var(--line);vertical-align:top}
.cal-table tr:last-child td{border-bottom:none}
.cal-event{color:var(--gold);font-weight:500}
.asym-up{color:var(--green)}.asym-dn{color:var(--red)}
.wrap-body{font-family:var(--serif);font-size:16px;line-height:1.85;color:var(--ink)}
.wrap-body p{margin-bottom:1.1rem}
.wrap-body strong{font-weight:600}
.alert-banner{background:#fff8f8;border:0.5px solid rgba(192,57,43,0.3);border-left:3px solid var(--red);border-radius:0 var(--radius-md) var(--radius-md) 0;padding:0.6rem 0.85rem;margin:1rem 0;font-size:13px;color:var(--red);line-height:1.5}
.info-banner{background:#f7f7f5;border:0.5px solid var(--line);border-left:3px solid var(--gold);border-radius:0 var(--radius-md) var(--radius-md) 0;padding:0.6rem 0.85rem;margin:1rem 0;font-size:12px;color:var(--ink-soft);line-height:1.5}

/* ── Dark theme ────────────────────────────────────────────── */
[data-theme="dark"]{
  --bg:#0d0f14;--surface:#161921;--ink:#e4dfd8;--ink-soft:#9e9990;
  --ink-mute:#5f5c58;--gold:#c9a830;--red:#e06060;--green:#45c47a;
  --line:rgba(255,255,255,0.1);
}
[data-theme="dark"] .alert-banner{background:rgba(224,96,96,0.12);border-color:rgba(224,96,96,0.3)}
[data-theme="dark"] .info-banner{background:rgba(255,255,255,0.05)}
[data-theme="dark"] .trade-card.warn{background:rgba(224,96,96,0.08);border-color:rgba(224,96,96,0.25)}

/* ── Theme toggle ──────────────────────────────────────────── */
#theme-toggle{position:absolute;top:0;right:0;background:var(--surface);border:0.5px solid var(--line);color:var(--ink-mute);font-size:11px;letter-spacing:0.06em;padding:5px 12px;border-radius:20px;cursor:pointer;font-family:var(--font);transition:color .15s,border-color .15s,background .15s}
#theme-toggle:hover{color:var(--ink);border-color:var(--gold)}
"""

# ── Helpers ───────────────────────────────────────────────────────────────────
def pips(conviction, cb):
    n = int(conviction)
    dots = "".join(
        f'<div class="pip{"  on" if i < n else ""}"></div>' for i in range(10)
    )
    detail = (
        f'gap({cb.get("gap",0)}/3) · '
        f'catalyst({cb.get("catalyst",0)}/2) · '
        f'pos({cb.get("positioning",0)}/2) · '
        f'confirm({cb.get("confirmation",0)}/2) · '
        f'stop({cb.get("stop_quality",0)}/1)'
    )
    return f'<div class="conv-bar">{dots}<span class="conv-detail">{e(detail)}</span></div>'

def pnl_span(p):
    if p is None:
        return '<span style="color:var(--ink-mute)">--</span>'
    cls = "pnl-pos" if p > 0 else ("pnl-neg" if p < 0 else "")
    return f'<span class="{cls}">{p:+.2f}%</span>'

def progress_pct(t, level):
    entry, target = t.get("entry"), t.get("target")
    if entry is None or target is None or target == entry:
        return 0
    d = 1 if target >= entry else -1
    p = d * (level - entry) / abs(target - entry)
    return max(0, min(100, int(p * 100)))

# Marks applied to trades before writing output
def apply_marks(trades):
    marks = {
        "MM-2026-001": {"level": 1.6504, "pnl": -0.33},
        "MM-2026-003": {"level": 3.63,   "pnl": 10.0},
        "MM-2026-004": {"level": 4.45,   "pnl": -0.23},
        "MM-2026-008": {"level": 3.0,    "pnl": -91.4},
        "MM-2026-009": {"level": 0.29,   "pnl": 93.3},
    }
    stops = {
        "MM-2026-002": {"level": 84.0,   "pnl": -7.69, "date": "2026-06-16", "days": 16},
        "MM-2026-005": {"level": 4250.0, "pnl": -6.04, "date": "2026-06-19", "days": 19},
    }
    new_open = []
    new_closed = list(trades.get("closed", []))
    for t in trades.get("open", []):
        tid = t["id"]
        if tid in stops:
            s = stops[tid]
            entry = {"date": s["date"], "level": s["level"], "pnl_pct": s["pnl"], "status": "stopped"}
            t["history"].append(entry)
            t["current"] = s["level"]
            t["current_pnl_pct"] = s["pnl"]
            t["exit"] = {"date": s["date"], "level": s["level"],
                         "result": "STOPPED", "pnl_pct": s["pnl"], "days_held": s["days"]}
            new_closed.append(t)
        elif tid in marks:
            m = marks[tid]
            t["history"].append({"date": TODAY, "level": m["level"], "pnl_pct": m["pnl"], "status": "open"})
            t["current"] = m["level"]
            t["current_pnl_pct"] = m["pnl"]
            new_open.append(t)
        else:
            new_open.append(t)
    return {"open": new_open, "closed": new_closed}

trades_raw = book.load_trades()
trades = apply_marks(trades_raw)

# Save updated trades.json
with open(os.path.join(HERE, "trades.json"), "w") as f:
    json.dump(trades, f, indent=2)

# ── Charts ────────────────────────────────────────────────────────────────────
eq_svg  = charts.equity_curve(trades["closed"])
cal_svg = charts.calibration(trades["closed"])
vix_svg = charts.vix_term_structure([
    {"label": "VIX9D", "value": 15.2},
    {"label": "VIX",   "value": 18.44},
    {"label": "VIX3M", "value": 19.8},
    {"label": "VIX6M", "value": 20.5},
])
yc_svg  = charts.yield_curve([
    {"label": "2Y",  "value": 4.16},
    {"label": "5Y",  "value": 4.28},
    {"label": "10Y", "value": 4.45},
    {"label": "30Y", "value": 4.72},
])

# ── Trade book HTML ───────────────────────────────────────────────────────────
def live_book_html(trades):
    closed = trades.get("closed", [])
    open_t = trades.get("open", [])
    graded = [t for t in closed if "exit" in t and "pnl_pct" in t["exit"]]
    if graded:
        pnls = [t["exit"]["pnl_pct"] for t in graded]
        wins  = [p for p in pnls if p > 0]
        hr    = 100 * len(wins) / len(graded)
        best  = max(graded, key=lambda t: t["exit"]["pnl_pct"])
        worst = min(graded, key=lambda t: t["exit"]["pnl_pct"])
        score = f"""
<div class="score-row">
  <div class="score-tile"><div class="sval">{len(graded)}</div><div class="slabel">Closed</div></div>
  <div class="score-tile"><div class="sval {'pos' if hr>=50 else 'neg'}">{hr:.0f}%</div><div class="slabel">Hit rate</div></div>
  <div class="score-tile"><div class="sval {'pos' if sum(pnls)>=0 else 'neg'}">{sum(pnls):+.1f}%</div><div class="slabel">Sum P&amp;L</div></div>
  <div class="score-tile"><div class="sval neg">{worst['id']}</div><div class="slabel">Worst</div></div>
</div>"""
    else:
        score = '<p style="font-size:12px;color:var(--ink-mute);margin-bottom:0.75rem">Scoreboard builds as trades close.</p>'

    open_rows = []
    for t in open_t:
        cur = t.get("current", t.get("entry"))
        pl  = t.get("current_pnl_pct")
        prog = progress_pct(t, cur) if cur is not None else 0
        warn = ""
        # Flag MM-2026-001 as near-stop, MM-2026-008 as expiring
        if t["id"] == "MM-2026-001":
            warn = ' style="color:var(--red)"'
        elif t["id"] == "MM-2026-008":
            warn = ' style="color:var(--red)"'
        open_rows.append(f"""<tr>
  <td><span class="pill">{e(t.get('id',''))}</span></td>
  <td style="max-width:130px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap"{warn}>{e(t.get('trade',''))}</td>
  <td style="font-variant-numeric:tabular-nums">{e(cur)}</td>
  <td>{pnl_span(pl)}</td>
  <td><div class="prog-bar"><span style="width:{prog}%"></span></div></td>
</tr>""")

    open_tbl = f"""
<table class="live-table">
  <thead><tr><th>ID</th><th>Trade</th><th>Mark</th><th>P&L</th><th>To target</th></tr></thead>
  <tbody>{"".join(open_rows) or '<tr><td colspan="5" style="color:var(--ink-mute)">no open trades</td></tr>'}</tbody>
</table>"""

    closed_rows = "".join(f"""<tr>
  <td><span class="pill">{e(t.get('id',''))}</span></td>
  <td style="max-width:110px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{e(t.get('trade',''))}</td>
  <td>{e(t.get('exit',{}).get('result',''))}</td>
  <td>{pnl_span(t.get('exit',{}).get('pnl_pct'))}</td>
  <td style="color:var(--ink-mute)">{e(t.get('exit',{}).get('days_held',''))}d</td>
</tr>""" for t in closed) if closed else ""

    closed_tbl = f"""
<div class="section-label" style="margin-top:1rem">Closed ledger</div>
<table class="live-table">
  <thead><tr><th>ID</th><th>Trade</th><th>Result</th><th>P&L</th><th>Held</th></tr></thead>
  <tbody>{closed_rows or '<tr><td colspan="5" style="color:var(--ink-mute)">none yet</td></tr>'}</tbody>
</table>""" if closed else ""

    return score + open_tbl + closed_tbl


# ── HTML sections ─────────────────────────────────────────────────────────────
MASTHEAD = f"""
<div class="masthead" style="position:relative">
  <button id="theme-toggle">&#9790; Dark</button>
  <div class="regime-tag">Ceasefire Unwind &middot; Brent -19% &middot; Two Stops Hit</div>
  <h1 class="article-title">The Hormuz Unwind</h1>
  <p class="meta">Pre-market intelligence brief &middot; {TODAY} &middot; {NOW} local &middot; self-graded book</p>
  <hr class="gold-rule">
</div>"""

ARTICLE = """
<div class="section-label">The view</div>
<div class="wrap-body">
<p>Three weeks have passed since the June 7 brief, and the macro landscape has
shifted decisively. The Iran-US memorandum of understanding, signed June 17, has
done what peace deals do to war-premium positions: it has priced them out. Brent
crude, which we marked at $93 on June 7, trades at $74.43 this morning — a
19.3% decline in nineteen days. Gold, which we entered at $4,523, has fallen
through our $4,250 stop and now trades near $4,000, weighed by hawkish signals
from the new Federal Reserve chair Kevin Warsh. Both stops were clean. The book
took the loss, closed the positions, and moves on.</p>

<p>The Federal Open Market Committee met June 17 — the same day as the MoU
signing — and held the federal funds rate at 3.5–3.75%, as expected. But the
"dot plot" told a different story: the median 2026 year-end estimate shifted from
3.4% to 3.8%, and for the first time this cycle, a majority of officials backed
a further hike. Markets now price a 60-plus percent probability of one 25bp
increase by October. Warsh's first press conference was measured but unmistakably
hawkish: he flagged lingering services inflation, dismissed the energy-driven
disinflation as transitory in reverse, and declined to signal any path to cuts.
That combination — oil falling fast but the Fed shifting to a hiking bias — is
the central tension in markets right now.</p>

<p>The European Central Bank moved first, hiking by 25 basis points on June 11 in
its first tightening since September 2023. The ECB cited the Iran-war inflation
impulse explicitly: eurozone HICP printed 3.2% year-on-year in May, above the
2% target and still rising. This hike is the dominant reason our short EURAUD
position is now offside. The EUR carried additional rate support into the cross
just as the AUD shed its oil-terms-of-trade tailwind; EURAUD has drifted from
1.615 at the last brief to 1.650 today, 12 basis points from our 1.662 stop.
This is the position to watch. We are giving it room while the geopolitical
picture resolves further, but if EURAUD closes above 1.658 it will be
mechanically stopped.</p>

<p>The May non-farm payrolls report on June 5 delivered a decisive verdict on the
"payrolls at 89k" thesis embedded in the 2s10s steepener: actual prints were
172k, well above the 80k consensus, with the unemployment rate unchanged at 4.3%.
The labor market is not breaking. That mattered for the Fed's reaction function
and explains why the FOMC felt comfortable shifting toward a hike rather than
toward cuts. The steepener (MM-2026-009) remains open — 2s10s has moved from
+38bp to +29bp, still well above our +15bp entry and a long way from the -10bp
stop — but the pace of steepening has slowed as the October hike narrative
anchors the front end.</p>

<p>The Brent-WTI spread trade (MM-2026-003) has been the quiet survivor. Both
crudes have fallen sharply on the Hormuz re-opening, but the spread has held
near $3.63 — above our $3.30 entry — because Brent retains a modest geopolitical
premium while WTI has been more aggressively re-priced on the US inventory
normalization. On June 20, Iran briefly threatened to close the Strait again,
citing Israeli violations of the MoU terms; the claim was denied by US Central
Command and shipping resumed, but the episode is a reminder that the ceasefire
remains provisional. The spread trade captures that residual optionality.</p>

<p>The SPX Jun-27 7300/7000 put spread (MM-2026-008) expires <strong>tomorrow</strong>.
With the S&P 500 at 7,358 — above the short strike of 7,300 — the spread is worth
approximately $3, down from $70 at the June 7 mark. The hedge functioned correctly
in that it provided positive carry into the post-payrolls dip; the May 172k print
reversed that move and the market held above 7,300 into expiry. Maximum loss is
the original $35 premium paid.</p>
</div>
"""

SINCE_LAST = """
<div class="section-label">Since the June 7 brief</div>
<div class="yesterday">
  <div class="yest-item">
    <span class="tick-r">X</span>
    <span><strong>Jun 5 — May NFP 172k</strong> vs 80k est. Unemployment 4.3%. Put-hedge rally reversed; steepener slowed.</span>
  </div>
  <div class="yest-item">
    <span class="tick-r">X</span>
    <span><strong>Jun 11 — ECB hike +25bp</strong>, first in 3 years. Deposit rate 2.25%. HICP 3.2%. EUR bid; EURAUD pushed to 1.650, near our stop.</span>
  </div>
  <div class="yest-item">
    <span class="tick-n">-</span>
    <span><strong>Jun 12 — Iran-US ceasefire</strong> agreed. Jun 17 MoU signed by both presidents. 60-day window to negotiate final terms.</span>
  </div>
  <div class="yest-item">
    <span class="tick-r">X</span>
    <span><strong>Jun 17 — FOMC holds</strong> (3.5-3.75%), dot plot flips hawkish. Warsh signals October hike possible. Gold and oil sell off.</span>
  </div>
  <div class="yest-item">
    <span class="tick-r">X</span>
    <span><strong>Jun 16-19 — MM-2026-002 & 005 stopped</strong>. Brent hit $84 stop (-7.7%); gold hit $4,250 stop (-6.0%).</span>
  </div>
  <div class="yest-item">
    <span class="tick-n">-</span>
    <span><strong>Jun 20 — Iran threatens Hormuz</strong> closure again, citing Israeli actions. US denies. Shipping resumes. Geopolitical risk not zero.</span>
  </div>
  <div class="yest-item">
    <span class="tick-n">-</span>
    <span><strong>Today — Brent $74.43, WTI $70.80</strong>. Brent-WTI spread $3.63. Gold $4,007. 10Y 4.45%. 2s10s +29bp.</span>
  </div>
</div>
"""

OPEN_TRADES_LHS = """
<div class="section-label">Open positions — updated marks</div>

<div class="alert-banner">
  <strong>EURAUD 1.6504 vs stop 1.662</strong> — 12 basis points from exit. ECB hike flipped this from a rate-differential short to a near-stop management situation. Watch for ECB July meeting (Jul 24) language.
</div>

<div class="alert-banner">
  <strong>MM-2026-008 expires tomorrow (Jun 27)</strong> — SPX Jun-27 7300/7000 put spread. SPX at 7,358 means the 7300 put is out-of-the-money. Current value ~$3. Full premium at risk; max loss = $35 original cost.
</div>
"""

# Detailed trade analysis per open position
OPEN_DETAIL = """
<div class="section-label" style="margin-top:1.5rem">Position-by-position</div>

<div class="tile tile-red">
  <div class="tile-head">MM-2026-001 &middot; Short EURAUD &middot; NEAR STOP</div>
  <div class="tile-claim">Entry 1.645 / Stop 1.662 / Target 1.610 &middot; Mark 1.6504 &middot; P&L -0.33%</div>
  <div class="tile-body">The ECB's June 11 hike (+25bp, first since 2023) injected rate support under EUR
  at exactly the wrong moment for this trade. EURAUD moved from 1.615 to 1.650 as the AUD simultaneously
  lost its commodity-terms-of-trade tailwind (iron ore softened with China PMI slipping back to 49.8 in May).
  The original thesis — ECB dovish while RBA still hawkish — has partially reversed. The cross is
  12bp from stop. No action until stop is either hit or the ECB July meeting (Jul 24) signals pause.</div>
</div>

<div class="tile tile-gold">
  <div class="tile-head">MM-2026-003 &middot; Long Brent / Short WTI Spread &middot; Open +10%</div>
  <div class="tile-claim">Entry $3.30 / Stop $1.50 / Target $6.50 &middot; Mark $3.63 &middot; P&L +10.0%</div>
  <div class="tile-body">The spread survived the Hormuz unwind. Brent ($74.43) fell harder than WTI ($70.80)
  in the initial ceasefire relief, but has since found support on the residual Brent-specific risk premium
  (European buyers still price in re-escalation tail; Saudi cargo restart is slower than expected).
  The Jun 20 Iranian Hormuz threat — however brief — is a reminder that the spread optionality is not zero.
  Entry is $3.30; spread at $3.63. Still inside the thesis.</div>
</div>

<div class="tile tile-muted">
  <div class="tile-head">MM-2026-004 &middot; Short US 10Y Yield &middot; Flat</div>
  <div class="tile-claim">Entry 4.44% / Stop 4.65% / Target 4.10% &middot; Mark 4.45% &middot; P&L -0.23%</div>
  <div class="tile-body">Essentially unchanged. The disinflation thesis (oil-driven CPI softening) is beginning
  to show in the data — May CPI will print in a few weeks — but the Warsh hawkish shift is an offset. The
  10Y yield has been anchored in the 4.40–4.55% range since mid-June. Stop at 4.65% is intact; the position
  is alive but the thesis is contested. The key upcoming catalyst is June CPI (July 10).</div>
</div>

<div class="tile tile-red">
  <div class="tile-head">MM-2026-008 &middot; SPX Jun-27 Put Spread &middot; EXPIRING TOMORROW</div>
  <div class="tile-claim">Entry $35 / Stop $0 / Target $265 &middot; Mark ~$3 &middot; P&L -91.4%</div>
  <div class="tile-body">The hedge served its purpose during the brief post-payrolls dip (marked $70 on Jun 7),
  but the 172k NFP print reversed the SPX decline. With SPX at 7,358 and expiry tomorrow (Jun 27), the
  7300/7000 put spread is effectively worthless. The original $35 premium is the loss. Max loss = $35 (the
  full premium paid); this was always the defined-risk hedge structure. Position closes worthless tomorrow.</div>
</div>

<div class="tile tile-green">
  <div class="tile-head">MM-2026-009 &middot; 2s10s UST Steepener &middot; Still Profitable</div>
  <div class="tile-claim">Entry +15bp / Stop -10bp / Target +60bp &middot; Mark +29bp &middot; P&L +93.3%</div>
  <div class="tile-body">The steepener is the book's best-performing survivor. 2Y yield at 4.16%, 10Y at 4.45%
  gives a +29bp spread vs +15bp entry. The pace has slowed from the +38bp June 7 mark — the "October Warsh
  hike" narrative is keeping the 2Y anchored above 4.10% — but the structural steepening thesis (late-cycle,
  post-inversion, Fed pause + fiscal supply pressure at the long end) remains intact. Stop at -10bp is
  comfortable; the next inflection is the FOMC July 28-29 meeting.</div>
</div>
"""

CANARY_WATCH = """
<div class="section-label">Canary watch</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>EURAUD 1.662 stop</strong> — if the cross closes above 1.658, initiate stop protocol.
  ECB July 24 meeting is the next EUR catalyst.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>Hormuz June 20 threat</strong> — Iran's claim that Israel violated the MoU was
  denied by CENTCOM but oil volumes through the strait are 18% below pre-crisis peaks. A second
  Hormuz incident would reprice MM-2026-003 (spread) sharply higher and partially vindicate the stopped
  MM-2026-002 thesis.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>June CPI (Jul 10)</strong> — first inflation print since oil's 19% drop. If
  headline CPI falls below 3.0%, Warsh's October hike timeline gets harder to justify; 10Y yields
  should rally and MM-2026-004 (short yield) will finally move toward target.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>June NFP (Jul 2)</strong> — labor market is the Fed's permission slip.
  If payrolls decelerate toward 100k or below, the October hike gets pushed; steepener and duration
  longs come alive.</div>
</div>
"""

AMMO = """
<div class="section-label">Talking points</div>
<div class="ammo">
  <div class="ammo-q">Why did the Brent long stop out but not the spread trade?</div>
  <div class="ammo-a">The outright Brent (MM-2026-002) had a stop at $84 — a sharp Hormuz
  re-opening move through that level. The spread (MM-2026-003) has a wider, percentage-based
  tolerance (stop at $1.50 spread vs $3.30 entry). When both crudes fell together, the ratio
  of their prices changed little, leaving the spread above entry while the outright level crashed
  through the stop. Different instruments, different risk parameters.</div>
</div>
<div class="ammo">
  <div class="ammo-q">Gold fell after the Fed was dovish-to-neutral — shouldn't it have risen?</div>
  <div class="ammo-a">Gold was long the "Fed pause + geopolitical premium" binary. The peace deal
  removed half the bid (geopolitical), and Warsh's hawkish dot plot removed the other half (rate cut
  optionality). Real yields rose as nominal yields stayed flat while inflation expectations fell with
  oil. Gold loses on that path.</div>
</div>
<div class="ammo">
  <div class="ammo-q">Is the 2s10s steepener at risk from the Warsh October hike?</div>
  <div class="ammo-a">Paradoxically, no — at least not in the near term. A Fed hike that causes a
  recession expectation repricing would actually steepen the curve faster: the 10Y rallies (lower
  yield) on growth fears while the 2Y stays anchored to the policy rate. The steepener only loses
  if the hike is credibly delivered AND the long end sells off on fiscal supply at the same time —
  a bear steepen within a hike cycle. That is a secondary risk, but it is the risk to monitor.</div>
</div>
"""

WEEK_AHEAD = """
<div class="section-label">Week ahead</div>
<table class="cal-table">
  <thead><tr><th>Date</th><th>Event</th><th>Asymmetry</th></tr></thead>
  <tbody>
    <tr><td>Jun 27</td><td class="cal-event">MM-2026-008 expiry</td><td>Put spread expires; book loss = $35 premium. No action required.</td></tr>
    <tr><td>Jul 2</td><td class="cal-event">June NFP</td><td class="asym-up">Below 120k = Fed pause reprices; 10Y rallies; steepener accelerates</td></tr>
    <tr><td>Jul 10</td><td class="cal-event">June CPI</td><td class="asym-up">Sub-3.0% print validates oil disinflation; duration long revives</td></tr>
    <tr><td>Jul 24</td><td class="cal-event">ECB meeting</td><td class="asym-dn">Second hike would stop out MM-2026-001 (EURAUD); EUR/AUD key risk</td></tr>
    <tr><td>Jul 28-29</td><td class="cal-event">FOMC</td><td>Unlikely to hike July; language around October is the tell</td></tr>
  </tbody>
</table>
"""

# ── Dashboard tiles ───────────────────────────────────────────────────────────
DASH = """
<div class="section-label">Live levels — Jun 26</div>
<div class="dash-grid">
  <div class="dash-tile"><div class="dlabel">Brent crude</div>
    <div class="dval">$74.43 <span class="chg-dn dchg">-19.3% vs Jun 7</span></div></div>
  <div class="dash-tile"><div class="dlabel">WTI crude</div>
    <div class="dval">$70.80 <span class="chg-dn dchg">extended 4-day slide</span></div></div>
  <div class="dash-tile"><div class="dlabel">Brent-WTI spread</div>
    <div class="dval">$3.63 <span class="chg-up dchg">+10.0% vs entry</span></div></div>
  <div class="dash-tile"><div class="dlabel">Gold (XAU)</div>
    <div class="dval">$4,007 <span class="chg-dn dchg">near $4,000 floor</span></div></div>
  <div class="dash-tile"><div class="dlabel">US 10Y yield</div>
    <div class="dval">4.45% <span class="chg-flat dchg">anchored</span></div></div>
  <div class="dash-tile"><div class="dlabel">US 2Y yield</div>
    <div class="dval">4.16% <span class="chg-flat dchg">Oct hike priced</span></div></div>
  <div class="dash-tile"><div class="dlabel">2s10s spread</div>
    <div class="dval">+29bp <span class="chg-up dchg">vs +15bp entry</span></div></div>
  <div class="dash-tile"><div class="dlabel">S&P 500</div>
    <div class="dval">7,358 <span class="chg-up dchg">above 7300 put</span></div></div>
  <div class="dash-tile"><div class="dlabel">VIX</div>
    <div class="dval">18.44 <span class="chg-flat dchg">near-term</span></div></div>
  <div class="dash-tile"><div class="dlabel">DXY</div>
    <div class="dval">101.68 <span class="chg-flat dchg">13-month high</span></div></div>
  <div class="dash-tile"><div class="dlabel">USDJPY</div>
    <div class="dval">161.84 <span class="chg-dn dchg">JPY weakening</span></div></div>
  <div class="dash-tile"><div class="dlabel">EURAUD</div>
    <div class="dval">1.6504 <span class="chg-dn dchg">12bp to stop</span></div></div>
</div>

<div class="info-banner">
  <strong>Stop-outs this cycle:</strong> MM-2026-002 Long Brent hit stop $84 (~Jun 16, -7.7%);
  MM-2026-005 Long Gold hit stop $4,250 (~Jun 19, -6.0%);
  MM-2026-006 Long AVGO hit stop $422 (Jun 7, -16.2%).
  AVGO stopped below $422 at $385.73 — stop level breached on the post-earnings gap-down.
</div>
"""

REGIME_LOG = """
<div class="section-label">Regime log</div>
<table class="cal-table">
  <thead><tr><th>Date</th><th>Regime</th></tr></thead>
  <tbody>
    <tr><td>2026-05-31</td><td>Book open — Hormuz binary; war premium + AI vertical</td></tr>
    <tr><td>2026-06-03</td><td>Brent near $98; Fed hike fully priced; AVGO pre-earnings</td></tr>
    <tr><td>2026-06-04</td><td>AVGO Q2 actuals (-13% AH); ADP 122k; AI revenue beat, 2027 guide held</td></tr>
    <tr><td>2026-06-07</td><td>Post-payrolls; AVGO stopped; Brent retreating from peak</td></tr>
    <tr><td>2026-06-11</td><td>ECB hike +25bp (first since 2023); HICP 3.2%; EUR bid</td></tr>
    <tr><td>2026-06-17</td><td>FOMC hold + hawkish dot; Iran-US MoU signed; oil selloff deepens</td></tr>
    <tr><td>2026-06-19</td><td>Two stops hit: Brent $84, Gold $4,250; Warsh October hike narrative builds</td></tr>
    <tr><td>2026-06-26</td><td>Hormuz unwind; Brent $74; Gold $4,007; EURAUD near stop; put spread expires tomorrow</td></tr>
  </tbody>
</table>
"""

VIX_SECTION = f"""
<div class="section-label">VIX term structure</div>
{vix_svg}
<div style="font-size:11px;color:var(--ink-mute);margin-top:4px">VIX 18.44 — elevated vs pre-crisis but off the conflict peak. Contango signals short-vol supply returning.</div>
"""

YC_SECTION = f"""
<div class="section-label">Yield curve</div>
{yc_svg}
<div style="font-size:11px;color:var(--ink-mute);margin-top:4px">2s10s +29bp (entry +15bp). 2Y anchored by Oct-hike pricing; 10Y held by fiscal supply + disinflation cross-current.</div>
"""

BOOK_SECTION = f"""
<div class="section-label">Trade book</div>
{live_book_html(trades)}
"""

# ── Final HTML ────────────────────────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Market Map {TODAY} — The Hormuz Unwind</title>
<script>(function(){{var t=localStorage.getItem('mm-theme');if(t==='dark')document.documentElement.setAttribute('data-theme','dark');}})();</script>
<style>{CSS}</style>
</head>
<body>
<div class="page">
  {MASTHEAD}
  <div class="two-col">
    <div class="lhs">
      {ARTICLE}
      {SINCE_LAST}
      {OPEN_TRADES_LHS}
      {OPEN_DETAIL}
      {CANARY_WATCH}
      {AMMO}
      {WEEK_AHEAD}
    </div>
    <div class="rhs">
      {DASH}
      {VIX_SECTION}
      {YC_SECTION}
      {BOOK_SECTION}
      {REGIME_LOG}
    </div>
  </div>
</div>
<script>
(function(){{
  var btn=document.getElementById('theme-toggle');
  function sync(){{btn.textContent=document.documentElement.getAttribute('data-theme')==='dark'?'☀ Light':'☾ Dark';}}
  sync();
  btn.addEventListener('click',function(){{
    var d=document.documentElement;
    var t=d.getAttribute('data-theme')==='dark'?'light':'dark';
    d.setAttribute('data-theme',t);
    try{{localStorage.setItem('mm-theme',t);}}catch(e){{}}
    sync();
  }});
}})();
</script>
</body>
</html>"""

out = os.path.join(HERE, "output.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"Wrote {len(HTML):,} bytes to {out}")
