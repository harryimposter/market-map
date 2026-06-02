#!/usr/bin/env python3
"""Market Map — 2026-06-03. Full refresh + dedicated AVGO earnings section.
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

# ── CSS — flat white Shark Tank / render_v2.py ────────────────────────────────
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
.avgo-banner{border:2px solid var(--gold);border-radius:var(--radius-lg);padding:1.25rem 1.4rem;margin-bottom:1.5rem;background:rgba(184,150,12,.04)}
.avgo-banner .section-label{color:var(--gold);margin-top:0}
.avgo-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:1rem 0}
.avgo-stat{background:var(--surface);border-radius:var(--radius-md);padding:.6rem .8rem;text-align:center}
.avgo-stat .av{font-size:1.25rem;font-weight:500;color:var(--ink);font-variant-numeric:tabular-nums}
.avgo-stat .al{font-size:10px;color:var(--ink-mute);margin-top:2px}
.avgo-stat.beat .av{color:var(--green)}.avgo-stat.miss .av{color:var(--red)}.avgo-stat.watch .av{color:var(--gold)}
.avgo-scenario{border:.5px solid var(--line);border-radius:var(--radius-lg);padding:.9rem 1rem;margin-bottom:6px}
.avgo-scenario .sh{font-size:11px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;margin-bottom:.4rem}
.avgo-scenario .st{font-size:13px;font-weight:500;color:var(--ink);margin-bottom:.3rem}
.avgo-scenario .sb{font-size:12px;color:var(--ink-soft);line-height:1.55}
.avgo-scenario.bull{border-left:3px solid var(--green)}.avgo-scenario.bear{border-left:3px solid var(--red)}.avgo-scenario.base{border-left:3px solid var(--gold)}
.avgo-trade{background:var(--surface);border-radius:var(--radius-md);padding:.8rem 1rem;margin-top:.75rem;font-size:12px;line-height:1.6}
.avgo-trade strong{color:var(--ink);font-weight:500}
.avgo-disc{font-size:10px;color:var(--ink-mute);margin-top:.5rem;font-style:italic}
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
.unverified-note{font-size:11px;color:var(--ink-mute);background:var(--surface);border-radius:var(--radius-md);padding:.5rem .75rem;margin:.5rem 0;line-height:1.5}
"""

# ── Helpers ───────────────────────────────────────────────────────────────────
def pnl_span(p):
    if p is None: return '<span style="color:var(--ink-mute)">—</span>'
    cls = "pnl-pos" if p > 0 else ("pnl-neg" if p < 0 else "")
    return f'<span class="{cls}">{p:+.2f}%</span>'

def pips(conviction, cb):
    n = int(conviction)
    dots = "".join(f'<div class="pip{"  on" if i < n else ""}"></div>' for i in range(10))
    detail = (
        f'gap({cb.get("gap",0)}/3) · catalyst({cb.get("catalyst",0)}/2) · '
        f'pos({cb.get("positioning",0)}/2) · confirm({cb.get("confirmation",0)}/2) · '
        f'stop({cb.get("stop_quality",0)}/1)'
    )
    return f'<div class="conv-bar">{dots}<span class="conv-detail">{e(detail)}</span></div>'

def prog_pct(t, level):
    entry, target = t.get("entry"), t.get("target")
    if not entry or not target or target == entry: return 0
    d = 1 if target >= entry else -1
    return max(0, min(100, int(d * (level - entry) / abs(target - entry) * 100)))

def trade_card(t):
    cb = t.get("conviction_breakdown", {})
    rows = [
        ("Asset",     t.get("asset_class", "")),
        ("Structure", t.get("structure", "")),
        ("Entry",     t.get("entry", "")),
        ("Stop",      t.get("stop", "")),
        ("Target",    t.get("target", "")),
        ("Horizon",   t.get("horizon", "")),
    ]
    if t.get("min_hold_days"):
        rows.append(("Min hold", f'{t["min_hold_days"]}d'))
    rows_html = "".join(
        f'<div class="tc-row"><span class="tc-k">{e(k)}</span>'
        f'<span class="tc-v">{e(v)}</span></div>'
        for k, v in rows
    )
    return (
        f'<div class="trade-card">'
        f'<div class="tc-top"><div>'
        f'<div class="tc-name">{e(t.get("trade",""))}</div>'
        f'<div class="tc-class">{e(t.get("type","reactive"))} · {e(t.get("asset_class",""))}</div>'
        f'</div><div class="conv-badge">{e(t.get("conviction","?"))}/10</div></div>'
        f'{rows_html}{pips(t.get("conviction",0), cb)}'
        f'<div class="tc-thesis">{e(t.get("thesis",""))}</div>'
        f'</div>'
    )

def live_book(trades):
    closed = trades.get("closed", [])
    open_t = trades.get("open", [])
    graded = [t for t in closed if "pnl_pct" in t.get("exit", {})]
    if graded:
        pnls = [t["exit"]["pnl_pct"] for t in graded]
        wins = [p for p in pnls if p > 0]
        best = max(graded, key=lambda t: t["exit"]["pnl_pct"])
        score = (
            f'<div class="score-row">'
            f'<div class="score-tile"><div class="sval">{len(graded)}</div><div class="slabel">Closed</div></div>'
            f'<div class="score-tile"><div class="sval">{100*len(wins)/len(graded):.0f}%</div><div class="slabel">Hit rate</div></div>'
            f'<div class="score-tile"><div class="sval {"pos" if sum(pnls)>=0 else "neg"}">{sum(pnls):+.1f}%</div><div class="slabel">Sum P&L</div></div>'
            f'<div class="score-tile"><div class="sval pos">{e(best["id"])}</div><div class="slabel">Best</div></div>'
            f'</div>'
        )
    else:
        score = '<p style="font-size:12px;color:var(--ink-mute);margin-bottom:.75rem">Book opened 2026-06-01 — scoreboard builds as trades close.</p>'
    h_map = {"weeks": 14, "months": 90, "2 weeks": 14, "3 months": 90, "26 days": 26}
    rows = []
    for t in open_t:
        cur  = t.get("current", t.get("entry"))
        pl   = t.get("current_pnl_pct")
        prog = prog_pct(t, cur) if cur else 0
        try:
            held = (date.today() - date.fromisoformat(t.get("opened","2026-06-01"))).days
            rem  = max(0, h_map.get(t.get("horizon",""), 30) - held)
            rc   = "var(--red)" if rem < 5 else "var(--ink-mute)"
            rem_s = f'<span style="color:{rc}">{rem}d</span>'
        except Exception:
            rem_s = "—"
        rows.append(
            f'<tr><td><span class="pill">{e(t.get("id",""))}</span></td>'
            f'<td style="max-width:130px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{e(t.get("trade",""))}</td>'
            f'<td>{e(t.get("opened",""))}</td>'
            f'<td style="font-variant-numeric:tabular-nums">{e(cur)}</td>'
            f'<td>{pnl_span(pl)}</td><td>{rem_s}</td>'
            f'<td><div class="prog-bar"><span style="width:{prog}%"></span></div></td></tr>'
        )
    open_tbl = (
        '<table class="live-table"><thead><tr>'
        '<th>ID</th><th>Trade</th><th>Opened</th><th>Current</th>'
        '<th>P&L</th><th>Window</th><th>&rarr; Target</th>'
        '</tr></thead><tbody>'
        + ("".join(rows) or '<tr><td colspan="7" style="color:var(--ink-mute)">no open trades</td></tr>')
        + '</tbody></table>'
    )
    if closed:
        cl = "".join(
            f'<tr><td><span class="pill">{e(t.get("id",""))}</span></td>'
            f'<td>{e(t.get("trade",""))}</td>'
            f'<td>{e(t.get("exit",{}).get("result",""))}</td>'
            f'<td>{pnl_span(t.get("exit",{}).get("pnl_pct"))}</td>'
            f'<td style="color:var(--ink-mute)">{e(t.get("exit",{}).get("days_held",""))}d</td></tr>'
            for t in closed
        )
        closed_tbl = (
            '<div class="section-label" style="margin-top:1rem">Closed ledger</div>'
            '<table class="live-table"><thead><tr>'
            '<th>ID</th><th>Trade</th><th>Result</th><th>P&L</th><th>Held</th>'
            '</tr></thead><tbody>' + cl + '</tbody></table>'
        )
    else:
        closed_tbl = '<p style="font-size:11px;color:var(--ink-mute);margin-top:.5rem">No closed trades yet.</p>'
    return score + open_tbl + closed_tbl

