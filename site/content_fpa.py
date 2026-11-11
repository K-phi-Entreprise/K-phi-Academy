# FP&A course content.

def L(code, title, minutes, objective, read, try_, points, resources=None):
    d = {"code": code, "title": title, "minutes": minutes, "objective": objective, "read": read, "try": try_, "points": points}
    if resources: d["resources"] = resources
    return d

def Q(q, options, answer, why):
    return {"q": q, "options": options, "answer": answer, "why": why}

COURSE = {
    "id": "fpa", "code": "P", "title": "FP&A", "badge": "FP&A", "duration": "About 4 hours", "status": "available",
    "audience": "Controllers, FP&A analysts, consultants.", "prereq": "Foundation, AI for finance",
    "summary": "From ledger to statements, KPIs, budgets, forecasts, scenarios and valuation you can defend.",
    "outcomes": [
        "Produce statements and KPIs from the ledger and explain every figure.",
        "Run budget versus actuals and build forecasts with explicit, versioned rules.",
        "Build a scenario and present what moves in profit, cash and covenant headroom.",
        "Produce a valuation whose inputs are measured from the client's own books.",
    ],
    "lab": "Practise in your own practice company, a copy of Halden Trading: three companies, 23 months of ledger, and the budget and forecasts you build from it.",
    "chapters": [
        {"code": "P1", "title": "From ledger to statements", "lessons": [
            L("P1.1", "P&L year to date, cumulative balance sheet", 7,
              "Read K-φ's statements the way they are built.",
              """
K-φ builds the statements from the ledger lines you imported, using each account's classification.

Two rules hold everywhere:

- **The P&L restarts at zero at the start of each fiscal year.** A P&L for May shows January to May (for a calendar fiscal year). This is the rule, not a setting.
- **The balance sheet is cumulative.** It shows balances at a date, built from everything booked up to that date.

The same selectors as everywhere else apply: entity, business unit, currency, units. A group view brings the entities together in the reporting currency chosen in the top bar; each entity's own view stays in its own currency.

Before presenting a statement, check that the balance sheet balances for each entity and that net income, less distributions, matches the movement in retained earnings for the year. If either fails, look at the classification of accounts before anything else.
""",
              "In your practice company, open the P&L for Halden Trading Ltd for March 2026 (Company view, Incremental), then switch the entity selector to the group and compare.",
              ["The P&L is year to date and restarts each fiscal year.", "The balance sheet is cumulative.", "Check balance and net income before presenting."]),
            L("P1.2", "Drilling down to ledger lines", 6,
              "Trace any figure to the lines that make it.",
              """
Every figure in a statement can be opened to show the ledger lines behind it. Use that before you change anything.

A good drill-down habit, from the top:

1. **Line of the statement**, for example "Other operating expenses".
2. **Accounts** that feed it, with their totals.
3. **Ledger lines** of the account that looks wrong, sorted by amount.

Most surprises come from a few large lines: a reclassification booked in the wrong period, a one-off posted to an operating account, an intercompany charge that does not eliminate in the view you are reading.

When the cause is a classification, fix it once in the account setup. When it is a booking, the fix belongs in the accounting system, followed by a new import. Never adjust the statement itself.
""",
              "In your practice company, drill from the group's operating expenses for September 2026 down to the ledger lines, then do the same for Halden Trading Inc. alone.",
              ["Every statement figure opens to its ledger lines.", "Sort by amount; large lines explain most surprises.", "Fix classifications in setup and bookings at the source."]),
            L("P1.3", "Distributions and retained earnings", 6,
              "Show dividends and distributions correctly, past and future.",
              """
Distributions to shareholders are not an expense. K-φ reports them **below net income**: net income, then distributions, then the amount retained.

- **The past** is read from the equity accounts you confirm as distribution accounts in setup.
- **The future** is an input per fiscal year, seeded from the last twelve months, which the client adjusts.

Getting this right matters for two reasons. Cash forecasts need the outflow on the right dates, and covenant tests often treat distributions differently from operating costs.

If a client books distributions to an expense account, the P&L margin is understated. Raise it, and agree on the fix in the accounting system.
""",
              "In your practice company, find the lines between profit before tax and net income in the P&L for September 2026, and see what feeds them.",
              ["Distributions sit below net income.", "Past from confirmed equity accounts; future as a yearly input.", "Distributions booked as expenses distort margins."]),
        ], "check": [
            Q("A user opens the P&L for April. What period does it cover, for a calendar fiscal year?", ["April only", "January to April", "The last twelve months"], 1, "The P&L is year to date and restarts each fiscal year."),
            Q("A total looks wrong in the statements. What is your first step?", ["Adjust the statement line", "Drill down to the ledger lines", "Re-import everything"], 1, "Find the cause first. Most surprises come from a few large lines."),
            Q("Where do dividends appear in K-φ's P&L?", ["In operating expenses", "Below net income", "They do not appear"], 1, "Distributions are reported below net income, then retained earnings."),
        ]},
        {"code": "P2", "title": "KPIs and covenants", "lessons": [
            L("P2.1", "The KPI set and their formulas", 7,
              "Know what each KPI measures before you present it.",
              """
K-φ computes some thirty KPIs from the tenant's data, each with its formula and thresholds. They fall into a few families:

| Family | Examples |
|---|---|
| Profitability | Gross margin, EBITDA and its margin, net margin |
| Working capital | DSO, DPO, DIO, cash conversion cycle |
| Liquidity | Current ratio, quick ratio, cash runway |
| Leverage and coverage | Debt to EBITDA, interest coverage, DSCR |

Each KPI shows its formula. Read it before you present the figure, because names are not standard across companies. "EBITDA" in one board pack may exclude items another includes.

When a client uses a different definition, write it down and agree whether to adopt K-φ's or document the gap. Two definitions of the same KPI in one meeting cost more than either definition.
""",
              "In your practice company, open the KPI page and read the formula behind EBITDA margin and the current ratio.",
              ["About thirty KPIs, each with its formula and thresholds.", "Names are not standard; read the formula.", "Agree on one definition per KPI with the client."]),
            L("P2.2", "Working capital: DSO, DPO, DIO and trailing windows", 8,
              "Read working capital KPIs without being fooled by seasonality.",
              """
**DSO** (days sales outstanding) estimates how long customers take to pay. **DPO** does the same for suppliers, **DIO** for inventory. The **cash conversion cycle** is DSO plus DIO minus DPO.

K-φ computes them over a **three-month trailing window** by default. A single month can mislead in either direction: a strong or weak month moves sales and receivables unevenly, so one month's DSO says little about how customers actually pay.

Three things to check before quoting a DSO:

- **Which receivables** are included. Intercompany balances should not count.
- **Which sales** are the denominator. Sales including tax against receivables including tax, or neither.
- **Whether a large invoice** at period end explains a jump.

DSO is a pointer, not a measure of any one customer. When it moves, open the receivables by third party and look at who moved it.
""",
              "In your practice company, find DSO for Halden Trading Inc. and compare it with the group's.",
              ["Cash conversion cycle = DSO + DIO − DPO.", "Three-month trailing window by default.", "Check intercompany and large invoices before quoting."]),
            L("P2.3", "Covenants and headroom", 7,
              "Test bank covenants and show how close the client is to a breach.",
              """
Loan agreements set **covenants**, usually ratios tested at each quarter end: debt to EBITDA below a ceiling, interest coverage or DSCR above a floor.

K-φ computes the ratio and shows the **headroom**: how far the figure is from the threshold. Headroom matters more than the ratio itself. A debt to EBITDA of 2.8 against a ceiling of 3.0 is a conversation with the CFO today, not at the test date.

Two habits:

- **Use the agreement's definitions.** Covenant EBITDA often adds back items the accounting EBITDA does not. Record the definition with the covenant.
- **Test the forecast, not only the past.** Run the ratio on the forecast version to see the next test dates. A breach you can see coming three months ahead can be negotiated.
""",
              "In your practice company, open the covenants page, set a debt to EBITDA covenant of 3.0 for the group and read the headroom.",
              ["Headroom matters more than the ratio.", "Use the loan agreement's definitions.", "Test covenants on the forecast as well as on actuals."]),
        ], "check": [
            Q("Why does K-φ use a three-month trailing window for DSO?", ["To make DSO look better", "To smooth seasonality", "Because banks require it"], 1, "A single month swings with seasonal sales; a trailing window is more stable."),
            Q("A covenant's EBITDA definition differs from the accounting one. What do you do?", ["Use the accounting EBITDA", "Record and use the agreement's definition", "Average the two"], 1, "The covenant is tested on the agreement's terms."),
        ]},
        {"code": "P3", "title": "Budget and versions", "lessons": [
            L("P3.1", "Versions and what they freeze", 7,
              "Keep budgets and forecasts apart, and know what a version protects.",
              """
A **version** is a set of figures together with its own forecast rules: the budget, a Q2 reforecast, a downside case.

- A new version **starts from the rules of the version it is created from**.
- Editing a version changes **only that version**. The budget stays as the board approved it.
- **Closing a period** freezes a copy, so last month's forecast can always be compared with what happened.

Name versions so that anyone can read them a year later: "Budget 2027", "Reforecast 2027 Q2", not "new v3 final".

Keep the number of live versions small. Each one is a set of rules someone has to maintain.
""",
              "In your practice company, create a budget from actuals for the group, then a version from it. Change one figure in the version and check the budget is unchanged.",
              ["A version holds figures and its own rules.", "Editing one version never changes another.", "Closing a period freezes a copy."]),
            L("P3.2", "Creating a budget from actuals", 5,
              "Give a client without a budget a starting point in one step.",
              """
Many smaller clients have no formal budget. K-φ offers two things in that case.

- **A forecast from the recent run rate**, flagged clearly as an assumption, so the forecast is not empty. This is different from the projected new sales of lesson P4.3, which you add to a forecast on purpose.
- **One click to create a budget from actuals**, which copies the recent pattern into a new budget the client then adjusts.

The second is usually the better start. It gives the client figures they recognise, and every change they make is a decision they can explain.

Walk through the result with the client line by line for the largest items: revenue, payroll, rent, major suppliers. The smaller lines can follow the pattern.
""",
              "In your practice company, look at how the budget compares with actuals for one entity, and note the line you would adjust first.",
              ["No budget: run-rate forecast, flagged as an assumption.", "Better start: create a budget from actuals.", "Review the largest lines with the client."]),
            L("P3.3", "Budget versus actuals", 6,
              "Explain variances, not just show them.",
              """
Budget versus actuals compares the version you choose with what was booked, line by line and period by period.

A variance report is only useful if it says why. For each material variance, find one of four causes:

| Cause | Example |
|---|---|
| Volume | Fewer shipments than planned |
| Price | Lower selling price, higher input cost |
| Timing | An invoice booked a month later than planned |
| Error | Wrong account or wrong period |

Timing and error variances need no business action (errors need an accounting correction), but they must be named so nobody acts on them. Set a threshold for "material" with the client, for example 5% and a fixed amount, and comment only above it.
""",
              "In your practice company, run budget versus actuals for the group and find the largest variance.",
              ["Compare any version with actuals.", "Name the cause: volume, price, timing or error.", "Agree a materiality threshold with the client."]),
            L("P3.4", "Variance commentary with an assistant", 7,
              "Let an assistant draft the commentary, and check it before it goes out.",
              """
Writing variance commentary every month is a good job for an assistant connected to K-φ (course A, lesson A6.1). It reads budget versus actuals through K-φ's tools and drafts the text; you check and sign.

A prompt that works:

> You are preparing the October variance commentary for Halden Trading's CFO. Use K-φ to get budget versus actuals for the group, October and year to date. Comment only on variances above 5% and 50,000 USD. For each, give the figure, whether it is favourable or unfavourable, and the likely cause (volume, price, timing or error). Say where you are unsure.

Then check, as in lesson A5.2:

- Every figure traces to K-φ.
- **Favourable and unfavourable** are right. For costs, over budget is unfavourable; assistants get this wrong more than anything else.
- The causes are plausible, and the ones the assistant marked as unsure are confirmed with the people who know.

Save the prompt with the month's file. Next month, reuse it and compare.
""",
              "Connect your assistant to your K-φ account, draft the commentary with the prompt above, then check every sign.",
              ["An assistant drafts; you check and sign.", "Check favourable and unfavourable on every line.", "Reuse the same prompt each month."]),
        ], "check": [
            Q("You edit the Q2 reforecast. What happens to the budget?", ["It changes too", "Nothing", "It is deleted"], 1, "Editing a version changes only that version."),
            Q("A variance comes from an invoice booked one month late. What kind is it?", ["Volume", "Timing", "Price"], 1, "It reverses next month and needs no management action, but it must be named."),
        ]},
        {"code": "P4", "title": "Forecasting", "lessons": [
            L("P4.1", "Forecast rules and deterministic replay", 8,
              "Build forecasts that give the same answer every time.",
              """
Each forecast line follows a **rule**: a growth rate, a payment term, a fixed amount, a link to another line. Rules are saved with the version and **replayed**. The same inputs always give the same forecast.

That property is what makes a forecast auditable. When a figure changes, there are only two possible reasons: an input changed (new actuals, a new rate) or a rule changed. Both are visible.

Practical consequences:

- **Change the rule, not the result.** Typing a figure over a forecast line breaks the link between inputs and output.
- **Keep rules simple.** A rule the client cannot explain will not be maintained.
- **Document unusual rules** in the line's comment.
""",
              "In your practice company, open the forecast and change the growth rule on one revenue line. Note which other lines move.",
              ["Rules are saved with the version and replayed.", "Same inputs, same forecast.", "Change rules, never results."]),
            L("P4.2", "Collections and disbursements: ledger or open invoices", 7,
              "Choose the right source for cash coming in and going out.",
              """
Opening receivables and payables (cash still to collect from customers and to pay to suppliers) can come from two sources. A toggle on the forecast chooses which:

- **GL to cash**, the default, works from the ledger balances through your rules and payment terms. It covers every line and works for any client.
- **Open invoices** works from the invoices still unpaid, each at its expected date. It is more precise for the coming weeks, but it needs the invoices in K-φ (lesson F3.2).

An invoice matched to a bank receipt or payment leaves the open list and the forecast; a partly paid one stays for what is left.

Use open invoices when the client's invoices are complete and up to date in K-φ. If they are not, the ledger is the safer source.
""",
              "In your practice company, find the switch between GL to cash and open invoices, and compare the next eight weeks.",
              ["Two sources: ledger (GL to cash, the default) or open invoices.", "Open invoices is more precise for the near term.", "Use it only when the invoices in K-φ are complete."]),
            L("P4.3", "Run-rate assumptions, opt-in", 5,
              "Use run-rate sales without hiding the assumption.",
              """
A forecast built only from open invoices stops when invoicing stops, which understates future collections. The fix is to add **projected new sales** based on the recent run rate.

In K-φ, this is **opt-in and off by default**. Turning it on is a decision someone has to take and can explain.

When you turn it on, say so in the forecast's notes: "New sales projected at the run rate of the last three months." A reader who does not know will mistake an assumption for an order book.
""",
              "In your practice company, find where projected new sales are turned on, and write the note you would add.",
              ["Run-rate new sales are opt-in and off by default.", "Turning it on is a decision to explain.", "Write the assumption in the forecast's notes."]),
            L("P4.4", "Stating assumptions", 5,
              "Make every forecast readable by someone who did not build it.",
              """
A forecast nobody can explain will not be trusted, however good it is. Before you share one, list its assumptions in plain words.

A short template:

- **Base:** actuals to the end of October, budget for the rest of the year.
- **Revenue:** run rate of the last three months, plus signed contracts.
- **Collections:** open invoices for eight weeks, ledger terms after.
- **Payroll:** headcount plan of 1 September.
- **Not included:** the acquisition under discussion.

The last line matters as much as the others. What a forecast leaves out is where the surprises come from.
""",
              "Write the assumptions of a forecast you know, using the template.",
              ["List assumptions in plain words.", "Say what is not included.", "A forecast must be readable without its author."]),
        ], "check": [
            Q("The forecast changed overnight and no rule was edited. What changed?", ["Nothing, it is random", "An input, such as new actuals", "The theme"], 1, "With deterministic replay, only inputs or rules can move a forecast."),
            Q("Projected new sales from the run rate are...", ["On by default", "Opt-in, off by default", "Not available"], 1, "They are an assumption, so they are opt-in and off by default."),
            Q("Which source is more precise for the next few weeks of collections?", ["Open invoices", "The ledger", "The budget"], 0, "Open invoices carry real amounts and due dates."),
        ]},
        {"code": "P5", "title": "Scenarios", "lessons": [
            L("P5.1", "Building a scenario", 7,
              "Change a few drivers and see the effect, without touching the base.",
              """
A **scenario** changes a few drivers on top of a version: volume, price, payment terms, a currency move. The base version stays as it is.

Good scenarios are few and specific:

- **One question per scenario.** "What if our largest customer pays 30 days later?" is a scenario. "Bad year" is not.
- **Few drivers.** Change two or three things, so the result can be explained.
- **Realistic sizes.** Use moves that have happened before, or that the client fears.

Build the scenario on the version management actually uses, usually the latest reforecast.
""",
              "In your practice company, build a scenario where the largest customer pays 30 days later.",
              ["A scenario changes a few drivers on a version.", "One question per scenario.", "Use realistic, explainable moves."]),
            L("P5.2", "Presenting the difference: profit, cash, headroom", 6,
              "Show what a scenario changes, not two full sets of figures.",
              """
Management does not need the scenario's full P&L. It needs the **difference** from the base, on three lines:

| | Base | Scenario | Difference |
|---|---|---|---|
| EBITDA, year | | | |
| Lowest cash balance, and when | | | |
| Covenant headroom at next test | | | |

The second line is usually the one that matters. Many scenarios barely move profit but move cash a lot, especially payment-term changes and currency moves.

End with one sentence on what management could do: draw on a facility, delay a payment, hedge.
""",
              "Fill the three-line table for the scenario you built in P5.1.",
              ["Present the difference, not two full sets.", "Profit, lowest cash, covenant headroom.", "End with what management could do."]),
        ], "check": [
            Q("Which is a well-formed scenario?", ["Bad year", "Largest customer pays 30 days later", "Everything down 20%"], 1, "One specific question, with a driver that can be explained."),
            Q("Which line of a scenario summary usually matters most for payment-term changes?", ["EBITDA", "Lowest cash balance", "Headcount"], 1, "Payment terms move cash much more than profit."),
        ]},
        {"code": "P6", "title": "Valuation", "lessons": [
            L("P6.1", "Inputs measured from the books", 8,
              "Build a valuation on the client's own data rather than on opinions.",
              """
Valuation sits in FP&A, under **Xplore, Valuation**. Its main difference from a spreadsheet valuation is where the inputs come from.

**Measured from the tenant:** DSO and DPO, customer concentration, churn, burn and runway, cash conversion. These come from the ledger, the invoices and the banks, so they can be traced.

**Market data:** risk premiums, country risk, betas and multiples come from free public datasets, by region (Europe, Global, US).

**Entered by the user:** the risk-free rate, with a dated suggested value, and the peer companies for comparables.

The earnings base always covers twelve months: trailing, or annualised from several months. A single month is never a basis for value.
""",
              "In your practice company, create a valuation case for the group and find which inputs were measured from the books.",
              ["Valuation is under FP&A, Xplore, Valuation.", "Operating inputs are measured from the tenant.", "Market data defaults; risk-free rate and peers entered."]),
            L("P6.2", "Projection and extrapolation", 7,
              "Know where projected cash flows come from and where they become guesses.",
              """
Projected cash flows come **from the budget, per company**. After the last budget year, K-φ extends the projection to five years at the budget's last growth and margins, and labels those years **extrapolated**.

The extrapolated years are an assumption. Say so when you present, and test how much of the value depends on them.

For groups, the **entity filter drives the valuation**. Multi-country groups are valued bottom-up by default, each company with its own risk; other groups are valued on the consolidated figures. A company that cannot be valued on its own stays in the filter: it cannot be unchecked.
""",
              "In your practice company, find which projection years are labelled extrapolated, and change one entity in the filter.",
              ["Cash flows come from the budget, per company.", "Years after the budget are extrapolated and labelled.", "The entity filter drives the valuation."]),
            L("P6.3", "Football field and the report", 6,
              "Reconcile methods into one range and present it carefully.",
              """
Each method (discounted cash flow, comparables and others) gives a range. The **football field** shows them side by side, with **weights you can edit**, and reconciles them into one value range.

A range is more honest than a single figure. Present it that way.

The printable **report** opens in its own window. It includes an assumptions and limiting conditions section. Read it before you send the report; it states what the valuation does and does not claim, and the client must agree with it.

A valuation is advice to the client's management, not a fairness opinion. Never present it as one.
""",
              "In your practice company, change the weights in the football field of your valuation case, save, and open the report.",
              ["Methods reconcile in a football field with editable weights.", "Present a range, not a point.", "Read the assumptions section before sending."]),
        ], "check": [
            Q("Where does DSO used in the valuation come from?", ["Management's estimate", "Measured from the tenant's data", "A public dataset"], 1, "Operating inputs are measured from the ledger, invoices and banks."),
            Q("Years after the last budget year are...", ["Left out", "Extended at the last growth and margins, labelled extrapolated", "Taken from a public dataset"], 1, "They are extrapolated and labelled so."),
        ]},
        {"code": "P7", "title": "Reporting", "lessons": [
            L("P7.1", "The board pack and why it calculates nothing", 5,
              "Use the board pack so its figures always match the app.",
              """
The board pack **calculates nothing of its own**. It picks statements, KPIs and forecasts from the app, as they are.

That is deliberate. If the board pack computed its own figures, they would drift from the screens over time, and someone would spend a meeting explaining why two numbers differ.

So when a board pack number looks wrong, the fix is never in the board pack. It is upstream: an import, a classification, a forecast rule. Fix it there, and the board pack follows.
""",
              "In your practice company, open the board pack and check that its EBITDA matches the KPI page.",
              ["The board pack only picks figures from the app.", "It always reconciles with the screens.", "Fix wrong figures upstream, never in the pack."]),
            L("P7.2", "Reconciling what you present", 5,
              "Make sure every figure you present ties to a source.",
              """
Before any figure leaves the team, tie it to something independent:

- **Revenue and net income** to the accounting system's own reports.
- **Cash** to the bank balances on the same date.
- **Receivables and payables** to the aged balances.

Write down what you tied and the difference found, even when it is zero. A one-page reconciliation note before each board meeting is cheap, and it is what an auditor or a new CFO will ask for.

If a difference stays unexplained, say so in the pack. An unexplained difference that is disclosed is a question; one that is found later is a credibility problem.
""",
              "In your practice company, tie the ledger's cash on 31 December 2025 to the bank balances on the same date, company by company.",
              ["Tie revenue, cash and balances to independent sources.", "Write down what you tied, even zero differences.", "Disclose differences you cannot explain."]),
        ], "check": [
            Q("The board pack shows the wrong EBITDA. Where do you fix it?", ["In the board pack", "Upstream: import, classification or rule", "In a spreadsheet"], 1, "The board pack calculates nothing; the cause is upstream."),
            Q("You cannot explain a small difference in cash before a board meeting. What do you do?", ["Adjust it", "Disclose it in the pack", "Leave it out"], 1, "Disclosed, it is a question; found later, it is a credibility problem."),
        ]},
    ],
    "exam": {
        "title": "Exam: statements, a gap in the books, a forecast version",
        "situation": "Your exam company is a fresh copy of Halden Trading: three companies, the ledger to September 2026, banks and invoices. One company's month never reached K-φ.",
        "tasks": [
            "Find the month of one company that is missing from the books. Download that company's full ledger file and import that month only: nothing may land twice.",
            "Produce the P&L for January to September 2026 for each company, and the balance sheet of Halden Trading Inc. on 30 September 2026.",
            "Create a budget named \"Forecast Q4\" from actuals.",
            "Submit net income for January to September 2026 for each company in its own currency, EBITDA for Halden Trading Inc., and its total assets on 30 September 2026.",
        ],
        "checks": [
            "Every company-month of the ledger matches the answer key, nothing twice",
            "Net income per company within half a percent",
            "EBITDA within 1%",
            "Total assets within half a percent",
            "A budget named Forecast Q4 exists",
        ],
        "report": [
            [
                "fail",
                "Ledger complete, nothing twice",
                "Halden Trading Ltd, 2024-11: too much (2,411,602.10 debits for 1,205,801.05); 21 more",
            ],
            [
                "fail",
                "Net income by company",
                "Not matching the answer key: Halden Trading Ltd",
            ],
            [
                "pass",
                "EBITDA",
                "Within 1% of the answer key",
            ],
            [
                "pass",
                "Balance sheet",
                "Total assets match",
            ],
            [
                "pass",
                "Forecast version",
                "Found \"Forecast Q4\"",
            ],
        ],
    },
}
