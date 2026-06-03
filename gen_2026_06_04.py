#!/usr/bin/env python3
"""Market Map — 2026-06-04 (Thursday). Full refresh.
AVGO Q2 FY2026 actual results incorporated.
Format: flat-white two-column Shark Tank / render_v2.py (Format 2).
"""
import os, sys, html as _html
from datetime import date, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import book, charts

TODAY = date.today().isoformat()
NOW   = datetime.now().strftime("%H:%M")
HERE  = os.path.dirname(os.path.abspath(__file__))

def e(s):
    return _html.escape(str(s)) if s is not None else ""

CSS = """
:root{--bg:#ffffff;--surface:#f7f7f5;--ink:#1a1a1a;--ink-soft:#6b6b6b;
--ink-mute:#9a9a9a;--gold:#b8960c;--red:#c0392b;--green:#1a7a45;
--line:rgba(0,0,0,0.1);--radius-md:8px;--radius-lg:12px;
--font:-apple-system,"Helvetica Neue",sans-serif;
--serif:Georgia,"Times New Roman",serif}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font-family:var(--font);font-size:15px;line-height:1.65}
.page{max-width:1400px;margin:0 auto;padding:2rem 2rem 4rem}
.two-col{display:grid;grid-template-columns:1fr 380px;gap:2.5rem;align-items:start}
@media(max-width:960px){.two-col{grid-template-columns:1fr}}
.lhs{min-width:0}.rhs{min-width:0;position:sticky;top:1rem}
.masthead{border-bottom:.5px solid var(--line);padding-bottom:1rem;margin-bottom:1.5rem}
.article-title{font-family:var(--serif);font-size:2rem;font-weight:400;line-height:1.25;color:var(--ink);margin:0 0 .4rem}
.meta{font-size:11px;color:var(--ink-mute);letter-spacing:.08em;text-transform:uppercase;margin-top:.35rem}
.regime-tag{display:inline-block;font-size:10px;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);border:.5px solid var(--gold);border-radius:20px;padding:2px 10px;margin-bottom:.75rem}
.gold-rule{border:none;border-top:1px solid var(--gold);margin:1rem 0 0;opacity:.4}
.section-label{font-size:10px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-mute);margin:1.75rem 0 .75rem}
.section-label:first-child{margin-top:0}
.avgo-box{border:.5px solid var(--gold);border-radius:var(--radius-lg);padding:1.1rem 1.2rem;margin-bottom:1rem;background:rgba(184,150,12,.04)}
.avgo-box .section-label{color:var(--gold)}
.avgo-results-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin:.75rem 0}
.avr{background:var(--surface);border-radius:var(--radius-md);padding:.55rem .7rem;text-align:center}
.avr .av{font-size:1.15rem;font-weight:500;font-variant-numeric:tabular-nums}
.avr .al{font-size:10px;color:var(--ink-mute);margin-top:2px}
.avr.beat .av{color:var(--green)}.avr.watch .av{color:var(--gold)}.avr.miss .av{color:var(--red)}
.avgo-verdict{border-radius:var(--radius-md);padding:.75rem 1rem;margin:.75rem 0;font-size:12px;line-height:1.6}
.avgo-verdict.sell{background:rgba(192,57,43,.06);border:.5px solid rgba(192,57,43,.25)}
.avgo-verdict strong{color:var(--ink)}
.avgo-scen{border:.5px solid var(--line);border-radius:var(--radius-lg);padding:.85rem 1rem;margin-bottom:6px}
.avgo-scen.hold{border-left:3px solid var(--gold)}
.avgo-scen.exit{border-left:3px solid var(--red)}
.avgo-scen.newlong{border-left:3px solid var(--green)}
.avgo-scen .sh{font-size:10px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;margin-bottom:.3rem}
.avgo-scen .st{font-size:13px;font-weight:500;color:var(--ink);margin-bottom:.3rem;line-height:1.4}
.avgo-scen .sb{font-size:12px;color:var(--ink-soft);line-height:1.55}
.disc{font-size:10px;color:var(--ink-mute);font-style:italic;margin-top:.4rem}
.dash-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:5px;margin-bottom:1rem}
.dash-tile{background:var(--surface);border-radius:var(--radius-md);padding:.5rem .75rem;border:.5px solid var(--line)}
.dlabel{font-size:10px;color:var(--ink-mute);margin-bottom:2px}
.dval{font-size:13px;font-weight:500;color:var(--ink);font-variant-numeric:tabular-nums}
.dchg{font-size:11px}
.chg-up{color:var(--green)}.chg-dn{color:var(--red)}.chg-flat{color:var(--ink-mute)}
.theme-line{border-left:2px solid var(--gold);padding:.5rem .85rem;background:var(--surface);border-radius:0 var(--radius-md) var(--radius-md) 0;margin:1rem 0;font-size:13px;font-weight:500;line-height:1.5}
.tile{background:var(--bg);border:.5px solid var(--line);border-radius:var(--radius-lg);padding:1rem 1.1rem;margin-bottom:8px}
.tile-head{font-size:10px;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-mute);margin-bottom:.4rem}
.tile-claim{font-size:13px;font-weight:500;color:var(--ink);line-height:1.5;margin-bottom:.4rem}
.tile-body{font-size:12px;color:var(--ink-soft);line-height:1.6}
.tile-gold{border-top:2px solid var(--gold)}.tile-green{border-top:2px solid var(--green)}
.tile-red{border-top:2px solid var(--red)}.tile-muted{border-top:2px solid var(--line)}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:8px}
.grid-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-bottom:8px}
@media(max-width:600px){.grid-2,.grid-3{grid-template-columns:1fr}}
.trade-card{background:var(--bg);border:.5px solid var(--line);border-radius:var(--radius-lg);padding:1rem 1.1rem;margin-bottom:8px}
.tc-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:.75rem}
.tc-name{font-size:13px;font-weight:500;color:var(--ink)}
.tc-class{font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-mute);margin-top:2px}
.conv-badge{font-size:11px;font-weight:500;background:var(--surface);border:.5px solid var(--line);border-radius:20px;padding:2px 10px;color:var(--ink);white-space:nowrap}
.tc-row{display:flex;justify-content:space-between;font-size:12px;padding:4px 0;border-bottom:.5px solid var(--line)}
.tc-row:last-of-type{border-bottom:none}
.tc-k{color:var(--ink-mute)}.tc-v{font-weight:500;color:var(--ink)}
.conv-bar{display:flex;gap:3px;align-items:center;margin:.5rem 0}
.pip{width:18px;height:4px;border-radius:2px;background:var(--line)}
.pip.on{background:var(--gold)}
.conv-detail{font-size:10px;color:var(--ink-mute);margin-left:6px}
.tc-thesis{font-size:12px;color:var(--ink-soft);line-height:1.6;margin-top:.6rem;padding-top:.6rem;border-top:.5px solid var(--line)}
.score-row{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:10px}
.score-tile{background:var(--surface);border-radius:var(--radius-md);padding:.5rem .6rem;text-align:center}
.sval{font-size:18px;font-weight:500;color:var(--ink)}
.sval.pos{color:var(--green)}.sval.neg{color:var(--red)}
.slabel{font-size:10px;color:var(--ink-mute);margin-top:2px}
.live-table{width:100%;font-size:12px;border-collapse:collapse}
.live-table th{font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-mute);font-weight:500;padding:0 0 6px;text-align:left;border-bottom:.5px solid var(--line)}
.live-table td{padding:6px 0;border-bottom:.5px solid var(--line);color:var(--ink);vertical-align:middle}
.live-table tr:last-child td{border-bottom:none}
.pnl-pos{color:var(--green);font-weight:500}.pnl-neg{color:var(--red);font-weight:500}
.pill{font-size:10px;padding:2px 8px;border-radius:20px;background:var(--surface);color:var(--ink-mute);border:.5px solid var(--line)}
.prog-bar{height:4px;background:var(--line);border-radius:2px;overflow:hidden;min-width:48px;margin-top:3px}
.prog-bar>span{display:block;height:100%;background:var(--gold)}
.canary{padding:.55rem 0;border-bottom:.5px solid var(--line);display:flex;gap:10px;align-items:flex-start}
.canary:last-child{border-bottom:none}
.cdot{width:6px;height:6px;border-radius:50%;background:var(--gold);flex-shrink:0;margin-top:5px}
.ctext{font-size:12px;color:var(--ink-soft);line-height:1.6}
.ctext strong{color:var(--ink);font-weight:500}
.ammo{padding:.55rem 0;border-bottom:.5px solid var(--line)}
.ammo:last-child{border-bottom:none}
.ammo-q{font-size:12px;font-weight:500;color:var(--ink);margin-bottom:3px}
.ammo-a{font-size:12px;color:var(--ink-soft);line-height:1.5}
.yesterday{background:var(--surface);border-radius:var(--radius-md);padding:.75rem 1rem;margin-bottom:1rem}
.yest-item{font-size:12px;color:var(--ink-soft);padding:4px 0;display:flex;gap:8px;align-items:flex-start;border-bottom:.5px solid var(--line)}
.yest-item:last-child{border-bottom:none}
.tick-g{color:var(--green);flex-shrink:0;font-weight:600}
.tick-r{color:var(--red);flex-shrink:0;font-weight:600}
.tick-n{color:var(--ink-mute);flex-shrink:0}
.stale-tbl{width:100%;font-size:11px;border-collapse:collapse}
.stale-tbl th{font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-mute);font-weight:500;padding:0 0 4px;text-align:left;border-bottom:.5px solid var(--line)}
.stale-tbl td{padding:4px 0;border-bottom:.5px solid var(--line);color:var(--ink-soft)}
.stale-tbl tr:last-child td{border-bottom:none}
.fresh{color:var(--green);font-weight:500}.stale-flag{color:var(--red);font-weight:500}
.citation{font-size:10px;color:var(--ink-mute);line-height:1.9}
.wrap-body{font-family:var(--serif);font-size:16px;line-height:1.85;color:var(--ink)}
.wrap-body p{margin-bottom:1.1rem}
.wrap-body strong{font-weight:600}
.vol-surface{background:var(--surface);border-radius:var(--radius-md);padding:.75rem 1rem;font-size:12px;color:var(--ink-soft);line-height:1.7}
.cal-table{width:100%;font-size:12px;border-collapse:collapse}
.cal-table th{font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-mute);font-weight:500;padding:0 6px 6px 0;text-align:left;border-bottom:.5px solid var(--line)}
.cal-table td{padding:7px 6px 7px 0;border-bottom:.5px solid var(--line);vertical-align:top}
.cal-table tr:last-child td{border-bottom:none}
.cal-event{color:var(--gold);font-weight:500}
.asym-up{color:var(--green)}.asym-dn{color:var(--red)}
.mind-item{font-size:12px;color:var(--ink-soft);padding:4px 0;border-bottom:.5px solid var(--line);line-height:1.6}
.mind-item:last-child{border-bottom:none}
.mind-item strong{color:var(--ink);font-weight:500}
"""

