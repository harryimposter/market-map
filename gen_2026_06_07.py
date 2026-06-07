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
    "MM-2026-001": 1.615,    # EURAUD ~1.615 (carried)
    "MM-2026-002": 93.09,    # Brent: gave back to ~$93 as risk assets sold off
    "MM-2026-003": 2.55,     # Brent-WTI spread: 93.09 − 90.54
    "MM-2026-004": 4.53,     # US 10Y: jumped >4.5% on the hot jobs print
    "MM-2026-005": 4328.0,   # Gold: ~$4,328 (TVC:GOLD) — sold in the liquidation
    "MM-2026-006": 385.73,   # AVGO: ~$385.73 — collapsed from $462; STOP $422 breached
    "MM-2026-007": 160.27,   # USDJPY: ~160.27 (DXY firm on hot jobs)
    "MM-2026-008": 70.0,     # SPX put spread: hedge paid as the S&P fell on the print
    "MM-2026-009": 0.38,     # 2s10s: steepened to ~+38bp (2Y 4.15, 10Y 4.53)
}
book.mark_to_market(trades, levels)

regime      = "Sell-the-Fact Became a Re-Rating; Hot Jobs Kill the Cut"
regime_note = (
    "Broadcom's light AI guide ($16B Q3 vs ~$17.2B hoped, no FY26 raise) turned a beat "
    "into a -14% rout; SOX -10%, Nasdaq -4.2%, ~$1T wiped in two sessions. Then May "
    "payrolls +172k vs ~80k expected sent the 10Y >4.5% and pushed rate-cut odds out "
    "(year-end hike odds ~70%). VIX +40% to ~21.5; even gold (-3.3%) sold. The book's "
    "AVGO long stopped out; the SPX put-spread hedge and the steepener earned their keep."
)
regime_log = book.update_regime_log(regime_log, regime, regime_note)

# Charts
eq_svg  = charts.equity_curve(trades["closed"])
cal_svg = charts.calibration(trades["closed"])
vix_svg = charts.vix_term_structure([
    {"label": "VIX9D", "value": 23.5},
    {"label": "VIX",   "value": 21.5},
    {"label": "VIX3M", "value": 20.8},
    {"label": "VIX6M", "value": 20.4},
])
yc_svg  = charts.yield_curve([
    {"label": "2Y",  "value": 4.15},
    {"label": "5Y",  "value": 4.34},
    {"label": "10Y", "value": 4.53},
    {"label": "30Y", "value": 5.02},
])

# ── AVGO Results Section (ACTUAL Q2 FY2026 numbers confirmed) ─────────────────
AVGO_SECTION = """
<div class="section-label">Broadcom (AVGO) — the guide that broke the tape</div>
<div class="avgo-box">

<p style="font-size:11px;color:var(--ink-mute);margin-bottom:.75rem">Sources: CNBC, 24/7 Wall St, TheStreet, GuruFocus (Jun 4–5, 2026). Prices via TradingView.</p>

<div class="section-label" style="color:var(--gold)">What actually happened</div>
<div class="avgo-results-grid">
  <div class="avr miss"><div class="av">$16.0B</div><div class="al">Q3 AI guide · vs ~$17.2B hoped · the miss that mattered</div></div>
  <div class="avr watch"><div class="av">no raise</div><div class="al">FY26 AI forecast left unchanged · the tell</div></div>
  <div class="avr miss"><div class="av">−14%</div><div class="al">AVGO on the session · classic sell-the-news</div></div>
  <div class="avr miss"><div class="av">~$386</div><div class="al">AVGO now (TradingView) · down from ~$462</div></div>
  <div class="avr miss"><div class="av">SOX −10%</div><div class="al">2-day semis rout · MU, AMD, INTC, ARM dragged</div></div>
  <div class="avr miss"><div class="av">~$1T</div><div class="al">Market cap wiped across chips in two sessions</div></div>
</div>

<div class="section-label" style="color:var(--gold)">Why it mattered</div>
<p style="font-size:12px;color:var(--ink-soft);line-height:1.6;margin-bottom:.75rem">
The numbers weren't a disaster — the <i>expectations</i> were. Broadcom guided Q3 AI revenue to ~$16B against a whisper closer to $17.2B and, critically, <strong>did not raise its full-year AI forecast.</strong> After a year of beat-and-raise conditioning, "merely good + no raise" was read as the first crack in the AI-capex super-cycle. HSBC flagged a slide in chip prices and a slowdown in AI spend/rollout as its biggest worries. The reaction was violent and broad: every AI/memory name was sold, not just AVGO.
</p>

<div class="section-label" style="color:var(--gold)">MM-2026-006 (long AVGO, entry $460) — STOPPED OUT</div>
<div class="avgo-verdict sell">
  <strong>The stop at $422 was breached; AVGO now ~$386.</strong> The brief's AVGO long is closed for a loss (~−16% from entry). This is the discipline working as designed — a hard stop turned a thesis-breaker into a bounded loss rather than an open wound. The "buy the confirmed cycle at 41×" thesis was wrong <i>for now</i>: a confirmed cycle with a higher discount rate and a single soft guide is a sell, not a hold.<br><br>
  <strong>Lesson logged:</strong> when a name has been beat-and-raise for a year, the asymmetry flips — the bar to <i>keep</i> rallying is a raise, and "in-line, no raise" is a downgrade catalyst. We were long the wrong side of that asymmetry into the print.
</div>

<div class="avgo-scen exit" style="margin-top:6px">
  <div class="sh" style="color:var(--red)">No re-entry yet — let the knife land</div>
  <div class="st">Confirmed cycle, but the multiple is resetting into higher yields — wait for a base</div>
  <div class="sb">AVGO at ~$386 is cheaper, and the AI backlog story is not dead. But catching a −14% day into a 10Y &gt; 4.5% and a hawkish-leaning FOMC (Jun 16–17) is low-quality. The setup I want: a few sessions of basing, hyperscaler capex commentary that holds, and memory pricing that stabilises — then a defined-risk re-entry. For now the book has no AVGO exposure, and that's the right place to be.
  <div class="disc">Informational analysis only. Not financial advice.</div>
  </div>
</div>

</div>"""

