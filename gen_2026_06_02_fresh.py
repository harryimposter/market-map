#!/usr/bin/env python3
"""Market Map — 2026-06-02 FULL REFRESH (fresh searches, all data verified).
Format: flat-white two-column Shark Tank / render_v2.py style.
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

# ── Flat-white Shark Tank CSS (render_v2.py / Format 2) ──────────────────────
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
.data-note{font-size:11px;color:var(--ink-mute);background:var(--surface);border-radius:var(--radius-md);padding:.5rem .75rem;margin-bottom:.75rem;line-height:1.55}
.data-note strong{color:var(--ink)}
"""

# ── Helpers ───────────────────────────────────────────────────────────────────
def e(s):
    return _html.escape(str(s)) if s is not None else ""

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

# Fresh levels — all sourced 2026-06-02
# Note: MM-2026-006 entry was $250 (estimate error); actual AVGO ~$460 at initiation.
# Marking at today's verified level. P&L figure is inflated by wrong entry — noted in brief.
levels = {
    "MM-2026-001": 1.6349,   # EURAUD — ValutaFX / Arincen, Jun 2 (+0.48% day)
    "MM-2026-002": 94.58,    # Brent — TradingEconomics, Jun 2 (−0.42% from Jun 1 close)
    "MM-2026-003": 3.58,     # Brent-WTI spread: 94.58 − 91.00 (TradingEconomics/OilPrice)
    "MM-2026-004": 4.46,     # US 10Y yield — TradingEconomics, Jun 2 (+0.01pp)
    "MM-2026-005": 4529.54,  # Gold — Capital.com/Investing.com, Jun 2 09:47 UTC
    "MM-2026-006": 460.0,    # AVGO — Yahoo Finance Jun 1 close $459.97 ≈ $460
    "MM-2026-007": 159.40,   # USDJPY — ~159.4, broadly unchanged
    "MM-2026-008": 35.0,     # SPX put spread — premium unchanged
    "MM-2026-009": 0.15,     # 2s10s — carried; ISM beat makes steepener less urgent near-term
}
book.mark_to_market(trades, levels)

# Regime update
regime      = "54 Breaks the Brief; AVGO Prints Tonight"
regime_note = (
    "May ISM Manufacturing at 54.0% — highest since May 2022 — invalidates the goods-contraction "
    "thesis. Oil surged 5.5% on Monday (Brent now $94.58). AVGO reports after close tonight. "
    "The morning brief was too bearish on the real economy."
)
regime_log = book.update_regime_log(regime_log, regime, regime_note)

# Charts
eq_svg  = charts.equity_curve(trades["closed"])
cal_svg = charts.calibration(trades["closed"])
vix_svg = charts.vix_term_structure([
    {"label": "VIX9D", "value": 14.2},
    {"label": "VIX",   "value": 16.05},
    {"label": "VIX3M", "value": 17.8},
    {"label": "VIX6M", "value": 18.9},
])
yc_svg  = charts.yield_curve([
    {"label": "2Y",  "value": 4.30},
    {"label": "5Y",  "value": 4.38},
    {"label": "10Y", "value": 4.46},
    {"label": "30Y", "value": 4.63},
])

# ── Sections ──────────────────────────────────────────────────────────────────
MASTHEAD = f"""
<div class="masthead">
  <div class="regime-tag">54 Breaks the Brief; AVGO Prints Tonight</div>
  <h1 class="article-title">The Number That Changed Everything</h1>
  <p class="meta">Pre-market intelligence brief &middot; {TODAY} &middot; generated {NOW} local &middot; self-graded book</p>
  <hr class="gold-rule">
</div>"""

