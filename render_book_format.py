#!/usr/bin/env python3
"""Render output.html using book.py's native Georgia-serif single-column format.
Content: 2026-06-02 brief. Styling: original book.py build_html() renderer.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import book

trades     = book.load_trades()
regime_log = book.load_json(book.REGIME_PATH, [])

# ── Reactive new ideas (MM-006, 007, 008) and pre-position (MM-009)
# Passed as idea dicts so book.py's render_trade_card() formats them.
reactive_ids   = {"MM-2026-006", "MM-2026-007", "MM-2026-008"}
prepos_ids     = {"MM-2026-009"}
new_ideas      = [t for t in trades["open"] if t["id"] in reactive_ids]
pre_pos_ideas  = [t for t in trades["open"] if t["id"] in prepos_ids]

# ── Brief dict — text sections use plain <p> HTML compatible with old .sec CSS
brief = {
    # ── Regime ──────────────────────────────────────────────────────────────
    "regime": "AI Vertical Meets Hormuz Binary",
    "regime_note": (
        "D-1 before AVGO Q2 print. Market positioned for the seventh consecutive "
        "AI revenue beat. Iran MoU still unsigned. Search API outage — all market "
        "data carried from 2026-06-01."
    ),

    # ── Yesterday, graded ───────────────────────────────────────────────────
    "yesterday_graded": """
<p style="font-size:13px;color:#9a9a9a;margin:0 0 10px">
  <strong style="color:#c0392b">Data outage — eyeball before trading.</strong>
  Search API returned 529 for all queries on 2026-06-02.
  All prices carried from 2026-06-01 last-good values.
</p>
<table>
<thead><tr><th>ID</th><th>Trade</th><th>Entry → Current</th><th>P&amp;L</th><th>Note</th></tr></thead>
<tbody>
<tr><td class="gold">MM-2026-001</td><td>Short EURAUD</td><td>1.645 → 1.621</td>
    <td class="num g">+1.46%</td><td>Working — ECB growth-error read intact. 1.1% from target 1.610.</td></tr>
<tr><td class="gold">MM-2026-002</td><td>Long Brent</td><td>$91.00 → $92.50</td>
    <td class="num g">+1.65%</td><td>Working — Hormuz mine bid holding. COT specs nearly net-long (−9.2k).</td></tr>
<tr><td class="gold">MM-2026-003</td><td>Long Brent/Short WTI spread</td><td>3.30 → 2.81</td>
    <td class="num r">−14.85%</td><td>Under pressure — WTI recovering faster. Stop 1.50 intact. Watch spread.</td></tr>
<tr><td class="gold">MM-2026-004</td><td>Short US 10Y yield</td><td>4.44% → 4.47%</td>
    <td class="num r">−0.68%</td><td>18bp from stop at 4.65%. Payrolls Fri + FOMC Jun 16-17 are the tests.</td></tr>
<tr><td class="gold">MM-2026-005</td><td>Long gold (pre-pos)</td><td>$4,523 → $4,541.80</td>
    <td class="num g">+0.42%</td><td>Holding. COT longs lighter (154.3k) — constructive. 43 days min-hold left.</td></tr>
<tr><td class="gold">MM-2026-006</td><td>Long AVGO</td><td>$250 → $252</td>
    <td class="num g">+0.80%</td><td>D-1 before earnings. UBS PT $490. Stop $228. Reports tomorrow after close.</td></tr>
<tr><td class="gold">MM-2026-007</td><td>Short USDJPY</td><td>159.37 → 159.37</td>
    <td class="num mute">flat</td><td>Unchanged. 160.00 is the intervention trigger. Hold.</td></tr>
<tr><td class="gold">MM-2026-008</td><td>SPX Jun-27 7300/7000 put spread</td><td>35 → 35</td>
    <td class="num mute">flat</td><td>Hold through AVGO tomorrow, payrolls Fri, ECB Jun 11, FOMC Jun 16-17.</td></tr>
<tr><td class="gold">MM-2026-009</td><td>2s10s UST steepener (pre-pos)</td><td>+15bp → +15bp</td>
    <td class="num mute">flat</td><td>Payrolls Fri is first catalyst. 45-day min-hold.</td></tr>