# ── LHS sections ──────────────────────────────────────────────────────────────
MASTHEAD = f"""
<div class="masthead">
  <div class="regime-tag">Sell-the-Fact Became a Re-Rating; Hot Jobs Kill the Cut</div>
  <h1 class="article-title">One Soft Guide, and the AI Trade Found the Door</h1>
  <p class="meta">Pre-market intelligence brief &middot; {TODAY} &middot; generated {NOW} local &middot; self-graded book</p>
  <hr class="gold-rule">
</div>"""

YESTERDAY = """
<div class="section-label">The book through the selloff, graded</div>
<div class="yesterday">
  <div class="yest-item"><span class="tick-r">✗</span>
    <span><strong>MM-2026-006</strong> · Long AVGO (entry $460) · <strong>STOPPED OUT ~$386</strong> · <span class="pnl-neg">−16%</span> · The big loss. A soft Q3 AI guide and no FY26 raise flipped a year of beat-and-raise; AVGO −14% on the day, broke the $422 stop. Discipline did its job — bounded loss, position closed, no AVGO exposure now.</span></div>
  <div class="yest-item"><span class="tick-g">✓</span>
    <span><strong>MM-2026-008</strong> · SPX put spread · 35 → 70 · <span class="pnl-pos">+100%</span> · The hedge that paid. S&P −2.6% on the jobs print, semis −10% — the put spread did exactly what a hedge is for in a crowded-trade washout.</span></div>
  <div class="yest-item"><span class="tick-g">✓</span>
    <span><strong>MM-2026-009</strong> · 2s10s steepener · +15bp → +38bp · <span class="pnl-pos">working</span> · Hot payrolls steepened via the long end (30Y &gt; 5%) while the front stayed anchored — the supply/term-premium thesis playing out.</span></div>
  <div class="yest-item"><span class="tick-n">→</span>
    <span><strong>MM-2026-002</strong> · Long Brent · $91.00 → $93.09 · <span class="pnl-pos">+2.3%</span> · Gave back most of the +7.5% as oil sold with everything in the liquidation. Still green vs entry; trailing stop $90.</span></div>
  <div class="yest-item"><span class="tick-r">✗</span>
    <span><strong>MM-2026-005</strong> · Long gold (pre-pos) · $4,523 → $4,328 · <span class="pnl-neg">−4.3%</span> · The hedge that didn't hedge. Gold sold in the cash-raising / stronger-real-yield move. Stop $4,250 still intact; this is a liquidation dip, not (yet) a trend break (Howell would add).</span></div>
  <div class="yest-item"><span class="tick-r">✗</span>
    <span><strong>MM-2026-004</strong> · Short US 10Y yield · 4.44% → 4.53% · <span class="pnl-neg">losing</span> · Wrong way. +172k payrolls sent the 10Y above 4.5%; stop 4.65% now ~12bp away. Most-exposed position into the FOMC.</span></div>
  <div class="yest-item"><span class="tick-r">✗</span>
    <span><strong>MM-2026-007</strong> · Short USDJPY · 158.80 → 160.27 · <span class="pnl-neg">losing</span> · DXY firmed on the hot print; yen back through 160. Stop 163.00. BoJ-divergence thesis intact but the dollar has the rate story for now.</span></div>
  <div class="yest-item"><span class="tick-n">→</span>
    <span><strong>MM-2026-003</strong> · Long Brent / Short WTI spread · 3.30 → 2.55 · <span class="pnl-neg">underwater</span> · Spread stayed compressed; WTI and Brent fell together. Edge has narrowed; watching for a close below 2.00.</span></div>
  <div class="yest-item"><span class="tick-n">→</span>
    <span><strong>MM-2026-001</strong> · Short EURAUD · 1.6150 → 1.615 · <span class="chg-flat">flat</span> · Quiet through the equity rout; FX crosses held. Target 1.610 still in sight.</span></div>
</div>"""