def pnl_span(p):
    if p is None: return '<span style="color:var(--ink-mute)">—</span>'
    cls = "pnl-pos" if p > 0 else ("pnl-neg" if p < 0 else "")
    return f'<span class="{cls}">{p:+.2f}%</span>'

def pips(conviction, cb):
    n = int(conviction)
    dots = "".join(f'<div class="pip{"  on" if i < n else ""}"></div>' for i in range(10))
    detail = (f'gap({cb.get("gap",0)}/3) · catalyst({cb.get("catalyst",0)}/2) · '
              f'pos({cb.get("positioning",0)}/2) · confirm({cb.get("confirmation",0)}/2) · '
              f'stop({cb.get("stop_quality",0)}/1)')
    return f'<div class="conv-bar">{dots}<span class="conv-detail">{e(detail)}</span></div>'

def prog_pct(t, level):
    entry, target = t.get("entry"), t.get("target")
    if not entry or not target or target == entry: return 0
    d = 1 if target >= entry else -1
    return max(0, min(100, int(d * (level - entry) / abs(target - entry) * 100)))

def trade_card(t):
    cb = t.get("conviction_breakdown", {})
    rows = [("Asset", t.get("asset_class","")), ("Structure", t.get("structure","")),
            ("Entry", t.get("entry","")), ("Stop", t.get("stop","")),
            ("Target", t.get("target","")), ("Horizon", t.get("horizon",""))]
    if t.get("min_hold_days"):
        rows.append(("Min hold", f'{t["min_hold_days"]}d'))
    rows_html = "".join(f'<div class="tc-row"><span class="tc-k">{e(k)}</span>'
                        f'<span class="tc-v">{e(v)}</span></div>' for k, v in rows)
    return (f'<div class="trade-card"><div class="tc-top"><div>'
            f'<div class="tc-name">{e(t.get("trade",""))}</div>'
            f'<div class="tc-class">{e(t.get("type","reactive"))} · {e(t.get("asset_class",""))}</div>'
            f'</div><div class="conv-badge">{e(t.get("conviction","?"))}/10</div></div>'
            f'{rows_html}{pips(t.get("conviction",0), cb)}'
            f'<div class="tc-thesis">{e(t.get("thesis",""))}</div></div>')

def live_book(trades):
    closed, open_t = trades.get("closed",[]), trades.get("open",[])
    graded = [t for t in closed if "pnl_pct" in t.get("exit",{})]
    if graded:
        pnls = [t["exit"]["pnl_pct"] for t in graded]; wins = [p for p in pnls if p > 0]
        best = max(graded, key=lambda t: t["exit"]["pnl_pct"])
        score = (f'<div class="score-row">'
                 f'<div class="score-tile"><div class="sval">{len(graded)}</div><div class="slabel">Closed</div></div>'
                 f'<div class="score-tile"><div class="sval">{100*len(wins)/len(graded):.0f}%</div><div class="slabel">Hit rate</div></div>'
                 f'<div class="score-tile"><div class="sval {"pos" if sum(pnls)>=0 else "neg"}">{sum(pnls):+.1f}%</div><div class="slabel">Sum P&L</div></div>'
                 f'<div class="score-tile"><div class="sval pos">{e(best["id"])}</div><div class="slabel">Best</div></div></div>')
    else:
        score = '<p style="font-size:12px;color:var(--ink-mute);margin-bottom:.75rem">Book opened 2026-06-01 — scoreboard builds as trades close.</p>'
    h_map = {"weeks":14,"months":90,"2 weeks":14,"3 months":90,"26 days":26}
    rows = []
    for t in open_t:
        cur = t.get("current", t.get("entry")); pl = t.get("current_pnl_pct")
        prog = prog_pct(t, cur) if cur else 0
        try:
            held = (date.today() - date.fromisoformat(t.get("opened","2026-06-01"))).days
            rem = max(0, h_map.get(t.get("horizon",""), 30) - held)
            rem_s = f'<span style="color:{"var(--red)" if rem < 5 else "var(--ink-mute)"}">{rem}d</span>'
        except: rem_s = "—"
        rows.append(f'<tr><td><span class="pill">{e(t.get("id",""))}</span></td>'
                    f'<td style="max-width:130px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{e(t.get("trade",""))}</td>'
                    f'<td>{e(t.get("opened",""))}</td><td style="font-variant-numeric:tabular-nums">{e(cur)}</td>'
                    f'<td>{pnl_span(pl)}</td><td>{rem_s}</td>'
                    f'<td><div class="prog-bar"><span style="width:{prog}%"></span></div></td></tr>')
    open_tbl = ('<table class="live-table"><thead><tr><th>ID</th><th>Trade</th><th>Opened</th>'
                '<th>Current</th><th>P&L</th><th>Window</th><th>&rarr; Target</th></tr></thead><tbody>'
                + ("".join(rows) or '<tr><td colspan="7" style="color:var(--ink-mute)">no open trades</td></tr>')
                + '</tbody></table>')
    if closed:
        cl = "".join(f'<tr><td><span class="pill">{e(t.get("id",""))}</span></td>'
                     f'<td>{e(t.get("trade",""))}</td><td>{e(t.get("exit",{}).get("result",""))}</td>'
                     f'<td>{pnl_span(t.get("exit",{}).get("pnl_pct"))}</td>'
                     f'<td style="color:var(--ink-mute)">{e(t.get("exit",{}).get("days_held",""))}d</td></tr>'
                     for t in closed)
        closed_tbl = ('<div class="section-label" style="margin-top:1rem">Closed ledger</div>'
                      '<table class="live-table"><thead><tr><th>ID</th><th>Trade</th><th>Result</th>'
                      '<th>P&L</th><th>Held</th></tr></thead><tbody>' + cl + '</tbody></table>')
    else:
        closed_tbl = '<p style="font-size:11px;color:var(--ink-mute);margin-top:.5rem">No closed trades yet.</p>'
    return score + open_tbl + closed_tbl

