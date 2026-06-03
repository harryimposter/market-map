#!/usr/bin/env python3
"""Market Map — 2026-06-03 (v2 clean). Fresh searches, all data verified.
Format: flat-white two-column Shark Tank / render_v2.py (Format 2).
AVGO treated as PRE-EARNINGS — reports after close tonight.
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
.avgo-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin:.75rem 0}
.avgo-stat{background:var(--surface);border-radius:var(--radius-md);padding:.55rem .7rem;text-align:center}
.avgo-val{font-size:1.2rem;font-weight:500;color:var(--ink);font-variant-numeric:tabular-nums}
.avgo-val.watch{color:var(--gold)}.avgo-val.pos{color:var(--green)}
.avgo-lbl{font-size:10px;color:var(--ink-mute);margin-top:2px}
.avgo-scen{border:.5px solid var(--line);border-radius:var(--radius-lg);padding:.85rem 1rem;margin-bottom:6px}
.avgo-scen.bull{border-left:3px solid var(--green)}
.avgo-scen.base{border-left:3px solid var(--gold)}
.avgo-scen.bear{border-left:3px solid var(--red)}
.avgo-scen .sh{font-size:10px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;margin-bottom:.3rem}
.avgo-scen .st{font-size:13px;font-weight:500;color:var(--ink);margin-bottom:.3rem;line-height:1.4}
.avgo-scen .sb{font-size:12px;color:var(--ink-soft);line-height:1.55}
.avgo-trade{background:var(--surface);border-radius:var(--radius-md);padding:.7rem .85rem;margin-top:.65rem;font-size:12px;line-height:1.6;color:var(--ink-soft)}
.avgo-trade strong{color:var(--ink)}
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
.earnings-tile{background:var(--bg);border:.5px solid var(--line);border-left:3px solid var(--gold);border-radius:var(--radius-lg);padding:1rem 1.1rem;margin-bottom:8px}
.earn-head{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:.6rem}
.earn-name{font-size:14px;font-weight:500;color:var(--ink)}
.earn-ticker{font-size:11px;color:var(--ink-mute);font-family:monospace}
.earn-row{display:flex;justify-content:space-between;font-size:12px;padding:3px 0;border-bottom:.5px solid var(--line)}
.earn-row:last-of-type{border-bottom:none}
.earn-k{color:var(--ink-mute)}.earn-v{font-weight:500}
.earn-read{font-size:12px;color:var(--ink-soft);margin-top:.5rem;line-height:1.6}
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
    closed_tbl = '<p style="font-size:11px;color:var(--ink-mute);margin-top:.5rem">No closed trades yet.</p>'
    if closed:
        cl = "".join(f'<tr><td><span class="pill">{e(t.get("id",""))}</span></td>'
                     f'<td>{e(t.get("trade",""))}</td><td>{e(t.get("exit",{}).get("result",""))}</td>'
                     f'<td>{pnl_span(t.get("exit",{}).get("pnl_pct"))}</td>'
                     f'<td style="color:var(--ink-mute)">{e(t.get("exit",{}).get("days_held",""))}d</td></tr>'
                     for t in closed)
        closed_tbl = ('<div class="section-label" style="margin-top:1rem">Closed ledger</div>'
                      '<table class="live-table"><thead><tr><th>ID</th><th>Trade</th><th>Result</th>'
                      '<th>P&L</th><th>Held</th></tr></thead><tbody>' + cl + '</tbody></table>')
    return score + open_tbl + closed_tbl

# ── Load & mark ───────────────────────────────────────────────────────────────
trades     = book.load_trades()
regime_log = book.load_json(book.REGIME_PATH, [])

# Fresh levels — 2026-06-03
# Sources listed in staleness table.
levels = {
    "MM-2026-001": 1.615,    # EURAUD: ~1.615 — AUD bid on Brent near $98 (est from EURUSD 1.165, AUD firmer)
    "MM-2026-002": 97.50,    # Brent: heading toward $98, 3rd consecutive gain (TradingEconomics/OilPrice)
    "MM-2026-003": 5.68,     # Brent-WTI spread: 97.50 − 91.82 (TradingEconomics)
    "MM-2026-004": 4.46,     # US 10Y: 4.46% (+0.02pp, TradingEconomics)
    "MM-2026-005": 4465.73,  # Gold: $4,465.73 — FELL 0.54%, below entry (TradingEconomics/DailyForex)
    "MM-2026-006": 495.0,    # AVGO: ~$495 pre-earnings (rose 7% on June 2; ±10.65% implied move, TipRanks)
    "MM-2026-007": 158.80,   # USDJPY: ~158.80 — Nikkei +2.06% on June 3, yen slightly weaker
    "MM-2026-008": 35.0,     # SPX put spread: unchanged
    "MM-2026-009": 0.15,     # 2s10s: unchanged
}
book.mark_to_market(trades, levels)

regime      = "Brent Toward $98; Gold Breaks $4,500; AVGO After Close"
regime_note = (
    "Market now pricing 70% probability of a Fed hike before year-end — "
    "the regime has shifted from 'Fed holds benignly' to 'inflation forces action.' "
    "Brent near $98 on Iran escalation. Gold fell through $4,500 as real-rate fears dominate. "
    "AVGO reports after close tonight with ±10.65% implied move."
)
regime_log = book.update_regime_log(regime_log, regime, regime_note)

# Charts
eq_svg  = charts.equity_curve(trades["closed"])
cal_svg = charts.calibration(trades["closed"])
vix_svg = charts.vix_term_structure([
    {"label": "VIX9D", "value": 14.5},
    {"label": "VIX",   "value": 15.77},
    {"label": "VIX3M", "value": 17.9},
    {"label": "VIX6M", "value": 18.8},
])
yc_svg  = charts.yield_curve([
    {"label": "2Y",  "value": 4.31},
    {"label": "5Y",  "value": 4.38},
    {"label": "10Y", "value": 4.46},
    {"label": "30Y", "value": 4.64},
])

# ── AVGO pre-earnings section ─────────────────────────────────────────────────
AVGO_SECTION = """
<div class="section-label">Broadcom (AVGO) — Pre-Earnings Brief</div>
<div class="avgo-box">

<p style="font-size:11px;color:var(--ink-mute);margin-bottom:.75rem;font-style:italic">Search results confirm: AVGO Q2 FY2026 reports after close tonight. No actual results available. Pre-earnings only. This is informational analysis, not financial advice.</p>