WRAP = """
<div class="section-label">The Wrap</div>
<div class="wrap-body">
<p>It took one soft sentence to end a year-long spell. Broadcom's quarter was fine —
but it guided Q3 AI revenue to ~$16B against a whisper near $17.2B and, the part that
mattered, <strong>did not raise its full-year AI forecast.</strong> After twelve months of
conditioning the market on beat-and-raise, "good and no raise" was treated as the first
crack. AVGO −14%, the SOX −10% over two sessions, the Nasdaq −4.2%, roughly $1T of chip
market cap gone.

<p>This is not yet a story about the AI cycle being wrong. It is a story about <strong>what
was priced</strong> and <strong>what it's discounted at.</strong> The most-crowded trade on
the planet was long AI/semis at full multiples, and it was carrying that position into a
rising discount rate. When the marginal guide stopped accelerating, the crowd reached for
the same exit at once.

<p>Then the macro made it worse. <strong>May payrolls printed +172k against ~80k expected</strong>,
unemployment 4.3%. That didn't just trim rate-cut odds — it flipped the conversation toward
<strong>hikes</strong> (year-end hike odds ~70%, a December hike now the base case in pricing).
The 10Y pushed above 4.5%, the 30Y above 5%. Long-duration equities — which is what an
un-earning, growth-priced AI multiple is — got the worst possible cocktail: growth doubt
and a higher discount rate in the same 48 hours.

<p><strong>L1 — Driver.</strong> The regime has inverted. For a year, "strong economy + AI
capex" was the melt-up. Now "strong economy" means "no cuts, maybe hikes," and that is the
thing that breaks the multiple. Good news is bad news again.

<p><strong>L2 — The hook.</strong> Even gold sold (−3.3%) and silver got hit (−8.3%). When the
hedges go down with the risk, you're seeing forced de-grossing / cash-raising, not a
considered rotation. That's typically a <i>positioning</i> event — violent, but it burns
out — rather than the start of a fundamental unwind. Howell's framework says buy the gold
dip; the equity dip needs the discount-rate side to stop getting worse first.

<p><strong>L3 — The gap.</strong> Priced now: no Fed cuts, a live hike, AI multiples reset a
notch. Not yet priced: whether this is a one-quarter air-pocket in AI capex or the first
domino. The June 16–17 FOMC and the next round of hyperscaler capex commentary decide
which. Until then, the book wants less beta, more hedge, and dry powder.
</div>

<div class="section-label">Scenarios into the June 16–17 FOMC</div>
<div class="grid-3">
  <div class="tile tile-green">
    <div class="tile-head">Bull — 35%</div>
    <div class="tile-claim">Positioning flush exhausts; AI names base and bounce</div>
    <div class="tile-body">The selloff was de-grossing, not a fundamental break. Dip-buyers step in on quality AI/memory at lower multiples; VIX falls back from ~21. Yields stabilise as the jobs print is digested. SPX recovers part of the drop into the FOMC. Gold rebounds off the liquidation low.</div>
  </div>
  <div class="tile tile-gold">
    <div class="tile-head">Base — 45%</div>
    <div class="tile-claim">Choppy de-risking; market waits for the FOMC dots</div>
    <div class="tile-body">No V-shape and no crash — a higher-vol range as the market reprices the rate path. AI leaders chop while the multiple resets; defensives, cash and the steepener outperform. 10Y holds 4.45–4.60%. The FOMC dot plot is the next real catalyst; a hawkish lean keeps pressure on duration assets.</div>
  </div>
  <div class="tile tile-red">
    <div class="tile-head">Bear — 20%</div>
    <div class="tile-claim">AI capex doubt + a hawkish Fed → the unwind broadens</div>
    <div class="tile-body">Hyperscaler capex commentary softens, more chip names guide light, and the FOMC pencils in a hike. The crowded long unwinds further; credit spreads start to widen off tight levels; the put-spread hedge keeps paying and gold/duration become the haven. This is the tail the hedges are there for.</div>
  </div>
</div>

<div class="wrap-body">
<p><strong>The crowding tell.</strong> The single most important thing about this drop is what
sold <i>together</i>: AVGO, MU, NVDA, AMD, ARM, Korea — every expression of one trade. That
correlation-to-one is the signature of a positioning unwind. The good news: those burn out.
The bad news: you don't know the bottom until the forced sellers are done, and a hawkish
Fed can extend the timeline.

<p><strong>The rates mechanic.</strong> +172k didn't just remove cuts — at 30Y &gt; 5% the long
end is doing the tightening for the Fed via term premium. That is the steepener's thesis
(MM-2026-009) and the reason short-duration cash is a real position here, not a cop-out.

<p><strong>The discipline note.</strong> The book's AVGO long stopped out for ~−16%. That stings,
but it's the system working: a hard stop converted a thesis-breaker into a bounded, known
loss while the put-spread hedge and the steepener offset much of it. The lesson logged —
into a name that's been beat-and-raise for a year, "in-line, no raise" is a sell catalyst,
and we were long the wrong side of that asymmetry into the print.
</div>"""