</tbody>
</table>""",

    # ── Dashboard ────────────────────────────────────────────────────────────
    "dashboard": [
        {"name": "S&P 500 (Jun 1 ⚠)", "level": "~7,580",     "chg": "carried",  "dir": "flat"},
        {"name": "Nasdaq (Jun 1 ⚠)",  "level": "~27,200",    "chg": "carried",  "dir": "flat"},
        {"name": "DAX",               "level": "unverified",  "chg": "",         "dir": "unverified"},
        {"name": "Nikkei",            "level": "unverified",  "chg": "",         "dir": "unverified"},
        {"name": "FTSE",              "level": "unverified",  "chg": "",         "dir": "unverified"},
        {"name": "EURUSD (Jun 1 ⚠)", "level": "1.1644",      "chg": "carried",  "dir": "flat"},
        {"name": "GBPUSD",            "level": "unverified",  "chg": "",         "dir": "unverified"},
        {"name": "USDJPY (Jun 1 ⚠)", "level": "159.37",      "chg": "carried",  "dir": "flat"},
        {"name": "DXY (Jun 1 ⚠)",    "level": "~99.0",       "chg": "carried",  "dir": "flat"},
        {"name": "US 10Y (Jun 1 ⚠)", "level": "4.47%",       "chg": "carried",  "dir": "flat"},
        {"name": "Bund 10Y",          "level": "unverified",  "chg": "",         "dir": "unverified"},
        {"name": "2s10s",             "level": "~+15bp",      "chg": "",         "dir": "flat"},
        {"name": "WTI (Jun 1 ⚠)",    "level": "$89.69",      "chg": "carried",  "dir": "flat"},
        {"name": "Brent (Jun 1 ⚠)",  "level": "~$92.50",     "chg": "carried",  "dir": "flat"},
        {"name": "Gold (Jun 1 ⚠)",   "level": "$4,541.80",   "chg": "carried",  "dir": "flat"},
        {"name": "VIX (May 29 ⚠)",   "level": "~15.32",      "chg": "carried",  "dir": "flat"},
        {"name": "SOFR (May 28 ⚠)",  "level": "3.62%",       "chg": "carried",  "dir": "flat"},
        {"name": "MOVE",              "level": "unverified",  "chg": "",         "dir": "unverified"},
    ],
    "dominant_theme": (
        "AVGO prints tomorrow after the close. The entire AI trade — from "
        "Nemotron 3 Ultra to AMD EPYC Venice — runs through one proof point at 41x "
        "forward earnings. The pain trade is careful guidance, not a miss."
    ),

    # ── The Wrap ─────────────────────────────────────────────────────────────
    "wrap": """
<p>The market has made a bet. Broadcom reports tomorrow after the close, and the consensus
has decided this is a confirmation event — a formality that rubber-stamps the AI capex
cycle for another quarter. At 41 times forward earnings, AVGO is pricing six more
consecutive AI revenue beats. An in-line print is not neutral at 41x. An in-line print
at 41x is the hidden bear case, and nobody is positioned for it.</p>

<p>The anatomy of today's market: the entire AI trade — from Nvidia's Nemotron 3 Ultra
keynote Monday, to AMD's Lisa Su at Computex Day 2 today, to the custom ASIC buildout at
Microsoft, Google, Meta, and TikTok — runs through a single proof point that prints
tomorrow night. If AVGO guides Q3 AI revenue above $11.5 billion, the cycle is confirmed
and every multiple is justified. If it guides in-line or conservatively, the 140% YoY
growth rate decelerates and funds that paid 41x for perpetual acceleration have to reprice
simultaneously. There is no middle path at these valuations.</p>

<p><strong>L1 — The driver.</strong> This is not a macro day. The June 3 AVGO print is the most
important earnings event of the quarter for the AI trade — not because AVGO is the
biggest AI name, but because its custom ASIC revenue is the cleanest measure of what
hyperscalers are actually committing to in capex, as opposed to announcing. Jensen Huang
announces. AVGO invoices.</p>