# ── Load & mark to market ─────────────────────────────────────────────────────
trades     = book.load_trades()
regime_log = book.load_json(book.REGIME_PATH, [])

# Fresh levels — 2026-06-03
# Sources: TradingEconomics, OilPrice, Capital.com, TheHill/Iran news
levels = {
    "MM-2026-001": 1.620,    # EURAUD: ~1.620 — ECB June 11 approaching, Iran risk bid AUD
    "MM-2026-002": 94.80,    # Brent: ~$94.80 — Iran halted talks, Hormuz escalation risk (TheHill)
    "MM-2026-003": 3.40,     # Brent-WTI spread: ~94.80 − 91.40 (Iran threatens Hormuz, Brent outperforms)
    "MM-2026-004": 4.46,     # US 10Y: 4.46% — carried, yield unchanged June 3
    "MM-2026-005": 4540.0,   # Gold: ~$4,540 — gold climbed back above $4,500, Iran risk bid (Capital.com)
    "MM-2026-006": 483.0,    # AVGO: ~$483 — opened +4.90% on June 2, pre-earnings
    "MM-2026-007": 158.90,   # USDJPY: ~158.90 — slight yen strength on risk-off Iran news
    "MM-2026-008": 35.0,     # SPX put spread: unchanged
    "MM-2026-009": 0.15,     # 2s10s: unchanged
}
book.mark_to_market(trades, levels)

regime      = "Iran Escalates; AVGO Reports Tonight"
regime_note = (
    "Iran halted ceasefire talks and vowed to keep Hormuz closed — the disinflation trade "
    "is reversing. AVGO reports after close tonight: the AI capex proof point. "
    "Two tails, one evening."
)
regime_log = book.update_regime_log(regime_log, regime, regime_note)

# Charts
eq_svg  = charts.equity_curve(trades["closed"])
cal_svg = charts.calibration(trades["closed"])
vix_svg = charts.vix_term_structure([
    {"label": "VIX9D", "value": 14.8},
    {"label": "VIX",   "value": 16.50},
    {"label": "VIX3M", "value": 18.2},
    {"label": "VIX6M", "value": 19.1},
])
yc_svg  = charts.yield_curve([
    {"label": "2Y",  "value": 4.31},
    {"label": "5Y",  "value": 4.39},
    {"label": "10Y", "value": 4.46},
    {"label": "30Y", "value": 4.64},
])

# ── AVGO Dedicated Section ────────────────────────────────────────────────────
# NOTE: Search results as of this run returned only pre-earnings preview data.
# AVGO Q2 FY2026 results report after close on June 3.
# This section covers: Q1 actuals, Q2 consensus, what to watch, MM-2026-006
# management, and post-earnings setup recommendations for each scenario.
# Verify actual results against this framework once released.