CORRELATION = """
<div class="section-label">Correlation Regime</div>
<div class="tile tile-muted">
  <div class="tile-claim">Everything-AI sold as one — correlation-to-1 is the unwind signature</div>
  <div class="tile-body">AVGO, MU, NVDA, AMD, ARM and Korea all fell together on the same catalyst. When a basket that <i>is</i> a single trade moves in lockstep, you are watching a positioning unwind, not stock-specific repricing. That's violent but mean-reverting — the tell that the bottom is near is when good names stop falling with bad ones.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">Hedges failed: gold −3.3%, silver −8.3% sold <i>with</i> equities</div>
  <div class="tile-body">In a genuine de-grossing / cash-raising day, correlations go to 1 and even the diversifiers get sold for liquidity. Gold down with stocks is a liquidity tell, not a regime change — Howell's framework says buy that dip. The week-ahead test: do metals re-decouple as the forced selling clears?</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">Stocks down, yields up, dollar up — the rate side did the damage</div>
  <div class="tile-body">The hot +172k jobs print pushed the 10Y &gt; 4.5%, the 30Y &gt; 5%, and firmed the dollar — the cleanest expression of "no cuts, maybe hikes." Long-duration equities (un-earning AI multiples) are most exposed to exactly this combination. Watch whether yields stabilise this week; equities can't base until they do.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">Defensives &amp; cash outperformed — first rotation, or just less-bad?</div>
  <div class="tile-body">Quality/low-beta and cash held up as the crowded growth trade unwound (Berkshire was actually green). It's too early to call it a durable rotation; into the FOMC it's more "where you hide" than "where you add." The week ahead tells us if money rotates or just de-risks.</div>
</div>"""

VOL_SKEW = """
<div class="section-label">Vol &amp; Skew</div>
<div class="vol-surface">
  <strong>VIX ~21.5, +40% on the move — and the term structure inverted (backwardation):</strong>
  VIX9D ~23.5 · VIX ~21.5 · VIX3M ~20.8 · VIX6M ~20.4.
  Front-month above the back is a stress signature — the market is paying up for
  near-dated protection. Backwardated VIX usually <i>resolves</i> within days/weeks (it
  un-inverts as panic fades), which historically marks tactical lows — but only once spot
  vol rolls over. Watch for VIX back under ~18 as the all-clear this week.
</div>
<div style="height:8px"></div>
<div class="tile tile-gold">
  <div class="tile-head">The hedge worked</div>
  <div class="tile-claim">MM-2026-008 SPX put spread doubled (35 → 70) as the index fell on the print</div>
  <div class="tile-body">This is the entire point of carrying a defined-cost hedge into a crowded, expensive tape: it pays when the unwind comes. With VIX still elevated, the remaining time value is worth more — consider monetising part of the gain into the spike rather than round-tripping it if the market stabilises this week.</div>
</div>"""