<p><strong>L2 — Counter-intuitive hook.</strong> The pain trade is not a miss — it's guidance that
is technically a beat on the quarter but conservative on the forward look. "$10.9B AI
revenue vs $10.7B expected, Q3 guided at $11.0B" is a beat on the headline and a
re-rate on the stock. The market is not positioned for careful guidance from a company
at 41x forward earnings.</p>

<p><strong>L3 — The gap.</strong> What's priced: perpetual AI capex acceleration at 140% YoY sustained
through 2027. What's possible: Microsoft, Meta, and Google have each given cautious capex
commentary on the margin. AVGO's four hyperscaler ASIC clients each have distinct refresh
cycles. If one pulls forward and another delays, the blended revenue looks smooth in the
aggregate but the forward book is thinner and lumpier than the headline implies.</p>

<p><strong>Burry tell.</strong> AVGO has four hyperscaler ASIC customers. The street models a
diversified AI capex cycle; the ASIC business is a two-to-three client business wearing a
four-client coat. The tell will not appear in the headline revenue. It will appear in the
Q&amp;A — in whether management names customers, gives a specific Q4 revenue commitment, or
hedges with "strong pipeline." Listen for the hedge.</p>

<p><strong>Pozsar mechanic.</strong> AVGO's AI revenue is paid via NRE (non-recurring engineering)
fees upfront; revenue recognition is lumpy but cash flow is front-loaded. Tomorrow's print
tells you what Google and Meta decided in Q4 2025 — it is a lagging indicator of actual
hyperscaler commitment. The real current commitment level lives in the backlog and Q&amp;A,
not the headline number.</p>