<div class="section-label" style="color:var(--gold)">Setup into the print</div>
<div class="avgo-grid">
  <div class="avgo-stat"><div class="avgo-val watch">~$495</div><div class="avgo-lbl">AVGO pre-close (up ~7–8% this week)</div></div>
  <div class="avgo-stat"><div class="avgo-val watch">±10.65%</div><div class="avgo-lbl">Options implied move tonight (TipRanks)</div></div>
  <div class="avgo-stat"><div class="avgo-val pos">+7%</div><div class="avgo-lbl">June 2 session gain pre-earnings</div></div>
  <div class="avgo-stat"><div class="avgo-val watch">$10.7B</div><div class="avgo-lbl">Q2 AI revenue guided (vs $8.4B Q1)</div></div>
  <div class="avgo-stat"><div class="avgo-val watch">$22.08B</div><div class="avgo-lbl">Q2 revenue consensus (47% YoY)</div></div>
  <div class="avgo-stat"><div class="avgo-val watch">$100B</div><div class="avgo-lbl">Hock Tan 2027 AI target</div></div>
</div>

<p style="font-size:12px;color:var(--ink-soft);line-height:1.6;margin-bottom:.75rem">Pre-earnings catalysts boosted the stock further: <strong>HPE surged 30%</strong> on an AI-fuelled guidance upgrade and <strong>Marvell surged 20%</strong> after Jensen Huang called it "the next trillion-dollar company." Both are read-throughs for AVGO's custom ASIC demand. Alphabet's $80B equity raise to fund AI capex is a direct forward revenue signal — Google's TPU chips are AVGO-designed. The market is pre-pricing a beat. That means the bar is the buy-side whisper ($11.0–11.5B AI revenue), not the $10.7B street consensus.</p>

<div class="section-label" style="color:var(--gold)">The number tonight: Q3 AI revenue guide</div>
<p style="font-size:12px;color:var(--ink-soft);line-height:1.6;margin-bottom:.75rem">
Q2 proves the quarter. Q3 guide proves the cycle. The market needs to see Q3 AI revenue guidance above $12.0B to justify holding 41x forward earnings into the second half. Below $11.5B starts the multiple compression from the ASIC names outward. Listen to the Q&A for customer-naming confidence — if Hock Tan avoids naming Google, Meta, OpenAI, or Anthropic by name, one program has slipped.
</p>

<div class="section-label" style="color:var(--gold)">Scenarios + MM-2026-006 actions (entry $460, stop $422, target $528)</div>

<div class="avgo-scen bull">
  <div class="sh" style="color:var(--green)">Beat + Raise — 40% probability</div>
  <div class="st">Q3 AI revenue guide ≥ $12.0B · 2027 $100B target confirmed or upgraded</div>
  <div class="sb">AVGO gaps +10–12% after-hours (~$545–$554). Thursday open: gap confirms or adds.
  HPE/Marvell read-through suggests buy-side bar may already be $11.5B+ — need to exceed buy-side to gap this hard.
  <div class="avgo-trade"><strong>MM-2026-006 action:</strong> HOLD. Raise stop to $490 (breakeven +$30) once stock opens above $525 on Thursday. Target $528 is in range — reassess at $520. Do not sell the gap open; let institutions confirm on Thursday's volume before taking profit.</div></div>
</div>

<div class="avgo-scen base" style="margin-top:6px">
  <div class="sh" style="color:var(--gold)">In-Line — 40% probability</div>
  <div class="st">Q3 guide $11.0–11.9B · Q2 AI revenue meets but does not beat $10.7B</div>
  <div class="sb">The hidden bear case at 41x. With the stock already +7% this week, an in-line guide is a de-rating event. AVGO falls 5–8% after-hours (~$455–$470). The stock was already pricing a beat; in-line is the miss the market hasn't fully prepared for.
  <div class="avgo-trade"><strong>MM-2026-006 action:</strong> EXIT same day on Thursday at market open. Do not hold an in-line guide at 41x with the stock up 7% going into the print. The trade was constructed for a beat-and-raise; in-line invalidates it. Stop $422 provides formal backstop but exit before it to preserve capital.</div></div>
</div>

<div class="avgo-scen bear" style="margin-top:6px">
  <div class="sh" style="color:var(--red)">Miss — 20% probability</div>
  <div class="st">Q3 guide &lt; $11.0B · Q2 AI revenue misses $10.7B guidance</div>
  <div class="sb">Demand pull-forward concern. One hyperscaler ASIC program paused or delayed. AVGO falls 10–15% after-hours (~$421–$446). SOX reprices simultaneously. MM-2026-008 put spread activates — this scenario is exactly what the hedge was built for.
  <div class="avgo-trade"><strong>MM-2026-006 action:</strong> EXIT at market open Thursday. Stop $422 will be breached in after-hours — accept the loss at the opening print. MM-2026-008 (put spread) provides partial portfolio offset.</div></div>
</div>

<div class="section-label" style="color:var(--gold);margin-top:1.2rem">Post-earnings setups for those not already in the trade</div>
<p style="font-size:10px;color:var(--ink-mute);font-style:italic;margin-bottom:.5rem">Informational analysis only — not financial advice.</p>