SECTOR_RV = """
<div class="section-label">Sector &amp; RV</div>
<div class="tile tile-red">
  <div class="tile-head">AI semis — the epicentre, SOX −10% in two sessions</div>
  <div class="tile-body">AVGO (−14%), Micron, NVDA, AMD, ARM all hit on the AVGO guide + HSBC's flag on chip prices / AI-spend slowdown. The cycle isn't confirmed dead — but "in-line, no raise" reset the multiple hard. The week-ahead swing factor is hyperscaler capex commentary and memory pricing; that decides air-pocket vs downgrade-cycle.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-head">Energy — softened with risk; oil is not the story this week</div>
  <div class="tile-body">Brent ~$93, WTI ~$90 gave back as risk assets sold. MM-2026-002 (long Brent) still green vs entry but off its highs. With the macro focus on rates and AI, energy is a follower this week, not a leader; watch inventories and any Middle East headlines.</div>
</div>
<div class="tile tile-red">
  <div class="tile-head">Rate-sensitives — duration &amp; gold pressured; steepener the bright spot</div>
  <div class="tile-body">10Y &gt; 4.5% pressured the short-yield trade (MM-2026-004, stop ~12bp away) and gold (−4.3% vs entry). The clean winner is the 2s10s steepener (+38bp) as the long end leads. Into the FOMC, the long end is where the action is.</div>
</div>"""

POSITIONING = """
<div class="section-label">Positioning &amp; Flows</div>
<div class="tile tile-muted">
  <div class="tile-head">The most-crowded trade got flushed — partway</div>
  <div class="tile-body">Long AI/semis at full multiples was the consensus book into this. The two-session, ~$1T de-grossing is a partial unwind; systematic sellers (CTAs, vol-control) typically add supply as realised vol jumps, which can extend the move early in the week before it clears. The tell that selling is done: down opens that get bought.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-head">Jobs flipped the macro positioning — cuts priced out</div>
  <div class="tile-body">+172k vs ~80k expected pushed traders to price out cuts and lift year-end hike odds toward ~70% (a December hike now the base case). That repriced the whole curve and the dollar in hours. The week ahead is about whether that pricing holds into the FOMC, or fades if data softens.</div>
</div>"""

FUNDING = """
<div class="section-label">Funding &amp; Plumbing</div>
<div class="tile tile-muted">
  <div class="tile-claim">No funding stress — this is an equity-positioning event, not a plumbing event</div>
  <div class="tile-body">Despite the equity air-pocket, money markets are orderly; this is risk being repriced, not dollars being hoarded. The thing to watch over the week: a firmer dollar + 30Y &gt; 5% tightens global financial conditions at the margin, and credit spreads are tight — any widening in IG/HY would be the signal that the equity unwind is becoming a credit event. Not there yet.</div>
</div>"""

TAPE_MISSING = """
<div class="section-label">What the Tape Is Missing</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>The whole AI complex sold on one company's guide — that's a positioning fact, not a fundamental one.</strong> AVGO guiding Q3 AI to ~$16B (vs ~$17.2B hoped) tells you about one quarter at one vendor; it does not, by itself, prove the $650–700B 2026 hyperscaler capex number is rolling over. The real test is the next round of hyperscaler capex commentary. Until that softens, treat this as an air-pocket in a crowded trade, not a confirmed downgrade cycle.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>+172k payrolls did more damage than AVGO.</strong> The chip guide started the selling; the jobs print generalised it. Removing cuts and pricing a possible hike lifts the discount rate on every long-duration asset at once — which is why a single-stock miss became an index-level, cross-asset event. Watch the 10Y: equities can't durably base until the long end stops rising.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>Gold and silver selling with stocks is a liquidity tell, not a macro reversal.</strong> In forced de-grossing, everything that can be sold for cash gets sold. Howell's framework — liquidity peaking but monetary debasement structural — argues the gold dip is for buying once the forced selling clears. The week-ahead signal: metals re-decoupling from equities = the flush is done.</div>
</div>"""

CONSENSUS = """
<div class="section-label">Consensus: Bid / Offer</div>
<div class="tile tile-muted">
  <div class="tile-head">Consensus BID (it's a dip to buy)</div>
  <div class="tile-body">A crowded-trade washout into a hot jobs print is a positioning event that exhausts. The AI capex story is intact; quality names are now cheaper; VIX backwardation historically marks tactical lows. Add quality AI/memory on the flush, buy the gold dip, and let the hedge pay. Recovery into/after the FOMC once the rate path is clarified.</div>
</div>
<div class="tile tile-gold">
  <div class="tile-head">Strongest argument against — the OFFER</div>
  <div class="tile-body">This is the first time in the cycle a marquee AI name guided "in-line, no raise" — and the macro now wants hikes, not cuts. If hyperscaler capex commentary softens this week and the FOMC pencils a hike dot, the multiple reset has further to run, the crowded long keeps unwinding, and tight credit spreads start to widen. Don't confuse the first −10% with the last.</div>
</div>"""