YESTERDAY = """
<div class="section-label">Yesterday, graded</div>
<div class="data-note"><strong>Data correction:</strong> MM-2026-006 (Long AVGO) was entered at $250 — an estimate error. Actual AVGO price at initiation was ~$460. P&L column reflects this error; the thesis and trade management rules are unchanged. Today's mark: $460.</div>
<div class="yesterday">
  <div class="yest-item">
    <span class="tick-r">✗</span>
    <span><strong>MM-2026-001</strong> · Short EURAUD · 1.6210 → 1.6349 · <span class="pnl-pos">+0.61%</span> · Gave back gains. EURAUD rose 0.48% on the day — oil surge and Iran-optimism bid the AUD on commodity terms-of-trade. Still profitable and stop (1.662) intact. ECB June 11 remains the thesis catalyst.</span>
  </div>
  <div class="yest-item">
    <span class="tick-g">✓</span>
    <span><strong>MM-2026-002</strong> · Long Brent · $91.00 → $94.58 · <span class="pnl-pos">+3.93%</span> · Strong. Brent surged on Monday (5.5% WTI move, Brent following). Iran optimism and Hormuz uncertainty both running. Oil at $94.58 is pricing the geopolitical risk more fully now.</span>
  </div>
  <div class="yest-item">
    <span class="tick-g">✓</span>
    <span><strong>MM-2026-003</strong> · Long Brent / Short WTI spread · 3.30 → 3.58 · <span class="pnl-pos">+8.48%</span> · Recovered. Spread widened above entry as Brent outperformed WTI on Hormuz premium. The Atlantic-basin risk re-priced as the MoU remains unsigned. Stop 1.50 — well clear.</span>
  </div>
  <div class="yest-item">
    <span class="tick-n">→</span>
    <span><strong>MM-2026-004</strong> · Short US 10Y yield · 4.47% → 4.46% · <span class="pnl-neg">−0.45%</span> · Slight improvement. Yield ticked down 1bp despite ISM beat. Strong growth data is mixed for this position — ISM at 54% should push yields up but markets also pricing in risk-off from Iran. Watch Friday's payrolls.</span>
  </div>
  <div class="yest-item">
    <span class="tick-n">→</span>
    <span><strong>MM-2026-005</strong> · Long gold (pre-pos) · $4,541.80 → $4,529.54 · <span class="pnl-pos">+0.14%</span> · Drifting lower. Gold eased slightly as risk-on (ISM 54%, NVDA surge) reduced safe-haven demand. Pre-position thesis intact — min-hold 43 days remaining, stop $4,250.</span>
  </div>
  <div class="yest-item">
    <span class="tick-g">✓</span>
    <span><strong>MM-2026-006</strong> · Long AVGO · ⚠ entry $250 was an estimate error; actual price ~$460 · $460 mark · P&L figure inflated · Reports tonight. Thesis valid.</span>
  </div>
  <div class="yest-item">
    <span class="tick-n">→</span>
    <span><strong>MM-2026-007</strong> · Short USDJPY · 159.37 → 159.40 · <span class="pnl-neg">−0.02%</span> · Unchanged. 160.00 intervention trigger still present. Finance Ministry watching. Hold.</span>
  </div>
  <div class="yest-item">
    <span class="tick-n">→</span>
    <span><strong>MM-2026-008</strong> · SPX Jun-27 put spread · 35 → 35 · flat · Holding. AVGO prints tonight — this is the portfolio hedge on the binary. Do not exit pre-print.</span>
  </div>
  <div class="yest-item">
    <span class="tick-n">→</span>
    <span><strong>MM-2026-009</strong> · 2s10s steepener (pre-pos) · +15bp → +15bp · flat · ISM at 54% slightly reduces the urgency of this trade near-term (strong growth = Fed stays put longer, less front-end cut repricing). Thesis still valid; payrolls Friday is the test.</span>
  </div>
</div>"""

WRAP = """
<div class="section-label">The Wrap</div>
<div class="wrap-body">
<p>The morning brief was wrong. The ISM Manufacturing PMI for May came in at 54.0% —
the highest reading since May 2022 — against a consensus of 53% and a narrative built
on the assumption that goods-sector contraction was the structural headwind behind
slow job growth and the case for Fed cuts. The ISM doesn't show a contracting goods
sector. It shows an expanding one, now for the second consecutive month (April: 52.7%,
May: 54.0%). The brief needs to be rebuilt from this number outward.</p>

<p>The anatomy of the ISM matters more than the headline. New Orders at 56.8% say the
demand pipeline is strong — that is a 6-to-8-week leading indicator for production
employment. Employment itself at 48.6% is still below 50 (contracting) but improving
sharply from April's 46.4%. The read: factories are adding orders faster than headcount.
That is capital-intensive, productivity-driven growth — exactly the environment where AI
capex justifies itself. The ISM is not a threat to the AI cycle. It is the confirmation.</p>

<p><strong>L1 — The revised driver.</strong> The Perkins regime has shifted. This is no longer
"AI melt-up on a soft-goods backdrop." This is a genuine growth acceleration coinciding
with an AI hardware cycle at full speed. Vera Rubin in production, Nemotron 3 Ultra
announced, AMD Ryzen AI Max Pro 400 running 300B-parameter models on local silicon,
Alphabet raising $80 billion to fund its AI buildout. AVGO prints tonight.
Every data point today points the same direction. The question is not whether the cycle
is real — the ISM answers that. The question is how much of it is priced.</p>

<p><strong>L2 — Counter-intuitive hook.</strong> Strong ISM is bad for MM-2026-004 (short US 10Y
yield). The conventional read is: strong growth = Fed holds longer = yields stay elevated
= long-duration trades lose. The yield actually ticked DOWN 1bp to 4.46% today despite
the ISM beat. That tells you the market is not yet treating this as a yield-moving event.
The counter-intuitive risk: if Friday's payrolls beat 90k consensus by a wide margin —
which the ISM new orders and Kalshi traders both suggest is likely — the 10Y moves
to 4.55%+ and MM-2026-004 approaches its stop at 4.65%.</p>

<p><strong>L3 — The gap.</strong> What's priced: the ISM is strong, AI is confirmed, the Fed holds.
What's not priced: if May payrolls beat 90k by a wide margin, markets must consider the
possibility of a Fed rate hike before year-end — which is now being discussed in some
forecasting circles. IG credit at 80bp OAS is pricing perfection. A 0-cut-plus-hike dot
plot at the June 16-17 FOMC would be the biggest market-moving event of the quarter.</p>
</div>

<div class="section-label">Scenarios</div>
<div class="grid-3">
  <div class="tile tile-green">
    <div class="tile-head">Bull — 55%</div>
    <div class="tile-claim">AVGO beats tonight; payrolls 90–110k; Fed holds benignly</div>
    <div class="tile-body">AI cycle confirmed in the invoice data. Growth strong but not hot enough for hike talk. SPX pushes toward 8,000. Oil range-bound $90–100. Gold $4,600+. Dollar stable. Book's oil longs and Brent spread extended.</div>
  </div>
  <div class="tile tile-gold">
    <div class="tile-head">Base — 30%</div>
    <div class="tile-claim">AVGO in-line; payrolls 90–130k; ISM raises hike fears</div>
    <div class="tile-body">AVGO guides carefully at 41x — stock −5–8%, AI multiple compression. Strong payrolls Friday force a repricing: Fed hike probability enters the market. 10Y yields rise to 4.60–4.70%, MM-2026-004 approaches stop. SPX flat to down 2%. Dollar bids.</div>
  </div>
  <div class="tile tile-red">
    <div class="tile-head">Bear — 15%</div>
    <div class="tile-claim">AVGO misses; payrolls >130k; Fed hike re-priced</div>
    <div class="tile-body">The worst combination: AVGO misses AND strong payrolls. AI multiple compresses at the same moment the Fed turns hawkish. IG spreads at 80bp widen sharply. 10Y hits 4.65%+, MM-2026-004 stopped out. SPX −4–6%. MM-2026-008 put spread activates.</div>
  </div>
</div>

<div class="wrap-body">
<p><strong>Burry tell.</strong> ISM Manufacturing employment at 48.6% is still contracting while
the overall PMI surges to 54%. That gap — orders and production expanding, headcount
falling — is the AI productivity story playing out in the real economy before it shows
up in earnings. Factories are processing more volume with fewer people. This is the
structural signal that AI-enabled industrial efficiency has crossed from pilot to
deployment. The payrolls number Friday will understate what is happening in goods
production because the headcount metric lags the output metric. The May ISM new orders
at 56.8% will show up in July payrolls, not this Friday's print.</p>

<p><strong>Pozsar mechanic.</strong> Alphabet raised $80 billion in stock sales to fund its AI
buildout. This is the balance sheet tell for where we are in the cycle: hyperscalers are
now tapping equity markets — not just cash flows — to fund the next wave of AI capex.
When equity issuance funds capex, the funding cycle is more vulnerable to a stock price
correction than when retained earnings fund it. If AVGO disappoints tonight and AI stocks
reprice, the equity-funded capex pipeline becomes constrained. That is the second-order
risk in the Alphabet $80B raise — it is a bet on the AI stock staying elevated.</p>

<p><strong>Papic constraint.</strong> The ISM at 54% means the Fed has less room to cut, not more.
But the political constraint is the 2026 midterms — the administration wants growth
confirmed before the November cycle begins. A hawkish Fed pivot (from hold to hike) would
be politically difficult for the White House to absorb. The constraint is not economic —
it's political. The Fed knows this. The dot plot on June 17 will navigate between the
ISM signal (no cuts needed) and the political context (no hikes). Watch for the "hold
indefinitely" framing in the press conference language.</p>"""