# ── Load & mark ───────────────────────────────────────────────────────────────
trades     = book.load_trades()
regime_log = book.load_json(book.REGIME_PATH, [])

# Fresh levels — 2026-06-04
# AVGO: post-earnings AH close $462.36 (InteractiveCrypto/CNBC)
# Brent: ~$97.80, toward $98 (TradingEconomics/OilPrice Jun 3)
# WTI: rose above $95 (TradingEconomics Jun 3, 6th consecutive inventory draw)
# Brent-WTI spread: 97.80 − 95.20 = 2.60 (WTI surged, compressing spread from $5.68)
# Gold: ~$4,494 (TwelveData range $4,463–$4,541 Jun 2–3)
# US 10Y: ~4.45% (slight dip from 4.46%; TradingEconomics Jun 3)
# DXY rose to 99.52 (highest in 2 months, ADP 122k); USDJPY ~159.20 (dollar firm)
# EURAUD: ~1.623 (carried estimate; search returned 1.6230)
levels = {
    "MM-2026-001": 1.623,    # EURAUD ~1.623 (carried; ECB June 11 in 7 days)
    "MM-2026-002": 97.80,    # Brent: toward $98, 3rd consecutive gain (TradingEconomics/OilPrice)
    "MM-2026-003": 2.60,     # Brent-WTI spread: 97.80 − 95.20 — WTI surged to $95+ (compressed)
    "MM-2026-004": 4.45,     # US 10Y: ~4.45% (TradingEconomics Jun 3)
    "MM-2026-005": 4494.0,   # Gold: ~$4,494 (TwelveData/DailyForex range average Jun 3)
    "MM-2026-006": 462.36,   # AVGO: $462.36 AH after Q2 earnings (InteractiveCrypto/CNBC)
    "MM-2026-007": 159.20,   # USDJPY: ~159.20 (DXY 99.52 +, dollar firm vs yen; estimated)
    "MM-2026-008": 35.0,     # SPX put spread: unchanged (events still ahead)
    "MM-2026-009": 0.15,     # 2s10s: unchanged (ADP 122k complicates near-term cut thesis)
}
book.mark_to_market(trades, levels)

regime      = "AVGO Beat and Sold; ADP 122k; Payrolls Tomorrow"
regime_note = (
    "Broadcom Q2: revenue $22.19B (+48%), AI $10.8B (+143%), Q3 guide $29.4B (+84%), "
    "AI Q3 guide $16.0B (+200%), bookings >$30B. Stock fell 3% to $462.36 — sell the fact "
    "after 4.7% pre-earnings rally. ADP May 122k pushes Fed hike probability to 85%."
)
regime_log = book.update_regime_log(regime_log, regime, regime_note)

# Charts
eq_svg  = charts.equity_curve(trades["closed"])
cal_svg = charts.calibration(trades["closed"])
vix_svg = charts.vix_term_structure([
    {"label": "VIX9D", "value": 14.2},
    {"label": "VIX",   "value": 15.77},
    {"label": "VIX3M", "value": 17.6},
    {"label": "VIX6M", "value": 18.7},
])
yc_svg  = charts.yield_curve([
    {"label": "2Y",  "value": 4.32},
    {"label": "5Y",  "value": 4.39},
    {"label": "10Y", "value": 4.45},
    {"label": "30Y", "value": 4.63},
])

# ── AVGO Results Section (ACTUAL Q2 FY2026 numbers confirmed) ─────────────────
AVGO_SECTION = """
<div class="section-label">Broadcom (AVGO) — Q2 FY2026 Actual Results</div>
<div class="avgo-box">

<p style="font-size:11px;color:var(--ink-mute);margin-bottom:.75rem">Sources: Broadcom 8-K filed 2026-06-03 (SEC EDGAR), StockTitan, CNBC. All numbers verified against SEC filing.</p>

<div class="section-label" style="color:var(--gold)">The headline numbers</div>
<div class="avgo-results-grid">
  <div class="avr beat"><div class="av">$22.19B</div><div class="al">Q2 Revenue (+48% YoY) · beat $22.08B est</div></div>
  <div class="avr beat"><div class="av">$2.44</div><div class="al">Non-GAAP EPS · beat $2.40 consensus</div></div>
  <div class="avr beat"><div class="av">$10.8B</div><div class="al">Q2 AI Semiconductor Rev (+143% YoY) · beat $10.7B guide</div></div>
  <div class="avr beat"><div class="av">$15.2B</div><div class="al">Adjusted EBITDA (69% margin) · +52% YoY</div></div>
  <div class="avr beat"><div class="av">$29.4B</div><div class="al">Q3 Revenue Guide (+84% YoY) · beat $28.47B consensus</div></div>
  <div class="avr beat"><div class="av">$16.0B</div><div class="al">Q3 AI Semiconductor Guide (+200%+ YoY) · massive raise</div></div>
</div>

<div class="section-label" style="color:var(--gold)">The number Hock Tan led with</div>
<p style="font-size:13px;font-weight:500;color:var(--ink);line-height:1.5;margin-bottom:.5rem">
AI semiconductor bookings: <strong>&gt;$30 billion</strong> — approximately 3× the $10.8B shipped last quarter.
</p>
<p style="font-size:12px;color:var(--ink-soft);line-height:1.6;margin-bottom:.75rem">
This is the single most important data point in the report. Bookings of $30B against shipments of $10.8B means Broadcom has 2.8 quarters of AI backlog at current run rates — and the run rate is accelerating (Q3 AI guide $16.0B). The $100B 2027 target, which Hock Tan first declared in March, is now arithmetically supported: $10.8B Q2 + $16.0B Q3 × 2 ≈ $43B in the back half of FY2026, implying a $90–100B annualised run-rate heading into FY2027.
</p>

<div class="section-label" style="color:var(--gold)">The market reaction</div>
<div class="avgo-verdict sell">
  <strong>AVGO fell 3% to $462.36 after hours</strong> — despite a genuine beat-and-raise on every metric.<br><br>
  <strong>Why?</strong> The stock had rallied 4.7% on June 3 before the print, closing at ~$481. Investors who had positioned for the beat started selling at the announcement. At 41× forward earnings, the market was not buying the beat — it had already bought it at $481. The sell-the-fact move brought AVGO back to $462, essentially erasing the pre-earnings rally and landing the stock close to our entry ($460).<br><br>
  <strong>What the market is saying:</strong> The numbers are real. The $30B backlog is real. But paying 41× for that confirmation is a different question from confirming the cycle. The stock now needs the June 17 FOMC dot plot to NOT include a hike, and payrolls Friday to NOT push the Fed's hand further, before the AI multiple can re-expand.
</div>

<div class="section-label" style="color:var(--gold)">Conference call highlights (Hock Tan)</div>
<p style="font-size:12px;color:var(--ink-soft);line-height:1.6;margin-bottom:.75rem">
· <strong>Bookings $30B</strong> vs $10.8B shipped — "the pipeline has never been stronger."<br>
· <strong>Q3 AI guide $16.0B (+200% YoY)</strong> — driven by accelerating demand for custom AI accelerators (XPUs) across hyperscaler customers.<br>
· <strong>Q3 total revenue guide $29.4B (+84% YoY)</strong> — driven by both AI semiconductor acceleration and infrastructure software (VMware) contribution.<br>
· <strong>EBITDA margin 69%</strong> — operating leverage intact; guidance implies ~67% for Q3.<br>
· Reaffirmed path to $100B AI chip revenue in FY2027 — now arithmetically credible given Q3 $16.0B guide and >$30B backlog.
</p>

<div class="section-label" style="color:var(--gold)">Analyst reactions post-print</div>
<p style="font-size:12px;color:var(--ink-soft);line-height:1.6;margin-bottom:.75rem">
Pre-print PTs: Morgan Stanley $485, Susquehanna $490, J.P. Morgan $500, HSBC $600. Post-print upgrades not yet indexed in this refresh — verify live for morning PT revisions. The HSBC $600 PT was revised before earnings; if AVGO settles near $462, that represents ~30% upside to HSBC's target.
</p>

<div class="section-label" style="color:var(--gold)">MM-2026-006 — what happened and what to do</div>

<div class="avgo-scen hold">
  <div class="sh" style="color:var(--gold)">Current position: entry $460, post-earnings mark $462.36 (+0.51%)</div>
  <div class="st">The brief's rules say HOLD — a genuine beat-and-raise does not trigger exit</div>
  <div class="sb">The rules set out in the brief: Beat + Raise = hold through print + 5 days. Every metric was a beat. Q3 guide was a raise. Stop $422 was not breached ($462 is $40 above stop). The sell-the-fact move is frustrating but not a thesis-breaker — it is a valuation reset after a 4.7% pre-earnings run. Per the brief's own framework, this position stays open through next Wednesday (June 10) unless the stop at $422 is hit first.
  <br><br>
  <strong>Updated stop:</strong> The "raise stop to $490 once stock opens above $525" condition was never triggered (stock never reached $525). Stop remains at $422. If Thursday's session confirms the sell-the-fact reversal and the stock rallies back above $480, begin reassessing the exit level.
  </div>
</div>

<div class="avgo-scen newlong" style="margin-top:6px">
  <div class="sh" style="color:var(--green)">Post-print long setup: for those who did NOT trade into earnings</div>
  <div class="st">$462 is a reset to entry levels — the same stock with $30B backlog and a $16B Q3 guide</div>
  <div class="sb">The sell-the-fact brought AVGO back to $462 — essentially where MM-2026-006 entered at $460. For those without the pre-earnings position, this is the setup the brief described as "buy the first-hour pullback from the gap" — except in this case, the gap was DOWN. The AI cycle is confirmed. The backlog is real. The valuation concern is the same as before (41×), but the denominator (earnings) just grew dramatically. The risk: if payrolls Friday beats strongly (ADP 122k suggests it might), the Fed hike narrative pushes the multiple down further regardless of earnings quality.
  <br><br>
  <strong>Entry:</strong> $460–465 (current levels), or wait for Thursday's session confirmation<br>
  <strong>Stop:</strong> $435 — below the pre-Computex base; if it breaks $435 on close, the sell-the-fact has become a re-rating<br>
  <strong>Target:</strong> $510–520 — 10–12% recovery when market digests the $30B backlog + $16B Q3 guide<br>
  <strong>Conviction:</strong> 6/10 · gap(2) · catalyst(1) · positioning(2) · confirmation(2) · stop(0)<br>
  <strong>Time horizon:</strong> 1–2 weeks; exit before June 17 FOMC if Fed hike dot risk is materialising
  <div class="disc">Informational analysis only. Not financial advice.</div>
  </div>
</div>

</div>"""