AVGO_SECTION = """
<div class="section-label">Broadcom (AVGO) — Full Earnings Brief</div>
<div class="avgo-banner">

<div class="unverified-note">⚠ Search results returned pre-earnings data only. AVGO Q2 FY2026 results are due after today's close. This section covers Q1 actuals, Q2 consensus, what to watch tonight, MM-2026-006 management rules, and post-earnings setups for each scenario. Verify all figures against the actual press release. This is informational analysis, not financial advice.</div>

<div class="section-label">The Foundation: Q1 FY2026 Actuals</div>
<div class="avgo-grid">
  <div class="avgo-stat beat"><div class="av">$8.4B</div><div class="al">Q1 AI Revenue (+106% YoY)</div></div>
  <div class="avgo-stat beat"><div class="av">$19.3B</div><div class="al">Q1 Total Revenue (+29% YoY)</div></div>
  <div class="avgo-stat beat"><div class="av">$100B+</div><div class="al">Hock Tan's 2027 AI rev target</div></div>
  <div class="avgo-stat watch"><div class="av">6</div><div class="al">Hyperscaler ASIC customers (5 in vol now; 6th deploying 2027)</div></div>
  <div class="avgo-stat watch"><div class="av">41x</div><div class="al">Forward P/E at ~$483</div></div>
  <div class="avgo-stat watch"><div class="av">77%</div><div class="al">Q2 guided gross margin</div></div>
</div>

<div class="section-label">Q2 FY2026 Consensus vs Buy-Side Bar</div>
<table style="width:100%;font-size:12px;border-collapse:collapse;margin-bottom:.75rem">
<thead><tr>
  <th style="text-align:left;padding:0 8px 6px 0;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-mute);border-bottom:.5px solid var(--line)">Metric</th>
  <th style="text-align:right;padding:0 8px 6px;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-mute);border-bottom:.5px solid var(--line)">Street Consensus</th>
  <th style="text-align:right;padding:0 0 6px;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--gold);border-bottom:.5px solid var(--line)">Buy-Side Bar (whisper)</th>
</tr></thead>
<tbody>
<tr><td style="padding:5px 8px 5px 0;border-bottom:.5px solid var(--line)">Revenue</td><td style="text-align:right;padding:5px 8px;border-bottom:.5px solid var(--line);font-variant-numeric:tabular-nums">$22.08B</td><td style="text-align:right;padding:5px 0;border-bottom:.5px solid var(--line);color:var(--gold);font-variant-numeric:tabular-nums">$22.3B+</td></tr>
<tr><td style="padding:5px 8px 5px 0;border-bottom:.5px solid var(--line)">Adj. EPS</td><td style="text-align:right;padding:5px 8px;border-bottom:.5px solid var(--line);font-variant-numeric:tabular-nums">$2.40</td><td style="text-align:right;padding:5px 0;border-bottom:.5px solid var(--line);color:var(--gold);font-variant-numeric:tabular-nums">$2.45+</td></tr>
<tr><td style="padding:5px 8px 5px 0;border-bottom:.5px solid var(--line)"><strong>AI Revenue (THE number)</strong></td><td style="text-align:right;padding:5px 8px;border-bottom:.5px solid var(--line);font-variant-numeric:tabular-nums"><strong>$10.7B</strong></td><td style="text-align:right;padding:5px 0;border-bottom:.5px solid var(--line);color:var(--gold);font-weight:500;font-variant-numeric:tabular-nums"><strong>$11.0–11.5B</strong></td></tr>
<tr><td style="padding:5px 8px 5px 0;border-bottom:.5px solid var(--line)">Q3 AI Revenue Guide</td><td style="text-align:right;padding:5px 8px;border-bottom:.5px solid var(--line);font-variant-numeric:tabular-nums">~$11.5B implied</td><td style="text-align:right;padding:5px 0;border-bottom:.5px solid var(--line);color:var(--gold);font-variant-numeric:tabular-nums">$12.0B+ for re-rate</td></div></td></tr>
<tr><td style="padding:5px 8px 5px 0">Semiconductor Revenue</td><td style="text-align:right;padding:5px 8px;font-variant-numeric:tabular-nums">$14.8B (+76% YoY)</td><td style="text-align:right;padding:5px 0;color:var(--gold);font-variant-numeric:tabular-nums">$15.0B+</td></tr>
</tbody>
</table>

<div class="section-label">What Moves the Stock Tonight</div>
<p style="font-size:12px;color:var(--ink-soft);line-height:1.6;margin-bottom:.75rem">
The Q2 AI revenue number ($10.7B guide) is the proof-of-quarter. But the stock moves on
<strong>Q3 AI revenue guidance</strong> — not Q2. The sequence: Q1 delivered $8.4B (+106% YoY).
Q2 guided $10.7B (+140% YoY). The market extrapolates Q3 from the guide delta.
Above $12.0B = Hock Tan's $100B 2027 target is on track → +8–12% gap.
$11.5–12.0B = modest beat, 2027 target intact → +3–6%.
$10.5–11.4B = in-line or slight miss at 41x forward → −5–8%, multiple compression begins.
Below $10.5B = demand pull-forward concern, 2027 target at risk → −10–15%.
</p>
<p style="font-size:12px;color:var(--ink-soft);line-height:1.6;margin-bottom:.75rem">
Secondary signals from the earnings call: (1) Customer naming — does Hock Tan mention
Google, Meta, OpenAI, Anthropic by name or avoid specifics? Avoidance = one customer
slipping. (2) Gross margin — 77% guided; above 78% confirms pricing power. (3) VMware
integration — infrastructure software revenue growing or declining? Declining would signal
enterprise spending caution despite AI strength. (4) The $100B 2027 target — reaffirmed,
upgraded, or quietly walked back?
</p>

<div class="section-label">Q2 Consensus History &amp; Context</div>
<p style="font-size:12px;color:var(--ink-soft);line-height:1.6;margin-bottom:.75rem">
AVGO has beaten consensus EPS in all four trailing quarters with an average surprise of
+1.93%. EPS consensus rose 11.1% (from $2.16 to $2.40) in the past 90 days — a strong
upward revision signal. Oppenheimer (Buy, PT $490) and Morgan Stanley (Overweight, PT
$485) both reaffirmed ahead of the print. Average analyst PT: $482.31 (47 analysts,
"Strong Buy" consensus). Current stock: ~$483 pre-earnings (opened +4.90% on June 2).
The market is already pricing a beat — meaning the bar is the buy-side whisper, not
street consensus.
</p>

<div class="section-label">Scenarios: Outcome + MM-2026-006 Action</div>

<div class="avgo-scenario bull">
  <div class="sh" style="color:var(--green)">Scenario A — Beat + Raise (45% probability)</div>
  <div class="st">Q2 AI revenue ≥ $11.0B; Q3 guide ≥ $12.0B; 2027 target reaffirmed or upgraded</div>
  <div class="sb">
    This is the outcome that justifies 41x. Hock Tan reaffirms the $100B 2027 AI target
    with specificity — names a new hyperscaler deployment milestone, confirms 6th customer
    deploying >1GW in 2027. Gross margin at or above 78%. Stock gaps +8–12% in after-hours
    (~$521–$541). Thursday open: market confirms or adds to the gap.
    <br><br>
    <strong>MM-2026-006 action:</strong> HOLD through print + 5 trading days.
    Target $528 comes into range — reassess at $520. Raise stop to $490 (breakeven +$30
    cushion) once stock opens above $520. Do not sell before Thursday's open gap confirmation.
  </div>
</div>

<div class="avgo-scenario base" style="margin-top:6px">
  <div class="sh" style="color:var(--gold)">Scenario B — In-Line (35% probability)</div>
  <div class="st">Q2 AI revenue $10.5–10.9B; Q3 guide $11.0–11.9B; 2027 target maintained with caveats</div>
  <div class="sb">
    The hidden bear case at 41x. Revenue in the guidance range, but no upside surprise.
    Management is careful — no specific customer upgrades, Q3 guide is "approximately
    $11–12B range." Stock reprices the lack of acceleration: −5–8% after-hours (~$444–$459).
    The multiple contracts because the 2027 $100B target now requires acceleration that
    isn't confirmed.
    <br><br>
    <strong>MM-2026-006 action:</strong> EXIT same day. If stock closes more than 5% lower
    on the print night, close position at the open of the following session. Do not hold
    an in-line guide at 41x. The trade was constructed for a beat-and-raise; in-line
    invalidates the setup.
  </div>
</div>

<div class="avgo-scenario bear" style="margin-top:6px">
  <div class="sh" style="color:var(--red)">Scenario C — Miss (20% probability)</div>
  <div class="st">Q2 AI revenue &lt; $10.5B; Q3 guide &lt; $11.0B; demand pull-forward concern</div>
  <div class="sb">
    The cycle-interruption signal. AI revenue below Q2's own guidance implies one or more
    hyperscaler ASIC programs delayed or paused. Stock gaps −10–15% (~$411–$435). The
    SOX re-rates simultaneously — NVDA, AMD, TSMC, ASML all re-price the ASIC demand
    timeline. This is the event MM-2026-008 (SPX put spread) was built for.
    <br><br>
    <strong>MM-2026-006 action:</strong> EXIT at market open. Stop $422 is likely breached
    in after-hours — accept the loss at the opening print, not the stop level. The thesis
    is broken; the put spread (MM-2026-008) partially offsets the portfolio damage.
  </div>
</div>

<div class="section-label">Post-Earnings Setup — For Those Who Did NOT Trade Into the Print</div>
<p style="font-size:11px;color:var(--ink-mute);font-style:italic;margin-bottom:.5rem">Informational analysis only. Not financial advice. Position sizing, leverage, and risk management are the reader's responsibility.</p>

<div class="avgo-scenario bull" style="margin-top:0">
  <div class="sh" style="color:var(--green)">Post-Earnings Long (Beat + Raise scenario confirmed)</div>
  <div class="st">Buy AVGO on the first 30-minute pullback after the gap open, not at the open itself</div>
  <div class="avgo-trade">
    <strong>Setup:</strong> After a genuine beat-and-raise, AVGO gaps up ~10%. The post-gap
    first-hour pullback — typically 30–50% of the gap — is the entry. If it gaps to $530,
    buy the retracement to ~$515–520.<br>
    <strong>Entry:</strong> ~$515–520 (intraday pullback from the opening gap)<br>
    <strong>Stop:</strong> $495 — below the gap fill zone; if it fills the gap entirely, the beat was not real<br>
    <strong>Target:</strong> $560–580 — extension of the gap move; hold 5–10 trading days<br>
    <strong>Conviction:</strong> 7/10 — gap(2) · catalyst(2) · positioning(1) · confirmation(2) · stop(0)<br>
    <strong>Rationale:</strong> Post-earnings gap-and-go on a genuine beat-and-raise at a structural
    AI inflection is one of the most reliable momentum setups. The first-hour pullback
    shakes out fast-money gap chasers; the second-day continuation is where institutional
    buyers (who couldn't act before the print) establish positions.
  </div>
</div>

<div class="avgo-scenario bear" style="margin-top:6px">
  <div class="sh" style="color:var(--red)">Post-Earnings Short (In-Line or Miss scenario confirmed)</div>
  <div class="st">Short AVGO on the first 30-minute dead-cat bounce after the gap down, not immediately</div>
  <div class="avgo-trade">
    <strong>Setup:</strong> After a miss or in-line guide, AVGO gaps down 8–12%. The knee-jerk bounce
    attempt in the first 30–60 minutes is the short entry — dip buyers step in, stock
    bounces 2–3% off the low, then the structural sellers (funds exiting 41x at
    "in-line") re-emerge.<br>
    <strong>Entry:</strong> ~$450–455 (on the dead-cat bounce, if gap down brings to ~$430–440)<br>
    <strong>Stop:</strong> $470 — above the gap fill zone; if it starts recovering meaningfully, cover<br>
    <strong>Target:</strong> $400–410 — retracement to the pre-Computex base; hold 5–10 trading days<br>
    <strong>Conviction:</strong> 6/10 — gap(2) · catalyst(2) · positioning(1) · confirmation(1) · stop(0)<br>
    <strong>Rationale:</strong> At 41x forward earnings, "in-line" is a de-rating event. The SOX
    doesn't need AVGO to miss badly — it just needs guidance not to accelerate beyond
    what the multiple prices. The AI infrastructure trade is priced for continuous
    beat-and-raise; the first quarter that doesn't deliver starts the multiple compression
    that was always arithmetically inevitable.
  </div>
</div>

</div>"""