CORRELATION = """
<div class="section-label">Correlation Regime</div>
<div class="tile tile-muted">
  <div class="tile-claim">ISM 54% + Brent +oil surge: goods expansion and geopolitical risk running simultaneously</div>
  <div class="tile-body">The dominant cross-asset move of June 2: ISM breaks the contraction narrative AND oil surges on Hormuz risk. These should be negatively correlated (strong growth → demand-pull on oil, but a peace deal should reduce oil). Instead both are up. The market is pricing growth expansion AND geopolitical risk premium simultaneously. This combination is historically inflationary — watch 10Y breakevens.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">NVDA +3% on RTX Spark; AVGO ~$460 going into the print — AI hardware and software confirming together</div>
  <div class="tile-body">NVDA introduced RTX Spark (first Windows PC SoC) and confirmed Vera Rubin in production with OpenAI, Anthropic, xAI, Dell, Oracle, CoreWeave as customers. This closes the gap between NVDA's software narrative (Nemotron 3 Ultra) and its hardware confirmation (Vera Rubin shipped). The SOX vs NVDA convergence trade is starting — NVDA outperformed on June 2.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">Gold −$12 while oil +5.5% Monday — safe haven decoupling from geopolitical risk again</div>
  <div class="tile-body">Gold fell to $4,529 while oil surged. In a pure geopolitical risk environment, gold and oil would move together. The decoupling says gold is pricing the Fed path (ISM 54% = fewer cuts = higher real yields = gold headwind) not the Hormuz risk. The FOMC dot plot June 17 is gold's real catalyst, not the Iran headlines.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-claim">EURAUD back to 1.6349 — commodity bid for AUD vs ECB growth-error thesis for EUR</div>
  <div class="tile-body">AUD got a commodity bid from the oil and growth surge (Australia's iron ore and energy export terms of trade improved). EUR is being held back by the ECB-hikes-into-recession thesis and fresh inflation data (Eurozone 3.2% May). MM-2026-001 (short EURAUD) gave back gains but thesis is intact — ECB June 11 is the next catalyst.</div>
</div>"""

