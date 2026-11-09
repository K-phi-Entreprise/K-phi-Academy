# FP&A course: lesson video scripts.
from scripts_f import T, E
def S(img, cap, d=7, zoom=1.2, focus=None, label=None):
    s = {"type": "shot", "d": d, "img": img, "zoom": zoom, "cap": cap}
    if focus: s["focus"] = focus
    if label: s["label"] = label
    return s
M = lambda code, mins: f"FP&A · {code} · {mins} min"

LESSONS = {
"P1.1": {"scenes": [
    T("P&L year to date,", "cumulative balance sheet", M("P1.1", 7), "P1.1 · P&L year to date, cumulative balance sheet"),
    {"type": "compare", "d": 10, "heading": "Two rules everywhere", "left": "P&L", "litems": ["Year to date", "Restarts each fiscal year"], "right": "Balance sheet", "ritems": ["Cumulative", "Balances at a date"],
     "cap": ["The P&L restarts at zero at the start of each fiscal year.", "The balance sheet is cumulative: balances at a date."]},
    S("pl_x", ["Statements are built from the ledger lines and each account's classification.", "A group view brings the entities together in the reporting currency."], d=8),
    {"type": "checklist", "d": 8, "eyebrow": "BEFORE PRESENTING", "heading": "Two checks", "step": 1.6,
     "items": ["The balance sheet balances, per entity", "Net income, less distributions, matches retained earnings"],
     "cap": "If either fails, look at account classification first."},
    E("Next  ·  P1.2  Drilling down to ledger lines")]},
"P1.2": {"scenes": [
    T("Drilling down", "to ledger lines", M("P1.2", 6), "P1.2 · Drilling down to ledger lines"),
    {"type": "flow", "d": 10, "eyebrow": "FROM THE TOP", "heading": "Find the cause before changing anything", "step": 1.2,
     "nodes": [("Statement line", "operating expenses"), ("Accounts", "with totals"), ("Ledger lines", "sorted by amount")],
     "cap": ["Every figure opens to the lines behind it.", "Sort by amount: a few large lines explain most surprises."]},
    {"type": "compare", "d": 9, "heading": "Where the fix belongs", "left": "Fix", "litems": ["Classification: in account setup", "Booking: in the accounting system"], "right": "Never", "ritems": ["Adjust the statement itself"],
     "cap": ["Fix a classification once in setup, a booking at the source.", "Then import again."]},
    E("Next  ·  P1.3  Distributions and retained earnings")]},
"P1.3": {"scenes": [
    T("Distributions and", "retained earnings", M("P1.3", 6), "P1.3 · Distributions and retained earnings"),
    {"type": "flow", "d": 9, "eyebrow": "BELOW NET INCOME", "heading": "Distributions are not an expense", "step": 1.2,
     "nodes": [("Net income", ""), ("Distributions", "dividends"), ("Retained", "kept in the company")],
     "cap": "K-φ reports distributions below net income, then the amount retained."},
    {"type": "table", "d": 9, "eyebrow": "PAST AND FUTURE", "heading": "Where the figures come from", "cols": ["", "Source"], "widths": [1, 3], "step": 1.2,
     "rows": [["Past", "Equity accounts you confirm as distribution accounts"], ["Future", "An input per fiscal year, seeded from the last twelve months"]],
     "cap": ["Distributions booked to an expense account understate the margin.", "Raise it, and fix it in the accounting system."]},
    E("Next  ·  P2.1  The KPI set and their formulas")]},
"P2.1": {"scenes": [
    T("The KPI set", "and their formulas", M("P2.1", 7), "P2.1 · The KPI set and their formulas"),
    {"type": "table", "d": 10, "eyebrow": "ABOUT THIRTY KPIs", "heading": "Four families", "cols": ["Family", "Examples"], "widths": [1, 2.4], "step": 1.0,
     "rows": [["Profitability", "Gross margin, EBITDA, net margin"], ["Working capital", "DSO, DPO, DIO, cash conversion cycle"], ["Liquidity", "Current ratio, quick ratio"], ["Leverage", "Debt to EBITDA, interest coverage, DSCR"]],
     "cap": ["K-φ computes some thirty KPIs, each with its formula and thresholds.", "Names are not standard across companies: read the formula."]},
    S("kpi", "Agree one definition per KPI with the client, and write it down.", d=7),
    E("Next  ·  P2.2  Working capital and trailing windows")]},
"P2.2": {"scenes": [
    T("Working capital:", "DSO, DPO, DIO", M("P2.2", 8), "P2.2 · Working capital: DSO, DPO, DIO and trailing windows"),
    {"type": "flow", "d": 9, "eyebrow": "CASH CONVERSION CYCLE", "heading": "DSO + DIO − DPO", "step": 1.1,
     "nodes": [("DSO", "customers pay"), ("DIO", "stock sits"), ("DPO", "we pay suppliers")],
     "cap": ["DSO, DPO and DIO estimate days to collect, to sell stock, and to pay.", "The cash conversion cycle is DSO plus DIO minus DPO."]},
    S("kpi", ["K-φ uses a three-month trailing window by default.", "A single month can mislead in either direction."], d=8, zoom=1.3),
    {"type": "checklist", "d": 8, "eyebrow": "BEFORE QUOTING A DSO", "heading": "Check", "step": 1.4,
     "items": ["Intercompany balances are excluded", "Sales and receivables on the same tax basis", "No single large invoice explains the jump"],
     "cap": "DSO is a pointer. When it moves, open the receivables by customer."},
    E("Next  ·  P2.3  Covenants and headroom")]},
"P2.3": {"scenes": [
    T("Covenants", "and headroom", M("P2.3", 7), "P2.3 · Covenants and headroom"),
    S("cov", ["Loan agreements set covenants, tested at each quarter end.", "K-φ shows each ratio and its headroom to the threshold."], d=9, zoom=1.3),
    {"type": "quote", "d": 7, "l1": "Headroom matters", "l2": "more than the ratio.", "cap": "2.8 against a ceiling of 3.0 is a conversation with the CFO today."},
    {"type": "checklist", "d": 8, "eyebrow": "TWO HABITS", "heading": "Covenants done right", "step": 1.6,
     "items": ["Use the loan agreement's definitions", "Test the forecast, not only the past"],
     "cap": "A breach you can see three months ahead can be negotiated."},
    E("Next  ·  P3.1  Versions and what they freeze")]},
"P3.1": {"scenes": [
    T("Versions and", "what they freeze", M("P3.1", 7), "P3.1 · Versions and what they freeze"),
    {"type": "flow", "d": 10, "eyebrow": "A VERSION", "heading": "Figures plus their own rules", "step": 1.2,
     "nodes": [("Budget 2027", "as approved"), ("Reforecast Q2", "starts from its rules"), ("Downside", "a copy to test")],
     "cap": ["A new version starts from the rules of the version it comes from.", "Editing one version never changes another."]},
    {"type": "bullets", "d": 8, "eyebrow": "GOOD PRACTICE", "heading": "Keep versions readable", "step": 1.3,
     "items": [("Closing a period freezes a copy", "compare later"), ("Names anyone can read", "\"Reforecast 2027 Q2\""), ("Few live versions", "each needs upkeep")],
     "cap": "Name versions so that anyone can read them a year later."},
    E("Next  ·  P3.2  Creating a budget from actuals")]},
"P3.2": {"scenes": [
    T("Creating a budget", "from actuals", M("P3.2", 5), "P3.2 · Creating a budget from actuals"),
    {"type": "compare", "d": 10, "heading": "A client with no budget", "left": "Better start", "litems": ["One click: budget from actuals", "Figures the client recognises"], "right": "Stopgap", "ritems": ["Run-rate forecast", "Flagged as an assumption"],
     "cap": ["Creating a budget from actuals gives figures the client recognises.", "Then review the largest lines together: revenue, payroll, rent, suppliers."]},
    E("Next  ·  P3.3  Budget versus actuals")]},
"P3.3": {"scenes": [
    T("Budget", "versus actuals", M("P3.3", 6), "P3.3 · Budget versus actuals"),
    S("vara", "Compare any version with what was booked, line by line and period by period.", d=7),
    {"type": "table", "d": 10, "eyebrow": "NAME THE CAUSE", "heading": "Four kinds of variance", "cols": ["Cause", "Example"], "widths": [1, 2.4], "step": 1.0,
     "rows": [["Volume", "Fewer shipments than planned"], ["Price", "Lower price, higher input cost"], ["Timing", "Invoice booked a month later"], ["Error", "Wrong account or period"]],
     "cap": ["A variance report is only useful if it says why.", "Comment only above a threshold agreed with the client."]},
    E("Next  ·  P3.4  Variance commentary with an assistant")]},
"P3.4": {"scenes": [
    T("Variance commentary", "with an assistant", M("P3.4", 7), "P3.4 · Variance commentary with an assistant"),
    {"type": "flow", "d": 9, "eyebrow": "THE WORKFLOW", "heading": "The assistant drafts, you sign", "step": 1.2,
     "nodes": [("Prompt", "role, period, threshold"), ("K-φ tools", "budget vs actuals"), ("Draft", "figures and causes"), ("You check", "and sign")],
     "cap": ["An assistant connected to K-φ reads budget versus actuals and drafts.", "You check every figure and sign."]},
    {"type": "quote", "d": 8, "l1": "For costs, over budget", "l2": "is unfavourable.", "cap": "Assistants get favourable and unfavourable wrong more than anything else."},
    E("Next  ·  P4.1  Forecast rules and deterministic replay")]},
"P4.1": {"scenes": [
    T("Forecast rules and", "deterministic replay", M("P4.1", 8), "P4.1 · Forecast rules and deterministic replay"),
    {"type": "flow", "d": 10, "eyebrow": "SAME INPUTS, SAME FORECAST", "heading": "Rules are saved and replayed", "step": 1.2,
     "nodes": [("Inputs", "actuals, rates"), ("Rules", "saved with the version"), ("Forecast", "reproducible")],
     "cap": ["Each forecast line follows a saved rule, replayed every time.", "When a figure moves, an input or a rule changed, and both are visible."]},
    {"type": "compare", "d": 8, "heading": "Keep the link", "left": "Do", "litems": ["Change the rule", "Comment unusual rules"], "right": "Never", "ritems": ["Type over a forecast line"],
     "cap": "Typing over a forecast line breaks the link between inputs and output."},
    E("Next  ·  P4.2  Ledger or open invoices")]},
"P4.2": {"scenes": [
    T("Collections and disbursements:", "ledger or open invoices", M("P4.2", 7), "P4.2 · Collections and disbursements: ledger or open invoices"),
    {"type": "compare", "d": 11, "heading": "One switch on the forecast", "left": "GL to cash (default)", "litems": ["Ledger balances and terms", "Works for any client"], "right": "Open invoices", "ritems": ["Each unpaid invoice", "Needs complete invoices"],
     "cap": ["Opening receivables and payables come from the ledger or from open invoices.", "Use open invoices only when the invoices in K-φ are complete."]},
    E("Next  ·  P4.3  Run-rate assumptions, opt-in")]},
"P4.3": {"scenes": [
    T("Run-rate assumptions,", "opt-in", M("P4.3", 5), "P4.3 · Run-rate assumptions, opt-in"),
    {"type": "flow", "d": 9, "eyebrow": "PROJECTED NEW SALES", "heading": "An assumption, so off by default", "step": 1.2,
     "nodes": [("Open invoices", "stop when invoicing stops"), ("+ run rate", "opt-in"), ("Written note", "the assumption")],
     "cap": ["A forecast from open invoices alone understates future collections.", "Projected new sales fix that, and are opt-in, off by default."]},
    E("Next  ·  P4.4  Stating assumptions")]},
"P4.4": {"scenes": [
    T("Stating", "assumptions", M("P4.4", 5), "P4.4 · Stating assumptions"),
    {"type": "table", "d": 12, "eyebrow": "A SHORT TEMPLATE", "heading": "Readable without its author", "cols": ["", ""], "widths": [1, 3], "step": 0.9, "hot": 4, "hot_at": 5,
     "rows": [["Base", "Actuals to October, budget after"], ["Revenue", "Run rate of three months, plus signed contracts"], ["Collections", "Open invoices for eight weeks, ledger after"], ["Payroll", "Headcount plan of 1 September"], ["Not included", "The acquisition under discussion"]],
     "cap": ["List a forecast's assumptions in plain words.", "What it leaves out is where the surprises come from."]},
    E("Next  ·  P5.1  Building a scenario")]},
"P5.1": {"scenes": [
    T("Building", "a scenario", M("P5.1", 7), "P5.1 · Building a scenario"),
    {"type": "compare", "d": 10, "heading": "Good scenarios", "left": "Do", "litems": ["One question each", "Two or three drivers", "Moves that have happened"], "right": "Avoid", "ritems": ["\"Bad year\"", "Everything down 20%"],
     "cap": ["A scenario changes a few drivers on top of a version.", "\"What if our largest customer pays 30 days later?\" is a scenario."]},
    E("Next  ·  P5.2  Presenting the difference")]},
"P5.2": {"scenes": [
    T("Presenting the", "difference", M("P5.2", 6), "P5.2 · Presenting the difference: profit, cash, headroom"),
    {"type": "table", "d": 11, "eyebrow": "THREE LINES", "heading": "Base, scenario, difference", "cols": ["", "Base", "Scenario", "Difference"], "widths": [2, 1, 1, 1], "step": 1.0, "hot": 1, "hot_at": 4,
     "rows": [["EBITDA, year", "4.2m", "4.1m", "−0.1m"], ["Lowest cash, week 46", "1.8m", "0.6m", "−1.2m"], ["Covenant headroom", "0.4x", "0.3x", "−0.1x"]],
     "cap": ["Show the difference on profit, lowest cash and covenant headroom.", "Payment-term changes barely move profit, and move cash a lot."]},
    E("Next  ·  P6.1  Inputs measured from the books")]},
"P6.1": {"scenes": [
    T("Inputs measured", "from the books", M("P6.1", 8), "P6.1 · Inputs measured from the books"),
    S("valuation", ["Valuation sits in FP&A, under Xplore, Valuation.", "Its operating inputs are measured from the tenant's own data."], d=9, zoom=1.25),
    {"type": "table", "d": 9, "eyebrow": "WHERE INPUTS COME FROM", "heading": "Three sources", "cols": ["Source", "Inputs"], "widths": [1, 2.6], "step": 1.0,
     "rows": [["Your books", "DSO, DPO, concentration, churn, burn, cash conversion"], ["Market data", "Risk premiums, betas, multiples (free datasets)"], ["You", "Risk-free rate, peer companies"]],
     "cap": "The earnings base always covers twelve months."},
    E("Next  ·  P6.2  Projection and extrapolation")]},
"P6.2": {"scenes": [
    T("Projection and", "extrapolation", M("P6.2", 7), "P6.2 · Projection and extrapolation"),
    {"type": "flow", "d": 10, "eyebrow": "FIVE YEARS", "heading": "Where projection becomes assumption", "step": 1.2, "color": {2: (255, 190, 90)},
     "nodes": [("Budget years", "per company"), ("Last budget year", "growth and margins"), ("Extrapolated", "labelled as such")],
     "cap": ["Projected cash flows come from the budget, per company.", "Years after the budget are extrapolated, and labelled. Test how much value depends on them."]},
    E("Next  ·  P6.3  Football field and the report")]},
"P6.3": {"scenes": [
    T("Football field", "and the report", M("P6.3", 6), "P6.3 · Football field and the report"),
    S("valuation", ["Each method gives a range; the football field reconciles them with editable weights.", "Present a range, not a point."], d=9, zoom=1.3),
    {"type": "quote", "d": 7, "l1": "Read the assumptions", "l2": "before you send the report.", "cap": "A valuation is advice to management, never a fairness opinion."},
    E("Next  ·  P7.1  The board pack")]},
"P7.1": {"scenes": [
    T("The board pack and", "why it calculates nothing", M("P7.1", 5), "P7.1 · The board pack and why it calculates nothing"),
    {"type": "flow", "d": 9, "eyebrow": "ONE SOURCE OF FIGURES", "heading": "The pack only picks", "step": 1.2,
     "nodes": [("Statements, KPIs", "computed in K-φ"), ("Board pack", "picks them as they are")],
     "cap": ["The board pack calculates nothing of its own.", "So its figures always match the screens. A wrong figure is fixed upstream."]},
    E("Next  ·  P7.2  Reconciling what you present")]},
"P7.2": {"scenes": [
    T("Reconciling", "what you present", M("P7.2", 5), "P7.2 · Reconciling what you present"),
    {"type": "table", "d": 10, "eyebrow": "TIE TO SOMETHING INDEPENDENT", "heading": "Before figures leave the team", "cols": ["Figure", "Tie to"], "widths": [1, 2], "step": 1.0,
     "rows": [["Revenue, net income", "The accounting system's own reports"], ["Cash", "Bank balances on the same date"], ["Receivables, payables", "The aged balances"]],
     "cap": ["Write down what you tied, even when the difference is zero.", "Disclose a difference you cannot explain."]},
    E("Next  ·  Exam  Statements, forecast and scenario")]},
}