# ── Sections ──────────────────────────────────────────────────────────────────
MASTHEAD = f"""
<div class="masthead">
  <div class="regime-tag">Iran Escalates; AVGO Reports Tonight</div>
  <h1 class="article-title">The Hormuz Shock Returns</h1>
  <p class="meta">Pre-market intelligence brief &middot; {TODAY} &middot; generated {NOW} local &middot; self-graded book</p>
  <hr class="gold-rule">
</div>"""

YESTERDAY = """
<div class="section-label">Yesterday, graded</div>
<div class="yesterday">
  <div class="yest-item">
    <span class="tick-g">✓</span>
    <span><strong>MM-2026-001</strong> · Short EURAUD · 1.6349 → 1.6200 · <span class="pnl-pos">+1.52%</span> · Working. ECB June 11 hike fully priced; Iran escalation bid AUD briefly but EUR weakness on growth concerns took over. Approaching target 1.610.</span>
  </div>
  <div class="yest-item">
    <span class="tick-g">✓</span>
    <span><strong>MM-2026-002</strong> · Long Brent · $91.00 → $94.80 · <span class="pnl-pos">+4.18%</span> · Strong. Iran halted ceasefire talks and vowed to keep Hormuz closed — the war premium is repricing. Thesis fully confirmed.</span>
  </div>
  <div class="yest-item">
    <span class="tick-g">✓</span>
    <span><strong>MM-2026-003</strong> · Long Brent / Short WTI spread · 3.30 → 3.40 · <span class="pnl-pos">+3.03%</span> · Working. Brent outperforming WTI as Iran threatens Hormuz specifically (Atlantic-basin premium). Spread holding above entry.</span>
  </div>
  <div class="yest-item">
    <span class="tick-n">→</span>
    <span><strong>MM-2026-004</strong> · Short US 10Y yield · 4.44% → 4.46% · <span class="pnl-neg">−0.45%</span> · Near flat. Yield stable — Iran risk-off bid bonds slightly but ISM 54% keeps yields elevated. ADP May report released today (April was 109k). Watch payrolls Friday.</span>
  </div>
  <div class="yest-item">
    <span class="tick-g">✓</span>
    <span><strong>MM-2026-005</strong> · Long gold (pre-pos) · $4,529 → $4,540 · <span class="pnl-pos">+0.38%</span> · Moving. Gold climbed back above $4,500 as Iran escalation bid safe-haven assets. Dual-tail thesis (geopolitical + Fed cut optionality) intact.</span>
  </div>
  <div class="yest-item">
    <span class="tick-g">✓</span>
    <span><strong>MM-2026-006</strong> · Long AVGO (entry $460) · $460 → $483 · <span class="pnl-pos">+5.00%</span> · Positioned. AVGO opened +4.90% on June 2, pre-earnings momentum. Reports tonight after close. Stop $422, target $528. See AVGO Earnings Brief section.</span>
  </div>
  <div class="yest-item">
    <span class="tick-g">✓</span>
    <span><strong>MM-2026-007</strong> · Short USDJPY · 159.37 → 158.90 · <span class="pnl-pos">+0.29%</span> · Working. Yen strengthened slightly on Iran risk-off. 160.00 intervention trigger less imminent now. Thesis intact.</span>
  </div>
  <div class="yest-item">
    <span class="tick-n">→</span>
    <span><strong>MM-2026-008</strong> · SPX put spread · 35 → 35 · flat · Holding. Iran escalation + AVGO binary tonight — this is the portfolio hedge. Do not exit pre-print.</span>
  </div>
  <div class="yest-item">
    <span class="tick-n">→</span>
    <span><strong>MM-2026-009</strong> · 2s10s UST steepener (pre-pos) · +15bp → +15bp · flat · Payrolls Friday is the catalyst. Iran risk-off competes with ISM 54% on the direction of 2Y vs 10Y.</span>
  </div>
</div>"""