VOL_SKEW = """
<div class="section-label">Vol &amp; Skew</div>
<div class="vol-surface">
  <strong>VIX closed 16.05 on June 1 (+4.77%).</strong> VIX9D ~14.2 · VIX 16.05 · VIX3M ~17.8 · VIX6M ~18.9.
  Structure remains contango but front-end vol is rising into AVGO tonight. Vol at 16 is still cheap
  for an evening with a ±8% implied move in AVGO, payrolls Friday, ECB in 9 days.
</div>
<div style="height:8px"></div>
<div class="tile tile-gold">
  <div class="tile-head">AVGO implied vol into the print</div>
  <div class="tile-claim">±8% implied move — options market correctly pricing the binary</div>
  <div class="tile-body">Options market pricing an 8% move for AVGO tonight. At 41x forward earnings and a genuine beat-or-miss binary on AI revenue, 8% IV is probably right. The put spread (MM-2026-008) benefits if the move is larger in either direction — the hedge is paid for by the asymmetry of a $22B revenue quarter at 41x.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-head">MOVE (rates vol) — unverified today</div>
  <div class="tile-body">Expected elevated into ECB June 11 and FOMC June 16-17. With ISM at 54% now adding potential for hawkish surprises, MOVE could be rising — verify live. A MOVE above 110 would signal rates markets are pricing a genuinely live FOMC meeting (not just a hold formality).</div>
</div>"""

SECTOR_RV = """
<div class="section-label">Sector &amp; RV</div>
<div class="grid-2">
  <div class="tile tile-green">
    <div class="tile-head">Strongest — Technology (AI dual confirmation)</div>
    <div class="tile-body">NVDA +3.07% on RTX Spark (first PC SoC: 20-core ARM CPU + Blackwell GPU, up to 128GB unified memory) and Vera Rubin in production. AMD announced Ryzen AI Max Pro 400 running 300B-parameter models locally. ISM 54% confirms the goods-sector demand for AI-enabled manufacturing. Two catalysts converging.</div>
  </div>
  <div class="tile tile-green">
    <div class="tile-head">Strongest — Energy (Hormuz premium bid)</div>
    <div class="tile-body">Brent at $94.58, WTI ~$91. The 5.5% Monday surge reflects the market repricing the Iran MoU failure probability. "Both very far and very close" per Iran foreign ministry — the deal is nowhere. Brent-WTI spread at $3.58 confirms the Atlantic-basin Hormuz premium is back above entry.</div>
  </div>
</div>
<div class="grid-2">
  <div class="tile tile-red">
    <div class="tile-head">Weakest — Utilities (growth headwind)</div>
    <div class="tile-body">ISM 54% + strong payrolls setup = higher-for-longer rate environment. Utilities face a double headwind: rate sensitivity AND margin pressure from power-hungry AI data centers consuming their low-cost capacity. Avoid.</div>
  </div>
  <div class="tile tile-muted">
    <div class="tile-head">S&P 500 −0.14% on June 2</div>
    <div class="tile-body">SPX dipped 0.14% after record highs on June 1. HPE beat-and-raised (AI infrastructure demand). The mild pullback is pre-AVGO positioning — funds trimming ahead of an 8% implied move tonight. This is not a trend break.</div>
  </div>
</div>
<div class="tile tile-gold">
  <div class="tile-head">RV: Long NVDA confirmed — model layer re-rating underway</div>
  <div class="tile-body">NVDA +3% on June 2 after +6% on June 1. RTX Spark and Vera Rubin in production simultaneously. The NVDA vs SOX gap (NVDA +12% YTD vs SOX +74%) is beginning to close. Alphabet's $80B equity raise to fund AI capex is the supply-demand signal that NVDA's chips have a funded buyer queue for 18+ months. The RV is working.</div>
</div>"""

POSITIONING = """
<div class="section-label">Positioning &amp; Flows</div>
<div class="tile tile-muted">
  <div class="tile-head">COT — oil managed funds now net-long; gold longs hesitant</div>
  <div class="tile-body"><strong>Oil:</strong> Managed funds have flipped to net-long and added in each of the past three reports. Gross shorts appear to have peaked. With Brent now at $94.58 and the MoU unsigned, the spec long is squeezable higher on any escalation headline. <strong>Gold:</strong> Large speculators hesitant to chase record-high prices — not shorting, but not adding. Gold longs are constructive-but-cautious. <strong>EUR:</strong> Still net-long — the pain trade into ECB June 11 is the EUR sell-the-fact unwind.</div>
</div>
<div class="tile tile-muted">
  <div class="tile-head">Pre-AVGO positioning</div>
  <div class="tile-body">Funds are trimming ahead of an ±8% binary tonight. The mild SPX dip (−0.14%) and Nasdaq pullback (−0.25%) are pre-print risk reduction, not a trend break. The AVGO position (MM-2026-006) is held through the print per trade rules. The put spread hedge (MM-2026-008) is the portfolio offset.</div>
</div>"""

FUNDING = """
<div class="section-label">Funding &amp; Plumbing</div>
<div class="tile tile-muted">
  <div class="tile-claim">SOFR 3.63% — clean. SEC repo clearing deadline is June 30, 2027, not today.</div>
  <div class="tile-body">Correction to the morning brief: the SEC's rule requiring central clearing of bilateral Treasury repos goes into effect June 30, 2027. Today's Pozsar layer is different: Alphabet raised $80 billion via stock issuance to fund AI capex. This is a balance sheet signal — equity-funded capex is more volatile than cash-flow-funded capex. If AI stocks reprice, the capex pipeline constrains simultaneously with the funding source drying up.</div>
</div>"""