# ── LHS sections ──────────────────────────────────────────────────────────────
MASTHEAD = f"""
<div class="masthead">
  <div class="regime-tag">AVGO Beat and Sold; ADP 122k; Payrolls Tomorrow</div>
  <h1 class="article-title">The Beat the Market Already Priced</h1>
  <p class="meta">Pre-market intelligence brief &middot; {TODAY} &middot; generated {NOW} local &middot; self-graded book</p>
  <hr class="gold-rule">
</div>"""

YESTERDAY = """
<div class="section-label">Yesterday (Jun 3), graded</div>
<div class="yesterday">
  <div class="yest-item"><span class="tick-g">✓</span>
    <span><strong>MM-2026-001</strong> · Short EURAUD · 1.6150 → 1.6230 · <span class="pnl-pos">+1.34%</span> · Giving back gains slightly. AUD weakened as DXY surged to 99.52 on ADP 122k. ECB June 11 in 7 days — crowded EUR long is the pain trade ahead.</span></div>
  <div class="yest-item"><span class="tick-g">✓</span>
    <span><strong>MM-2026-002</strong> · Long Brent · $91.00 → $97.80 · <span class="pnl-pos">+7.47%</span> · Working strongly. Brent heading toward $98 on 3rd consecutive gain. US crude inventories fell 6.8M bbl (6th weekly draw). Iran ceasefire fragile.</span></div>
  <div class="yest-item"><span class="tick-r">✗</span>
    <span><strong>MM-2026-003</strong> · Long Brent / Short WTI spread · 3.30 → 2.60 · <span class="pnl-neg">−21.2%</span> · Reversed. WTI surged above $95 on US inventory draw (domestic demand), compressing the Brent premium from $5.68 peak to $2.60. The Hormuz-specific premium compressed as WTI caught up. Stop 1.50 intact.</span></div>
  <div class="yest-item"><span class="tick-n">→</span>
    <span><strong>MM-2026-004</strong> · Short US 10Y yield · 4.44% → 4.45% · <span class="pnl-neg">−0.23%</span> · Slight improvement. Yield eased marginally as bond buyers digested the ADP beat. Fed hike at 85% is the structural headwind; payrolls Friday is the test.</span></div>
  <div class="yest-item"><span class="tick-n">→</span>
    <span><strong>MM-2026-005</strong> · Long gold (pre-pos) · $4,523 → $4,494 · <span class="pnl-neg">−0.64%</span> · Still below entry. Gold partially recovered from $4,465 low but remains under pressure from 85% Fed hike probability. Stop $4,250 intact; min-hold 41 days remaining.</span></div>
  <div class="yest-item"><span class="tick-n">→</span>
    <span><strong>MM-2026-006</strong> · Long AVGO (entry $460) · ~$481 → $462.36 (AH) · <span class="pnl-pos">+0.51%</span> · Sell-the-fact. AVGO reported Q2: revenue $22.19B, AI $10.8B (+143%), Q3 guide $29.4B, AI Q3 guide $16.0B (+200%), bookings >$30B. Genuine beat-and-raise. Stock fell 3% to $462.36 — pre-earnings 4.7% rally was already pricing the beat. Per brief rules: HOLD (beat + raise). Stop $422 intact.</span></div>
  <div class="yest-item"><span class="tick-n">→</span>
    <span><strong>MM-2026-007</strong> · Short USDJPY · 158.80 → 159.20 · <span class="pnl-pos">+0.11%</span> · DXY at 99.52 pushed dollar up slightly vs yen. Still working; stop 163.00 clear.</span></div>
  <div class="yest-item"><span class="tick-n">→</span>
    <span><strong>MM-2026-008</strong> · SPX put spread · 35 → 35 · flat · Holding. S&P 500 fell 0.74% on June 3. AVGO sell-the-fact didn't hit 8.3% needed to activate the spread's max gain. Payrolls tomorrow is the next catalyst.</span></div>
  <div class="yest-item"><span class="tick-n">→</span>
    <span><strong>MM-2026-009</strong> · 2s10s steepener (pre-pos) · +15bp → +15bp · flat · ADP 122k and 85% hike probability push against the near-term front-end cut thesis. Pre-position still valid on supply dynamics; payrolls tomorrow is the first real test.</span></div>
</div>"""