WRAP = """
<div class="section-label">The Wrap</div>
<div class="wrap-body">
<p>The ceasefire is off. Iran halted talks with the United States and announced it will keep
the Strait of Hormuz closed. The mine in the strait is no longer an ambiguous floating
object — it is the punctuation mark on a breakdown in negotiations. The oil trade that
was "priced for hope" is now priced for prolonged closure. Brent at $94.80 is not
the ceiling; it is the starting point for a world without a signed MoU.</p>

<p>The Doomberg pivot: the market spent six days believing the disinflation from oil was
borrowed but real. It wasn't borrowed — it was fictional. The MoU was always a term sheet
without signatures. The real Brent price was always somewhere between $95 and $105,
depending on how long Hormuz stays closed. Today's move is the market correcting that
misread, not a new shock. The shock was in May when oil fell.</p>

<p>And into this Iran escalation, Broadcom reports after the close tonight. The
juxtaposition is not coincidental — it is the defining tension of this cycle. The AI
infrastructure trade (AVGO at $483, up 4.9% yesterday pre-earnings) and the geopolitical
oil trade (Brent at $94.80, Hormuz closed) are running simultaneously at maximum
intensity. The portfolio is long both sides: MM-2026-002 and MM-2026-003 benefit from
Iran escalation; MM-2026-006 depends on AVGO confirming the AI cycle tonight. If both
resolve favorably — AVGO beats and Iran eventually deals — this is the melt-up structure.
If AVGO misses and Iran escalates further, the stagflation trade takes hold.</p>

<p><strong>L1 — Revised driver.</strong> The Perkins regime is no longer "AI melt-up on a
soft-goods backdrop." It is: AI capex cycle + energy price shock + ECB hiking into it =
a stagflation setup in Europe, a growth-and-earnings divergence in the US. The US equity
market is holding together because AI earnings are real. European equities face the ECB
hiking into Hormuz-driven inflation while manufacturing was already contracting.
MM-2026-001 (short EURAUD) captures this divergence precisely.</p>

<p><strong>L2 — Counter-intuitive hook.</strong> Iran escalation should be bad for equities.
S&P 500 is at 7,600, a record, with Iran having just halted ceasefire talks.
The reason: the market trusts that AI earnings will outrun geopolitical noise. That is
the bet. AVGO reports tonight and either validates the trust or exposes it.
If AVGO misses and Hormuz is still closed, both pillars of the market's complacency
collapse simultaneously. The VIX at 16.5 is not pricing that tail.</p>

<p><strong>L3 — The gap.</strong> What's priced: AI beats (AVGO), Iran deal eventually happens
(oil at $94.80 vs $100 when talks stalled), Fed holds benignly (one cut by year-end),
ECB hike is priced and digested. What's not: Hock Tan cautious on the call tonight (the
in-line scenario). Iran refusing to talk indefinitely (oil $100–105). ADP May report
today: April was 109k, above consensus of 99k — May ADP likely above 100k. If payrolls
Friday also beats 130k, the Fed hike scenario moves from tail to base case.</p>
</div>

<div class="section-label">Scenarios — today's dual binary</div>
<div class="grid-2">
  <div class="tile tile-green">
    <div class="tile-head">Bull — AI beats + Iran eventually blinks</div>
    <div class="tile-body">AVGO Q3 guide ≥ $12B. Iran reopens Hormuz within 2 weeks (a new deal emerges under pressure). Oil disinflation resumes. Fed holds benignly. SPX 8,000+. Book's oil longs take profit, gold holds. AVGO target $528 in play.</div>
  </div>
  <div class="tile tile-red">
    <div class="tile-head">Bear — AVGO in-line + Iran stays closed</div>
    <div class="tile-body">AVGO guides $10.5–11.4B (in-line at 41x = −5–8%). Iran keeps Hormuz closed into June 11 ECB. Stagflation narrative takes hold. SPX −3–5%. IG spreads at 80bp start to widen. MM-2026-008 put spread activates.</div>
  </div>
</div>

<div class="wrap-body">
<p><strong>Burry tell.</strong> ADP April reported 109k private sector jobs vs 99k consensus.
The May ADP released today (June 3) is the preview of Friday's payrolls. If May ADP also
beats — say 120k+ — the market has to take seriously that payrolls Friday could hit 130k+.
At that level, with ISM at 54%, the Fed's June 17 dot plot becomes a genuine wildcard.
One hike dot added to the 2026 projections would be the biggest market shock of the
quarter — larger than AVGO's print. Nobody is positioned for a Fed hike.</p>

<p><strong>Pozsar mechanic.</strong> Iran's decision to halt talks is a balance sheet move, not
a negotiating tactic. Iran's Hormuz-related institutions — the Persian Gulf Strait
Authority — have been sanctioned by the US Treasury. Those institutions need funding.
With sanctions on oil sales still in place and Iranian sovereign reserves depleted by
three months of war, Iran's central bank balance sheet cannot sustain an extended closure
without economic damage that exceeds the political value of holding out. The break-even
point for Iran's reserves — at current oil revenue blockade — is approximately 90 days.
The clock started in April. The negotiating window narrows by the week.</p>

<p><strong>Papic constraint.</strong> Trump needs Iran to reopen Hormuz before June 11
(ECB hike day). A Hormuz closure on ECB hike day creates a stagflation narrative that
is politically toxic. Iran's decision to halt talks is partly a reading of this political
calendar — they know the pressure on Trump is highest between now and June 11.
The Papic constraint for Iran is the reverse: their internal political economy demands
they be seen winning something before any MoU is signed. The "we halted talks" move is
a public negotiating position, not a final decision. Watch for back-channel signals
in the next 48–72 hours.</p>"""

CORRELATION = """
<div class="section-label">Correlation Regime</div>
<div class="tile tile-muted">
  <div class="tile-claim">Iran halts talks → Brent +$0.22 and Brent-WTI spread widens — Hormuz premium re-pricing in real time</div>
  <div class="tile-body">MM-2026-003 (Long Brent/Short WTI spread at 3.40 from entry 3.30) is the direct beneficiary. Brent outperforms WTI when the Hormuz specific risk is elevated — WTI is Cushing-priced, Brent is Atlantic-basin priced. The spread widening is the cleanest expression of the Iran binary.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">Gold +$11 as Iran escalates while SPX holds record 7,600 — safe haven and risk-on coexisting</div>
  <div class="tile-body">Gold at $4,540 is bidding on Iran while equities hold records on AI. This is the dual-tail thesis for MM-2026-005 (long gold) working in real time — gold wins whether the Iran tail or the Fed-cut tail resolves. The correlation is broken between gold and equities because they're each pricing a different narrative.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">AVGO +4.9% on June 2 pre-earnings while broader Nasdaq −0.25% — AI ASIC cycle decoupled from market</div>
  <div class="tile-body">The only stock that matters today is AVGO. Every other equity position is secondary until the print. AVGO's +4.9% pre-earnings move means the market is already pricing a beat — the implied move (±8%) is now asymmetric: a beat delivers +8% from $483 = $521; a miss delivers −8% from $483 = $444. The options market is pricing the binary correctly; the stock price is not neutral.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">USDJPY at 158.90 — yen strengthening on Iran risk-off, intervention risk diminishing slightly</div>
  <div class="tile-body">The yen strengthened 47 pips on Iran news. Finance Minister Katayama's 160.00 intervention trigger is now further away. MM-2026-007 (short USDJPY) is working in the right direction — +0.29% P&L. Iran escalation and risk-off sentiment is the unexpected accelerant for this trade.</div>
</div>"""

VOL_SKEW = """
<div class="section-label">Vol &amp; Skew</div>
<div class="vol-surface">
  <strong>VIX rising into the dual binary:</strong> VIX9D ~14.8 · VIX ~16.50 · VIX3M ~18.2 · VIX6M ~19.1.
  VIX is climbing — from 15.32 on June 1 to ~16.50 today. The Iran escalation added ~0.5 VIX points;
  AVGO event premium added another ~0.5. The structure is still in contango but tightening.
  The front-end is the cheapest it will be on both catalysts (AVGO tonight, payrolls Friday).
</div>
<div style="height:8px"></div>
<div class="tile tile-gold">
  <div class="tile-head">AVGO implied vol</div>
  <div class="tile-claim">±8% implied — correctly priced; options market is not complacent on this binary</div>
  <div class="tile-body">At $483, ±8% = $444–$521. The options market has correctly calibrated this as a high-stakes event. MM-2026-008 (SPX put spread) captures broad market downside if AVGO misses and Iran stays closed simultaneously — the two-tail scenario.</div>
</div>"""