ONE_CHART = """
<div class="section-label">This Week's One Chart That Matters</div>
<div class="tile tile-gold">
  <div class="tile-claim">The US 10-year yield — the master variable into the FOMC</div>
  <div class="tile-body">With cuts priced out and the 30Y &gt; 5%, the 10Y (~4.53%) is the single number that governs the AI multiple this week. If it stabilises or eases, the equity flush can base and dip-buyers get paid. If it grinds toward 4.65%+ into the June 16–17 FOMC, the long-duration unwind extends and the short-yield trade (MM-2026-004) stops out. Watch the long end before you watch the chips.</div>
</div>"""

CAT_CAL = """
<div class="section-label">Week Ahead — Catalyst Calendar</div>
<table class="cal-table">
<thead><tr><th>Day</th><th>Date</th><th>Event</th><th>Consensus</th><th>View</th><th>Asymmetry</th></tr></thead>
<tbody>
<tr>
  <td>Mon</td><td>Jun 8</td>
  <td class="cal-event">Open after the rout — does the dip get bought?</td>
  <td>Stabilisation attempt; VIX easing from ~21.5</td>
  <td>The first tell of the week: a down open that gets bought = forced selling is clearing; another leg lower = systematic supply (CTA/vol-control) still in play. Watch semis (SOX) and whether gold re-decouples from equities.</td>
  <td class="asym-up">Bought dip → tactical low; failed bounce → flush continues</td>
</tr>
<tr>
  <td>Tue–Wed</td><td>Jun 9–10</td>
  <td class="cal-event">Hyperscaler / chip capex commentary &amp; conference headlines</td>
  <td>Mixed; market hypersensitive after AVGO</td>
  <td>The fundamental swing factor: any confirmation that AI capex is digesting (not collapsing) re-bids the complex; any second name guiding light validates the downgrade-cycle fear. Memory pricing data is the other watch-item.</td>
  <td class="asym-dn">Soft capex talk → AI leg-down; reassurance → sharp relief rally</td>
</tr>
<tr>
  <td>Wed/Thu</td><td>Jun 10–11</td>
  <td class="cal-event">US CPI (mid-week) — the inflation side of the rate story</td>
  <td>Watch core MoM; a hot print compounds the hawkish jobs read</td>
  <td>After +172k jobs, a firm CPI cements "no cuts, maybe a hike" and pressures duration/gold further (MM-2026-004 stop risk). A soft CPI is the bulls' best hope — it reopens the cut debate and lets equities base.</td>
  <td class="asym-dn">Hot CPI: 10Y +, gold −, AI −; soft CPI: relief across duration &amp; growth</td>
</tr>
<tr>
  <td>Tue–Wed</td><td>Jun 16–17</td>
  <td class="cal-event">FOMC + dot plot ⚡ — the decisive event</td>
  <td>Hold; but post-jobs the dots may pencil a 2026 hike</td>
  <td>The regime-definer. A hawkish dot plot reprices every equity multiple, IG spread and gold lower and validates the steepener; a neutral hold (no hike dot) is the relief that lets the AI dip-buy work. Position the book — less beta, keep the hedge, hold the steepener — before this.</td>
  <td class="asym-dn">Hike dot: SPX −3–5%, 10Y +, gold −; neutral hold: risk relief, DXY −</td>
</tr>
</tbody>
</table>"""