<p><strong>Papic constraint.</strong> All four hyperscaler ASIC customers are US-domiciled. US chip
export control expansion is the political constraint behind AVGO's growth ceiling. The
current administration is setting precedents in a direction that constrains the next ASIC
generation's TAM. If controls tighten further in June, the constraint lands in Q4 2026
guidance, not tomorrow's print.</p>""",

    # ── Correlation Regime ───────────────────────────────────────────────────
    "correlation_regime": """
<p><strong>AVGO vs SPX — the AI trade is more concentrated than the index implies.</strong>
Tomorrow's AVGO print will move the market more than its SPX weight suggests because it is
the proxy for the entire hyperscaler-ASIC capex theme. A miss reprices NVDA (competitive
read-through), AMD (data center AI), and the SOX simultaneously. This is not AVGO-to-SPX
correlation — it is AVGO-to-AI-risk-premium, priced across every major index.</p>

<p><strong>Gold flat, WTI steady, dollar near lows — the macro is on hold pending the print.</strong>
When a single event dominates the forward risk calendar, cross-asset correlations compress.
Everything is waiting for AVGO. DXY ~99, WTI ~$89.69, Gold $4,541.80 all carried from
June 1 (data outage today). Real moves come Wednesday night and Thursday morning.</p>

<p><strong>EURUSD held 1.1644 — ECB June 11 hike is 9 days away, EUR still not rallying.</strong>
The EUR spec long (crowded dollar-bear trade of 2026) is not front-running the ECB hike
bullishly. That is the setup for a violent sell-the-fact on June 11. MM-2026-001 (short
EURAUD) is 1.1% from target at 1.610.</p>

<p><strong>Brent-WTI spread at $2.81 (carried) — Iran binary unchanged, MoU still unsigned.</strong>
At $2.81 the market prices ~65% deal probability. No fresh Iran data today. The political
constraint (Trump needs a deal before June 11) is unchanged. Iran is not in a hurry.</p>""",

    # ── Vol & Skew ───────────────────────────────────────────────────────────
    "vol_skew": """
<p><strong>VIX term structure — contango, data from June 1:</strong> VIX9D ~13.5 · VIX ~15.32 ·
VIX3M ~17.2 · VIX6M ~18.5. Front-end vol is the cheapest on the board relative to the
event calendar. AVGO prints tomorrow; payrolls Friday; ECB in 9 days. VIX9D at 13.5
going into this 72-hour window is cheap.</p>

<p><strong>CBOE SKEW elevated (~140–145).</strong> Elevated skew at low spot VIX is the classic
"everyone's hedged but nobody believes it" setup. The skew premium is real and expensive.
The cheapest hedge is in the front end — MM-2026-008 (SPX put spread) owns this.</p>

<p><strong>D-1 vol setup.</strong> AVGO implied vol into earnings (data unavailable today, search
outage) is typically 8–12% for a print of this magnitude. If IV is still 8% on a stock
at 41x reporting the AI cycle's proof point, the surface is wrong. MM-2026-008 benefits
from any vol expansion: AVGO miss, Iran escalation, or payrolls surprise Friday.</p>

<p><strong>MOVE — unverified today.</strong> Expected elevated into ECB June 11 and FOMC June 16-17.
MOVE above 100 would signal rates markets are no longer treating the ECB hike as benign.</p>""",

    # ── Sector & RV ──────────────────────────────────────────────────────────
    "sector_rv": """
<p><strong>Computex Day 2 — AMD Lisa Su keynote.</strong> AMD confirmed EPYC Venice (TSMC 2nm) in
mass production. The second supply-chain confirmation this week that AI compute
buildout is accelerating. AVGO's custom ASIC thesis is structurally supported by the
entire Computex narrative. AMD's GPU roadmap (if announced today) is the secondary
catalyst for the SOX vs NVDA pair trade.</p>

<p><strong>ISM Manufacturing May — released today, data unavailable.</strong> ISM Manufacturing for
May is typically released on the first business day of June. April reading was 48.9 PMI,
46.4 employment. A May reading below 48.0 would be the 19th consecutive month of
manufacturing contraction and adds to the 2s10s steepener case (MM-2026-009). If it
printed above 50.0, the soft-landing narrative gets a data point — dollar could bid and
MM-2026-004 (short 10Y yield) faces pressure. Eyeball live before acting.</p>

<p><strong>Technology strongest, Utilities / Consumer Discretionary weakest (data from June 1).</strong>
Computex AI narrative carries tech. Rate sensitivity hits utilities. Goods-sector payroll
risk hits consumer discretionary ahead of Friday's print.</p>

<p><strong>RV: Long NVDA vs Short SOX equal-weight.</strong> NVDA +12% YTD vs SOX +74%. Nemotron
3 Ultra (Monday) and AMD EPYC Venice (today) both feed the infrastructure layer. NVDA's
software-layer pivot gets its first market test tomorrow via AVGO. If AVGO beats strongly
and NVDA outperforms the SOX the next day, the model-layer value rotation has started.</p>""",

    # ── Positioning & Flows ──────────────────────────────────────────────────
    "positioning": """
<p><strong>COT data carried from May 27.</strong> Oil large spec net at −9.2k — nearly net-long. A
Hormuz escalation after the AVGO print would be the worst-timed geopolitical shock for
a market in "risk-on AI" mode; squeeze amplified by light positioning. Gold: 154.3k net
long — lighter, constructive. EUR: net long — pain trade building into June 11 ECB.</p>

<p><strong>Positioning into AVGO print.</strong> The AI equity trade is crowded long. A miss doesn't
just move AVGO — it triggers simultaneous de-risking across NVDA, AMD, TSMC, ASML, and
the broader SOX. Crowded long + single binary event + 41x multiple = tail risk is
asymmetric to the downside. MM-2026-008 (put spread) is the portfolio-level hedge.</p>""",

    # ── Funding & Plumbing ───────────────────────────────────────────────────
    "funding": """
<p><strong>SOFR 3.62% — carried from June 1 (SEC repo clearing deadline is today).</strong>
June 2, 2026 is the SEC's deadline for repo market central clearing compliance. If SOFR
spikes above 3.75% today, that is a clearing-transition plumbing signal, not a credit
event. The repo market has been restructuring toward central clearing for months. Current:
3.62% (carried) — verify live. This is the Pozsar-layer event of the day, not the AVGO
print. If SOFR spikes, it tightens dollar funding conditions at exactly the moment the
market needs liquidity to manage AVGO event risk tomorrow.</p>""",

    # ── What the Tape Is Missing ─────────────────────────────────────────────
    "tape_missing": """
<p><strong>1. AVGO's four-customer concentration is not in the model.</strong> The street models
AVGO's AI revenue as a diversified hyperscaler buildout. It is a four-customer ASIC
program where each customer has a distinct refresh cycle. If one pulls forward and
another delays, revenue blends to consensus — but the forward book is thinner and
lumpier than the headline implies. Signal: listen for management to avoid naming customers
on the Q&amp;A. Avoidance is the tell. The level that changes the story: if management
provides a Q4 revenue commitment (bullish) vs hedges with "strong pipeline" (bear).</p>

<p><strong>2. ISM Manufacturing May may be the 19th consecutive month below 50.</strong> April PMI
48.9, employment 46.4. A May reading below 48 is the goods-sector contraction signal that
precedes payroll softness by 6–8 weeks. If it printed below 48 today, the 89k payrolls
consensus for Friday becomes aggressive and the 2s10s steepener (MM-2026-009) accelerates
its thesis. Data not confirmed today — eyeball live before trading.</p>

<p><strong>3. June 2 is the SEC repo clearing deadline — completely under-watched.</strong> The
SEC's rule for central clearing of bilateral repo takes effect today. A SOFR spike above
3.75% is not a credit signal — it is a clearing-transition artifact. But if it persists,
it tightens dollar funding at exactly the moment the market needs liquidity for AVGO event
positioning tomorrow. Watch SOFR alongside the AVGO print setup.</p>""",

    # ── Consensus: Bid/Offer ─────────────────────────────────────────────────
    "consensus": """
<p><strong>Consensus BID:</strong> AVGO beats tomorrow — seventh consecutive AI revenue beat — AI
cycle confirmed for Q3. Market rallies Thursday. Iran deal before June 11. VIX stays
below 17 through the event calendar.</p>

<p><strong>Strongest argument against:</strong> The consensus bid requires AVGO to not just beat but
beat-and-raise at 41x. "In-line" is the hidden bear case: $10.9B AI revenue vs $10.7B
expected, Q3 guide at $11.0B. The market calls that a beat; the 41x multiple calls it
deceleration. Nobody is positioned for careful guidance from a company at these
valuations. The pain trade is a technically-positive print that the multiple punishes.</p>""",

    # ── Today's One Chart ────────────────────────────────────────────────────
    "one_chart": """
<p><strong>AVGO implied volatility into tomorrow's print.</strong> Data unavailable today (search
outage), but the framework: AVGO at 41x pricing continued AI capex acceleration. If
implied vol for the June 6 expiry is below 12%, vol is mispriced — the stock should move
10–15% on a beat-or-miss binary at this valuation. If IV is above 15%, the market is
appropriately hedged. Check the AVGO options chain live before the close today: that
number tells you whether consensus is complacent or positioned.</p>

<p><strong>Second chart: SOFR intraday.</strong> SEC repo clearing deadline is today. SOFR above
3.75% = plumbing stress. SOFR below 3.70% = clean. Two charts that matter today; neither
is Brent.</p>""",

    # ── New ideas (rendered by book.py's render_trade_card) ──────────────────
    "new_ideas": new_ideas,
    "pre_position_ideas": pre_pos_ideas,
    "event_radar_note": (
        "<p>Next key events: AVGO Q2 earnings Wednesday June 3 (after close) — "
        "the AI cycle proof point. US May payrolls Friday June 5 — 89k consensus. "
        "ECB +25bp June 11. FOMC dot plot June 16-17 — live 7/7 split on no-cut vs 1-cut.</p>"
    ),

    # ── Catalyst calendar (rendered by book.py's render_catalyst) ────────────
    "catalyst_calendar": [
        {
            "day": "Tue", "date": "Jun 2",
            "event": "Computex Day 2 (AMD Lisa Su) · ISM Mfg May · SEC repo deadline",
            "consensus": "AMD EPYC Venice confirmed; ISM ~49; SOFR stable",
            "view": "ISM below 48 = 19th consecutive mfg contraction, adds to payroll-weakness case. SOFR spike = clearing-transition risk, not credit.",
            "asymmetry": "ISM <48: bonds bid, 2s10s accelerates; SOFR spike: vol up",
            "dir": "flat",
        },
        {
            "day": "Wed", "date": "Jun 3",
            "event": "Broadcom (AVGO) Q2 FY2026 earnings — after close",
            "consensus": "EPS $2.40, revenue $22.11B, AI revenue $10.7B (+140% YoY)",
            "view": "Q3 AI revenue guide is the only number. >$11.5B = beat-and-raise. $10.8–11.4B = in-line, 41x punishes. <$10B = miss, multi-compression.",
            "asymmetry": ">$11.5B: AVGO +10–15%; <$10.7B: AVGO −5–10%, AI re-rate",
            "dir": "up",
        },
        {
            "day": "Fri", "date": "Jun 5",
            "event": "US May payrolls (BLS 8:30 ET) + German IFO",
            "consensus": "+89k payrolls, unemployment 4.3%",
            "view": "Below 75k: 2+ cuts priced — DXY breaks 98, bonds +15bp, gold bids. Above 110k: dollar recovers, ECB hike amplified.",
            "asymmetry": "<75k: DXY −0.8%, 2Y −15bp; >110k: DXY +0.5%",
            "dir": "down",
        },
        {
            "day": "Wed", "date": "Jun 11",
            "event": "ECB rate decision (+25bp fully priced)",
            "consensus": "+25bp; neutral-to-hawkish press conference",
            "view": "'One and done' = EUR sell-the-fact; spec long unwinds. 'Further hikes' = EUR spike then fade on growth concerns.",
            "asymmetry": "EUR/USD −0.8% on pause signal; +0.5% then fade if hawkish",
            "dir": "down",
        },
        {
            "day": "Tue–Wed", "date": "Jun 16–17",
            "event": "FOMC meeting + dot plot (live 7/7 split on no-cut vs 1-cut)",
            "consensus": "No cut. One-cut median holds.",
            "view": "Zero-cut dot: DXY +0.7%, gold −2%, MM-2026-004 stop approaches. Two-cut dot (requires payroll miss Friday): DXY −1.2%, 10Y −20bp.",
            "asymmetry": "0-cut: DXY +0.7%, 10Y +8bp; 2-cut: DXY −1.2%, 10Y −20bp",
            "dir": "flat",
        },
    ],

    # ── What Changes My Mind ─────────────────────────────────────────────────
    "what_changes_mind": """
<p><strong>MM-2026-001 · Short EURAUD:</strong> Close if EURAUD holds above 1.640 post-ECB June 11.
Currently 1.1% from target 1.610. Holding.</p>
<p><strong>MM-2026-002 · Long Brent:</strong> Exit below $87 weekly close. No fresh Iran data.
Brent-WTI spread at 2.81 is the live signal — below 2.00 = deal fully priced.</p>
<p><strong>MM-2026-003 · Long Brent/Short WTI spread:</strong> Discretionary close below 2.00.
Most likely near-term close in the book.</p>
<p><strong>MM-2026-004 · Short US 10Y yield:</strong> Stop 4.65% — 18bp away at 4.47%. Strong payrolls
(&gt;130k) or zero-cut FOMC dot are the two triggers.</p>
<p><strong>MM-2026-005 · Long gold (pre-pos):</strong> Min hold until July 15. Stop $4,250.
No discretionary close permitted. FOMC June 17 is the first structural test.</p>
<p><strong>MM-2026-006 · Long AVGO — tomorrow is the exit event.</strong> Exit same day if AI
revenue guide below $10.7B or stock closes &gt;8.8% lower. Hold through print + 5 days
on a genuine beat-and-raise. Do not hold a miss.</p>
<p><strong>MM-2026-007 · Short USDJPY:</strong> Stop 163.00. 160.00 is the intervention trigger —
Finance Ministry watching. Exit immediately above 160.00.</p>
<p><strong>MM-2026-008 · SPX put spread:</strong> Hold through the event window. Max loss = $35
premium. This is the hedge on the AVGO binary — do not exit pre-print.</p>""",

    # ── Client-call ammo (rendered by render_client_ammo) ────────────────────
    "client_ammo": [
        {
            "q": "Should I add to AVGO before the print tomorrow?",
            "a": ("No — not here, not today. You already own it at $250 in MM-2026-006. "
                  "Adding at $252 the day before a binary print at 41x concentrates the wrong risk. "
                  "The asymmetry is already captured. Size the hedge (MM-2026-008) appropriately "
                  "instead of adding delta the day before the event."),
        },
        {
            "q": "What does an AVGO miss mean for the rest of the portfolio?",
            "a": ("An AVGO miss reprices every AI-adjacent name simultaneously: NVDA (competitive "
                  "read-through), AMD (data center AI), TSMC (wafer demand), ASML (EUV volume). "
                  "SOX sells 3–5% on the open. MM-2026-008 (put spread) activates. "
                  "Gold (MM-2026-005) holds or bids on risk-off flows. USDJPY (MM-2026-007 short) "
                  "benefits from safe-haven yen flows."),
        },
        {
            "q": "Why does the SEC repo deadline matter today?",
            "a": ("It's the Pozsar layer nobody is watching. The SEC's requirement for central "
                  "clearing of bilateral repo is effective today (June 2). If SOFR spikes above 3.75% "
                  "intraday — verify live — it tightens dollar funding at exactly the moment the "
                  "market needs liquidity for AVGO event positioning tomorrow. It's a plumbing event, "
                  "not a credit event, but the timing with AVGO is uncomfortable."),
        },
    ],

    # ── Charts data ──────────────────────────────────────────────────────────
    "vix_term": [
        {"label": "VIX9D", "value": 13.5},
        {"label": "VIX",   "value": 15.32},
        {"label": "VIX3M", "value": 17.2},
        {"label": "VIX6M", "value": 18.5},
    ],
    "yield_curve_pts": [
        {"label": "2Y",  "value": 4.32},
        {"label": "5Y",  "value": 4.40},
        {"label": "10Y", "value": 4.47},
        {"label": "30Y", "value": 4.62},
    ],

    # ── Staleness check (rendered by render_staleness) ───────────────────────
    "staleness": [
        {"datum": "All market prices",        "source": "Carried from Jun 1",        "asof": "2026-06-01", "stale": True},
        {"datum": "WTI $89.69",               "source": "TradingEconomics/OilPrice", "asof": "2026-06-01", "stale": True},
        {"datum": "Brent ~$92.50",            "source": "ICE/Reuters (estimated)",   "asof": "2026-06-01", "stale": True},
        {"datum": "Gold $4,541.80",           "source": "TwelveData",                "asof": "2026-06-01", "stale": True},
        {"datum": "US 10Y 4.47%",             "source": "TradingEconomics / FRED",   "asof": "2026-06-01", "stale": True},
        {"datum": "EURUSD 1.1644",            "source": "TradingEconomics",          "asof": "2026-06-01", "stale": True},
        {"datum": "USDJPY 159.37",            "source": "TradingEconomics",          "asof": "2026-06-01", "stale": True},
        {"datum": "DXY ~99.0",                "source": "TradingView/StreetStats",   "asof": "2026-06-01", "stale": True},
        {"datum": "VIX 15.32",                "source": "Yahoo Finance",             "asof": "2026-05-29", "stale": True},
        {"datum": "SOFR 3.62%",               "source": "NY Fed / SOFRrate.com",     "asof": "2026-05-28", "stale": True},
        {"datum": "COT positioning",          "source": "CFTC via StoneX",           "asof": "2026-05-27", "stale": True},
        {"datum": "AVGO ~$252",               "source": "Estimated Jun 1",           "asof": "2026-06-01", "stale": True},
        {"datum": "ISM Manufacturing May",    "source": "Not available (529 outage)","asof": "unavailable","stale": True},
        {"datum": "AVGO implied vol pre-print","source": "Not available (529 outage)","asof": "unavailable","stale": True},
        {"datum": "DAX / Nikkei / FTSE / Bund / Gilt / MOVE", "source": "Not available (529 outage)", "asof": "unavailable", "stale": True},
    ],
}

# ── Render via book.py's native build_html ────────────────────────────────────
book.step("Rendering with book.build_html (old format)")
html_out = book.build_html(brief, trades, regime_log)

book.step("Writing output.html")
with open(book.OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(html_out)

book.save_json(book.TRADES_PATH, trades)
book.save_json(book.REGIME_PATH, regime_log)

sz = len(html_out)
print(f"output.html: {sz:,} bytes")
print(f"Open: {len(trades['open'])} | Closed: {len(trades['closed'])}")

import subprocess
subprocess.Popen(["start", book.OUTPUT_PATH], shell=True)