SECTOR_RV = """
<div class="section-label">Sector &amp; RV</div>
<div class="tile tile-green">
  <div class="tile-head">Energy — Iran halt is a direct catalyst</div>
  <div class="tile-body">Brent at $94.80 after Iran halted ceasefire talks. MM-2026-002 (+4.18%) and MM-2026-003 (+3.03%) are the direct beneficiaries. Energy sector YTD +34.5% — the Hormuz premium is back after being temporarily priced out. The "oil was falling because the deal was coming" narrative is dead.</div>
</div>
<div class="tile tile-green">
  <div class="tile-head">AI Infrastructure — AVGO at $483, pre-print momentum</div>
  <div class="tile-body">AVGO +4.9% on June 2. Vera Rubin in production, 6 hyperscaler ASIC customers, Hock Tan's $100B 2027 target. Every preview points toward a beat. The question is the Q3 guide. Oppenheimer, Morgan Stanley both maintained Buy/Overweight. ARK added 300k NVDA shares June 1.</div>
</div>
<div class="tile tile-red">
  <div class="tile-head">European equities — ECB hike in 8 days, Iran makes it worse</div>
  <div class="tile-body">DAXK −0.5% YTD. ECB hiking June 11 into 3.2% eurozone inflation while Hormuz closure keeps energy costs elevated. This is the Papic constraint on Europe: monetary tightening AND supply-side inflation simultaneously. Short EURAUD (MM-2026-001) is the most direct expression.</div>
</div>"""

POSITIONING = """
<div class="section-label">Positioning &amp; Flows</div>
<div class="tile tile-muted">
  <div class="tile-head">Oil: managed funds added net-long 3 consecutive weeks; Iran halt is a squeeze catalyst</div>
  <div class="tile-body">Oil managed fund positioning had flipped to net-long with 3 consecutive weeks of additions. The Iran halt announcement is the squeeze catalyst — any remaining shorts are underwater. This adds velocity to any Brent move above $95. MM-2026-002 benefits from this positioning dynamic.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-head">AVGO: options traders bet on strong earnings (CNBC); implied move ±8% absorbed in stock price</div>
  <div class="tile-body">Pre-earnings, options traders were positioned for a positive outcome. AVGO's +4.9% on June 2 means some of the upside was pulled forward. A genuine beat-and-raise still delivers +8–12% from $483; an in-line print now hurts more (the stock is already pricing optimism). The asymmetry to the downside has increased.</div>
</div>"""

FUNDING = """
<div class="section-label">Funding &amp; Plumbing</div>
<div class="tile tile-muted">
  <div class="tile-claim">SOFR 3.63% — stable. ADP May report released today (April: 109k vs 99k consensus).</div>
  <div class="tile-body">No funding stress. The Pozsar layer today: ADP May is the first concrete payroll signal before Friday's BLS print. April ADP beat 99k consensus with 109k. If May ADP is 120k+, the Friday payrolls market will be on edge for a 130k+ print that triggers Fed hike discussion. ADP and payrolls are not perfectly correlated, but the directional read matters. Verify the May ADP number released this morning.</div>
</div>"""

TAPE_MISSING = """
<div class="section-label">What the Tape Is Missing</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>Iran's "halt talks" is a negotiating move, not a final position — the clock is working against them.</strong> Iran's sovereign reserve depletion at current oil revenue blockade levels reaches a critical threshold in approximately 90 days from April (the start of the conflict). Today is Day 56. The political decision to halt talks publicly is designed to maximize negotiating leverage before their economic position forces them to accept worse terms. The Papic constraint is symmetrical: Trump needs a deal before June 11; Iran needs one before their reserves hit critical. Watch for back-channel signals in the next 72 hours as the public posturing peaks.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>The AVGO in-line scenario (−5 to −8%) cascades into AI spending re-evaluation across all hyperscalers.</strong> Google (Alphabet) just raised $80 billion to fund AI capex. If Broadcom's AI revenue misses its own Q2 guidance, the immediate question is: which hyperscaler pulled back? Microsoft, Meta, Google, or Anthropic? The market will assign the miss to the weakest link — the one whose AI ROI case is most uncertain. If it's Anthropic or OpenAI (the startup customers), the market recalibrates the whole AI capex cycle. If it's Google, it reprices the $80B equity raise. A miss doesn't just move AVGO; it moves the probability distribution on every AI infrastructure name.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>ADP May + ISM 54% + payrolls Friday = three consecutive strong labor signals heading into FOMC June 17.</strong> If ADP today comes in above 120k, the FOMC dot plot on June 17 becomes a live event where a hike dot is possible. Nobody in the market is positioned for a hike. IG at 80bp, HY at 285bp, SPX at 30x — these are all priced for a benign hold. A hike dot would be the largest repricing event of the quarter, larger than AVGO. The level that changes the conversation: ADP May above 125k today.</div>
</div>"""

CONSENSUS = """
<div class="section-label">Consensus: Bid / Offer</div>
<div class="tile tile-muted">
  <div class="tile-head">Consensus BID</div>
  <div class="tile-body">AVGO beats tonight (seventh consecutive AI revenue beat). Iran blinks within a week and signs the MoU. ADP and payrolls are solid but not hot enough for hike talk. ECB hike June 11 absorbed as priced. VIX retreats below 16. SPX pushes toward 8,000.</div>
</div>
<div class="tile tile-gold">
  <div class="tile-head">Strongest argument against — the OFFER</div>
  <div class="tile-body">The consensus requires three things to go right simultaneously: AVGO beats tonight, Iran reverses in the next 72 hours, and payrolls Friday stay below 130k. Any one of these three outcomes going wrong causes a repricing. All three going wrong simultaneously creates a stagflation narrative for the US (oil up, growth hot, Fed hike risk) that no current position in the market is hedged against. The put spread (MM-2026-008) is the only hedge we have on that three-tail-risk scenario.</div>
</div>"""

ONE_CHART = """
<div class="section-label">Today's One Chart That Matters</div>
<div class="tile tile-gold">
  <div class="tile-claim">Brent crude intraday — the Hormuz risk premium in real time</div>
  <div class="tile-body">Brent at $94.80 after Iran halted talks. The war was already partly priced; this is the market correcting the "deal is imminent" discount that never should have been applied. The Brent-WTI spread at $3.40 (above entry 3.30) tells you physical traders believe the Hormuz premium is real. Watch Brent's close today: above $96 signals full Hormuz closure re-pricing; below $93 signals the market thinks Iran will reverse quickly. Our oil positions (MM-2026-002, MM-2026-003) want a close above $95. AVGO dominates attention but Brent is the silent tell on whether the brief's macro framework survives the week intact.</div>
</div>"""