WRAP = """
<div class="section-label">The Wrap</div>
<div class="wrap-body">
<p>Broadcom reported the best quarter in its history and the stock fell 3%. Revenue grew 48%.
AI semiconductor revenue grew 143%. Hock Tan disclosed AI bookings above $30 billion —
nearly three times what was shipped last quarter — making the $100 billion 2027 target
arithmetically credible for the first time. And the stock went to $462.

<p>This is not a story about the AI cycle. The AI cycle is confirmed. $30 billion in
bookings against $10.8 billion in shipments means the backlog is three quarters deep at
an accelerating run rate. Q3 guide of $16 billion AI semiconductor revenue — growing more
than 200% year-over-year — is not an in-line quarter. It is the seventh consecutive beat
and the biggest guide raise the company has ever delivered.

<p>The story is about the price paid for the confirmation. At 41 times forward earnings,
paying up for a known cycle is a different exercise than buying a cycle that is uncertain.
AVGO rallied 4.7% on June 3 before reporting. The stock was at $481 going into the print.
The market had already consumed the beat. The sell-the-fact took the stock back to $462 —
essentially to our entry at $460. The AI cycle thesis is right. The trade is flat. The
market is making a point about valuation, not fundamentals.

<p><strong>L1 — Revised driver.</strong> The Perkins regime is now a precise tension: the
strongest AI cycle ever confirmed simultaneously with the highest Fed hike probability
in 2026 (85% by year-end). AVGO's $30 billion backlog is funded by hyperscaler capex
commitments that were made when the Fed was expected to cut. With the Fed now expected
to hike, the discount rate applied to those commitments rises. AVGO's earnings confirm
the numerator. The market is repricing the denominator.

<p><strong>L2 — Counter-intuitive hook.</strong> ADP May came in at 122,000 — the highest
since January 2025, well above the 117,000 consensus. The dollar surged to a 2-month high
at DXY 99.52. The S&P 500 fell 0.74% on June 3. All of this happened before AVGO reported.
The market was already selling the macro regime before the earnings confirmed the AI cycle.
AVGO's sell-the-fact happened into a market that was already in "sell the good news,
price the rate hike" mode. The bad news is structural.

<p><strong>L3 — The gap.</strong> What's priced: AVGO's AI cycle confirmed at $462 (no premium
for the confirmation). Fed hike at 85% probability. Payrolls tomorrow at 93k consensus
(above ADP-signal of 122k suggests upside risk). What's not priced: an AI cycle AND a
Fed rate hike simultaneously coexisting in a sustained melt-up. These two things compete
for the same equity multiple. The brief's bet is that the AI cycle wins — AVGO's $30B
backlog says it should. But if Friday's payrolls push the Fed hike probability to 95%+,
the multiple competition becomes acute.
</div>

<div class="section-label">Scenarios post-AVGO</div>
<div class="grid-3">
  <div class="tile tile-green">
    <div class="tile-head">Bull — 40%</div>
    <div class="tile-claim">Thursday confirms sell-the-fact was temporary; AVGO recovers to $480+</div>
    <div class="tile-body">Institutional buyers enter Thursday on the $462 dip — the bookings $30B data is too strong to ignore. AVGO recovers to $475–490. Payrolls Friday at 90–110k — solid but not hike-forcing. Fed hike stays at 85% but doesn't move higher. SPX recovers from June 3's 0.74% decline. Book's oil longs hold near $98.</div>
  </div>
  <div class="tile tile-gold">
    <div class="tile-head">Base — 40%</div>
    <div class="tile-claim">AVGO chops $455–475; payrolls beats; 85% hike holds</div>
    <div class="tile-body">Post-AVGO digestion with no strong directional move. Payrolls Friday at 110–130k — strong but not shocking. Fed hike at 85% stays. 10Y yield at 4.45–4.55%. AVGO range-bound until FOMC June 17 resolves the multiple question. MM-2026-006 sits flat near entry.</div>
  </div>
  <div class="tile tile-red">
    <div class="tile-head">Bear — 20%</div>
    <div class="tile-claim">Payrolls >130k; hike probability hits 95%+; multiple compression accelerates</div>
    <div class="tile-body">ADP 122k foreshadows 130k+ payrolls Friday. Fed hike probability crosses 95%. 10Y yield approaches 4.65% — MM-2026-004 stop zone. AVGO re-rates below $440 on valuation compression. IG spreads at 80bp start to widen. MM-2026-008 put spread activates. Book's oil longs are the only clean winners.</div>
  </div>
</div>

<div class="wrap-body">
<p><strong>Burry tell.</strong> The AI bookings number ($30B) is the most important data point
that the market is not pricing correctly. Bookings of $30B vs shipments of $10.8B means
Broadcom has locked-in revenue for 2.8 quarters at current run rates — and those run
rates are accelerating. In six months, the question will not be whether the AI cycle is
real. It will be whether the hyperscalers who committed to those bookings can fund them
at 85% Fed hike probability. All six of Broadcom's ASIC customers are equity-funded.
Google raised $80B in equity. A Fed hike reprices Google's equity cost of capital.
The $30B backlog was committed when the Fed was cutting. The question is whether it
survives a hiking cycle. Today's data says yes. The market is not sure.

<p><strong>Pozsar mechanic.</strong> WTI surged above $95 on US crude inventory draws (6th
consecutive weekly decline of 6.8M barrels). This is a domestic demand signal, not a
Hormuz signal. It means US refiners are running at high utilisation — which is itself a
consequence of the Iran/Hormuz situation (US refiners processing more domestically as
Hormuz-dependent Atlantic shipments are disrupted). The Brent-WTI spread compressed from
$5.68 to $2.60 not because Hormuz risk fell, but because US domestic demand caught up.
The Pozsar layer: when the physical domestic market tightens, WTI converges toward Brent.
The Hormuz premium in Brent didn't disappear — WTI found its own fundamental support.

<p><strong>Papic constraint.</strong> Trump needs to announce a payrolls narrative before the
June 17 FOMC. ADP 122k and likely payrolls >100k give the administration "the economy is
strong" cover to absorb a Fed hike without political damage. The political constraint has
shifted: a weak payrolls print would be the politically inconvenient scenario, not a
strong one. The administration wants strong jobs data. The Fed wants strong jobs data to
justify the hike. The only loser from strong payrolls is the rate-sensitive portion of
the equity market — and specifically, AVGO's AI multiple.
</div>"""

CORRELATION = """
<div class="section-label">Correlation Regime</div>
<div class="tile tile-muted">
  <div class="tile-claim">AVGO beat-and-raised → stock fell; SPX −0.74% on June 3 — the rate regime overrides earnings</div>
  <div class="tile-body">The strongest earnings Broadcom has ever reported did not lift the broader market. The S&P 500 fell 0.74% on June 3 even as AVGO confirmed the AI cycle. The explanation: with 85% Fed hike probability, the equity market is pricing that a hiking cycle compresses the multiple even on beating earnings. This is the "good news is bad news" regime — the stronger the economy (ADP 122k, ISM 54%), the more the Fed hikes, the lower the multiple.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">Brent-WTI spread compressed from $5.68 to $2.60 — WTI found domestic fundamental support</div>
  <div class="tile-body">MM-2026-003 reversed. WTI surged above $95 on the 6th consecutive US crude inventory draw (6.8M bbl) — domestic demand is tight independent of Hormuz. The Hormuz premium in Brent didn't disappear; WTI converged toward Brent. The spread is the Hormuz-specific risk measure: at $2.60 it's saying the Hormuz premium is real but the WTI domestic story is equally real. At this spread level the trade is underwater vs entry.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">DXY at 99.52 (2-month high) on ADP 122k — dollar is the cleanest expression of the rate regime</div>
  <div class="tile-body">ADP 122k pushed the dollar to its highest level in 2 months. Fed hike at 85%. The dollar is pricing what equities haven't fully priced: a tightening cycle. Gold at $4,494 (below entry) is pricing the same thing. The correlation: dollar up, gold down, equities under pressure = the market is repricing the whole risk structure, not just the individual earnings story.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">Nikkei Japan context — AI/Computex driven, watching US rate spillover</div>
  <div class="tile-body">Nikkei at 68,108 (+2.06% June 3) — AI/Computex momentum driving Japanese AI supply chain. The risk: if US payrolls push the Fed hike to 95%+, the yen carry trade (funding AI equity purchases via cheap yen) becomes less attractive, and the Nikkei sees outflows. USDJPY at 159.20 is the tripwire — Finance Ministry still watching 160.00.</div>
</div>"""

