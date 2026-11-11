# Cash course content.
from content_fpa import L, Q

COURSE = {
    "id": "cash", "code": "C", "title": "Cash", "badge": "Cash", "duration": "About 4 hours", "status": "available",
    "audience": "Treasurers, cash managers, consultants.", "prereq": "Foundation, AI for finance",
    "summary": "Bank structure, categorisation, the cash position, receivables and payables, the cash forecast and payment controls.",
    "outcomes": [
        "Organise bank accounts by entity and by pool, the way treasury reads them.",
        "Categorise transactions so the position and forecast mean something.",
        "Manage receivables and payables, including intercompany, and reconcile them.",
        "Build a cash forecast from banks, invoices and the budget, and spot funding needs early.",
    ],
    "lab": "Practise in your own practice company, a copy of Halden Trading: six bank accounts with eleven months of statements, open invoices, and the ledger behind them.",
    "chapters": [
        {"code": "C1", "title": "Bank structure", "lessons": [
            L("C1.1", "Accounts by entity and by pool", 7,
              "Set up the account structure treasury actually reads.",
              """
Bank accounts arrive from bank connections or files. Before anything else, give them a structure.

- **By entity.** Every account belongs to one legal company. This is what auditors and banks read.
- **By pool.** Accounts managed together, for example all GBP accounts swept into one, form a pool. This is how the treasurer reads cash day to day.

The same account appears in both views. Choose names people recognise: "HSBC GBP main" says more than an account number.

Accounts held with payment providers are shown apart from bank accounts. They are not part of the bank account list, so they never inflate the bank position by mistake.
""",
              "In your practice company, check which entity each bank account belongs to.",
              ["Every account belongs to one entity.", "Pools group accounts managed together.", "Payment-provider accounts stay out of the bank list."]),
            L("C1.2", "Header accounts and reserves", 6,
              "Model cash pools with a header account.",
              """
In a pool, one account often acts as the **header**: the account that receives the sweeps or funds the others, and holds the reserve.

Set the header so that:

- the pool's balance reads at a glance on the header line;
- transfers between the header and the other accounts are categorised as internal movements, never as income or spending;
- funding needs show on the account that will actually be drawn.

Ask the treasurer how the pool works in practice: zero-balancing at day end, target balances, or manual transfers. The setup should follow what the bank actually does.
""",
              "In your practice company, look at how accounts are grouped, and decide which one you would make the header of a pool.",
              ["A header account holds the pool's reserve.", "Transfers inside a pool are not income or spending.", "Follow how the bank actually sweeps."]),
            L("C1.3", "Daily balances and history", 5,
              "Use stored balances to answer questions about the past.",
              """
K-φ stores each account's balance **day by day**. That lets you rebuild the position on any past date, which is what you need for:

- month-end reconciliation with the ledger;
- checking a covenant that is tested on cash at a date;
- explaining to a CFO what happened in a given week.

When a bank connection is renewed after a gap, check that the missing days were filled. A gap shows as a flat line in the chart, which is easy to mistake for a quiet week.
""",
              "In your practice company, read the group position on 31 January 2026.",
              ["Balances are stored daily.", "Any past position can be rebuilt.", "Check for gaps after a connection is renewed."]),
        ], "check": [
            Q("Why are payment-provider accounts kept out of the bank account list?", ["They are not real accounts", "So they never inflate the bank position by mistake", "Banks require it"], 1, "They are shown apart so the bank position stays what it says."),
            Q("A transfer from a pool's header to another pool account is...", ["Income", "Spending", "A movement inside the pool"], 2, "It changes neither the pool's total nor the group's."),
        ]},
        {"code": "C2", "title": "Transactions", "lessons": [
            L("C2.1", "Categorisation rules", 7,
              "Categorise most transactions automatically, and correctly.",
              """
A cash position is only useful when transactions carry a **category**: customer receipts, supplier payments, payroll, tax, financing, intercompany.

Rules do most of the work. A rule matches on what a bank line contains (counterparty, reference, amount pattern) and assigns a category.

Write rules from the largest flows down:

1. Payroll and tax, which repeat and are easy to match.
2. The ten largest customers and suppliers.
3. Financing: loan repayments, interest, facility drawings.
4. Intercompany flows, matched on the group companies' names and accounts.

A good set of rules categorises most lines. The rest goes to review.
""",
              "In your practice company, open the transactions and find three that a payroll or tax rule would catch.",
              ["Categories make the position readable.", "Rules match counterparty, reference or pattern.", "Start with the largest, most regular flows."]),
            L("C2.2", "Reviewing what remains", 5,
              "Keep uncategorised transactions at zero.",
              """
What the rules miss goes to **review**. Review it on a fixed rhythm, daily or weekly depending on volume.

For each line, decide:

- **Categorise it once** if it is a one-off.
- **Write or adjust a rule** if it will come back.

Track the number of uncategorised lines. It should trend to zero and stay there. An "Other" category that keeps growing is a review that is not happening.
""",
              "In your practice company, find the transactions without a category and decide, for each, one-off or rule.",
              ["Review on a fixed rhythm.", "One-off: categorise; recurring: write a rule.", "A growing \"Other\" means review is not happening."]),
            L("C2.3", "Intercompany movements", 7,
              "Stop intercompany flows from inflating the group position.",
              """
When Halden Trading Inc. pays Halden Trading Ltd, the money leaves one group account and arrives in another. For the group, nothing happened.

If both sides are categorised as ordinary receipts and payments, the group view shows money coming in and going out that never left the group. Totals of receipts and payments are inflated, and a forecast built on them is wrong.

So:

- **Categorise both sides as intercompany.**
- **Match them**: same amount (after conversion when the two accounts are in different currencies), close dates, the two group companies as counterparties.
- **Check timing**: a transfer that leaves on the 30th and arrives on the 2nd sits in neither account at month end. Note it as cash in transit.
""",
              "In your practice company, find one transfer between two group companies and check how both sides are categorised.",
              ["For the group, intercompany is neither income nor spending.", "Categorise and match both sides.", "Note cash in transit at period end."]),
            L("C2.4", "Rule suggestions with an assistant", 6,
              "Use an assistant to propose categorisation rules, and review them before they run.",
              """
Writing categorisation rules is repetitive: look at uncategorised lines, find a pattern, write a rule. An assistant is good at finding the patterns.

Export the uncategorised lines (or let a connected assistant read them through K-φ) and ask:

> Here are bank lines that have no category. Group them by pattern (counterparty, reference, amount). For each group, propose a rule and a category from this list: customer receipts, supplier payments, payroll, tax, financing, intercompany, other. Show three example lines per rule and say which lines no rule covers.

Then review before any rule runs:

- **Too broad?** A rule matching "PAYMENT" in the reference will catch half the bank.
- **Intercompany** must match group companies only (lesson C2.3).
- **Payroll and tax** lines may hold personal data; share only what the task needs (lesson A4.1).

You create the rules in K-φ yourself, after review. The assistant proposes; the rules you approve are what run.
""",
              "Export a few uncategorised bank lines you have, ask your assistant for rule proposals with the prompt above, and reject one that is too broad.",
              ["The assistant finds patterns and proposes rules.", "Review breadth, intercompany and personal data.", "You create the rules after review."]),
        ], "check": [
            Q("Which flows should rules cover first?", ["The rarest ones", "The largest and most regular", "Card payments"], 1, "Payroll, tax and the largest counterparties cover most of the volume."),
            Q("Both sides of an intercompany transfer are categorised as customer receipt and supplier payment. What is wrong in the group view?", ["Nothing", "Receipts and payments are both inflated", "The bank balance is wrong"], 1, "Money that never left the group shows as coming in and going out."),
        ]},
        {"code": "C3", "title": "Cash position", "lessons": [
            L("C3.1", "The cash worksheet", 7,
              "Read the position by entity, account, category and period.",
              """
The **cash worksheet** shows a chart on top and a pivot-style report below. You choose the rows and columns: entity, account, pool, category, and period (day, week, month).

Typical questions it answers:

- Where is our cash today, by entity and currency?
- What came in and went out last week, by category?
- Which account is trending down?

The chart always shows today's date, so actuals and forecast are clearly separated.

Agree with the treasurer on the two or three views used every week, and use the same ones each time, so the numbers are comparable from one week to the next.
""",
              "In your practice company, open the cash worksheet and set entities in rows, weeks in columns.",
              ["Chart on top, pivot-style report below.", "Rows and columns are yours to choose.", "Use the same weekly views every time."]),
            L("C3.2", "Presenting the position", 5,
              "Give management the position in three lines.",
              """
Management rarely wants the worksheet. It wants three things:

1. **Cash today**, by entity and in total, in one currency.
2. **What changed** since the last report, and why: the two or three largest movements.
3. **What is coming**: the lowest point in the next weeks, and when.

Use the same layout every time, so the reader learns where to look. State the exchange rates and their date when you convert currencies.
""",
              "In your practice company, write the three-line position for the group as of the last statement date, 31 October 2026.",
              ["Cash today, what changed, what is coming.", "Same layout every time.", "State exchange rates and their date."]),
        ], "check": [
            Q("What separates actuals from forecast on the worksheet chart?", ["The colour of the bars", "Today's date", "Nothing"], 1, "The chart always shows the real current date."),
            Q("What does management need first from a cash report?", ["The full worksheet", "Cash today, what changed, what is coming", "Every transaction"], 1, "Three lines, in the same layout each time."),
        ]},
        {"code": "C4", "title": "Receivables and payables", "lessons": [
            L("C4.1", "One data model with FP&A", 6,
              "Use the same entities, business units and third parties for invoices as for the ledger.",
              """
Invoices share FP&A's data model. The same top-bar selectors apply: entity, business unit, third party, currency, units.

One point needs care: **payer and payee swap** between receivables and payables.

- In a **receivable**, our entity is the payee; the third party pays us.
- In a **payable**, our entity is the payer; we pay the third party.

Because the third party is the same object in the ledger and in the invoices, you can go from a DSO to the customers behind it, and from a supplier's invoices to its ledger account.
""",
              "In your practice company, filter the receivables on one customer, then open that customer in FP&A.",
              ["Invoices use the same selectors as FP&A.", "Payer and payee swap between AR and AP.", "Third parties link invoices and ledger."]),
            L("C4.2", "Direction and intercompany rules", 7,
              "Know how K-φ decides whether a document is a receivable, a payable or intercompany.",
              """
When an invoice file names two parties, K-φ decides the direction:

- A **group company being paid** makes it a **receivable**.
- A **group company paying a third party** makes it a **payable**. If that third party does not exist yet, it is created.
- If **both parties are group companies**, the document is **intercompany**.

Intercompany invoices matter twice: they must not count in group receivables and payables, and they explain intercompany bank flows (lesson C2.3).

When the direction looks wrong, check the parties' names first. A group company spelled differently in the file is the most common cause.
""",
              "In your practice company, find invoices between two group companies and check they are flagged intercompany.",
              ["Group company paid: receivable. Group company paying: payable.", "Both parties in the group: intercompany.", "Wrong direction usually means a name mismatch."]),
            L("C4.3", "Import mappings", 5,
              "Handle files from any system, and teach K-φ once.",
              """
Invoice files come in many formats, from different accounting systems. K-φ accepts varied exports and maps their columns to its own fields.

When neither party in a document is recognised, a **mapping to a group company is missing**. The import asks which company it is, once, and remembers the answer for the next import.

Review those questions carefully on the first import. A wrong answer is remembered too, and it will send every later document from that source to the wrong company.
""",
              "Take an invoice export you have and list which parties a first import would ask you to map.",
              ["Varied export formats are accepted.", "Unknown parties: the import asks once and remembers.", "A wrong answer is remembered too; check the first import."]),
            L("C4.4", "Reconciliation and tolerances", 6,
              "Match payments to invoices and see what is still open.",
              """
The receivables and payables ledgers show, for each invoice, its **status**, the **date it was paid**, and whether it is **reconciled** with a bank movement.

Matching follows a **tolerance**, set in percent or as an amount, in the ledgers' match settings. A tolerance absorbs bank fees and small differences; too wide a tolerance matches the wrong payments.

A good starting point: a small fixed amount for bank fees, and no percentage until the client asks for one. Look at what remains unmatched each week; it is where disputes and errors hide.

You match customer receipts to invoices from the receivables ledger, not from the payments screen.
""",
              "In your practice company, find the oldest open receivable of Halden Négoce SAS and note how many days it is overdue.",
              ["Each invoice shows status, paid date and reconciliation.", "Tolerance in percent or amount; keep it narrow.", "Review what remains unmatched each week."]),
        ], "check": [
            Q("Halden Trading Ltd pays Halden Négoce SAS for goods. What is the document?", ["A receivable", "A payable", "Intercompany"], 2, "Both parties are group companies."),
            Q("You answered a mapping question wrongly on the first import. What happens next time?", ["K-φ asks again", "The wrong answer is reused", "The import fails"], 1, "Answers are remembered, so check them on the first import."),
        ]},
        {"code": "C5", "title": "Cash forecast", "lessons": [
            L("C5.1", "What the forecast combines", 7,
              "Know every input of the cash forecast.",
              """
The cash forecast brings together:

- **Bank balances and transactions**, the starting point;
- **Open receivables and payables**, with their due dates;
- **The FP&A budget and ledger**, mapped to cash categories;
- **Known movements** the treasurer types or pastes in: a tax payment, a loan repayment, a dividend. Each has a date, a signed amount and an account, and can repeat. When the other party is a group company, K-φ adds the mirror line in that company and keeps the two linked.

Each input covers a different horizon. Bank and invoices are precise for the coming weeks. The budget takes over further out.

The usual view for treasury is **13 weeks**, week by week: long enough to see a quarter-end, short enough to stay precise.

When a forecast surprises you, find which input drives the surprise before you change anything.
""",
              "In your practice company, open the cash forecast and identify which input drives the next four weeks.",
              ["Banks, invoices, budget and known movements.", "Invoices for the near term, budget further out.", "Find the driving input before changing anything."]),
            L("C5.2", "Category rules and versions", 6,
              "Keep the cash forecast reproducible.",
              """
Each cash category follows a **saved, versioned rule**: from open invoices, from the budget with a payment delay, a fixed amount, a schedule.

The same inputs always give the same forecast. When the forecast moves, either an input changed (a new bank statement, new invoices) or a rule changed. Both are recorded.

Keep one rule per category and write down why it was chosen. "Payroll: budget, paid on the 25th" is enough.
""",
              "In your practice company, change the rule for supplier payments and compare the forecast before and after.",
              ["Each category has one saved, versioned rule.", "Same inputs, same forecast.", "Write down why each rule was chosen."]),
            L("C5.3", "Funding needs and overdraft windows", 7,
              "Spot when an entity will run short, and for how long.",
              """
When an entity's forecast goes below zero, K-φ shows a **funding need**: an **overdraft window** with a start date and an end date. The end date can be open if the forecast never recovers.

For each window, the treasurer needs three answers:

1. **How much**, at the lowest point.
2. **From when to when.**
3. **How to fund it**: a transfer from another entity, a facility drawing, a delayed payment.

Look at funding needs by entity, not only for the group. A group in surplus can still have one company that cannot pay its suppliers.
""",
              "In your practice company, open Funding needs and note the first window, if there is one: entity, start, end, amount.",
              ["A funding need shows start and end dates.", "The end date can be open.", "Read funding needs per entity, not only for the group."]),
        ], "check": [
            Q("The group forecast is positive. Can an entity still have a funding need?", ["No", "Yes", "Only in another currency"], 1, "A group surplus does not pay one company's suppliers."),
            Q("What does an overdraft window with no end date mean?", ["A display bug", "The forecast never recovers within the horizon", "The overdraft is approved"], 1, "The need does not close inside the forecast horizon."),
        ]},
        {"code": "C6", "title": "Payments and controls", "lessons": [
            L("C6.1", "Payment runs and approvals", 6,
              "Pay suppliers from where the payables are.",
              """
Payments sit with payables: a **payment run** picks the invoices to pay, the beneficiaries and the account to pay from, then goes for **approval** and **signature**.

Paying a supplier invoice and moving cash between group companies use the same mechanism, with the same controls.

Before a run, check:

- the balance on the paying account, against the forecast;
- beneficiaries added or changed since the last run;
- invoices disputed or not yet approved.

Changed beneficiary details are the most common route for payment fraud. K-φ pays a new beneficiary, or one whose account changed, only 24 hours after another person approved it. Use that time: confirm the change by a call to a known number, not by replying to the email that asked for it.
""",
              "In your practice company, open Payments and note what has to be in place before a first payment run can be prepared, approved and signed.",
              ["Payment runs live with payables.", "Supplier payments and group transfers share one mechanism.", "Confirm changed bank details by phone."]),
            L("C6.2", "Two signers by default", 5,
              "Apply the payment control auditors look at first.",
              """
K-φ separates every step of a payment run, and enforces it in the system, not in a policy document:

- The person who **prepares** a run cannot approve it or sign it.
- The **approver** cannot sign it.
- The run is executed only after **two different signers**, each within their own **signing limit**. "No limit" does not exist: a signer without a limit cannot sign.
- A change to anyone's payment rights takes effect only when a **second administrator** confirms it.

The consequence is deliberate: a tenant with a single user cannot pay. Like a bank, it needs a second person.

Review who can sign, and their limits, each quarter, along with the roles review. A signer who has left the company is still a signer until someone removes them.
""",
              "In your practice company, open Payment rights and check that nobody can both prepare and sign.",
              ["Preparer, approver and two signers are four different people.", "Every signer has a limit; rights changes need a second admin.", "Review signers and limits every quarter."]),
        ], "check": [
            Q("A supplier emails new bank details. What do you do?", ["Update them", "Confirm by calling a known number", "Reply to the email to confirm"], 1, "Changed bank details are the most common fraud route."),
            Q("Maya prepared a payment run. What can she do with it?", ["Approve it", "Sign it", "Neither; others approve and sign"], 2, "The preparer can neither approve nor sign; the run needs an approver and two other signers."),
        ]},
    ],
    "exam": {
        "title": "Exam: position, invoices and forecast",
        "situation": "Your exam tenant is a fresh copy of Halden Trading, already set up: three entities, the ledger and budget, six bank accounts with three months of statements, and open receivables and payables.",
        "tasks": [
            "Organise the six accounts by entity, and create one pool for the two GBP accounts with the main account as header.",
            "Categorise all transactions. Nothing may stay uncategorised.",
            "Import the open invoices file. Make sure each document has the right direction and that intercompany documents are flagged.",
            "Build the 13-week cash forecast for the group.",
            "In the submission form, give the group cash position at the statement end date, the lowest forecast balance for Halden Négoce SAS and its week, and any funding need (start and end date).",
        ],
        "checks": [
            "Account grouping and pool structure",
            "Zero uncategorised transactions; category totals within tolerance",
            "Invoice directions and intercompany flags",
            "Forecast balances per entity per week within tolerance",
            "Submitted figures and dates",
        ],
        "report": [
            ["pass", "Accounts and pool", "Six accounts by entity; GBP pool with header set"],
            ["fail", "Categorisation", "Customer receipts 1,204,800 USD expected, 1,454,800 found. Both sides of a 250,000 USD intercompany transfer counted as ordinary flows"],
            ["pass", "Invoice directions", "All directions right; 4 intercompany documents flagged"],
            ["pass", "13-week forecast", "Within tolerance for all entities"],
            ["pass", "Submitted figures", "Position, lowest balance and funding window match"],
        ],
    },
}