CAT_CAL = """
<div class="section-label">Catalyst Calendar</div>
<table class="cal-table">
<thead><tr><th>Day</th><th>Date</th><th>Event</th><th>Consensus</th><th>View</th><th>Asymmetry</th></tr></thead>
<tbody>
<tr>
  <td>Wed</td><td>Jun 3</td>
  <td class="cal-event">AVGO Q2 FY2026 earnings (after close) · ADP May report (8:15 ET)</td>
  <td>AVGO: EPS $2.40, rev $22.08B, AI rev $10.7B. ADP: ~100k (Apr was 109k)</td>
  <td>AVGO: Q3 guide is the only number. ADP above 125k = payrolls Friday setup for 130k+. Both catalysts run today.</td>
  <td class="asym-up">AVGO beat: +8–12% AH; ADP >125k: 10Y +5bp, hike talk starts</td>
</tr>
<tr>
  <td>Thu</td><td>Jun 4</td>
  <td class="cal-event">Post-AVGO open · Iran back-channel signals · ADP May (if released Wed)</td>
  <td>Market processes AVGO result; Iran negotiations could resume or escalate</td>
  <td>Post-beat: buy first-hour dip in AVGO. Post-miss: short dead-cat bounce. Iran reversal would compress Brent-WTI spread immediately — watch for diplomatic signals.</td>
  <td class="asym-up">AVGO gap confirm: SOX +2–3%; Iran reversal: Brent −$3–5</td>
</tr>
<tr>
  <td>Fri</td><td>Jun 5</td>
  <td class="cal-event">US May payrolls (BLS, 8:30 ET) + German IFO</td>
  <td>+90k (Dow Jones); ISM 54% and ADP beat point to potential upside</td>
  <td>If ADP today beats 125k, Friday's payrolls consensus of 90k is almost certainly too low. Above 130k payrolls: DXY bids, 10Y spikes toward 4.60%, MM-2026-004 stop at 4.65% is live. IFO below 90 = ECB June 11 hike is a confirmed policy error.</td>
  <td class="asym-dn">>130k: 10Y +15bp, MM-2026-004 stop live; &lt;75k: DXY −0.8%, gold +$50</td>
</tr>
<tr>
  <td>Wed</td><td>Jun 11</td>
  <td class="cal-event">ECB rate decision (+25bp fully priced; inflation now 3.2%, services 3.5%)</td>
  <td>+25bp hike; potentially hawkish forward guidance given inflation surprise</td>
  <td>Hormuz closure + 3.2% eurozone CPI = the ECB hike is the most unambiguous decision of 2026. EUR sell-the-fact remains the pain trade as spec longs unwind. MM-2026-001 is positioned for exactly this.</td>
  <td class="asym-dn">EUR/USD −0.8% on pause signal; +0.5% then fade if hawkish</td>
</tr>
<tr>
  <td>Tue–Wed</td><td>Jun 16–17</td>
  <td class="cal-event">FOMC meeting + dot plot — live event if payrolls surprise Friday</td>
  <td>No cut. But ISM 54% + ADP beats + payrolls >130k could introduce hike dot.</td>
  <td>The dot plot is now a genuine market-moving event, not a formality. If a hike dot appears for 2026 or 2027, IG spreads widen from 80bp, DXY rallies, gold sells. If 0-cut median with no hike: DXY +0.7%, gold −2%. If 2-cut median (requires weak Friday): DXY −1.2%.</td>
  <td class="asym-dn">Hike dot: DXY +1.5%, 10Y +20bp; 0-cut: DXY +0.7%; 2-cut: DXY −1.2%</td>
</tr>
</tbody>
</table>"""

MIND = """
<div class="section-label">What Changes My Mind</div>
<div class="mind-item"><strong>MM-2026-001 · Short EURAUD (1.620, P&L +1.52%):</strong> Close if EURAUD holds above 1.640 post-ECB June 11. Currently 0.6% from target 1.610. Iran escalation bid AUD temporarily but ECB hike thesis is dominant. Hold.</div>
<div class="mind-item"><strong>MM-2026-002 · Long Brent ($94.80, P&L +4.18%):</strong> Exit below $87 weekly close (deal signed and Hormuz fully open). Iran halting talks moves this scenario much further away. Raise mental stop to $90 if Iran signs a deal. Current trajectory: $100+ if Hormuz stays closed through June 11.</div>
<div class="mind-item"><strong>MM-2026-003 · Long Brent/WTI spread ($3.40, P&L +3.03%):</strong> The trade has recovered above entry. Stop 1.50 — well clear. Close if spread closes below 2.50 (deal imminent) or raises stop to $3.00 to protect half the recovery. Iran halt extends the trade's life significantly.</div>
<div class="mind-item"><strong>MM-2026-004 · Short US 10Y yield (4.46%, P&L −0.45%):</strong> Stop 4.65% — now 19bp away. Iran risk-off slightly bid bonds today (yields fell 1bp) but ISM + ADP threat looms. If ADP today >125k, reduce position size before Friday. The risk is a Friday payrolls shock into the stop.</div>
<div class="mind-item"><strong>MM-2026-005 · Long gold ($4,540, P&L +0.38%):</strong> Min hold until July 15. Stop $4,250. Gold is working on both tails (Iran bid + Fed cut optionality). Iran halt is a near-term catalyst; FOMC dot plot June 17 is the structural catalyst. Hold.</div>
<div class="mind-item"><strong>MM-2026-006 · Long AVGO ($483, P&L +5.00%) — TONIGHT is the exit event:</strong> See AVGO section above. Beat-and-raise: hold through print + 5 days, raise stop to $490 once stock opens above $520. In-line: exit same day. Miss: exit at market open Thursday.</div>
<div class="mind-item"><strong>MM-2026-007 · Short USDJPY (158.90, P&L +0.29%):</strong> Working. Iran risk-off bid yen 47 pips. Stop 163.00 — further away now. BoJ September hike thesis intact. Hold.</div>
<div class="mind-item"><strong>MM-2026-008 · SPX put spread:</strong> Do NOT exit. AVGO tonight + payrolls Friday + Iran escalation = three concurrent catalysts. The premium is the cheapest portfolio hedge available right now.</div>"""

CLIENT_AMMO = """
<div class="section-label">Talking Points Today</div>
<div class="ammo">
  <div class="ammo-q">Iran just halted talks. What does that mean for our oil trades?</div>
  <div class="ammo-a">It's the thesis confirmation we've been waiting for. MM-2026-002 (Long Brent, +4.18%) and MM-2026-003 (Long Brent/WTI spread, +3.03%) were built on the premise that the MoU was being priced too optimistically. Iran halting talks removes the last justification for pricing a deal. Brent has room to $100+ if Hormuz stays closed through June 11. The stop on MM-2026-002 is $87 — we're $7.80 above it. This is the strongest part of the book right now.</div>
</div>
<div class="ammo">
  <div class="ammo-q">What's the one number to watch in AVGO's earnings call tonight?</div>
  <div class="ammo-a">The Q3 AI revenue guidance figure. Q2's own guidance was $10.7B. The market needs the Q3 guide to be above $12.0B to justify 41x forward earnings. Above $12B = beat-and-raise, stock +8–12% after-hours. In the $11.0–11.9B range = in-line, −5–8% as the multiple contracts. Below $10.5B = demand pull-forward concern, −10–15%. Listen to the Q&A for whether Hock Tan names customers by name — if he avoids naming them, one of the six ASIC programs has slipped.</div>
</div>
<div class="ammo">
  <div class="ammo-q">Can stocks stay at records if Iran keeps Hormuz closed?</div>
  <div class="ammo-a">They have so far. The reason: the market believes AI earnings growth can outrun the oil price shock. At SPX 7,600 with Brent at $94.80, equities are saying the AI growth premium is larger than the energy cost headwind. That calculus holds only if AVGO confirms it tonight. A miss from AVGO tonight plus Hormuz closed would simultaneously remove the growth premium and add the cost headwind. That scenario is not priced — VIX at 16.5 doesn't reflect two simultaneous bear cases.</div>
</div>"""