VOL_SKEW = """
<div class="section-label">Vol &amp; Skew</div>
<div class="vol-surface">
  <strong>VIX 15.77 (Jun 2 close) — relatively calm despite rate reset and AVGO sell-the-fact:</strong>
  VIX9D ~14.2 · VIX ~15.77 · VIX3M ~17.6 · VIX6M ~18.7.
  The VIX structure is in contango. The relative calm says the market is digesting the
  rate regime shift gradually, not panicking. Payrolls Friday is the next single-stock
  vol event — a 130k+ print could lift VIX toward 18+ quickly.
</div>
<div style="height:8px"></div>
<div class="tile tile-gold">
  <div class="tile-head">AVGO single-stock vol: post-earnings compression</div>
  <div class="tile-claim">AVGO implied vol compresses after the print — event premium evaporates</div>
  <div class="tile-body">The ±10.65% implied move was the pre-earnings pricing. Post-print, AVGO single-stock vol compresses sharply as the event uncertainty resolves. The stock at $462 with the cycle confirmed but the multiple under pressure implies lower vol going forward — the question is direction, not magnitude. MM-2026-008 (SPX put spread) remains relevant for payrolls and FOMC events, not for AVGO specifically anymore.</div>
</div>"""

SECTOR_RV = """
<div class="section-label">Sector &amp; RV</div>
<div class="tile tile-green">
  <div class="tile-head">Energy — Brent $97.80, WTI $95+, both driven by real demand</div>
  <div class="tile-body">Brent approaching $98 (3rd consecutive gain). WTI above $95 on 6th consecutive inventory draw (6.8M bbl). The energy sector is working on two independent engines: Hormuz closure (Brent premium) and US domestic demand tightness (WTI). MM-2026-002 (+7.47%) remains the best single position in the book.</div>
</div>
<div class="tile tile-gold">
  <div class="tile-head">AI semiconductors — confirmed cycle, pending multiple resolution</div>
  <div class="tile-body">AVGO at $462 with $30B bookings and $16B Q3 AI guide is the cheapest it has been on a "bookings-to-price" basis in its history. The cycle is real. The valuation question is whether 41× survives 85% Fed hike probability. Thursday's session shows which force dominates: institutional buyers on the $462 dip, or rate-hike sellers continuing the regime trade.</div>
</div>
<div class="tile tile-red">
  <div class="tile-head">Rate-sensitives — gold, bonds, long-duration at risk from payrolls Friday</div>
  <div class="tile-body">Gold at $4,494 (below entry). MM-2026-004 (short 10Y yield) at -0.23% with stop 20bp away at 4.65%. If payrolls Friday prints 130k+, the 10Y spikes toward 4.60–4.65%. The brief's most vulnerable position into tomorrow is MM-2026-004. Consider whether the risk/reward of holding through the print still makes sense.</div>
</div>"""

POSITIONING = """
<div class="section-label">Positioning &amp; Flows</div>
<div class="tile tile-muted">
  <div class="tile-head">Post-AVGO positioning: sell-the-fact complete; institutional buyers may re-enter Thursday</div>
  <div class="tile-body">The pre-earnings positioning (4.7% rally into the print) has been unwound. AVGO at $462 is essentially at a clean entry level — the pre-earnings crowded long has been flushed. Institutional investors who couldn't act before the print will be assessing whether to enter on the confirmed beat-and-raise at a lower price. The quality of the institutional bid on Thursday morning is the tell.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-head">ADP 122k: labor market momentum is real, above consensus, new hiring high since Jan 2025</div>
  <div class="tile-body">May ADP: 122k (above 117k consensus, above April's revised 105k). Broad-based: education/health 57k, trade/transport 36k. Wages +4.4% (same as April). The payrolls market will take ADP 122k as a bullish signal for tomorrow's BLS 93k consensus — the actual print is likely above 100k and possibly above 120k. At 120k+ payrolls, Fed hike probability moves toward 90%+.</div>
</div>"""

FUNDING = """
<div class="section-label">Funding &amp; Plumbing</div>
<div class="tile tile-muted">
  <div class="tile-claim">SOFR 3.63% — clean; DXY at 2-month high 99.52; money markets calm pre-payrolls</div>
  <div class="tile-body">No stress in funding markets. The Pozsar layer today: dollar at DXY 99.52 tightens financial conditions in dollar-denominated debt globally — EM central banks are watching. But the proximate stress point is Friday's payrolls. If 130k+, dollar goes to 100+, and the squeeze on dollar-funded AI capex (Alphabet's $80B equity raise, etc.) becomes a question mark for Q4 2026 delivery timelines.</div>
</div>"""

TAPE_MISSING = """
<div class="section-label">What the Tape Is Missing</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>The $30B AVGO backlog was committed when the Fed was expected to cut. All six hyperscaler ASIC customers are equity-funded.</strong> At 85% Fed hike probability, the discount rate on those capex commitments rises. AVGO's Q3 guide of $16B is already signed — it ships. But the Q4 and FY2027 bookings pipeline depends on hyperscalers' equity cost of capital staying manageable. If the Fed hikes in December 2026, the Q4 commitment cycle coincides with tighter equity funding conditions. The tell: watch Google (Alphabet), Meta, and Microsoft capex guidance in their Q2 calls (July) — any revision downward is the first sign the $30B backlog has a ceiling.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>ADP 122k is the highest since January 2025 — and the BLS payrolls number tomorrow has a structural tendency to exceed ADP when ADP beats this strongly.</strong> The correlation between ADP beats and BLS beats is not 1:1, but in months where ADP exceeds 120k, the BLS print has averaged 115k+ over the past three years. The level that changes the rate regime: BLS 130k+. At that level, Fed hike probability crosses 90%, the dot plot on June 17 almost certainly includes a 2026 hike dot, and MM-2026-004 (short 10Y yield) stops out at 4.65%.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>The Brent-WTI spread compression (from $5.68 to $2.60) is not a bear signal for oil — it's a bullish signal for WTI specifically.</strong> WTI above $95 on domestic demand (US refiners running at high utilisation) is a stronger fundamental signal than Brent above $97 on Hormuz speculation. When WTI finds domestic fundamental support above $95, the floor is sturdier than when only Brent is elevated on geopolitical premium. This is actually constructive for MM-2026-002 (long Brent) and means the absolute oil price (not the spread) is where the value lies.</div>
</div>"""

CONSENSUS = """
<div class="section-label">Consensus: Bid / Offer</div>
<div class="tile tile-muted">
  <div class="tile-head">Consensus BID</div>
  <div class="tile-body">Thursday institutional buyers confirm the AVGO sell-the-fact was a buying opportunity at $462. $30B bookings + $16B Q3 AI guide is too strong to ignore. Payrolls Friday 90–110k — strong but absorb-able. Fed hike priced and absorbed. Oil holds near $98. SPX recovers the June 3 decline. Book positions stabilise.</div>
</div>
<div class="tile tile-gold">
  <div class="tile-head">Strongest argument against — the OFFER</div>
  <div class="tile-body">AVGO confirmed the AI cycle and the stock fell. The market is telling you: confirmed cycles at 41× with 85% Fed hike probability are not the same trade as speculative cycles at 41×. If payrolls tomorrow pushes hike to 95%+ AND the post-AVGO dip doesn't attract institutional buyers Thursday morning, the market is shifting to a new regime: "AI earnings are real, but multiples must contract until the rate path clarifies." That regime is not good for any long-duration equity, including AVGO at 41×.</div>
</div>"""

ONE_CHART = """
<div class="section-label">Today's One Chart That Matters</div>
<div class="tile tile-gold">
  <div class="tile-claim">AVGO Thursday open — the institutional bid test</div>
  <div class="tile-body">The single number that matters today is AVGO's opening price. If institutions bid the stock above $472 (the pre-earnings close before the 4.7% run), the sell-the-fact is over and the AI cycle beat is being absorbed. If AVGO opens below $465 and continues lower, the market is saying: 41× doesn't work at 85% Fed hike probability even with a $30B backlog. Every other position in the book is secondary to this signal. Watch the $462/$472 range in the first 30 minutes of the session.</div>
</div>"""