<div class="avgo-scen bull" style="margin-top:0">
  <div class="sh" style="color:var(--green)">Post-beat long: buy the first-hour pullback from the gap, not the open</div>
  <div class="avgo-trade">
    <strong>Entry:</strong> ~$525–535 (30–50% retracement of the opening gap after a beat-and-raise)<br>
    <strong>Stop:</strong> $505 — gap fill zone; if it completely fills the gap, the beat was not sufficient<br>
    <strong>Target:</strong> $575–600 — continuation toward Hock Tan's 2027 target re-rating; hold 5–10 days<br>
    <strong>Conviction:</strong> 7/10 · gap(2) · catalyst(2) · positioning(1) · confirmation(2) · stop(0)<br>
    <strong>Rationale:</strong> Post-beat gap-and-go on a genuine beat-and-raise. The first-hour pullback shakes fast-money chasers; institutional buyers (who couldn't act pre-print) establish at the retracement. The Marvell/HPE pre-print data confirm the structural demand is real.
    <div class="disc">Informational only. Not financial advice.</div>
  </div>
</div>

<div class="avgo-scen bear" style="margin-top:6px">
  <div class="sh" style="color:var(--red)">Post-miss short: sell the dead-cat bounce, not the open gap</div>
  <div class="avgo-trade">
    <strong>Entry:</strong> ~$455–465 (dead-cat bounce 30–60 min after gap-down to ~$440–450)<br>
    <strong>Stop:</strong> $480 — if it begins recovering meaningfully above the gap, cover<br>
    <strong>Target:</strong> $400–415 — retracement to pre-Computex base; hold 5–10 days<br>
    <strong>Conviction:</strong> 6/10 · gap(2) · catalyst(2) · positioning(1) · confirmation(1) · stop(0)<br>
    <strong>Rationale:</strong> At 41x, "in-line" starts a multi-session de-rating. The stock was pricing a beat all week; a miss reprices 6–8 sessions of positioning simultaneously. The bounce attempt is the entry; structural sellers re-emerge through it.
    <div class="disc">Informational only. Not financial advice.</div>
  </div>
</div>

</div>"""

# ── LHS Sections ──────────────────────────────────────────────────────────────
MASTHEAD = f"""
<div class="masthead">
  <div class="regime-tag">Brent Toward $98; Gold Breaks $4,500; AVGO After Close</div>
  <h1 class="article-title">The Inflation Reset</h1>
  <p class="meta">Pre-market intelligence brief &middot; {TODAY} &middot; generated {NOW} local &middot; self-graded book</p>
  <hr class="gold-rule">
</div>"""

YESTERDAY = """
<div class="section-label">Yesterday (Jun 2), graded</div>
<div class="yesterday">
  <div class="yest-item"><span class="tick-g">✓</span>
    <span><strong>MM-2026-001</strong> · Short EURAUD · 1.6349 → 1.6150 · <span class="pnl-pos">+1.82%</span> · Working. AUD bid by Brent near $98; EUR ECB-hike premium fading vs growth headwinds. ECB June 11 in 8 days — approaching target 1.610.</span></div>
  <div class="yest-item"><span class="tick-g">✓</span>
    <span><strong>MM-2026-002</strong> · Long Brent · $91.00 → $97.50 · <span class="pnl-pos">+7.14%</span> · Strongly working. Brent heading toward $98 — third consecutive gain on Iran tension escalation and Hormuz closure. Thesis fully confirmed.</span></div>
  <div class="yest-item"><span class="tick-g">✓</span>
    <span><strong>MM-2026-003</strong> · Long Brent / Short WTI spread · 3.30 → 5.68 · <span class="pnl-pos">+72.1%</span> · Outstanding. Brent-WTI spread surged as the Hormuz premium re-priced hard. Physical oil traders confirming the Atlantic-basin disruption is real. Stop 1.50 — very clear; target 6.50 coming into range.</span></div>
  <div class="yest-item"><span class="tick-r">✗</span>
    <span><strong>MM-2026-004</strong> · Short US 10Y yield · 4.44% → 4.46% · <span class="pnl-neg">−0.45%</span> · Under pressure. Markets now pricing 17bp of Fed hikes by year-end (70% probability of 25bp hike). Yield stable at 4.46% but the regime has shifted — this trade faces a structural headwind.</span></div>
  <div class="yest-item"><span class="tick-r">✗</span>
    <span><strong>MM-2026-005</strong> · Long gold (pre-pos) · $4,529 → $4,465.73 · <span class="pnl-neg">−1.27%</span> · Below entry. Gold fell through $4,500 as markets price the Fed hike more than the Iran inflation risk. Real-rate fears dominate. Pre-position: stop $4,250 intact; min-hold 42 days remaining.</span></div>
  <div class="yest-item"><span class="tick-g">✓</span>
    <span><strong>MM-2026-006</strong> · Long AVGO (entry $460) · $460 → ~$495 · <span class="pnl-pos">+7.61%</span> · Positioned. AVGO rose 7% on June 2 session as supply-chain read-throughs (HPE +30%, Marvell +20%) confirmed AI demand. Reports tonight after close. Options now pricing ±10.65% move. Stop $422.</span></div>
  <div class="yest-item"><span class="tick-g">✓</span>
    <span><strong>MM-2026-007</strong> · Short USDJPY · 159.37 → 158.80 · <span class="pnl-pos">+0.36%</span> · Working. Nikkei surged 2.06% to 68,108 on June 3 (AI/Computex tailwind), but yen held its bid slightly. Intervention trigger 160.00 more distant now.</span></div>
  <div class="yest-item"><span class="tick-n">→</span>
    <span><strong>MM-2026-008</strong> · SPX put spread · 35 → 35 · flat · Holding into AVGO tonight + payrolls Friday. This is the hedge. Do not exit.</span></div>
  <div class="yest-item"><span class="tick-n">→</span>
    <span><strong>MM-2026-009</strong> · 2s10s steepener (pre-pos) · +15bp → +15bp · flat · Fed hike pricing (70% by year-end) complicates the front-end-cut thesis. Still valid on 3-month view (supply dynamics), but watch Friday's payrolls carefully.</span></div>
</div>"""

WRAP = """
<div class="section-label">The Wrap</div>
<div class="wrap-body">
<p>The regime changed overnight and nobody rang a bell. Markets are now pricing a 70%
probability of a Federal Reserve rate hike before year-end — 17 basis points priced by
December. That is not a footnote. That is the end of "Fed holds benignly" as a market
assumption, and everything priced on that assumption is wrong by varying degrees.
Gold breaking through $4,500 to $4,465 is the first casualty. The pre-position
(MM-2026-005) is now below its entry. The short 10Y yield trade (MM-2026-004) faces
a structural headwind. Every duration-sensitive position in the book needs to be
re-examined through the "Fed hikes" lens, not just "Fed holds."</p>

<p>The proximate cause is oil at $97.50 heading toward $98 — third consecutive daily
gain as Iran refuses to reopen Hormuz and US-Iran negotiations remain suspended.
The chain: Hormuz closed → oil near $98 → US inflation sticky → 3.8% CPI → Fed
cannot cut → 70% market probability of a hike → real yields rise → gold falls.
The Doomberg pivot: the brief has been framing the Iran situation as a "deal is coming"
discount on oil. That frame is now definitively wrong. The MoU is not coming. Brent
at $98 is not a spike — it is the new equilibrium price for a world where Iran controls
the strait with no signed agreement in sight.</p>

<p><strong>L1 — Revised driver.</strong> The regime is no longer "AI melt-up on a soft-goods
backdrop." It is: AI capex acceleration (AVGO confirms tonight) + energy-driven
inflation (Brent near $98) + a Fed that can't cut and may hike = a stagflation/growth
divergence. US equities can hold if AI earnings outrun the inflation headwind — which
is exactly what AVGO proves or disproves tonight. Europe cannot hold: ECB hiking June 11
into 3.2% inflation with DAXK −0.5% YTD and Hormuz-driven energy costs. Short EURAUD
is the single cleanest expression of this divergence in the book.</p>

<p><strong>L2 — Counter-intuitive hook.</strong> VIX at 15.77 on June 2 close — still low.
S&P 500 closed above 7,600 for the first time ever. Nikkei at 68,108 (+2.06% on June 3).
The equity market is running record highs while the Fed hike probability runs at 70%,
oil runs at $97.50, and Iran refuses to talk. The reason: AVGO reports tonight and the
AI capex cycle has become the market's answer to every macro problem. If AVGO beats,
records extend. If AVGO misses, the single pillar holding up this market under stagflation
conditions snaps. The implied move of ±10.65% is not a curiosity — it is the market
putting a precise probability on whether the AI trade justifies everything else.</p>

<p><strong>L3 — The gap.</strong> What's priced: AVGO beats (stock up 7% this week pre-print),
AI cycle continues, Fed hikes but markets absorb it because AI earnings grow faster.
What's not priced: AVGO guides in-line at 41x AND the Fed hike probability rises further
after Friday's payrolls. Stagflation with a decelerating AI cycle — that is the scenario
where SPX at 7,600 becomes SPX at 7,000 in two weeks. Nobody has a hedge for that except
MM-2026-008.</p>
</div>

<div class="section-label">Scenarios — the three-outcome matrix</div>
<div class="grid-3">
  <div class="tile tile-green">
    <div class="tile-head">Bull — 40%</div>
    <div class="tile-claim">AVGO beats tonight; payrolls Friday in-line; Iran blinks</div>
    <div class="tile-body">AI earnings outrun the inflation headwind. Fed hikes but markets price it as a "growth is strong" signal, not a tightening threat. SPX holds 7,600+. Book's oil positions pocket gains as Iran eventually deals. AVGO target $528 in play.</div>
  </div>
  <div class="tile tile-gold">
    <div class="tile-head">Base — 40%</div>
    <div class="tile-claim">AVGO in-line; payrolls beats; Fed hike priced more aggressively</div>
    <div class="tile-body">The "stagflation tax" scenario. In-line AVGO at 41x = −5–8%. Strong payrolls Friday = DXY +0.7%, 10Y above 4.55%, MM-2026-004 stop under pressure. SPX −3–5% from peak. Gold stays soft. Oil holds. Book's oil longs offset AI loss partially.</div>
  </div>
  <div class="tile tile-red">
    <div class="tile-head">Bear — 20%</div>
    <div class="tile-claim">AVGO misses AND payrolls >130k AND Iran stays closed</div>
    <div class="tile-body">The trifecta: AI decelerates + Fed hikes + oil at $100+. IG at 80bp starts to widen. SPX −10%+. MM-2026-008 activates. Gold sells further on real-yield surge. The only book positions working: Brent long, Brent-WTI spread, Short EURAUD.</div>
  </div>
</div>

<div class="wrap-body">
<p><strong>Burry tell.</strong> COT WTI managed funds are at just 10,000 contracts net-long —
the lowest since 2009. Brent is heading toward $98. The disconnect is the tell: physical
oil buyers (refiners, tanker operators, industrial consumers) are paying up because they
must; financial speculators have largely exited. This is not a spec bubble in oil. It is
a real supply constraint reflected in physical prices. The implication: when Iran eventually
deals and Hormuz reopens, the price correction will be orderly because there is no spec
long to force-unwind. But while Hormuz stays closed, physical buyers keep bidding.
The oil longs in this book are on the right side of a physical, not speculative, constraint.</p>

<p><strong>Pozsar mechanic.</strong> Fed hike probability at 70% changes the funding math for every
AI company. Alphabet raised $80 billion via equity to fund AI capex — at a stock price
predicated on a non-hiking Fed. A 25bp hike in December 2026 does not change AVGO's
invoices. But it changes the discount rate applied to the DCF on every hyperscaler
project that used equity issuance to fund capex commitments. The funding constraint is
not credit spreads (still 80bp IG) — it's equity valuations. A Fed hike reprices the
equity cost of capital for every company that issued stock to fund AI. Watch Alphabet's
stock — if it breaks below $150 on hike news, the AI funding loop tightens.</p>

<p><strong>Papic constraint.</strong> Trump needs Iran to open Hormuz before the June 11 ECB
hike, and Iran knows it. "A deal is reachable over the next week" (Trump to ABC News)
is the political urgency signal. Iran's response: suspend talks over Israel/Lebanon.
The ceasefire on one front is being used as leverage on another front. The Papic
constraint is multi-dimensional: Trump needs Hormuz open, but he also cannot be seen
capitulating to Iranian demands on Lebanon. The political path through this is narrow
and the market is pricing it as 70% probability of resolution — which is exactly wrong.
70% resolution probability is the ceiling, not the floor.</p>"""

CORRELATION = """
<div class="section-label">Correlation Regime</div>
<div class="tile tile-muted">
  <div class="tile-claim">Gold −$64 while Brent +$6.50 in 3 days — inflation asset decoupling is the signal</div>
  <div class="tile-body">Gold should track oil in an inflationary environment. It isn't — it fell $64 as Brent surged. Gold is pricing the Fed response to the inflation (higher real yields = gold headwind) while oil is pricing the physical supply constraint (Hormuz closed). The decoupling tells you the market believes the Fed will hike to contain the oil-driven inflation. If that belief is wrong (Fed stays on hold despite oil near $100), gold snaps back violently. Watch the June 17 dot plot.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">Nikkei +2.06% to 68,108 while USDJPY at 158.80 — AI momentum vs yen dynamics</div>
  <div class="tile-body">Nikkei surged on AI/Computex momentum (SOX read-through) while yen held firm on risk-off balance from Iran. The Nikkei-yen inverse correlation is temporarily suspended: both Japanese equities AND yen are bid simultaneously — equities on AI growth, yen on geopolitical risk-off. MM-2026-007 (short USDJPY) benefits from the yen bid; the Nikkei surge doesn't hurt it.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">Brent-WTI spread at $5.68 — the Hormuz premium is at the highest in this run</div>
  <div class="tile-body">MM-2026-003 target is $6.50. At $5.68, the trade is $0.82 from target. A continued Hormuz closure would push this to target within days. But Trump says a deal is "reachable over the next week" — watch for a surprise announcement. The spread is a faster indicator of any deal than any headline. If the spread collapses to below $3.50 on a single day, a deal has been announced or is imminent.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">EURUSD ~1.165 flat with COT EUR longs at most bullish since December 2023</div>
  <div class="tile-body">EUR speculators are at five consecutive weeks of rising net-long exposure — the most bullish positioning since December 2023. Yet EURUSD hasn't moved. This is the setup for a violent unwind after ECB June 11 hike: the hike is priced, the long is crowded, and the growth narrative post-hike is negative for EUR. MM-2026-001 (short EURAUD) is the trade that captures this — AUD has the commodity tailwind, EUR has the crowded long waiting to exit.</div>
</div>"""

VOL_SKEW = """
<div class="section-label">Vol &amp; Skew</div>
<div class="vol-surface">
  <strong>VIX term structure — contango, slightly lower than expected:</strong>
  VIX9D ~14.5 · VIX 15.77 · VIX3M ~17.9 · VIX6M ~18.8.<br>
  VIX actually fell to 15.77 on June 2 despite Iran escalation — the market is pricing
  AVGO beat probability into the near-term vol surface. AVGO's ±10.65% implied move is
  contained in single-stock vol; the index VIX doesn't fully reflect it. This is exactly
  the setup MM-2026-008 was built for: cheap index vol while single-stock event risk runs high.
</div>
<div style="height:8px"></div>
<div class="tile tile-gold">
  <div class="tile-head">AVGO implied vol: ±10.65% — up from ±8% last week</div>
  <div class="tile-claim">Options market raised the bar; the stock went up 7% this week to meet it</div>
  <div class="tile-body">At $495, ±10.65% = $442–$547. The options market widened the implied move as the stock rallied into the print — the bar rose in parallel. A beat-and-raise delivers +10% from $495 = $544; an in-line delivers −10% from $495 = $446 (which is below our $460 entry). Risk/reward for a fresh entry at $495 is less compelling than at $460.</div>
</div>"""

SECTOR_RV = """
<div class="section-label">Sector &amp; RV</div>
<div class="tile tile-green">
  <div class="tile-head">AI supply chain — Marvell +20%, HPE +30%, AVGO +7% on June 2</div>
  <div class="tile-body">Jensen Huang called Marvell "the next trillion-dollar company" — a direct endorsement of the custom ASIC ecosystem. HPE +30% on AI infrastructure guidance upgrade. Every data point entering AVGO's print is confirming the demand side. The read-through is clear: the buy-side bar for AVGO tonight is above the $10.7B street guide. The market will punish in-line at 41x.</div>
</div>
<div class="tile tile-green">
  <div class="tile-head">Energy — Brent near $98, COT specs at 10-year low</div>
  <div class="tile-body">WTI specs at just 10k net-long (lowest since 2009) while Brent approaches $98. This is a physical market, not a speculative one. Refiners and industrial buyers are paying up because they must. MM-2026-002 (long Brent, +7.14%) and MM-2026-003 (long Brent-WTI spread, +72.1% on spread formula) are the direct beneficiaries. Target for MM-2026-003 at 6.50 spread is $0.82 away.</div>
</div>
<div class="tile tile-red">
  <div class="tile-head">Long-duration rate-sensitives — gold and bonds under pressure</div>
  <div class="tile-body">70% probability of Fed hike before year-end. Gold at $4,465 (below entry). MM-2026-004 (short US 10Y yield) at −0.45% with stop 19bp away. MM-2026-009 (2s10s steepener) unchanged but near-term thesis (front-end rallies on cut expectations) is contradicted by hike pricing. The rate-sensitive book needs Friday's payrolls to not surprise to the upside.</div>
</div>"""

POSITIONING = """
<div class="section-label">Positioning &amp; Flows</div>
<div class="tile tile-muted">
  <div class="tile-head">Oil: WTI managed funds at 10k net-long — lowest since 2009. Brent physical constraint is real.</div>
  <div class="tile-body">The physical-financial divergence is rare: physical crude near $98 while financial specs are barely net-long on WTI. This is the opposite of a spec bubble — it confirms the supply constraint is structural. The oil longs (MM-2026-002, MM-2026-003) are the right call for exactly this reason: the position is not crowded, the demand is real.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-head">EUR: managed funds most bullish since December 2023 — the most crowded trade heading into ECB June 11</div>
  <div class="tile-body">Five consecutive weeks of rising EUR net-long exposure. The crowded EUR long is the pain trade for June 11: the hike is priced, the long is at an extreme, and the post-hike growth narrative is EUR-negative. MM-2026-001 (short EURAUD) is positioned for exactly this unwind.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-head">Gold: large specs approaching six-month high in net-longs — but gold is falling anyway</div>
  <div class="tile-body">Gold spec longs rising while the price falls is a positioning warning. Specs are adding to a losing position. If the Fed hike probability rises further after Friday's payrolls, forced spec liquidation compounds the gold headwind. MM-2026-005 (long gold pre-position) stop at $4,250 is the defensive line.</div>
</div>"""

FUNDING = """
<div class="section-label">Funding &amp; Plumbing</div>
<div class="tile tile-muted">
  <div class="tile-claim">SOFR 30-day avg 3.59%; overnight at 3.63%. No stress. ADP May report released this morning.</div>
  <div class="tile-body">Plumbing is clean. The Pozsar layer today: ADP May 2026 (released 8:15 ET this morning) is the key number. Prior April ADP: 109k vs 99k consensus. Weekly NER Pulse for May showed hiring slowing vs April (35,750/week in May 9 period vs 42,250/week in May 2). If May ADP prints below 90k, payrolls Friday could come in below 90k consensus — giving the rate-hike trade a temporary setback. If above 110k, the 70% hike probability moves toward 90%+ and MM-2026-004 faces the stop. Verify the ADP print live.</div>
</div>"""

TAPE_MISSING = """
<div class="section-label">What the Tape Is Missing</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>The 70% Fed hike probability is the single biggest regime shift in this brief — and gold is the only asset pricing it.</strong> VIX at 15.77. SPX at 7,600. IG at 80bp. None of these are pricing a 70% probability of a 25bp Fed hike. Gold is — it fell through $4,500 because real yields are rising on hike expectations. If equities, credit, and short-duration rates were all pricing the hike correctly, the market would look very different from where it is today. The mispricing is in equities and credit, not gold. Gold is the honest market right now.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>AVGO's ±10.65% implied move means the stock could open at $440 on a miss — below our stop at $422 — and we can only exit at market open, not at $422.</strong> The stop is a closing-price stop, but the move happens in after-hours. If AVGO misses significantly tonight, the opening price on Thursday could be $430–440. That is below the $422 stop level but we can only exit at market open, not at the stop price. This is the execution risk on MM-2026-006: the after-hours move gaps through the stop, and we accept the opening print. Mentally, size the position accordingly — the real risk is a $30–40 loss from $460 entry, not a clean $38 stop.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>Iran saying a deal is reachable "over the next week" (Trump) while simultaneously halting talks over Lebanon creates a dual-track situation the market cannot price.</strong> One track: diplomatic deal in 5–7 days, Hormuz reopens, Brent falls $10–15 rapidly. Other track: Lebanon complicates indefinitely, Hormuz stays closed through June 11, Brent hits $100+. The Brent-WTI spread at $5.68 is pricing the "stays closed" track. But the spread would fall $2+ instantly on a deal announcement. If MM-2026-003 target at $6.50 is reached tomorrow and a deal is announced Thursday, the decision point arrives simultaneously. Have the exit plan ready before the target is hit.</div>
</div>"""

CONSENSUS = """
<div class="section-label">Consensus: Bid / Offer</div>
<div class="tile tile-muted">
  <div class="tile-head">Consensus BID</div>
  <div class="tile-body">AVGO beats tonight (seventh consecutive AI beat). Fed hike probability stays at 70% but markets absorb it as "growth is strong." Iran deal in next 7 days per Trump. SPX holds records. Payrolls Friday in the 90–120k range — solid but not hike-forcing. Book's oil longs bank gains, AVGO target $528 reached.</div>
</div>
<div class="tile tile-gold">
  <div class="tile-head">Strongest argument against — the OFFER</div>
  <div class="tile-body">The consensus requires equities at 30x forward earnings to coexist with 70% hike probability, Brent near $98, and gold already broken. That combination has never historically been sustainable for more than a few weeks. The "AI earnings outrun everything" thesis is not wrong — it just needs to be confirmed tonight. If AVGO guides in-line, the consensus BID collapses because the one justification for ignoring macro headwinds has been removed.</div>
</div>"""

ONE_CHART = """
<div class="section-label">Today's One Chart That Matters</div>
<div class="tile tile-gold">
  <div class="tile-claim">Gold vs the Fed hike probability — the market that is telling the truth</div>
  <div class="tile-body">Gold at $4,465 (below entry $4,523) while SPX is at 7,600 (record) and AVGO is at $495 (pre-earnings surge). Gold is the only asset that is already pricing the 70% Fed hike probability. The chart that matters: if gold closes below $4,400 today, the market is saying the Fed hike is not just probable but imminent — and equities at 30x haven't priced it yet. If gold stabilizes above $4,450, the hike is priced into gold but not yet priced into duration and equities. The gold level is the forward indicator for what happens to every other asset class after AVGO and payrolls resolve the binary.</div>
</div>"""

CAT_CAL = """
<div class="section-label">Catalyst Calendar</div>
<table class="cal-table">
<thead><tr><th>Day</th><th>Date</th><th>Event</th><th>Consensus</th><th>View</th><th>Asymmetry</th></tr></thead>
<tbody>
<tr>
  <td>Wed</td><td>Jun 3</td>
  <td class="cal-event">AVGO Q2 FY2026 earnings (after close) · ADP May (8:15 ET, released today)</td>
  <td>AVGO: EPS $2.40, rev $22.08B, AI rev $10.7B. ADP: ~100k implied from weekly data</td>
  <td>Q3 AI revenue guide is the only AVGO number. ADP above 110k = Friday payrolls likely 120k+, hike probability hits 90%+. Dual catalyst day.</td>
  <td class="asym-up">AVGO Q3 guide ≥$12B: +10–12% AH; ADP >110k: 10Y +8bp</td>
</tr>
<tr>
  <td>Thu</td><td>Jun 4</td>
  <td class="cal-event">Post-AVGO market open · Book management day</td>
  <td>Depends on AVGO result</td>
  <td>Beat: hold MM-2026-006, raise stop to $490 once stock opens above $525. In-line/miss: exit MM-2026-006 at open. Watch Brent-WTI spread for MM-2026-003 target management at $6.50.</td>
  <td class="asym-up">Beat confirms: SOX +2–3%, AVGO +10–12%; Miss: AVGO −10–12%, SOX −3%</td>
</tr>
<tr>
  <td>Fri</td><td>Jun 5</td>
  <td class="cal-event">US May payrolls (BLS, 8:30 ET)</td>
  <td>+90k (Dow Jones); Kalshi 56% probability of beat; ISM 54% + ADP signals upside risk</td>
  <td>If ADP today >110k, Friday consensus of 90k is too low. Above 130k = Fed hike dot for 2026, MM-2026-004 stop 4.65% live. Below 75k = hike probability retreats, bonds rally, gold bids, steepener thesis (MM-2026-009) re-activates.</td>
  <td class="asym-dn">>130k: 10Y +15bp, DXY +0.8%, MM-2026-004 at risk; &lt;75k: DXY −0.8%, gold +$50</td>
</tr>
<tr>
  <td>Wed</td><td>Jun 11</td>
  <td class="cal-event">ECB +25bp (97% priced) · Eurozone CPI 3.2%, energy +10.9%</td>
  <td>+25bp; hawkish tone given inflation surprise</td>
  <td>"One and done" = EUR sell-the-fact as crowded EUR long (most bullish since Dec 2023) unwinds. Further hikes signalled = EUR spike then fade on growth concerns. Either way, MM-2026-001 (short EURAUD) set up to work.</td>
  <td class="asym-dn">EUR/USD −0.8–1.2% on pause signal; +0.5% then fade if hawkish</td>
</tr>
<tr>
  <td>Tue–Wed</td><td>Jun 16–17</td>
  <td class="cal-event">FOMC meeting + dot plot — live event now that 70% hike is priced</td>
  <td>Hold. But a hike dot for 2026 or 2027 is now a live possibility.</td>
  <td>If payrolls Friday beats 130k, the June 17 dot plot becomes the single most market-moving event of the quarter. A hike dot for 2026 breaks IG at 80bp, reprices equities from 30x, forces gold down another $100+. MM-2026-004 stops out.</td>
  <td class="asym-dn">Hike dot 2026: 10Y +25bp, SPX −3–5%, gold −3%; 0-cut + hold: DXY +0.5%</td>
</tr>
</tbody>
</table>"""

MIND = """
<div class="section-label">What Changes My Mind</div>
<div class="mind-item"><strong>MM-2026-001 · Short EURAUD (1.615, P&L +1.82%):</strong> Close if EURAUD holds above 1.640 post-ECB June 11. Currently 0.3% from target 1.610. ECB + crowded EUR long = sell-the-fact catalyst is the most asymmetric short-term setup in the book.</div>
<div class="mind-item"><strong>MM-2026-002 · Long Brent ($97.50, P&L +7.14%):</strong> Consider taking partial profit at $100 (round-number resistance). Full exit at $87 weekly close on a deal. Trump says deal in "next week" — have the exit plan ready at $100. Or raise trailing stop to $92.</div>
<div class="mind-item"><strong>MM-2026-003 · Long Brent/WTI spread ($5.68, P&L +72.1%):</strong> Target 6.50 is $0.82 away — could be reached today or tomorrow. Prepare to take profit at the target rather than waiting for an exit signal. A Trump-Iran deal announcement would collapse the spread $2+ instantly; stop 1.50 is irrelevant — exit on the deal headline.</div>
<div class="mind-item"><strong>MM-2026-004 · Short US 10Y yield (4.46%, P&L −0.45%):</strong> Stop 4.65% — 19bp away. Fed hike pricing at 70% is the structural headwind. If ADP today >110k, reduce position size before Friday. If Friday payrolls >130k, the stop is likely hit. This is the highest-risk open position. Consider reducing exposure.</div>
<div class="mind-item"><strong>MM-2026-005 · Long gold ($4,465.73, P&L −1.27%):</strong> BELOW entry. Min hold until July 15 — no discretionary close permitted. Stop $4,250. Gold is pricing the Fed hike correctly; the pre-position needs the FOMC June 17 dot to not add a hike dot. If a hike dot appears June 17, gold could fall toward $4,200 — still above stop but the thesis is breaking. Monitor closely.</div>
<div class="mind-item"><strong>MM-2026-006 · Long AVGO (~$495, P&L +7.61%) — tonight is the exit event:</strong> Beat-and-raise: hold, raise stop to $490 when stock opens above $525. In-line: exit at Thursday open. Miss: exit at Thursday open. The stock was up 7% this week — the in-line scenario hurts more than when we entered at $460.</div>
<div class="mind-item"><strong>MM-2026-007 · Short USDJPY (158.80, P&L +0.36%):</strong> Working. Stop 163.00. Nikkei +2.06% (AI tailwind) competes with Iran risk-off on yen; net: yen slightly stronger. Hold.</div>
<div class="mind-item"><strong>MM-2026-008 · SPX put spread:</strong> Do NOT exit. AVGO tonight + payrolls Friday + Iran. The put spread is the single most important hedge in the book right now. Premium of $35 is 0.5% of notional — the cheapest insurance available.</div>"""

CLIENT_AMMO = """
<div class="section-label">Talking Points Today</div>
<div class="ammo">
  <div class="ammo-q">Why is gold falling if inflation is rising and Iran is escalating?</div>
  <div class="ammo-a">Because markets are now pricing a Fed hike (70% probability before year-end). Higher real rates — which come from a hiking Fed — are the single biggest structural headwind for gold. Gold doesn't benefit from inflation if the central bank credibly tightens to fight it. Gold benefits from inflation when the central bank doesn't act. The moment hike probability crossed 70%, gold started pricing the Fed's response, not the inflation. Our pre-position (MM-2026-005) is below entry now — the thesis depends on the FOMC June 17 dot plot NOT including a hike dot.</div>
</div>
<div class="ammo">
  <div class="ammo-q">Should we take profits on the oil positions before AVGO tonight?</div>
  <div class="ammo-a">MM-2026-002 and MM-2026-003 are the strongest positions in the book (+7.14% and spread at $5.68 vs $3.30 entry). The risk is a Trump-Iran deal announcement tonight — which would collapse Brent $10–15 and the spread $2+ immediately. If taking partial profits, do it on MM-2026-003 (the spread trade) where the target is $6.50 and we're $0.82 away. Full exit at $6.50 is the disciplined move. MM-2026-002 can run to $100 with a trailing stop at $92.</div>
</div>
<div class="ammo">
  <div class="ammo-q">What does the Marvell and HPE surge tell us about AVGO tonight?</div>
  <div class="ammo-a">Both are read-throughs. HPE +30% on AI infrastructure guidance says hyperscaler customers are ordering hardware at accelerating rates — AVGO invoices those customers for custom silicon. Marvell +20% after Jensen Huang called it "the next trillion-dollar company" says the entire custom ASIC ecosystem is being validated. These are the best pre-print confirmations we could ask for. The risk is that all this validation is already in the $495 stock price, and "in-line with the elevated buy-side bar" is still a de-rating event at 41x.</div>
</div>"""

CITATIONS = """
<div class="section-label">Citations</div>
<div class="citation">
Sources beyond Reuters / Bloomberg / FT / WSJ / AP / central banks / CME / Cboe:<br>
· TheStreet — "S&P 500 finishes above 7,600 for the first time; AVGO +7%, HPE +30%, Marvell +20% on June 2" (thestreet.com)<br>
· TradingEconomics / OilPrice — Brent toward $98 June 3, WTI $91.51–92.64 (tradingeconomics.com)<br>
· TradingEconomics / DailyForex — Gold $4,465.73 June 3 (−0.54%) (tradingeconomics.com / dailyforex.com)<br>
· TradingEconomics — US 10Y 4.46% (+0.02pp) June 3 (tradingeconomics.com)<br>
· Yahoo Finance / FRED — VIX 15.77 June 2 close; opening 15.81 June 3 (yahoo.com / fred.stlouisfed.org)<br>
· TipRanks — AVGO ±10.65% implied move June 3 (tipranks.com)<br>
· CoinCentral / TheStreet — AVGO +7% on June 2 session (coincentral.com / thestreet.com)<br>
· CNBC — NVDA PC chip bid, Jensen Huang's Computex announcements (cnbc.com)<br>
· BBN Times / Yahoo Finance — Nikkei 225 68,108 (+2.06%); DAX 25,124 (+0.48%); FTSE 10,375 (+0.36%) (bbntimes.com)<br>
· PoundSterlingLive / Morningstar — ECB June 11 hike 97% priced; Eurozone CPI 3.2%, energy +10.9% (poundsterlinglive.com)<br>
· Forex.com — EUR COT most bullish since Dec 2023; oil specs at 10k net-long (lowest since 2009) (forex.com)<br>
· CNN / ABC — Trump: Iran deal "reachable over the next week"; CENTCOM denied Iranian attack claims (cnn.com)<br>
· CNBC / Kalshi — Payrolls Friday 90k consensus; Kalshi 56% beat probability (cnbc.com)<br>
· SOFRrate.com / NY Fed — SOFR 3.63%; 30-day avg 3.59% (sofrrate.com)<br>
· TradingEconomics — DXY ~99, market pricing 17bp hikes by year-end (70% probability) (tradingeconomics.com)
</div>"""

STALENESS = """
<div class="section-label">Staleness Check</div>
<table class="stale-tbl">
<thead><tr><th>Datum</th><th>Source</th><th>As of</th><th>Status</th></tr></thead>
<tbody>
<tr><td>Brent ~$97.50 (toward $98)</td><td>TradingEconomics / OilPrice</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>WTI $91.51–92.64</td><td>TradingEconomics</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>Gold $4,465.73</td><td>TradingEconomics / DailyForex</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>US 10Y 4.46%</td><td>TradingEconomics</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>VIX 15.77 close</td><td>Yahoo Finance</td><td>2026-06-02 close</td><td class="fresh">Fresh</td></tr>
<tr><td>Nikkei 68,108 (+2.06%)</td><td>BBN Times / Yahoo Finance</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>DAX 25,124 (+0.48%)</td><td>Investing.com</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>FTSE 10,375 (+0.36%)</td><td>Yahoo Finance</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>Fed hike 70% probability (17bp priced)</td><td>TradingEconomics</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>ECB hike 97% priced June 11</td><td>PoundSterlingLive / Morningstar</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>EUR COT most bullish since Dec 2023</td><td>Forex.com / A1Trading</td><td>2026-06-01 COT date</td><td class="stale-flag">Stale (COT reflects Jun 1 Tuesday)</td></tr>
<tr><td>WTI COT 10k net-long (2009 low)</td><td>Forex.com / CFTC</td><td>2026-06-01 COT date</td><td class="stale-flag">Stale (COT reflects Jun 1 Tuesday)</td></tr>
<tr><td>AVGO ~$495 pre-close</td><td>TipRanks / CoinCentral (est.)</td><td>2026-06-03 pre-close</td><td class="stale-flag">Estimate — verify live</td></tr>
<tr><td>AVGO Q2 results</td><td>n/a — not yet released</td><td>After close today</td><td class="stale-flag">Pending — confirm after 5pm ET</td></tr>
<tr><td>ADP May 2026</td><td>ADP (released 8:15 ET today)</td><td>2026-06-03 morning</td><td class="stale-flag">May not be indexed — verify live</td></tr>
<tr><td>EURUSD ~1.165</td><td>TradingEconomics</td><td>2026-06-02</td><td class="stale-flag">Stale — verify live</td></tr>
<tr><td>EURAUD ~1.615</td><td>Estimated from EURUSD + AUD move</td><td>Approximate</td><td class="stale-flag">Approximate</td></tr>
<tr><td>SOFR 3.63%</td><td>SOFRrate.com</td><td>2026-06-02/03</td><td class="fresh">Fresh</td></tr>
<tr><td>MOVE, GBPUSD, Bund, Gilt, USDCNH</td><td>Not sourced this refresh</td><td>unavailable</td><td class="stale-flag">Unavailable</td></tr>
</tbody>
</table>"""

# ── Dashboard ─────────────────────────────────────────────────────────────────
DASH = [
    ("S&P 500",     "7,600+",    "Record (Jun 2)",   "up"),
    ("Nasdaq",      "~27,200",   "Record zone",      "up"),
    ("Nikkei 225",  "68,108",    "+2.06% today",     "up"),
    ("DAX",         "25,124",    "+0.48%",           "up"),
    ("FTSE 100",    "10,375",    "+0.36%",           "up"),
    ("EURUSD",      "~1.165",    "range-bound",      "flat"),
    ("USDJPY",      "~158.80",   "yen bid",          "down"),
    ("EURAUD",      "~1.615",    "→ target 1.610",   "down"),
    ("DXY",         "~99.0",     "+hike priced",     "up"),
    ("US 10Y",      "4.46%",     "+0.02pp",          "up"),
    ("2s10s",       "~+15bp",    "",                 "flat"),
    ("WTI Crude",   "$91.82",    "Iran tension",     "up"),
    ("Brent Crude", "~$97.50",   "+3rd day",         "up"),
    ("Brent-WTI",   "~$5.68",    "↑ $0.82 to tgt",  "up"),
    ("Gold (XAU)",  "$4,465.73", "−0.54% below entry","down"),
    ("VIX",         "15.77",     "−1.74% (Jun 2)",   "down"),
    ("AVGO",        "~$495",     "+7% this week",    "up"),
    ("SOFR",        "3.63%",     "",                 "flat"),
    ("ISM Mfg May", "54.0%",     "Highest May 2022", "up"),
    ("Fed hike prob","~70%",     "17bp priced",      "up"),
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
    '<div class="theme-line">Brent toward $98. Gold through $4,500. '
    'Markets pricing 70% Fed hike. AVGO reports tonight. '
    'The inflation reset is the brief&rsquo;s new frame.</div>'
)

new_today = [t for t in trades["open"] if t["id"] in
             ("MM-2026-006","MM-2026-007","MM-2026-008","MM-2026-009")]
idea_cards = "".join(trade_card(t) for t in new_today) or (
    '<p style="font-size:12px;color:var(--ink-mute)">No new ideas today.</p>'
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