CITATIONS = """
<div class="section-label">Citations</div>
<div class="citation">
Sources beyond Reuters / Bloomberg / FT / WSJ / AP / central banks / CME / Cboe:<br>
· TheHill — "Iran halts ceasefire talks with US, says it will keep Strait of Hormuz closed" (thehill.com)<br>
· TradingEconomics / Capital.com — Brent $94.80, Gold $4,540 June 3 (tradingeconomics.com)<br>
· TradingKey / CNBC — AVGO opened +4.90% on June 2; options traders bet on strong earnings (tradingkey.com)<br>
· AlphaStreet / S&P Global — AVGO EPS consensus $2.40, rev $22.08B; avg PT $482.31 (47 analysts) (alphastreet.com)<br>
· GuruFocus — Morgan Stanley AVGO PT raised to $485; ARK adds 300k NVDA shares June 1 (gurufocus.com)<br>
· Motley Fool / TECHi — Broadcom earnings preview, AI ASIC bar analysis (fool.com / techi.com)<br>
· ADP / PRNewswire — April ADP: 109k private sector jobs vs 99k consensus (adpemploymentreport.com)<br>
· CNBC / Kalshi — Payrolls Friday consensus 90k; traders expect beat (cnbc.com)<br>
· Rio Times / Euronews — Eurozone CPI 3.2% May, services 3.5% (riotimesonline.com)<br>
· Broadcom Investor Relations — Q2 FY2026 guidance: $22B revenue, $10.7B AI revenue (investors.broadcom.com)<br>
· TIKR / PRNewswire — Hock Tan: "$100 billion AI chip revenue in 2027" (tikr.com)
</div>"""

STALENESS = """
<div class="section-label">Staleness Check</div>
<table class="stale-tbl">
<thead><tr><th>Datum</th><th>Source</th><th>As of</th><th>Status</th></tr></thead>
<tbody>
<tr><td>Iran halted talks + Hormuz closure</td><td>TheHill</td><td>2026-06-02/03</td><td class="fresh">Fresh</td></tr>
<tr><td>Brent ~$94.80</td><td>TradingEconomics</td><td>2026-06-03 (est)</td><td class="fresh">Fresh</td></tr>
<tr><td>WTI ~$91.40</td><td>TradingEconomics (est)</td><td>2026-06-03 (est)</td><td class="fresh">Fresh</td></tr>
<tr><td>Gold ~$4,540</td><td>Capital.com / TradingEconomics</td><td>2026-06-03</td><td class="fresh">Fresh</td></tr>
<tr><td>AVGO ~$483</td><td>TradingKey (Jun 2 open +4.90%)</td><td>2026-06-02</td><td class="stale-flag">Stale — verify pre-print</td></tr>
<tr><td>AVGO Q2 actual results</td><td>Not yet released (reports tonight)</td><td>n/a</td><td class="stale-flag">Pending — report after close today</td></tr>
<tr><td>ADP May 2026</td><td>ADP (released Jun 3 08:15 ET)</td><td>2026-06-03</td><td class="stale-flag">May not be indexed yet — verify live</td></tr>
<tr><td>US 10Y 4.46%</td><td>TradingEconomics</td><td>2026-06-02</td><td class="stale-flag">Stale — verify live</td></tr>
<tr><td>EURUSD ~1.165</td><td>TradingEconomics</td><td>2026-06-02</td><td class="stale-flag">Stale — verify live</td></tr>
<tr><td>USDJPY ~158.90</td><td>Estimated from Iran risk-off move</td><td>est. 2026-06-03</td><td class="stale-flag">Approximate</td></tr>
<tr><td>EURAUD ~1.620</td><td>Est. from Jun 2 data (1.6349)</td><td>est. 2026-06-03</td><td class="stale-flag">Approximate</td></tr>
<tr><td>VIX ~16.50</td><td>Estimated from Jun 1 close 16.05 + Iran premium</td><td>est.</td><td class="stale-flag">Approximate</td></tr>
<tr><td>Bund, Gilt, MOVE, USDCNH</td><td>Not sourced this refresh</td><td>unavailable</td><td class="stale-flag">Unavailable</td></tr>
</tbody>
</table>"""

# ── Dashboard ─────────────────────────────────────────────────────────────────
DASH = [
    ("S&P 500",      "7,599.96",  "+0.26% (Jun 1 record)", "up"),
    ("Nasdaq",       "27,086.81", "+0.42% (Jun 1 record)", "up"),
    ("Nikkei 225",   "66,934",    "+31.8% YTD",            "up"),
    ("DAX",          "~25,200",   "−0.5% YTD",             "flat"),
    ("FTSE 100",     "~10,350",   "",                      "flat"),
    ("EURUSD",       "~1.165",    "",                      "flat"),
    ("GBPUSD",       "—",         "",                      "unverified"),
    ("USDJPY",       "~158.90",   "yen bid on Iran",       "down"),
    ("EURAUD",       "~1.620",    "ECB→short thesis",      "down"),
    ("DXY",          "~99.1",     "+0.1%",                 "up"),
    ("US 10Y",       "4.46%",     "",                      "flat"),
    ("2s10s",        "~+15bp",    "",                      "flat"),
    ("WTI Crude",    "~$91.40",   "Iran halt bid",         "up"),
    ("Brent Crude",  "~$94.80",   "Hormuz closure risk",   "up"),
    ("Brent-WTI",    "~$3.40",    "+0.10 vs entry",        "up"),
    ("Gold (XAU)",   "~$4,540",   "+$11 Iran bid",         "up"),
    ("VIX",          "~16.50",    "rising into AVGO",      "up"),
    ("AVGO",         "~$483",     "+4.9% pre-earnings",    "up"),
    ("SOFR",         "3.63%",     "",                      "flat"),
    ("ISM Mfg May",  "54.0%",     "highest since May 2022","up"),
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
    '<div class="theme-line">Iran halted talks; Hormuz stays closed. '
    'AVGO reports tonight. Two tails, one evening — '
    'the brief holds if both resolve; breaks on either one.</div>'
)

# Trade cards
new_today = [t for t in trades["open"] if t["id"] in
             ("MM-2026-006", "MM-2026-007", "MM-2026-008", "MM-2026-009")]
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

# ── Assemble ──────────────────────────────────────────────────────────────────
LHS = "\n".join([
    YESTERDAY, AVGO_SECTION, WRAP,
    CORRELATION, VOL_SKEW, SECTOR_RV, POSITIONING, FUNDING,
    TAPE_MISSING, CONSENSUS, ONE_CHART, CAT_CAL, MIND,
    CLIENT_AMMO, CITATIONS, STALENESS,
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