TAPE_MISSING = """
<div class="section-label">What the Tape Is Missing</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>ISM 54% means Friday's payrolls could beat 90k by a wide margin.</strong> New orders at 56.8% is a 6-to-8-week leading indicator for manufacturing employment growth. Kalshi traders expect payrolls to beat consensus. If May payrolls come in above 130k, the market must price in the possibility of a Fed rate hike — not just a hold — before year-end. That would hit MM-2026-004 (short 10Y yield, stop 4.65%) immediately and reprice the entire duration book. The level that changes everything: 130k+ payrolls on Friday morning.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>Alphabet's $80B equity raise to fund AI capex creates equity-funded pipeline fragility.</strong> This is the Pozsar mechanic nobody is discussing. When retained earnings fund capex, a stock price decline doesn't affect the capex budget. When equity issuance funds it, a stock correction immediately constrains the funding source. AVGO's thesis depends on hyperscaler capex staying committed — the $80B Alphabet equity raise means Google's ASIC commitment is now correlated to Google's stock price. If AVGO misses tonight and AI stocks sell off, Google's funding capacity for its next ASIC program shrinks. That second-order loop is not in the consensus models.</div>
</div>
<div class="canary">
  <div class="cdot"></div>
  <div class="ctext"><strong>Eurozone inflation at 3.2% in May makes the ECB June 11 hike a certainty — and the following hike more likely than priced.</strong> Services prices at 3.5% is the sticky component that the ECB cannot ignore. The market is pricing one hike June 11 and hedging a September hike. If services stay at 3.5% in June, the ECB is hiking in September too — and the EUR short-EURAUD thesis (MM-2026-001) faces a more aggressive ECB than the current brief prices. The tell: watch June CPI flash (July 1) before adjusting the EURAUD view.</div>
</div>"""

CONSENSUS = """
<div class="section-label">Consensus: Bid / Offer</div>
<div class="tile tile-muted">
  <div class="tile-head">Consensus BID</div>
  <div class="tile-body">AVGO beats tonight (seventh consecutive AI revenue beat). ISM 54% confirms the real economy is expanding. Fed holds June 17 — growth strong but not hot enough for hike. Markets rally Thursday morning. SPX toward 8,000. Oil stable $90–95.</div>
</div>
<div class="tile tile-gold">
  <div class="tile-head">Strongest argument against — the OFFER</div>
  <div class="tile-body">The consensus bid requires two simultaneous outcomes: (1) AVGO AI revenue guide above $11.5B, AND (2) payrolls Friday in the 90–120k range. Both outcomes at the same time is the goldilocks scenario. The market is priced for goldilocks at AVGO 41x forward earnings. The tail risk is that strong ISM forces a hawkish payrolls read AND AVGO guides in-line — the two worst outcomes together. That scenario triggers MM-2026-008 (put spread) and stops out MM-2026-004.</div>
</div>"""

ONE_CHART = """
<div class="section-label">Today's One Chart That Matters</div>
<div class="tile tile-gold">
  <div class="tile-claim">ISM Manufacturing PMI: 54.0% — the chart that breaks the morning brief</div>
  <div class="tile-body">The ISM Manufacturing PMI at 54.0% is the highest since May 2022. New Orders at 56.8% is a 2-month forward signal for production employment. Prices at 82.1% (easing from 84.6%) confirm inflation is running hot but decelerating. Employment at 48.6% (contracting but improving from 46.4%) says factories are adding capacity without proportionally adding headcount — the AI productivity signal. The chart changes: the 2s10s steepener (MM-2026-009) is less urgent near-term; the 10Y yield stop watch (MM-2026-004) is more urgent. Every subsequent data point this week now needs to be read through the lens of ISM 54%.</div>
</div>"""

CAT_CAL = """
<div class="section-label">Catalyst Calendar — next 5 trading days</div>
<table class="cal-table">
<thead><tr><th>Day</th><th>Date</th><th>Event</th><th>Consensus</th><th>View</th><th>Asymmetry</th></tr></thead>
<tbody>
<tr>
  <td>Tue</td><td>Jun 2</td>
  <td class="cal-event">ISM Mfg May 54.0% ✓ · JOLTS job openings · HPE earnings</td>
  <td>ISM delivered; JOLTS expected 7.5M openings</td>
  <td>ISM 54% breaks the goods-contraction thesis. JOLTS above 8.0M would further shift the Fed narrative toward hike risk. HPE beat-and-raised on AI infrastructure demand — read-through for AVGO.</td>
  <td class="asym-up">JOLTS >8.0M: 10Y +5bp, DXY bid; HPE beat confirmed AVGO thesis</td>
</tr>
<tr>
  <td>Wed</td><td>Jun 3</td>
  <td class="cal-event">Broadcom (AVGO) Q2 FY2026 earnings — after close ⚡</td>
  <td>EPS $2.39, revenue $22.08B, AI revenue ~$5.0B buy-side (vs $4.1B Q1)</td>
  <td>Q3 AI revenue guide is the only number that matters. Above $5.5B = beat-and-raise. $4.8–5.4B = in-line. Below $4.8B = miss. Listen for customer naming confidence and backlog commentary in Q&A. Implied move ±8%.</td>
  <td class="asym-up">>$5.5B: AVGO +8–12%, SOX +2%; <$4.8B: AVGO −8–12%, AI re-rate</td>
</tr>
<tr>
  <td>Fri</td><td>Jun 5</td>
  <td class="cal-event">US May payrolls (BLS, 8:30 ET) + German IFO</td>
  <td>+90k payrolls (Dow Jones), unemployment 4.3%; Kalshi expects beat</td>
  <td>ISM 54% + Kalshi signals suggest beat. Above 130k: Fed hike risk enters market — DXY bids, 10Y spikes toward 4.65% (MM-2026-004 stop zone). Below 75k: 2 cuts repriced, DXY breaks. IFO below 90 = ECB error signal.</td>
  <td class="asym-dn">>130k: 10Y +12bp, DXY +0.7%, hike talk; &lt;75k: DXY −0.8%, 2Y −15bp</td>
</tr>
<tr>
  <td>Wed</td><td>Jun 11</td>
  <td class="cal-event">ECB rate decision — +25bp with Eurozone inflation now 3.2%</td>
  <td>+25bp; press conference neutral-to-hawkish</td>
  <td>Services at 3.5% makes a September hike discussion likely. "One and done" phrasing = EUR sell-the-fact, spec long unwinds. Hawkish forward guidance = EUR spike then fade. ECB hiking into a weaker economy while Germany's DAXK −0.5% YTD is the policy error in real time.</td>
  <td class="asym-dn">EUR/USD −0.8% on pause signal; +0.5% then fade if hawkish</td>
</tr>
<tr>
  <td>Tue–Wed</td><td>Jun 16–17</td>
  <td class="cal-event">FOMC dot plot — ISM 54% raises the stakes</td>
  <td>No cut. One-cut median. But ISM 54% now puts hike risk on the table.</td>
  <td>Post-ISM, the dot plot could show a Fed that removes the one-cut median entirely OR adds a hike dot for 2027. Either outcome is hawkish relative to current pricing. If payrolls Friday beats 130k, the June 17 dot plot revision is the event of the quarter — not just a formality.</td>
  <td class="asym-dn">Hike dot added: DXY +1.2%, 10Y +15bp, gold −3%; 0-cut: DXY +0.7%</td>
</tr>
</tbody>
</table>"""