MIND = """
<div class="section-label">What Changes My Mind</div>
<div class="mind-item"><strong>MM-2026-006 · AVGO — CLOSED (stopped −16%):</strong> Lesson logged. Re-entry only after the stock bases and hyperscaler capex commentary holds; no rush to catch the knife into the FOMC. The discipline (hard stop) is exactly why one bad call didn't become a portfolio event.</div>
<div class="mind-item"><strong>MM-2026-008 · SPX put spread (35 → 70, +100%):</strong> The hedge paid. With VIX backwardated, consider monetising part of the gain into the spike; keep a residual hedge through the June 16–17 FOMC. Don't round-trip the whole thing if the market stabilises.</div>
<div class="mind-item"><strong>MM-2026-009 · 2s10s steepener (+38bp):</strong> Working as the long end leads (30Y &gt; 5%). Add conviction if the FOMC pencils a hike dot (term-premium story). Trim only if the long end rallies hard on a growth scare.</div>
<div class="mind-item"><strong>MM-2026-004 · Short US 10Y yield (4.53%):</strong> Wrong way; stop 4.65% ~12bp away — the most-exposed position into CPI + FOMC. If the 10Y closes above 4.60% or CPI runs hot, reduce/exit before the FOMC rather than hoping. Honest about it: this is fighting the current rate impulse.</div>
<div class="mind-item"><strong>MM-2026-005 · Long gold ($4,328):</strong> Min-hold rules apply; stop $4,250 (~1.8% below). Sold in the liquidation, not on a thesis break — Howell's debasement case is intact. Hold to the stop; the dip is for adding, not panicking, once forced selling clears.</div>
<div class="mind-item"><strong>MM-2026-002 · Long Brent ($93.09, +2.3%):</strong> Gave back most of the gain with the risk selloff. Trailing stop $90. Energy is a follower this week; hold unless $90 breaks on a close.</div>
<div class="mind-item"><strong>MM-2026-007 · Short USDJPY (160.27):</strong> Losing as the dollar firmed on jobs; stop 163.00. BoJ-divergence thesis intact but the rate impulse favours the dollar near-term — hold small, respect the stop.</div>
<div class="mind-item"><strong>MM-2026-003 · Brent/WTI spread (2.55) &amp; MM-2026-001 · Short EURAUD (1.615):</strong> Both quiet through the equity rout. Spread edge has narrowed (watch &lt;2.00); EURAUD still targeting 1.610. No changes.</div>"""

CLIENT_AMMO = """
<div class="section-label">Talking Points This Week</div>
<div class="ammo">
  <div class="ammo-q">What actually caused the selloff — is the AI trade over?</div>
  <div class="ammo-a">Two things, 24 hours apart. First, Broadcom guided Q3 AI revenue a touch light (~$16B vs ~$17.2B hoped) and didn't raise its full-year number — after a year of beat-and-raise, "in-line, no raise" was read as the first crack, and the whole AI/semis complex sold together (SOX −10%, ~$1T wiped). Then a hot jobs print (+172k vs ~80k) pushed yields up and cuts out, hammering long-duration growth. Is the AI trade over? Not on this evidence — one soft guide isn't a capex collapse. But it's a positioning flush plus a higher discount rate, and that can run a while. We want quality, hedges and dry powder, not heroics.</div>
</div>
<div class="ammo">
  <div class="ammo-q">Why did gold fall too — isn't it supposed to be a hedge?</div>
  <div class="ammo-a">On a forced-selling day, everything that can be sold for cash gets sold — gold included. That's a liquidity tell, not a regime change. The structural case (debasement, central-bank buying) is intact; the dip is for buying once the forced selling clears. The thing that confirms the flush is over is gold re-decoupling from equities.</div>
</div>
<div class="ammo">
  <div class="ammo-q">What do I watch this week?</div>
  <div class="ammo-a">Three things, in order: (1) the US 10-year yield — equities can't base until the long end stops rising; (2) hyperscaler/chip capex commentary — air-pocket vs downgrade-cycle; (3) the June 16–17 FOMC dot plot — a hike dot reprices everything lower, a neutral hold is the relief that lets the dip-buy work. CPI mid-week is the swing factor in between.</div>
</div>"""

CITATIONS = """
<div class="section-label">Citations</div>
<div class="citation">
Sources beyond Reuters / Bloomberg / FT / WSJ / AP / central banks / CME / Cboe:<br>
· CNBC — chipmakers sink as Broadcom's AI outlook disappoints (AVGO/MU/INTC/Marvell) (cnbc.com, Jun 4)<br>
· 24/7 Wall St — Broadcom's disappointing AI outlook triggers a semiconductor selloff; Micron −7% (247wallst.com, Jun 4)<br>
· TheStreet — Nasdaq −4% as semiconductor slide wipes ~$1T from markets (thestreet.com, Jun 5)<br>
· Kavout — what triggered the recent semiconductor sell-off (HSBC: chip-price slide + AI-spend slowdown) (kavout.com)<br>
· CNBC — US payrolls rose +172k in May vs ~80k expected; unemployment 4.3% (cnbc.com, Jun 5)<br>
· CNBC — hot jobs report puts Fed cuts further out of reach; hike odds rising into year-end (cnbc.com, Jun 5)<br>
· TradingKey — gold falls (below ~$4,400) as NFP overturns rate-cut hopes; DXY/yields up (tradingkey.com, Jun 5)<br>
· Live cross-asset levels (AVGO ~$386, SOX, VIX ~21.5, 10Y ~4.53%, 30Y &gt; 5%, gold ~$4,328, USDJPY ~160) via TradingView, 2026-06-07
</div>"""