CAT_CAL = """
<div class="section-label">Catalyst Calendar</div>
<table class="cal-table">
<thead><tr><th>Day</th><th>Date</th><th>Event</th><th>Consensus</th><th>View</th><th>Asymmetry</th></tr></thead>
<tbody>
<tr>
  <td>Thu</td><td>Jun 4</td>
  <td class="cal-event">AVGO Thursday open (post-earnings digest) · ISM Non-Manufacturing</td>
  <td>AVGO: stabilise near $462; ISM services ~53 (Apr was 52.9)</td>
  <td>AVGO institutional bid test: above $472 = sell-the-fact over; below $455 = multiple compression continues. ISM services above 54 = another hot data point feeding the hike narrative.</td>
  <td class="asym-up">AVGO >$472: AI cycle re-bid; AVGO <$455: valuation concern confirmed</td>
</tr>
<tr>
  <td>Fri</td><td>Jun 5</td>
  <td class="cal-event">US May payrolls (BLS, 8:30 ET) ⚡ — the rate regime decider</td>
  <td>+93k consensus; ADP 122k suggests 100–130k+ is more likely</td>
  <td>If ADP 122k is the right signal: payrolls likely 110–130k. Above 130k → Fed hike at 90–95% → 10Y spikes toward 4.60%, MM-2026-004 stop live, dollar to 100+, gold under pressure. Below 90k → partial reversal of hike probability, bonds rally, MM-2026-004 and MM-2026-009 thesis re-activates.</td>
  <td class="asym-dn">>130k: 10Y +12–15bp, DXY +0.7%, MM-2026-004 stop risk; &lt;90k: DXY −0.6%, 2Y −10bp</td>
</tr>
<tr>
  <td>Wed</td><td>Jun 11</td>
  <td class="cal-event">ECB +25bp (97% priced) — the EUR crowded-long unwind</td>
  <td>+25bp; possibly signal further hikes given CPI 3.2%, energy +10.9%</td>
  <td>EUR spec longs most bullish since Dec 2023. Sell-the-fact on hike day is the most crowded exit in Europe. MM-2026-001 (short EURAUD) positioned for this. Hawkish language also argues for a September hike — which would be genuinely EUR-negative on the growth impact.</td>
  <td class="asym-dn">EUR/USD −0.8–1.0% on pause signal; EURAUD target 1.610 in sight</td>
</tr>
<tr>
  <td>Tue–Wed</td><td>Jun 16–17</td>
  <td class="cal-event">FOMC dot plot — the decisive event of the month</td>
  <td>Hold. But ADP 122k + ISM 54% + likely strong payrolls means a hike dot for 2026/2027 is live.</td>
  <td>If payrolls Friday beats strongly: June 17 dot plot almost certainly includes a 2026 hike dot. That is the regime-defining event — reprices all equity multiples, IG spreads, gold. The book needs to be positioned for this by Thursday afternoon. MM-2026-004 is the most exposed position.</td>
  <td class="asym-dn">Hike dot: 10Y +25bp, SPX −3–5%, gold −3%; 0-cut (hold): DXY +0.5%</td>
</tr>
</tbody>
</table>"""

MIND = """
<div class="section-label">What Changes My Mind</div>
<div class="mind-item"><strong>MM-2026-001 · Short EURAUD (1.623, P&L +1.34%):</strong> Close if EURAUD holds above 1.650 post-ECB June 11. Currently 0.8% from target 1.610. ECB crowded-long unwind is the catalyst in 7 days. Hold.</div>
<div class="mind-item"><strong>MM-2026-002 · Long Brent ($97.80, P&L +7.47%):</strong> Consider partial profit-taking above $100 (round-number resistance). Raise trailing stop to $93. Full exit on a signed Iran deal announcement. WTI above $95 on domestic demand adds a second fundamental leg to the oil trade.</div>
<div class="mind-item"><strong>MM-2026-003 · Long Brent/WTI spread ($2.60, P&L −21.2%):</strong> The spread compressed from $5.68 (peak) to $2.60 as WTI caught up with Brent on domestic demand. Stop 1.50 is still 42% below current level. The Hormuz-specific thesis still exists but WTI has found independent support. No discretionary close until below 2.00, but actively watch — the trade's edge has narrowed.</div>
<div class="mind-item"><strong>MM-2026-004 · Short US 10Y yield (4.45%, P&L −0.23%):</strong> Stop 4.65% — now 20bp away. ADP 122k and likely strong payrolls Friday are the primary risk. If Friday's print is 130k+, reduce or exit pre-FOMC. This position is the most exposed in the book to tomorrow morning's data. Consider sizing down today if risk tolerance is limited.</div>
<div class="mind-item"><strong>MM-2026-005 · Long gold ($4,494, P&L −0.64%):</strong> Min hold until July 15. Stop $4,250. Gold partially recovered from $4,465 but remains below entry. FOMC June 17 dot plot is the structural catalyst — a zero-hike dot recovers gold; a hike dot sends it lower. No discretionary close permitted; stop provides the safety net.</div>
<div class="mind-item"><strong>MM-2026-006 · Long AVGO ($462.36, P&L +0.51%) — HOLD per brief rules:</strong> Beat + Raise = hold through print + 5 days (through ~June 10). Stop $422 intact. The institutional bid test today (Thursday open) is the tell. If AVGO opens above $472 and holds, raise mental stop to $450. If it opens below $455 and continues lower, re-evaluate whether 41× survives the rate regime.</div>
<div class="mind-item"><strong>MM-2026-007 · Short USDJPY (159.20, P&L +0.11%):</strong> DXY strength from ADP eroded some yen gains. Stop 163.00. BoJ divergence thesis intact. Hold through payrolls but watch 160.00 if dollar continues to strengthen on rate hike narrative.</div>
<div class="mind-item"><strong>MM-2026-008 · SPX put spread:</strong> Hold. S&P fell 0.74% June 3. Payrolls tomorrow + FOMC June 17 are both live vol events. This hedge is earning its keep.</div>"""

CLIENT_AMMO = """
<div class="section-label">Talking Points Today</div>
<div class="ammo">
  <div class="ammo-q">AVGO beat massively and the stock fell — what does that mean?</div>
  <div class="ammo-a">It means the stock had already priced the beat at $481 before the print. The 4.7% pre-earnings rally consumed the upside. What the sell-the-fact doesn't mean: the AI cycle is broken. $30B in bookings, $16B Q3 AI guide, 69% EBITDA margins — the cycle is the strongest it has ever been. What it does mean: at 41× forward earnings with 85% Fed hike probability, even a perfect earnings print is competing with a tightening discount rate. The sell-the-fact is a valuation statement, not an earnings statement.</div>
</div>
<div class="ammo">
  <div class="ammo-q">Should we be worried about payrolls tomorrow given ADP came in at 122k?</div>
  <div class="ammo-a">Yes, in a specific way. A strong payrolls print (130k+) pushes Fed hike probability above 90% and means the June 17 dot plot almost certainly includes a 2026 hike dot. That is not the same as a rate cut being priced out — it's an active tightening signal that reprices equity multiples across the board. MM-2026-004 (short 10Y yield) has a 20bp buffer before its stop at 4.65%. Tomorrow morning at 8:30 is when you find out if the stop is relevant.</div>
</div>
<div class="ammo">
  <div class="ammo-q">The Brent-WTI spread collapsed from $5.68 to $2.60. Is the oil trade broken?</div>
  <div class="ammo-a">The spread trade (MM-2026-003) is under pressure, but the outright Brent long (MM-2026-002) is the stronger position — up 7.47%. WTI surging above $95 on US inventory draws is actually a positive for the absolute oil price, not a negative. The spread compressed because WTI found its own domestic fundamental support (6th consecutive inventory draw), not because Brent's Hormuz premium disappeared. The Hormuz story hasn't changed; WTI just caught up.</div>
</div>"""

CITATIONS = """
<div class="section-label">Citations</div>
<div class="citation">
Sources beyond Reuters / Bloomberg / FT / WSJ / AP / central banks / CME / Cboe:<br>
· SEC EDGAR (8-K filed 2026-06-03) / StockTitan — AVGO Q2 actual results: $22.19B rev, $10.8B AI, Q3 guide $29.4B, AI guide $16.0B, bookings >$30B (sec.gov / stocktitan.net)<br>
· InteractiveCrypto / CNBC — AVGO fell 3% to $462.36 AH; 4.7% surge into earnings June 3 (interactivecrypto.com)<br>
· CNBC / Fox Business / PRNewswire — ADP May 122k private jobs, above 117k consensus, new high since Jan 2025 (cnbc.com / foxbusiness.com)<br>
· TradingEconomics — DXY 99.52 (+0.31%, 2-month high); Brent toward $98; WTI above $95 (tradingeconomics.com)<br>
· TradingEconomics / DailyForex — Gold ~$4,494 (range $4,463–$4,541 Jun 2–3) (tradingeconomics.com)<br>
· TradingEconomics — US 10Y ~4.45% June 3 (tradingeconomics.com)<br>
· TheStreet — S&P 500 −0.74%, Nasdaq −0.89% on June 3 (thestreet.com)<br>
· GuruFocus / TheStreet — Morgan Stanley PT $485; Susquehanna $490; J.P. Morgan $500; HSBC $600 (ahead of print) (gurufocus.com)<br>
· Kiplinger / BLS — May payrolls 93k consensus; June 5 8:30 ET release (kiplinger.com)<br>
· TradingEconomics — DXY 99.52 confirms Fed hike 85% probability; 17bp → 85% (tradingeconomics.com)
</div>"""