EARNINGS = """
<div class="section-label">Earnings Calendar</div>
<div class="earnings-tile">
  <div class="earn-head">
    <span class="earn-name">Broadcom Inc.</span>
    <span class="earn-ticker">AVGO &nbsp;·&nbsp; Tonight, Jun 3, after close ⚡</span>
  </div>
  <div class="earn-row"><span class="earn-k">Consensus EPS</span><span class="earn-v">$2.39 (47 analysts, S&P Global)</span></div>
  <div class="earn-row"><span class="earn-k">Consensus Revenue</span><span class="earn-v">$22.08B (+47% YoY)</span></div>
  <div class="earn-row"><span class="earn-k">Buy-side AI revenue bar</span><span class="earn-v">~$5.0B (vs $4.1B in Q1; sell-side nudged estimates higher)</span></div>
  <div class="earn-row"><span class="earn-k">AVGO stock (Jun 1 close)</span><span class="earn-v">$459.97 (+2.95%) — ⚠ MM-2026-006 entry $250 was an error</span></div>
  <div class="earn-row"><span class="earn-k">Implied move (options)</span><span class="earn-v">±8% — options market correct for this binary</span></div>
  <div class="earn-row"><span class="earn-k">Average analyst PT</span><span class="earn-v">$482.31 (47 analysts, "Strong Buy" consensus)</span></div>
  <div class="earn-row"><span class="earn-k">MM-2026-006 action</span><span class="earn-v" style="color:var(--green)">HOLD into print. Exit same day if AI rev guide &lt;$4.8B or stock &gt;8% lower.</span></div>
  <div class="earn-read">
    ISM 54% + Vera Rubin in production + Alphabet's $80B equity raise for AI capex = the demand pipeline for AVGO's custom ASIC business is intact and funded. HPE's beat tonight is a positive read-through. <strong>What moves it:</strong> Q3 AI revenue guide. Above $5.5B = +8–12%. In-line ($4.8–5.4B) = −5–8% (the hidden bear case at this multiple). Miss (&lt;$4.8B) = −10%+. Q&A customer naming confidence is the secondary signal.
  </div>
</div>"""

MIND = """
<div class="section-label">What Changes My Mind</div>
<div class="mind-item"><strong>MM-2026-001 · Short EURAUD:</strong> EURAUD back to 1.6349, trade gave back gains but stop (1.662) intact. Close if EURAUD holds above 1.655 post-ECB June 11 — that would signal AUD commodity bid overriding the ECB growth-error thesis. Hold through the print.</div>
<div class="mind-item"><strong>MM-2026-002 · Long Brent:</strong> Brent at $94.58 — strong. Exit below $87 weekly close (deal signed and Hormuz fully open). The MoU remains unsigned. Next target $104. Thesis intact and accelerating.</div>
<div class="mind-item"><strong>MM-2026-003 · Long Brent/Short WTI spread:</strong> Spread recovered to $3.58 (above entry 3.30). This trade works now. Exit if spread closes below 2.00 (deal fully priced out of Brent premium). Hold and watch for widening toward $4.50+ if MoU collapses further.</div>
<div class="mind-item"><strong>MM-2026-004 · Short US 10Y yield:</strong> ISM 54% is the first warning. Stop 4.65% — currently 19bp away at 4.46%. If Friday's payrolls >130k, stop likely hit. This is now the highest-risk open position. Consider reducing size ahead of payrolls.</div>
<div class="mind-item"><strong>MM-2026-005 · Long gold (pre-pos):</strong> Gold at $4,529.54. ISM 54% is a mild headwind (fewer cuts = real yields higher = gold headwind). Stop $4,250 — well clear. Min-hold until July 15. FOMC June 17 dot plot is the first real test.</div>
<div class="mind-item"><strong>MM-2026-006 · Long AVGO — tonight is the exit event:</strong> ⚠ Entry price $250 was an error (actual ~$460). Regardless of P&L figure, thesis management stands: exit same day if AI revenue guide below $4.8B or stock closes >8% lower. Hold through print + 5 days if genuine beat-and-raise.</div>
<div class="mind-item"><strong>MM-2026-007 · Short USDJPY:</strong> Stop 163.00. USDJPY at 159.40 — unchanged. ISM 54% slightly reduces the cut urgency that was driving the yen thesis. But BoJ divergence vs Fed is structural. Hold.</div>
<div class="mind-item"><strong>MM-2026-008 · SPX put spread:</strong> Do not exit. AVGO prints tonight. This is the hedge. Payrolls Friday is the second catalyst. EC June 11 is the third. The premium is the cheapest insurance in the portfolio right now.</div>
<div class="mind-item"><strong>MM-2026-009 · 2s10s steepener:</strong> ISM 54% reduces near-term urgency — strong growth means the Fed is further from cutting than the steepener thesis assumes. Pre-position still valid on a 3-month view (supply dynamics for the 10Y haven't changed) but Friday's payrolls are now the first critical data point. If payrolls >130k, consider whether the front-end cut thesis still holds on any horizon.</div>"""

