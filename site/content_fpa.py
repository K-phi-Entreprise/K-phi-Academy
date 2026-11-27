# FP&A course content.

def L(code, title, minutes, objective, read, try_, points, resources=None):
    d = {"code": code, "title": title, "minutes": minutes, "objective": objective, "read": read, "try": try_, "points": points}
    if resources: d["resources"] = resources
    return d

def Q(q, options, answer, why):
    return {"q": q, "options": options, "answer": answer, "why": why}

COURSE = {
    "id": "fpa", "code": "P", "title": "FP&A", "badge": "FP&A", "duration": "About 4 hours", "status": "available",
    "audience": "Controllers, FP&A analysts, consultants.", "prereq": "Agentic finance, MCP, Data foundation",
    "summary": "From ledger to statements, KPIs, budgets, forecasts, scenarios and valuation you can defend.",
    "outcomes": [
        "Produce statements and KPIs from the ledger and explain every figure.",
        "Run budget versus actuals and build forecasts with explicit, versioned rules.",
        "Build a scenario and present what moves in profit, cash and covenant headroom.",
        "Produce a valuation whose inputs are measured from the client's own books.",
    ],
    "lab": "Practise in your own practice company, a copy of Halden Trading, which opens set up: three companies, 23 months of ledger, and the budget and forecasts you build from it.",
    "chapters": [
        {"code": "P1", "title": "From ledger to statements", "lessons": [
            L("P1.0", "Versions: one per closing", 6,
              "Know which closing you are looking at, and go back to any earlier one.",
              """
In K-φ **a version is a closing**: 2026-09 is the September 2026 close. Each month you close is kept as a version, and a version holds everything as it stood at that close: the ledger, the statements, the forecast made from it, the KPIs. That gives you three things:

- **Keep track.** Each close adds a version; the earlier ones stay.
- **Freeze.** What you presented for June stays as presented, whatever is booked afterwards.
- **Go back.** Pick an earlier version and you see the situation as it was: the cash at the end of June, what the forecast said then, the DSO then.

**Where you pick it.**

- **On the statements** (Balance Sheet, P&L, cash flow statement), the **Versions row** above the statement decides the columns. You can pick several closings at once and read them side by side: June beside September.
- **On the other pages** (KPIs, forecast, variance, exports), the **first box of the top bar** sets the closing you read "as of". On a statement, picking a closing there that is not already in the Versions row replaces the columns with that one closing.

The app opens on the latest closing. Most mistakes in a review come from reading the wrong version, so say it out loud in a meeting: "these are the figures at the September close".

Budgets have versions of their own, which are a different thing: lesson P3.1 covers them.
""",
              """In your practice company, go back to the June 2026 close and read the cash as it was then.
1. In the menu on the left, under FP&A > Statements, open Balance Sheet.
2. Any company will do, or the whole group: the lesson is about versions. ENTITIES in the top bar says which one you are reading.
3. Above the statement, the Versions row shows the closings; 2026-09, the September close, is selected. Read the line Total Cash & Cash Equivalents.
4. In the Versions row, click 2026-06: the June close appears as a column beside September.
5. Read Total Cash & Cash Equivalents in the 2026-06 column and type it below.""",
              ["A version is a closing, kept as it stood.", "Statements: the Versions row, several closings side by side.", "Other pages: the first box of the top bar sets the closing."]),
            L("P1.1", "P&L year to date, cumulative balance sheet", 7,
              "Read K-φ's statements the way they are built.",
              """
K-φ builds the statements from the ledger lines you imported, using each account's classification.

Two rules hold everywhere:

- **The P&L restarts at zero at the start of each fiscal year.** A P&L for May shows January to May (for a calendar fiscal year). This is the rule, not a setting.
- **The balance sheet is cumulative.** It shows balances at a date, built from everything booked up to that date.

The same selectors as everywhere else apply: entity, business unit and third party (both optional), currency, units. A group view brings the entities together in the reporting currency chosen in the top bar; each entity's own view stays in its own currency.

Before presenting a statement, check that the balance sheet balances for each entity and that net income, less distributions, matches the movement in retained earnings for the year. If either fails, look at the classification of accounts before anything else.
""",
              """In your practice company, read Halden Trading Ltd's net revenue twice: year to date, then March alone.
1. In the menu on the left, under FP&A > Statements, open P&L Statement.
2. In the top bar, open ENTITIES, click None, then tick Halden Trading Ltd.
3. In the first box of the top bar, pick 2026-03: the P&L shows that closing alone (lesson P1.0).
4. In the top bar, click Company next to Group: the amounts change from USD, the group's currency, to GBP, the company's own.
5. Basis shows YTD, as the P&L opens: the Net Revenue line (sales less discounts, accounts 4000 and 4900) is January to March. Type it in the first box below.
6. Click Incremental next to YTD: the same line now shows March alone. Type it in the second box.
7. Last, switch ENTITIES back to all three companies and click Group: the group view adds them up in USD.""",
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
              """In your practice company, drill from the group's operating expenses for September 2026 down to the ledger lines, then do the same for Halden Trading Inc. alone.
1. Open P&L Statement (FP&A > Statements). It opens on the September 2026 close, 2026-09.
2. The operating expenses are the lines under Gross Profit: Personnel Expenses, Sales & Marketing, IT & Software and the rest. The cost of goods sold (account 5000) sits above Gross Profit and is not one of them.
3. Click the ▶ next to an account to drill down.
4. In ENTITIES, click None, then tick Halden Trading Inc. Find its largest operating expense account and type its name or number below.""",
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
              """In your practice company, follow Halden Trading Ltd's profit from the P&L to the balance sheet, at September 2026.
1. Open P&L Statement (FP&A > Statements). In the top bar: ENTITIES, click None, tick Halden Trading Ltd; check the statement shows the September 2026 close, 2026-09; click Company to read GBP.
2. Keep Basis on YTD. The last line, Net Income, is January to September 2026. Type it in the first box below.
3. Open Balance Sheet (FP&A > Statements), same top bar. Under Equity, read the line Retained Earnings (Net Income). Type it in the second box.
4. Compare. The balance sheet line is larger: it holds every profit not yet closed into account 3200, Retained Earnings. Halden has not booked a year-end closing for 2025, so 2025's profit is still in it. Nothing was distributed, so all of it is retained.""",
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

K-φ's definitions are the defaults, and some can be adjusted: DSO, DPO and DIO use a three-month window, which you can switch to the latest month, six or twelve months; the benchmark industry can be changed too. If a client measures a KPI differently, say so before the meeting and set the window to match.
""",
              """In your practice company, read a DSO and the formula behind it.
1. In the menu on the left, under FP&A > Analyze, open Financial KPIs.
2. In the top bar, open ENTITIES, click None, then tick Halden Trading Inc.; the period box shows 2026-09.
3. Read the DSO tile, under the cash conversion cycle. The line under the figure is its formula: receivables divided by the annualized revenue, times 365, with the revenue averaged over 3 months (WINDOW: 3M, top right).
4. Type the DSO below. Then click Latest, 6M and 12M in WINDOW to see it move, and come back to 3M.""",
              ["About thirty KPIs, each with its formula and thresholds.", "Names are not standard; read the formula.", "DSO, DPO and DIO: three-month window by default, adjustable."]),
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
            L("P3.1", "Budget versions, approval and overlaps", 8,
              "Know which budget feeds the forecast, who approved it, and which one wins when two cover the same months.",
              """
A budget in K-φ is not a closing version (lesson P1.0). It is a plan for a fiscal year, and a client usually has several: Budget 2026, approved; Budget 2027, in draft; a revised 2027 made in June. Each one lives on its own and keeps its history.

**Approval workflow, per company.** Each company in a budget moves through three statuses: draft, submitted, approved. Submitting and approving are separate rights, so a controller can prepare and a CFO can approve. With segregation of duties switched on, whoever submitted a company's budget cannot approve it. Every step is logged with who and when, so "which numbers did the board approve?" has an answer.

**Which budget feeds the forecast.** Comparing budget against actuals works with any budget you pick. The forecast is different: it uses only the budgets you flag for it, with the star next to the budget's name on the Budget → Cash page. A flag covers a window of months (by default the budget's own year) and a set of companies.

**When two flagged budgets overlap.** Say Budget 2027 is flagged for January to December 2027, and the June revision, Budget 2027 R1, is flagged for July to December. For July to December, two budgets claim the same companies and months. K-φ does not choose for you:

- the Budget → Cash page shows a banner listing each conflict, company and month;
- until you pick, neither budget feeds that month;
- you click "Use Budget 2027 R1" (or the other) for that company and month, and that choice is kept.

The clean way to avoid conflicts is to end the old flag where the new one starts: Budget 2027 for January to June, R1 for July to December. One month, one company, one budget.
""",
              """In your practice company, find where budgets, their status and the forecast flag live.
1. In the menu on the left, under FP&A > Plan, open Budget → Cash. A new practice company has no budget yet: lesson P3.2 creates one.
2. Once a budget exists, its name shows in the bar at the top of the page, with its status: draft, submitted or approved.
3. Next to the name is a star. Hover it: "Flag as the budget to use for forecasting". A filled star means the forecast uses it.
4. If two flagged budgets ever cover the same company and month, the banner with the "Use …" buttons appears on this page.""",
              ["Budgets are plans per fiscal year, not closings.", "Draft, submitted, approved, per company, logged.", "Two flagged budgets on the same month: you pick which one wins."]),
            L("P3.2", "Creating a budget from actuals", 5,
              "Give a client without a budget a starting point in one step.",
              """
Many smaller clients have no formal budget. K-φ offers two things in that case.

- **A forecast from the recent run rate**, flagged clearly as an assumption, so the forecast is not empty. This is different from the projected new sales of lesson P4.3, which you add to a forecast on purpose.
- **One click to create a budget from actuals**, which copies the recent pattern into a new budget the client then adjusts.

The second is usually the better start. It gives the client figures they recognise, and every change they make is a decision they can explain.

**Seed from Actuals offers five ways to extend the history into the budget year.** All of them work per company and per line (revenue, cost of sales, payroll, rent and the other expenses, plus receivables, payables and stock), from the months in the ledger.

| Method | What it does | When to use it |
|---|---|---|
| **Linear** (default) | Measures the seasonality of each calendar month (that month's average revenue against the overall average), removes it, draws a straight trend line through the rest (least squares), projects it and puts the seasonality back. | A business growing or shrinking steadily, with a seasonal pattern. |
| **Flat** | Repeats the last twelve months as they were. | A mature business, or a neutral baseline the client then adjusts. |
| **YoY** | Measures the average growth of each month against the same month a year earlier and applies it to last year's months. Needs at least 13 months. | A clear yearly pattern with steady growth. |
| **Holt** | Smooths the level and the trend of the series, then lets the trend fade month after month so it does not run away; seasonality is put back. | Noisy history, where a straight line would overreact. |
| **AI** | Claude reads the history and the context you type (industry, headwinds, tailwinds, strategic target) and proposes the months. | When the client knows things the history cannot show: a launch, a lost contract. Review every line. |

Whichever method you pick, the result is a starting point: walk through it with the client line by line for the largest items: revenue, payroll, rent, major suppliers. The smaller lines can follow the pattern.
""",
              """In your practice company, create a budget from actuals and look at its first lines.
1. In the menu on the left, under FP&A > Plan, open Budget → Cash.
2. Click Seed from Actuals. Keep the name (Budget 2027) and the fiscal year, then OK.
3. Choose the extrapolation method (Linear is the default; the table above says what each does), keep the three companies, then OK: K-φ fills every month from the ledger and saves the budget.
4. It starts as a draft, the first step of its approval workflow (draft, submitted, approved). Press Check below.
5. Compare it with actuals for one entity and note the line you would adjust first.""",
              ["No budget: run-rate forecast, flagged as an assumption.", "Seed from Actuals: Linear, Flat, YoY, Holt or AI.", "Review the largest lines with the client."]),
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

Timing and error variances need no business action (errors need an accounting correction), but they must be named so nobody acts on them. Start with the largest variances in amount: the bridge at the top of the page shows which lines explain the gap in net income.
""",
              "In your practice company, run budget versus actuals for the group and find the largest variance.",
              ["Compare any version with actuals.", "Name the cause: volume, price, timing or error.", "Start with the largest variances."]),
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
            L("P4.0", "One forecast: GL to cash, then budget to cash", 8,
              "See how the ledger and the budget join into a single cash forecast, and where the handoff sits.",
              """
A K-φ cash forecast is one line of months built from two engines, joined at a **cutoff**.

| Zone | Months | Source |
|---|---|---|
| Actuals | up to the latest closing | the ledger, as booked |
| GL to cash | from the closing to the cutoff | the ledger's open balances and its recent pattern, through the flow rules |
| Budget to cash | after the cutoff | the flagged budget, through the budget cash rules (lesson P4.1) |

**GL to cash.** At the latest closing the ledger still holds money on its way: receivables to collect, payables to pay, accruals, tax due. The flow rules turn each balance into cash at its own timing: receivables by their DSO or their aging, payables by their DPO, payroll and tax on their schedule. That is the most reliable part of any forecast, because the amounts are already booked.

**The cutoff.** By default it sits three months after the latest closing: the month in progress, the next one, and one month of headroom so a late close does not hand months to the budget too early. With the September 2026 close, that is December 2026. On the forecast's cash flows chart the cutoff is a violet line you can drag, and a selector at the top (GL→Budget cutoff, Auto) sets it too.

**Budget to cash.** After the cutoff, the budget flagged for forecasting takes over, converted into cash by its own rules. With no budget, a banner says so: future purchases continue at the average of the last three closed months, as a stated assumption kept out of treasury exports, and new sales are projected only if you tick Project new invoices on the receivables rule (lesson P4.3).

**Why it stays alive.** Each month you import the ledger, a new closing appears (lesson P1.0). The actuals of that month replace the budget's assumption for it, the open balances are the new ones, and the cutoff moves forward with them. Nobody re-keys the forecast: it is rebuilt from the latest closing every time.
""",
              """In your practice company, find the three zones on the forecast.
1. In the menu on the left, under FP&A > Plan, open GL → Cash. A new practice company has no flow rules yet: click Global (15 rules) to create one rule per account family.
2. Open K-φ Forecast, just below. The chart is titled "Cash flows — drag the cutoff to set the GL→Budget handoff".
3. The bars before "today" are actuals. The shaded region after them is the forecast, and the violet dashed line marked Dec '26 is the cutoff.
4. Before the cutoff, the months come from the ledger (GL run-off). After it, from the budget; without one, the banner at the top says which assumption fills them.
5. Drag the violet line one month later, then set the selector GL→Budget cutoff back to Auto.""",
              ["Actuals, then GL to cash, then budget to cash.", "Cutoff: three months after the latest closing, draggable.", "Each closing replaces assumptions with actuals."]),
            L("P4.1", "Budgets: drivers, import from Claude, conversion to cash", 9,
              "Bring any client budget into K-φ, and see how it becomes future cash flows.",
              """
**A K-φ budget is driver-based.** You do not type a figure on every P&L line; you set the drivers and K-φ computes the lines:

| Category | Drivers |
|---|---|
| Revenue | revenue base, or price × volume per product line |
| Cost of sales | margin in %, plus a fixed part |
| Payroll | headcount × average salary, plus social charges and bonus |
| Operating expenses | rent, IT, marketing, travel, other |
| Below EBITDA | depreciation, interest and debt service, tax, capex |

Gross profit, EBITDA, operating income and net income are always computed, never typed.

**Main categories fixed, detail free.** The categories above, Revenue, Cost of sales, Payroll, Operating expenses, Depreciation, Financial, Tax, are the canonical structure: they are the same for every client, because K-φ needs to know what each amount is to turn it into cash. What sits under each one is the client's own: their product lines, their cost centres, their names. That is why any budget fits.

**Import it from Claude.** Clients rarely start from a blank page; they have a budget spreadsheet. Two ways bring it in, and both call the same engine functions:

- **Claude, through the K-φ connector (MCP).** Give Claude the spreadsheet and ask it to create the budget in K-φ. Claude reads it in any layout and any language, maps each line to its canonical category and keeps the detail underneath. It can preview first, without writing. The connector needs write access ("Allow write actions" when you connect it).
- **The Consultant inside K-φ** does the same from the app.

Every write is tagged with where it came from (Claude, the Consultant, the app) and recorded in the audit log. The new budget appears in Plan → Budget like any other, in draft.

**Then K-φ turns it into future cash flows.** Each cash-bearing category gets a cash rule, on the Flow Rules tab of Budget → Cash:

| Category | Becomes cash |
|---|---|
| Revenue | collected after the DSO |
| Cost of sales, operating expenses | paid to suppliers after the DPO |
| Payroll | salaries paid on their schedule |
| Interest, tax | paid on their schedule |
| Depreciation | no cash |

A category without a rule is flagged: its budget will not turn into cash until it has one. Once the rules exist, the budget's cash flows feed the forecast for the months after the cutoff.
""",
              """In your practice company, turn the budget of lesson P3.2 into cash rules.
1. In the menu on the left, under FP&A > Plan, open Budget → Cash, then the Flow Rules tab.
2. Read the alert: it lists the categories without a cash rule, whose budget will not convert to cash yet.
3. Click Generate rules: K-φ proposes one rule per category, with its timing (DSO, DPO or a schedule).
4. Check the list: Revenue collected after the DSO, Payroll on a schedule, Depreciation without cash.
5. Open the → Forecast tab to see the budget's cash flows month by month.""",
              ["Budgets are driver-based; subtotals are computed.", "Canonical categories fixed, detail free: any budget fits.", "Import with Claude (MCP) or the Consultant; rules turn it into cash."]),
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
            L("P4.3", "Flow rules: generate them, then fit each one", 12,
              "Create the rules that turn the ledger into cash, and choose the right timing for each flow.",
              """
**No rules, no forecast.** GL to cash (lesson P4.0) runs on flow rules: one rule per family of accounts, saying in which direction cash moves and when. Without them, the forecast page shows "No flow rules — no forecast": K-φ would rather show nothing than guess.

**Generate them.** On GL → Cash, Auto-generate rules proposes a full set from the chart of accounts:

- **Global**: one rule per account family, for all companies. The usual start.
- **Per Entity**: one set per company, when they collect or pay differently.
- **Per BU**, **Per Entity×BU**: the same, by business unit.

Each proposal carries a confidence: 0.9 when its parameter was measured from your ledger, 0.7 when the account was identified but the parameter not measured, 0.5 for a generic default to review. Rules belong to the version you are editing (lesson P1.0): change them at the September close and earlier closings keep their own.

**Then fit each one.** The timing decides when cash moves:

| Flow | Timing that fits | Why |
|---|---|---|
| Receivables, payables | **Aging buckets** (0-30, 31-60, 61-90, 91-120, 120+), or **DSO / DPO** | Aging gives each age band its own collection and bad-debt rate; DSO or DPO is one figure measured from the ledger |
| Salaries | **Fixed interval** (every 14 days for biweekly, 30 for monthly) or **Schedule** | Payroll goes out on known dates |
| Loans, rent, tax instalments | **Schedule**, monthly or quarterly | Contractual dates and amounts |
| Capex, supplier purchases | **Historical run-rate** | No date to follow: the average of recent months is the honest guess |
| Stock | **DIO** | Purchases follow the stock you keep, not only what you sell |
| Income tax | **Custom formula** (on EBIT, with the effective rate) | Tax follows profit, not a calendar alone |
| Depreciation | **Non-cash** | It reduces book value, never the bank |

**Check the coverage.** Above the table, the coverage bar counts the cash categories with a rule, and lists the missing ones with a → Fix button that proposes the right rule. Warnings say when a rule looks under-sized against history, for example collections far below past months.

**One detail: projected new sales.** The receivables rule collects what is already on the books. With no budget, new invoices are projected only if you tick **Project new invoices** on it. It is off by default because it is an assumption, and it applies to every receivables rule at once. When you turn it on, say so to whoever reads the forecast.
""",
              """In your practice company, create Halden's rules and fit two of them. Halden pays salaries once a month, and its capex has no schedule.
1. In the menu on the left, under FP&A > Plan, open GL → Cash. The page lists the cash categories without a rule.
2. Next to "Auto-generate rules", click Global. Read the table: receivables (110) and payables (200) get aging buckets, salaries (600) a fixed interval of 14 days, other expenses 30 days.
3. Click the row of 600, Salaries & Wages, and set Days to 30.
4. The coverage still lists CapEx & Asset Acquisitions (accounts 1500 and 1510). Click → Fix next to it, keep Historical run-rate, then Save Rule.
5. Press Check below.""",
              ["No rules, no forecast: generate them with Global.", "Fit each timing: aging or DSO/DPO, intervals, schedules, run rate.", "Project new invoices: off by default, an assumption to state."]),
            L("P4.4", "Exporting the forecast to a TMS or a file", 8,
              "Send the forecast where treasury works: liquidity entries for a TMS, or a file.",
              """
A forecast is only useful where treasury works. K-φ turns it into **liquidity entries**, the lines a treasury management system (TMS) such as Kyriba imports: a liquidity plan, a company, a budget code, an amount, a due date.

**Three steps, on the K-φ Forecast's Export to TMS tab.**

| Step | What you do |
|---|---|
| Choose the lines | tick the forecast lines to send: collections, payments, payroll, tax, interest, or the net cash flow |
| Give each line its code | the budget code your TMS knows it by; K-φ proposes one (AR, PAYROLL, FUNDING), you type your own |
| Generate Entries | one entry per line and month; months at zero are left out |

A line can go **rolled up**, one entry per month, or **in detail**: click its chevron and it sends one entry per component (per account family or rule), each with its own code. The totals are the same either way. The **Liq. Plan** field is the liquidity plan identifier your TMS reads from the file; left blank, it is the current month.

**The Forecast List is the outbox.** Generated entries land there, with the scenarios you send from Simulate (Generate Forecast List). Filter by date, tick rows, then:

- **Download** gives the TMS file. **⚙ Format** sets its columns, separator and line endings, and **Value Mapping** translates codes, so the file fits your TMS's import template.
- **K Upload** sends the entries straight to Kyriba and runs its process template, when the TMS connection is set up.
- Each entry keeps its source (forecast from actuals, or a scenario) and whether it was exported.

**What never leaves.** An assumption is not a forecast: when there is no budget, the purchases K-φ continues at the run rate are shown on screen but **left out of treasury exports**. With Global rules, the entries are the group's; rules per company give one forecast per company.

For a file rather than a TMS, **Export** at the top of the K-φ Forecast downloads the page as Excel or CSV.
""",
              """In your practice company, send the forecast to the Forecast List.
1. If the forecast has no rules yet, open GL → Cash and click Global next to "Auto-generate rules" (lesson P4.3).
2. Open K-φ Forecast and click Export to TMS at the top.
3. Tick Collections (AR), Payments (AP) and Payroll & Benefits. Keep the codes K-φ proposes, or type your own.
4. Click Generate Entries: the entries appear below, one per line and month.
5. Click Forecast List: the same entries, ready to Download or upload. Click ⚙ Format to see the columns of the file.""",
              ["Export to TMS: lines, budget codes, Generate Entries.", "The Forecast List is the outbox: Download or upload to the TMS.", "Run-rate assumptions never reach a TMS."]),
        ], "check": [
            Q("In the forecast, where do the figures of a month after the cutoff come from?",
              ["The ledger's open balances, run off by the flow rules", "The budget flagged for the forecast, turned into cash by its cash rules", "Always the run rate of the last three months"], 1,
              "Up to the cutoff the ledger feeds the forecast (GL to cash); after it, the flagged budget does (budget to cash). The run rate only fills in when there is no budget."),
            Q("Your latest closing is September 2026. Where does the cutoff sit by default?",
              ["September 2026", "December 2026", "December 2027"], 1,
              "Three months after the latest closing: the month in progress, the next one, and one month of headroom so a late close does not hand months to the budget too early. You can drag it."),
            Q("The October 2026 ledger is imported. What happens to the forecast?",
              ["Nothing until someone re-keys it", "October's actuals replace the budget for October, the run-off restarts from the new balances and the cutoff moves to January", "The budget is overwritten by the actuals"], 1,
              "A new closing appears (lesson P1.0). The forecast is rebuilt from it: actuals where they exist, then the ledger's balances, then the budget. The budget itself stays as approved."),
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
            L("P6.1", "Valuation cases, methods and drivers", 10,
              "Build several valuations of the same company, and know what drives each figure.",
              """
**Several cases, side by side.** A valuation in K-φ is a **case**: a name, a valuation date, a currency and its inputs. You can keep as many as you need on the same company: a base case, an investor's view with a higher risk premium, an exit at a lower multiple. **Duplicate** copies a case so you change one assumption and keep the other intact; the Cases menu lists them all.

**Two families of methods, reconciled.**

- **Discounted cash flows (DCF).** The free cash flows of the projection (below), discounted at the WACC, plus a terminal value: perpetual growth or an exit multiple.
- **Comparables.** Your company's metric times the peers' multiple, low, median and high: EV/Revenue, EV/EBITDA, EV/EBIT and P/E. An illiquidity discount applies when the peers are listed and the company is not.
- **Reconciliation.** By default DCF counts 50% and the comparables' average 50%, or DCF alone when there are no peers. You can change the weights; they must add up to 100%.

Every method goes from enterprise value to equity value through the same bridge (net debt and the other adjustments), then per share.

**The drivers of the DCF.**

| Driver | Made of |
|---|---|
| Cash flows | base revenue and EBITDA margin from the books, growth per year, D&A, capex and working capital as % of revenue, tax |
| Cost of equity | risk-free rate + beta × equity risk premium + size, country and specific premiums |
| Beta | the industry's unlevered beta, relevered with the company's debt-to-equity and tax rate |
| Cost of debt | the pre-tax rate, after tax |
| WACC | cost of equity and cost of debt, weighted by equity and debt |
| Terminal value | growth after the last year, or an exit multiple |

**Where the cash flows come from.** With a budget, the projection is the budget, company by company, read through the K-φ forecast. After the last budget year it runs on to five years at the budget's last growth and margins, and those years are labelled **extrapolated**: say so when you present, and test how much of the value rests on them. Without a budget, the case projects from the ledger: twelve months of revenue and EBITDA margin, then your growth, capex and working capital drivers.

For a group, the **entity filter drives the valuation**. Multi-country groups are valued bottom-up by default, each company with its own country risk; other groups are valued on the consolidated figures.

**Where the inputs come from.** Operating inputs are **measured from the books**: DSO and DPO, customer concentration, churn, burn and runway, cash conversion, each with its source. Risk premiums, country risk, betas and multiples come from free public datasets by region. You enter the risk-free rate (a dated value is suggested) and the peers.

**What moves the value most.** The Value menu shows a sensitivity grid, WACC against terminal growth (or exit multiple), and flags the usual traps: terminal growth above 4%, comparables and DCF more than 30% apart, no illiquidity discount on a private company.
""",
              """In your practice company, build two cases and see what moves the value.
1. Open Valuation, under Xplore. In New case, name it Base, pick a country and an industry (they set the risk premiums, beta and multiples), then click Create and read the ledger.
2. In the Inputs panel on the right, read the cost of capital line by line: risk-free rate, equity risk premium, beta, the premiums, the cost of debt.
3. In Value, read the sensitivity grid: how much one point of WACC or of terminal growth changes the equity value.
4. Click Duplicate: it opens "Base (copy)", your investor view. Set Company-specific premium to 2 and click Recompute. Compare its equity value with Base (All cases, then open Base).""",
              ["Several cases on one company: compare the views.", "DCF and comparables, reconciled 50/50 by default.", "WACC and terminal value drive the DCF; see the grid."]),
            L("P6.2", "Value over time: what moved it", 8,
              "Keep the valuation live from the books, and explain each change in value.",
              """
A valuation done once a year is out of date the month after. In K-φ a case is read from the books, so it can follow the company.

**Update at each close.** After a closing, **Update from the books** reads the ledger and the forecast again: revenue, EBITDA, net debt and the measured inputs. **Recompute** values the case. The value is recorded once a day, so the **Value over time** card on the Value menu draws the line of the reconciled value, with its range as a band.

**The value walk.** Between two points, K-φ explains the change step by step. It swaps one group of inputs at a time from the earlier state to the later one and values the case after each swap:

| Step | Who moved it |
|---|---|
| Operating performance (EBITDA, cash flows) | management |
| Working capital | management |
| Net debt and bridge items | management and financing |
| Market multiples | the market |
| Cost of capital and terminal assumptions | the market and you |
| Method weights | you |

The steps add up to the total change. This is the key value: it separates the value management created from what the market did. "Equity value rose 4 million, 3 of them from EBITDA and working capital, despite higher rates" is a sentence a board remembers.

**Sign off with Lock.** A locked case never changes; duplicate it to continue. The Home page's Valuation tile shows the most recent locked value, so everyone reads the figure that was signed off, not a draft.
""",
              """In your practice company, sign off a value.
1. Open your Base case and, in Value, find the Value over time card: one point so far, today's.
2. Click Lock and confirm. The case can no longer change.
3. Open Home: the Valuation tile shows Base's value, without "draft".
4. Click Duplicate on Base to keep working; next month, Update from the books on the copy and read the walk.""",
              ["Update from the books at each close; the value is recorded.", "The walk splits the change: management, market, method.", "Lock signs off a value; the Home tile shows it."]),
            L("P6.3", "Football field and the report", 6,
              "Reconcile methods into one range and present it carefully.",
              """
Each method (discounted cash flow, comparables and others) gives a range. The **football field** shows them side by side, with **weights you can edit**, and reconciles them into one value range.

A range is more honest than a single figure. Present it that way, and say which years of the projection are extrapolated.

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
            L("P7.1", "The board pack: built once, ready at every close", 7,
              "Set up the board pack once, so it is ready every month without rebuilding it.",
              """
A board pack in K-φ is a **report you set up once**. Each month it is rebuilt from the latest closing, with the same sections in the same order, so the board reads the same document every time.

**What goes in it.** In Reports, a Board Pack has eleven sections you switch on or off:

| Section | What it shows |
|---|---|
| Risks & Recommendations | risk flags and advice written from the figures: leverage, stock days, DSO, cash conversion |
| P&L with Variances | the closing against budget and against the prior period |
| Balance Sheet Snapshot | key lines, working capital, net debt |
| Cash Flow Summary | operating, investing, financing |
| KPI Dashboard | margins, DSO and DPO, ratios, trends |
| Covenant Compliance | each covenant with its headroom, green, amber or red |
| Cash Position | balances and liquidity |
| Forecast & Outlook | the year's projection and the rolling forecast |
| Forecasted P&L, B/S, CFS | last month through three months ahead |

**Consolidated or by entity.** Consolidated gives the group. *Consolidated + by entity* adds one pack per company (its own P&L, balance sheet, cash flow and cash, in its own figures). *By entity only* drops the group.

**When it runs.** Manual runs it when you click Run. *On Period Close* runs it by itself each time a period is closed in Financial Close, so the pack of the month is ready when the close is done. *Scheduled* and *On Validation* are the other two triggers.

**Where it goes.** Run shows it on screen; PDF and PPTX export it for the board, CSV for a spreadsheet. Its figures are the app's own: the same as the statements and the KPI page, so a wrong figure is fixed where it comes from, never in the pack.
""",
              """In your practice company, set up a board pack that is ready at every close.
1. In the menu on the left, under REP, open Reports, then click + New Report.
2. Give it a name, and under Statement type pick Board Pack. Keep the eleven sections.
3. Under Breakdown by entity, pick Consolidated + by entity.
4. Under Schedule & triggers, pick On Period Close.
5. Click Save Report, then Run, and look at the pack: Risks & Recommendations first, then the statements. PDF and PPTX are at the top right.
6. Press Check below.""",
              ["Set it up once: sections, entities, versions.", "On Period Close: ready when the close is done.", "Same figures as the screens; PDF and PowerPoint."]),
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
              "In your practice company, tie the ledger's cash on 31 December 2025 to the bank balances on the same date, company by company, each in its own currency (click Company in the top bar; Group shows everything in the group's USD).",
              ["Tie revenue, cash and balances to independent sources.", "Write down what you tied, even zero differences.", "Disclose differences you cannot explain."]),
        ], "check": [
            Q("The board pack shows the wrong EBITDA. Where do you fix it?", ["In the board pack", "Upstream: import, classification or rule", "In a spreadsheet"], 1, "The board pack calculates nothing; the cause is upstream."),
            Q("You cannot explain a small difference in cash before a board meeting. What do you do?", ["Adjust it", "Disclose it in the pack", "Leave it out"], 1, "Disclosed, it is a question; found later, it is a credibility problem."),
        ]},
    ],
}