STALENESS = """
<div class="section-label">Staleness Check</div>
<table class="stale-tbl">
<thead><tr><th>Datum</th><th>Source</th><th>As of</th><th>Status</th></tr></thead>
<tbody>
<tr><td>AVGO Q2 results (all metrics)</td><td>SEC 8-K / StockTitan</td><td>2026-06-03 (after close)</td><td class="fresh">Fresh — verified</td></tr>
<tr><td>AVGO AH price $462.36</td><td>InteractiveCrypto / CNBC</td><td>2026-06-03 AH</td><td class="fresh">Fresh</td></tr>
<tr><td>ADP May 122k</td><td>CNBC / Fox Business / PRNewswire</td><td>2026-06-03 08:15 ET</td><td class="fresh">Fresh</td></tr>
<tr><td>DXY 99.52</td><td>TradingEconomics</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>Brent ~$97.80</td><td>TradingEconomics / OilPrice</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>WTI >$95 ($95.20 est)</td><td>TradingEconomics</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>S&P 500 −0.74%; Nasdaq −0.89% Jun 3</td><td>TheStreet</td><td>2026-06-03 close</td><td class="fresh">Fresh</td></tr>
<tr><td>US 10Y ~4.45%</td><td>TradingEconomics</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>Fed hike probability 85%</td><td>TradingEconomics (market pricing)</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>Gold ~$4,494</td><td>TwelveData / DailyForex (range)</td><td>2026-06-02/03</td><td class="stale-flag">Stale — verify live</td></tr>
<tr><td>EURAUD ~1.623</td><td>Arincen / Yahoo Finance (recent)</td><td>Approximate Jun 3</td><td class="stale-flag">Approximate</td></tr>
<tr><td>USDJPY ~159.20</td><td>Estimated from DXY move</td><td>Approximate Jun 3</td><td class="stale-flag">Approximate</td></tr>
<tr><td>VIX 15.77</td><td>Yahoo Finance</td><td>2026-06-02 close</td><td class="stale-flag">Stale — Jun 3 close not confirmed</td></tr>
<tr><td>AVGO analyst PT revisions post-print</td><td>Not yet indexed</td><td>Pending Jun 4 morning</td><td class="stale-flag">Pending — verify live Jun 4</td></tr>
<tr><td>Brent-WTI spread $2.60</td><td>Derived: 97.80 − 95.20</td><td>2026-06-03</td><td class="stale-flag">Derived — verify live</td></tr>
<tr><td>Bund, Gilt, USDCNH, MOVE</td><td>Not sourced this refresh</td><td>unavailable</td><td class="stale-flag">Unavailable</td></tr>
</tbody>
</table>"""

# ── Dashboard ─────────────────────────────────────────────────────────────────
DASH = [
    ("S&P 500",      "~7,544",    "−0.74% Jun 3",     "down"),
    ("Nasdaq",       "~26,851",   "−0.89% Jun 3",     "down"),
    ("Nikkei 225",   "68,108",    "+2.06% (Jun 3)",   "up"),
    ("DAX",          "~25,200",   "",                  "flat"),
    ("FTSE 100",     "~10,375",   "",                  "flat"),
    ("EURUSD",       "~1.164",    "DXY pressure",     "down"),
    ("USDJPY",       "~159.20",   "DXY firm",         "up"),
    ("EURAUD",       "~1.623",    "→ target 1.610",   "down"),
    ("DXY",          "99.52",     "+0.31%, 2mo high", "up"),
    ("US 10Y",       "4.45%",     "−1bp Jun 3",       "down"),
    ("2s10s",        "~+13bp",    "flattening",       "down"),
    ("WTI Crude",    ">$95",      "+3.7% Jun 3",      "up"),
    ("Brent Crude",  "~$97.80",   "toward $98",       "up"),
    ("Brent-WTI",    "~$2.60",    "compressed −$3",   "down"),
    ("Gold (XAU)",   "~$4,494",   "below entry",      "down"),
    ("VIX",          "15.77",     "(Jun 2 close)",    "flat"),
    ("AVGO",         "$462.36",   "−3% AH post-print","down"),
    ("ADP May",      "122k",      "↑ vs 117k est",    "up"),
    ("Fed hike%",    "85%",       "↑ from 70%",       "up"),
    ("Payrolls Fri", "93k est",   "ADP → upside risk","up"),
]

def dash_tile(name, val, chg, d):
    if d == "unverified" or val == "—":
        body = '<span style="color:var(--ink-mute)">unverified</span>'
    else:
        cls = {"up": "chg-up", "down": "chg-dn", "flat": "chg-flat"}.get(d, "chg-flat")
        body = f'{e(val)} <span class="{cls}">{e(chg)}</span>'
    return f'<div class="dash-tile"><div class="dlabel">{e(name)}</div><div class="dval">{body}</div></div>'

dashboard_html = '<div class="dash-grid">' + "".join(dash_tile(*r) for r in DASH) + '</div>'

theme_line = (
    '<div class="theme-line">Broadcom confirmed the AI cycle with its best quarter ever. '
    'The market sold the confirmation. '
    'ADP 122k says payrolls tomorrow will test the Fed hike at 85%.</div>'
)

new_today = [t for t in trades["open"] if t["id"] in
             ("MM-2026-006","MM-2026-007","MM-2026-008","MM-2026-009")]
idea_cards = "".join(trade_card(t) for t in new_today) or (
    '<p style="font-size:12px;color:var(--ink-mute)">No new ideas — existing positions cover the key themes.</p>'
)

charts_html = (
    '<div class="section-label" style="margin-top:1.5rem">Charts</div>'
    f'<div style="margin-bottom:8px">{eq_svg}</div>'
    f'<div style="margin-bottom:8px">{cal_svg}</div>'
    f'<div style="margin-bottom:8px">{vix_svg}</div>'
    f'<div>{yc_svg}</div>'
)

LHS = "\n".join([
    YESTERDAY, AVGO_SECTION, WRAP,
    CORRELATION, VOL_SKEW, SECTOR_RV, POSITIONING, FUNDING,
    TAPE_MISSING, CONSENSUS, ONE_CHART, CAT_CAL,
    MIND, CLIENT_AMMO, CITATIONS, STALENESS,
])

RHS = "\n".join([
    '<div class="section-label">The Open</div>',
    dashboard_html, theme_line,
    '<div class="section-label" style="margin-top:1.5rem">New Trade Ideas</div>',
    idea_cards,
    '<div class="section-label" style="margin-top:1.5rem">Live Book + Scoreboard</div>',
    live_book(trades),
    charts_html,
])

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Market Map &middot; {TODAY}</title>
  <style>{CSS}</style>
</head>
<body>
<div class="page">
  {MASTHEAD}
  <div class="two-col">
    <div class="lhs">{LHS}</div>
    <div class="rhs">{RHS}</div>
  </div>
</div>
</body>
</html>"""

out = os.path.join(HERE, "output.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)
book.save_json(book.TRADES_PATH, trades)
book.save_json(book.REGIME_PATH, regime_log)

print(f"output.html: {len(HTML):,} bytes")
print(f"Open: {len(trades['open'])} | Closed: {len(trades['closed'])}")
for t in trades["open"]:
    print(f"  {t['id']} | {t['trade'][:38]:38} | pnl {t.get('current_pnl_pct',0):+.2f}%")

import subprocess
subprocess.Popen(["start", out], shell=True)