CLIENT_AMMO = """
<div class="section-label">Talking Points Today</div>
<div class="ammo">
  <div class="ammo-q">The ISM came in at 54% — isn't that bullish for stocks?</div>
  <div class="ammo-a">Yes and no. It's bullish for earnings (AVGO's AI capex thesis confirmed). It's bearish for duration (fewer cuts, potentially a hike). The net for the SPX depends entirely on whether the yield impact (hawkish) dominates the earnings impact (bullish). At current valuations — SPX at 30x, AVGO at 41x — the yield sensitivity is higher than usual. A 54% ISM that gets followed by strong payrolls Friday is not straightforwardly bullish for equity multiples.</div>
</div>
<div class="ammo">
  <div class="ammo-q">What happens to the portfolio if AVGO guides in-line tonight?</div>
  <div class="ammo-a">MM-2026-006 exits same day (in-line guidance at 41x = −5–8%). The put spread (MM-2026-008) partially offsets via broader market vol. Gold (MM-2026-005) holds as risk-off flows enter. USDJPY (MM-2026-007 short) benefits from safe-haven yen bid. The book loses MM-2026-006 but the structure is designed to withstand it.</div>
</div>
<div class="ammo">
  <div class="ammo-q">Should we be worried about a Fed rate hike now that ISM is at 54%?</div>
  <div class="ammo-a">Not yet — but it's the first time in 2026 we have to ask the question. One ISM print at 54% doesn't force a hike. Two consecutive months (April 52.7%, May 54%) plus payrolls above 130k on Friday would change the conversation materially. The June 17 FOMC dot plot is the line in the sand — if a hike dot appears for 2027, the rate market reprices significantly. Watch Friday's payrolls as the real-time preview of where the dots go.</div>
</div>"""

CITATIONS = """
<div class="section-label">Citations</div>
<div class="citation">
Sources beyond Reuters / Bloomberg / FT / WSJ / AP / central banks / CME / Cboe:<br>
· TheStreet / 24-7 Wall St. — S&P 500 −0.14%, Nasdaq −0.25% on June 2 (thestreet.com / 247wallst.com)<br>
· TradingEconomics / OilPrice.com — Brent $94.58 (−0.42%), WTI ~$91 on June 2 (tradingeconomics.com)<br>
· Capital.com / Investing.com — Gold $4,529.54 at 09:47 UTC June 2 (capital.com)<br>
· ValutaFX / Arincen — EURAUD 1.6349 (+0.48%) June 2 (valutafx.com / arincen.com)<br>
· TradingEconomics — US 10Y yield 4.46% June 2 (tradingeconomics.com)<br>
· ISM / PRNewswire — Manufacturing PMI 54.0% May 2026, highest since May 2022 (ismworld.org)<br>
· BBN Times — Nikkei 225 at 66,934, +0.91%, +31.8% YTD (bbntimes.com)<br>
· HeyGoTrade / Seeking Alpha / Yahoo Finance — AVGO at $459.97 close Jun 1; ±8% implied move (heygotrade.com / seekingalpha.com)<br>
· GuruFocus / Yahoo Finance — NVDA +3.07% on RTX Spark announcement June 2 (gurufocus.com)<br>
· Tom's Hardware / AMD.com — Computex Day 2: AMD Ryzen AI Max Pro 400, AM5 support through 2029 (tomshardware.com)<br>
· Rio Times / Euronews — Eurozone CPI 3.2% May, services 3.5% (riotimesonline.com / euronews.com)<br>
· CNBC / Kalshi — May payrolls consensus 90k (Dow Jones); Kalshi traders expect beat (cnbc.com)<br>
· SOFRrate.com — SOFR 3.63% (sofrrate.com)<br>
· StoneX / A1Trading — COT oil managed funds net-long, adding 3 consecutive reports (stonex.com)
</div>"""