STALENESS = """
<div class="section-label">Staleness Check</div>
<table class="stale-tbl">
<thead><tr><th>Datum</th><th>Source</th><th>As of</th><th>Status</th></tr></thead>
<tbody>
<tr><td>AVGO Q3 AI guide ~$16B; no FY26 raise; −14%</td><td>CNBC / 24/7 Wall St</td><td>2026-06-04</td><td class="fresh">Fresh — verified</td></tr>
<tr><td>Nasdaq −4.2%; SOX −10% (2d); ~$1T wiped</td><td>TheStreet</td><td>2026-06-05</td><td class="fresh">Fresh</td></tr>
<tr><td>May payrolls +172k vs ~80k; U-rate 4.3%</td><td>CNBC</td><td>2026-06-05 08:30 ET</td><td class="fresh">Fresh</td></tr>
<tr><td>Rate cuts priced out; hike odds rising</td><td>CNBC (market pricing)</td><td>2026-06-05</td><td class="fresh">Fresh</td></tr>
<tr><td>AVGO ~$386; SOX; 10Y 4.53%; 30Y &gt;5%; gold ~$4,328; USDJPY ~160</td><td>TradingView (live)</td><td>2026-06-07</td><td class="fresh">Fresh</td></tr>
<tr><td>VIX ~21.5 (+40%); term structure backwardated</td><td>TradingView</td><td>2026-06-07</td><td class="fresh">Fresh</td></tr>
<tr><td>HSBC: chip-price slide + AI-spend slowdown</td><td>Kavout</td><td>2026-06-04/05</td><td class="fresh">Fresh</td></tr>
<tr><td>EURAUD ~1.615; Brent-WTI spread 2.55</td><td>Carried / derived</td><td>~2026-06-07</td><td class="stale-flag">Approximate</td></tr>
<tr><td>CPI date / FOMC Jun 16–17 specifics</td><td>Calendar (consensus)</td><td>upcoming</td><td class="stale-flag">Verify exact prints/times live</td></tr>
<tr><td>Bund, Gilt, USDCNH, MOVE, credit spreads</td><td>Not sourced this refresh</td><td>unavailable</td><td class="stale-flag">Unavailable</td></tr>
</tbody>
</table>"""

# ── Dashboard ─────────────────────────────────────────────────────────────────
DASH = [
    ("S&P 500",      "~7,384",    "−2.6% on the print","down"),
    ("Nasdaq 100",   "~28,958",   "−4.8%",            "down"),
    ("SOX (semis)",  "~12,221",   "−10% (2 sessions)","down"),
    ("VIX",          "~21.5",     "+40%, backwardated","up"),
    ("FTSE 100",     "~10,368",   "+0.1% (relative haven)","flat"),
    ("Nikkei 225",   "~66,588",   "−1.3%",            "down"),
    ("DXY",          "~100.1",    "+0.6% on hot jobs","up"),
    ("EURUSD",       "~1.152",    "−0.8%",            "down"),
    ("USDJPY",       "~160.3",    "dollar firm",      "up"),
    ("US 2Y",        "4.15%",     "anchored",         "flat"),
    ("US 10Y",       "4.53%",     ">4.5% on +172k",   "up"),
    ("US 30Y",       ">5.0%",     "term premium",     "up"),
    ("2s10s",        "~+38bp",    "steepening",       "up"),
    ("WTI Crude",    "~$90.5",    "sold with risk",   "down"),
    ("Brent Crude",  "~$93.1",    "off the highs",    "down"),
    ("Gold (XAU)",   "~$4,328",   "−3.3% (liquidation)","down"),
    ("Silver",       "~$67.7",    "−8.3%",            "down"),
    ("Bitcoin",      "~$62.5k",   "+2.6% (held up)",  "up"),
    ("AVGO",         "~$386",     "−14% on the guide","down"),
    ("May Payrolls", "+172k",     "vs ~80k expected", "up"),
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
    '<div class="theme-line">Last 24h: one soft Broadcom AI guide + a hot +172k jobs print '
    'took the SOX −10% and sent the 10Y above 4.5%. Week ahead: watch the long end, '
    'hyperscaler capex commentary, CPI, and the June 16–17 FOMC dot plot.</div>'
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