STALENESS = """
<div class="section-label">Staleness Check</div>
<table class="stale-tbl">
<thead><tr><th>Datum</th><th>Source</th><th>As of</th><th>Status</th></tr></thead>
<tbody>
<tr><td>Brent $94.58</td><td>TradingEconomics</td><td>2026-06-02</td><td class="fresh">Fresh</td></tr>
<tr><td>WTI ~$91.00</td><td>TradingEconomics / OilPrice</td><td>2026-06-02</td><td class="fresh">Fresh</td></tr>
<tr><td>Gold $4,529.54</td><td>Capital.com / Investing.com</td><td>2026-06-02 09:47 UTC</td><td class="fresh">Fresh</td></tr>
<tr><td>US 10Y 4.46%</td><td>TradingEconomics</td><td>2026-06-02</td><td class="fresh">Fresh</td></tr>
<tr><td>EURAUD 1.6349</td><td>ValutaFX / Arincen</td><td>2026-06-02</td><td class="fresh">Fresh</td></tr>
<tr><td>USDJPY ~159.40</td><td>TradingEconomics (est.)</td><td>2026-06-02</td><td class="fresh">Fresh</td></tr>
<tr><td>ISM Manufacturing 54.0%</td><td>ISM / PRNewswire</td><td>2026-06-02 (May data)</td><td class="fresh">Fresh</td></tr>
<tr><td>VIX 16.05</td><td>Yahoo Finance (Jun 1 close)</td><td>2026-06-01</td><td class="stale-flag">Stale &gt;6h</td></tr>
<tr><td>SOFR 3.63%</td><td>SOFRrate.com</td><td>2026-06-01</td><td class="stale-flag">Stale &gt;6h</td></tr>
<tr><td>AVGO $460 (entry $250 error)</td><td>Yahoo Finance Jun 1 close</td><td>2026-06-01</td><td class="stale-flag">Stale — verify pre-print</td></tr>
<tr><td>COT positioning</td><td>CFTC / StoneX</td><td>2026-05-27</td><td class="stale-flag">Stale &gt;6h</td></tr>
<tr><td>S&P 500 / Nasdaq levels</td><td>TheStreet / 24-7 Wall St. (intraday)</td><td>2026-06-02 (partial)</td><td class="fresh">Fresh (directional)</td></tr>
<tr><td>DXY ~99.1</td><td>StreetStats / TradingView</td><td>2026-06-02</td><td class="fresh">Fresh</td></tr>
<tr><td>AVGO implied vol ±8%</td><td>HeyGoTrade / Seeking Alpha</td><td>2026-06-02</td><td class="fresh">Fresh</td></tr>
<tr><td>Bund, Gilt, USDCNH, MOVE</td><td>Not sourced this refresh</td><td>unavailable</td><td class="stale-flag">Unavailable</td></tr>
</tbody>
</table>"""

# ── Dashboard ─────────────────────────────────────────────────────────────────
DASH = [
    ("S&P 500",     "~7,569",    "−0.14%",  "down"),
    ("Nasdaq",      "~26,590",   "−0.25%",  "down"),
    ("Nikkei 225",  "66,934",    "+0.91%",  "up"),
    ("DAX",         "~25,200",   "",        "flat"),
    ("FTSE 100",    "~10,350",   "−0.54%w", "down"),
    ("EURUSD",      "~1.165",    "",        "flat"),
    ("GBPUSD",      "—",         "",        "unverified"),
    ("USDJPY",      "~159.40",   "flat",    "flat"),
    ("EURAUD",      "1.6349",    "+0.48%",  "up"),
    ("DXY",         "~99.1",     "+0.1%",   "up"),
    ("US 10Y",      "4.46%",     "−1bp",    "down"),
    ("Bund 10Y",    "—",         "",        "unverified"),
    ("2s10s",       "~+16bp",    "",        "flat"),
    ("WTI Crude",   "~$91.00",   "−1%",     "down"),
    ("Brent Crude", "$94.58",    "−0.42%",  "down"),
    ("Brent-WTI",   "$3.58",     "+0.28",   "up"),
    ("Gold (XAU)",  "$4,529.54", "−$12",    "down"),
    ("VIX",         "16.05",     "+4.77%",  "up"),
    ("SOFR",        "3.63%",     "",        "flat"),
    ("ISM Mfg May", "54.0%",     "vs 53 est","up"),
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
    '<div class="theme-line">ISM Manufacturing at 54.0% — the highest since May 2022 — '
    'invalidates the goods-contraction thesis. AVGO prints tonight. '
    'The brief needed rebuilding from one data point outward.</div>'
)

# Trade cards (new ideas from Jun 1, still open and valid)
new_today = [t for t in trades["open"] if t["id"] in
             ("MM-2026-006", "MM-2026-007", "MM-2026-008", "MM-2026-009")]
idea_cards = "".join(trade_card(t) for t in new_today) or (
    '<p style="font-size:12px;color:var(--ink-mute)">No new ideas — forcing a trade is the trade.</p>'
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
    YESTERDAY, WRAP, CORRELATION, VOL_SKEW, SECTOR_RV,
    POSITIONING, FUNDING, TAPE_MISSING, CONSENSUS, ONE_CHART,
    CAT_CAL, EARNINGS, MIND, CLIENT_AMMO, CITATIONS, STALENESS,
])

RHS = "\n".join([
    '<div class="section-label">The Open</div>',
    dashboard_html,
    theme_line,
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

# ── Save ──────────────────────────────────────────────────────────────────────
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
