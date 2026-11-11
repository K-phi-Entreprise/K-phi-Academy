# Foundation course content. Lessons are Markdown in "read"; everything else is plain text.

COURSE = {
    "id": "foundation",
    "code": "F",
    "title": "Foundation",
    "badge": "Foundation",
    "duration": "About 2 hours",
    "status": "available",
    "audience": "Everyone. Required before any other course.",
    "prereq": "None",
    "summary": "How K-φ is organised, who can do what, how data comes in, and how to work safely in a client tenant.",
    "outcomes": [
        "Explain how a K-φ tenant is organised: entities, axes and the three workspaces.",
        "Set up users, roles and approvers so that no one makes a sensitive change alone.",
        "Bring data in through the right door and check it before anyone relies on it.",
        "Answer \"who changed what, and when\" from the audit trail.",
    ],
    "chapters": [
        {
            "code": "F1", "title": "Welcome to K-φ",
            "lessons": [
                {
                    "code": "F1.1", "title": "One system of record for FP&A, Cash and Build", "minutes": 6,
                    "objective": "Understand what K-φ is for, and why everything happens in one place.",
                    "read": """
Most finance teams run on a ledger, a few bank portals, and a large number of spreadsheets that connect them. The logic that matters (how cash is forecast, how a covenant is tested, how a margin call is funded) often lives in those spreadsheets, outside any system.

K-φ brings that work into one **system of record**:

- **FP&A** turns the general ledger into statements, KPIs, budgets, forecasts, scenarios and valuation.
- **Cash** holds bank accounts, transactions, receivables and payables, the cash position and the cash forecast.
- **Build** holds the client's own logic: extensions that read K-φ's data and write their results back into it.

The three share one data model. A figure is imported once and reused everywhere, so the P&L, the cash forecast and an extension built on top of them always agree.

As an implementer, this is the idea to keep in mind: **custom logic belongs inside the system that holds the data**, not in a file next to it.
""",
                    "try": "In the demo, switch between the workspaces with the tabs at the top of the left panel.",
                    "points": [
                        "K-φ is one system of record for FP&A, Cash and Build.",
                        "Data comes in once and is reused across workspaces.",
                        "Custom logic is built inside K-φ, next to the data it uses.",
                    ],
                },
                {
                    "code": "F1.2", "title": "A tour of the interface", "minutes": 7,
                    "objective": "Find your way around: workspace tabs, left panel, top bar, notifications.",
                    "read": """
The interface has four fixed areas.

1. **The workspace tabs** at the top of the left panel: FP&A and CASH, plus BUILD once Build is turned on for the account. You switch by clicking. Pointing at a tab does nothing.
2. **The left panel** lists the pages of the selected workspace, and only those.
3. **The top bar** holds the selectors that filter what you see: entity, business unit, third party, currency, units. They apply in FP&A and Cash alike.
4. **The bell** collects notifications: finished imports, sync results, approvals waiting for you.

The top bar also carries **Sync all**, which refreshes every connected data source in turn. Its progress shows in the button itself; the detail of what was refreshed goes to the bell.

Every page has a back button. Every dialog is a K-φ dialog, never a browser pop-up, so if you see a raw browser box, report it.

K-φ works in light and dark themes. Everything should stay readable in both; if something doesn't, that is a bug worth reporting.
""",
                    "try": "In the demo, change the entity selector in the top bar, then open a page in FP&A and one in Cash and check that the filter follows you.",
                    "points": [
                        "Click a workspace tab to switch; the left panel follows it.",
                        "Top-bar selectors filter FP&A and Cash the same way.",
                        "Sync all refreshes every source; details go to the bell.",
                    ],
                },
                {
                    "code": "F1.3", "title": "Tenants, entities and reporting axes", "minutes": 8,
                    "objective": "Know how a client is modelled, so you set it up right the first time.",
                    "read": """
**Tenant.** One client account. Everything lives inside it: users, data, extensions. Tenants never see each other, which is why every lab and every exam in this academy runs on a tenant of its own.

**Entities.** The legal companies of the group. Each entity has its own currency. A group with a US, a UK and a French company has three entities in USD, GBP and EUR.

**Reporting axes.** Beside entities, K-φ reports by:

- **Business unit**, for brands, divisions or product lines;
- **Third party**, for customers and suppliers.

The same axes run through FP&A and Cash. A customer is the same third party in the ledger and in the open receivables, so a DSO can be traced to the invoices behind it.

Two setup decisions are hard to change later, so take them early with the client:

| Decision | Ask |
|---|---|
| Entity list | Which legal companies are in scope, now and within a year? |
| Business units | How does management actually read the business? |

A wrong entity list shows up everywhere downstream: consolidated totals, intercompany, cash pools.
""",
                    "try": "In the demo, open the entity selector and note the entities and their currencies. Then find one customer that appears both in FP&A and in Cash.",
                    "points": [
                        "A tenant is one client, fully isolated.",
                        "Entities are legal companies, each with a currency.",
                        "Business units and third parties are shared axes across FP&A and Cash.",
                    ],
                },
            ],
            "check": [
                {"q": "A user points at the CASH tab without clicking. What happens?",
                 "options": ["The left panel switches to Cash", "Nothing; switching needs a click", "A preview of Cash opens"],
                 "answer": 1, "why": "Switching is by click only, so the panel never changes by accident."},
                {"q": "Where do you look to find out whether last night's data sync finished?",
                 "options": ["The bell", "The audit trail of each user", "The entity list"],
                 "answer": 0, "why": "Sync all shows progress in its button and sends the details to the bell."},
                {"q": "Which decision is the most expensive to change after go-live?",
                 "options": ["The theme", "The entity list", "The order of pages in the left panel"],
                 "answer": 1, "why": "Entities drive consolidation, intercompany and cash pools, so a wrong list spreads everywhere."},
            ],
        },
        {
            "code": "F2", "title": "Access and governance",
            "lessons": [
                {
                    "code": "F2.1", "title": "Users and roles", "minutes": 7,
                    "objective": "Give each person the access their job needs, and no more.",
                    "read": """
Every user has one of four **roles**:

| Role | Can |
|---|---|
| Owner | Everything, including the account's governance and billing. Usually one person |
| Admin | Manage users and settings, and change data |
| Editor | Change data: imports, budgets, forecasts, categorisation |
| Viewer | Read only |

Start from the job, not from the person's seniority. A controller preparing the close is an editor. A CFO who reads everything and approves sensitive changes can be an admin named as governance approver. An analyst who only presents figures is a viewer.

Keep owners and admins few. Every extra admin is one more person who can change who can do what.

Three habits keep a tenant clean:

- **One person, one login.** Shared logins make the audit trail useless.
- **Remove access on the day someone leaves**, not at the next review.
- **Review roles at each quarter end.** Access tends to grow over time and rarely shrinks by itself.

An LLM never gets an admin's credentials. When a builder works with an assistant, the assistant acts through the builder pass, with the builder's rights, never through someone else's account.
""",
                    "try": "On paper: list five people of a client team you know and give each one of the four roles. Who would be admin, and why?",
                    "points": [
                        "Roles follow the job, not seniority.",
                        "One login per person, removed the day they leave.",
                        "Assistants act with the builder's rights, never an admin's.",
                    ],
                },
                {
                    "code": "F2.2", "title": "Governance approvers and dual control", "minutes": 8,
                    "objective": "Make sure sensitive changes always need a second person.",
                    "read": """
Some changes are too important for one person to make alone. K-φ handles them with **dual control**: one person prepares the change, a **governance approver** approves it, and only then does it take effect.

Dual control is on by default for Build:

- naming a builder,
- letting an extension write into Cash,
- adding server keys to an extension.

Approvers are named in the account's governance settings, using the roles you already set up. There is no separate mechanism to learn.

The rule for implementers is simple: **the person who prepares a change never approves it.** If a client has only one admin, K-φ's own team confirms Build changes in place of a second admin; do not work around it by creating a second account for the same person.

When you design a client's setup, write down who prepares and who approves for each sensitive action. That page is what an auditor will ask for first.
""",
                    "try": "On paper: for the same team, write who prepares and who approves each Build change. Check nobody does both.",
                    "points": [
                        "Sensitive changes take effect only after approval.",
                        "Approvers come from the roles already in the account.",
                        "The preparer never approves their own change.",
                    ],
                },
                {
                    "code": "F2.3", "title": "Segregation of duties and two-factor authentication", "minutes": 6,
                    "objective": "Apply the two controls auditors check first.",
                    "read": """
**Segregation of duties.** For payments, the person who prepares a run can neither approve nor sign it, and the run needs two different signers, each within a signing limit. K-φ enforces this; it is not a setting to loosen. The Cash course covers it in lesson C6.2.

**Two-factor authentication.** Every user can turn it on, and admins and approvers should. Once it is on, sign-in through an accounting system or single sign-on also asks for the code.

Two-factor authentication protects the login; it never blocks work in progress. A user who has not set it up can still save what they are doing.

A short checklist for a new client:

1. Payment signers each have a signing limit, and there are at least two of them.
2. Every approver has two-factor authentication on.
3. No user holds both preparer and approver duties for the same action.
""",
                    "try": "In the demo, open Cash, Payments, Payment rights and read who can prepare, approve and sign, and each signer's limit.",
                    "points": [
                        "Two signers for payments is the default; keep it.",
                        "Admins and approvers should use two-factor authentication.",
                        "Check preparer and approver duties never sit with one person.",
                    ],
                },
            ],
            "check": [
                {"q": "Maya prepares a change that lets an extension write into Cash. Who can approve it?",
                 "options": ["Maya, if she is an admin", "A governance approver other than Maya", "Any user with read access"],
                 "answer": 1, "why": "The preparer never approves their own change."},
                {"q": "A client has a single admin. What do you do about dual control on Build changes?",
                 "options": ["Create a second account for the same person", "Let K-φ's team confirm in place of a second admin", "Turn dual control off"],
                 "answer": 1, "why": "For single-admin accounts, K-φ's team confirms. A second account for the same person defeats the control."},
                {"q": "Can a user without two-factor authentication still save their work?",
                 "options": ["Yes", "No, saving is blocked until they set it up"],
                 "answer": 0, "why": "Two-factor authentication protects sign-in and never blocks saving."},
            ],
        },
        {
            "code": "F3", "title": "Bringing data in",
            "lessons": [
                {
                    "code": "F3.1", "title": "Importing a general ledger", "minutes": 9,
                    "objective": "Load a ledger file so that statements and KPIs are right from day one.",
                    "read": """
The general ledger is the base of FP&A: statements, KPIs and the forecast all start from it.

K-φ accepts ledger exports as CSV or Excel, from most accounting systems. A good file has, for each line:

| Field | Why it matters |
|---|---|
| Entity | Which company the line belongs to |
| Date | Puts the line in the right period |
| Account | Drives the classification in the statements |
| Debit and credit, or a signed amount | The value, with its direction |
| Third party (optional) | Links the line to a customer or supplier |
| Business unit (optional) | Feeds the business-unit view |

Before you import, open the file and look:

- Does it cover the periods you expect, with no month missing?
- Do debits equal credits per entity and per month?
- Are there lines dated in the wrong year, or amounts in thousands mixed with units?

Large files are fine. What matters is that the file is complete and consistent.
""",
                    "try": "In the demo, open the P&L and drill into one line until you reach the ledger lines behind it.",
                    "points": [
                        "The ledger is the base of everything in FP&A.",
                        "Check completeness and balance before importing.",
                        "Size is not the problem; inconsistency is.",
                    ],
                    "resources": ["Sample ledger, Halden Trading, 24 months (CSV)"],
                },
                {
                    "code": "F3.2", "title": "Accounting connectors", "minutes": 6,
                    "objective": "Keep the ledger, invoices and bills in sync with the client's accounting system.",
                    "read": """
For clients on **QuickBooks** or **Xero**, a connector keeps K-φ in sync without files. The client's accounting user signs in once and authorises K-φ; after that, the ledger, invoices and bills flow in on each sync.

Points to settle with the client before connecting:

- **Who authorises.** It must be someone with the right to grant access in the accounting system, usually an admin there.
- **Which companies.** One connection per company in the accounting system, mapped to the right K-φ entity.
- **From which date.** Agree the history you need for the forecast, usually at least twelve months.

Invoices imported this way follow the direction rule: when a group company is paid, it is a receivable; when it pays a third party, it is a payable. If both parties are group companies, the document is intercompany.

If the client's system has no connector, a ledger export (lesson F3.1) and an invoice file work the same way.
""",
                    "try": "In the demo, open Cash, Φ Setup, Data sources and note what is connected and which entity each source feeds.",
                    "points": [
                        "QuickBooks and Xero connect directly; others use files.",
                        "Map each connected company to the right entity.",
                        "Agree on the history you need before connecting.",
                    ],
                },
                {
                    "code": "F3.3", "title": "Bank connections", "minutes": 7,
                    "objective": "Bring balances and transactions in, and organise accounts the way treasury reads them.",
                    "read": """
Banks connect through open banking: the client authorises each bank once, and balances and transactions arrive on each sync. K-φ stores balances day by day, so the position on any past date can be rebuilt.

Once accounts are in, organise them:

- **By entity**, so each company's cash is visible on its own.
- **By pool**, for accounts managed together. A pool can have a header account that acts as reserve.

Payment-provider accounts are shown apart from bank accounts and are not part of the bank list.

Agree with the treasurer on the account names before go-live. Names are what people read on every screen; "Main EUR" helps more than a sixteen-digit number.

Bank connections expire after a period set by the bank, after which the client has to authorise again. Put a reminder in the client's calendar; an expired connection is the most common reason for a "missing" balance.
""",
                    "try": "In the demo, open the bank accounts and note which entity each belongs to and how they are grouped.",
                    "points": [
                        "Balances are stored daily, so past positions can be rebuilt.",
                        "Organise accounts by entity and by pool.",
                        "Bank authorisations expire; plan the renewal.",
                    ],
                },
                {
                    "code": "F3.4", "title": "Sheets, files and Data sources", "minutes": 7,
                    "objective": "Use Google Sheets and files as sources without losing control.",
                    "read": """
Some data lives in spreadsheets and will keep living there: a budget, a register of contracts, a price list. K-φ connects them as **data sources** instead of asking the client to retype them.

You find them in Cash, under **Φ Setup**, then **Data sources**: bank connections, Google Sheets, and **variables** (your own reference series, such as a price or an index). Ledger and invoice files come in through their own imports (lessons F3.1 and F3.2).

Good practice with a sheet as a source:

- **One sheet, one purpose.** A register of forward contracts is a source; a workbook that also holds the budget and a holiday plan is not.
- **Fixed column names.** If someone renames a column, the sync breaks. Agree on who may edit the structure.
- **Owner named.** Every sheet source has an owner on the client side who answers for its content.

Anything that has an API can also come in through the developer portal. That route belongs to Build and is covered in the Build course.
""",
                    "try": "In the demo, open Data sources and look at the Google Sheets section. Think of one sheet a client of yours could connect.",
                    "points": [
                        "Sheets and variables connect under Φ Setup, Data sources; files use their own imports.",
                        "One sheet per purpose, with fixed column names.",
                        "Each sheet source has a named owner at the client.",
                    ],
                    "resources": ["Sample register, FX forwards (Google Sheet template)"],
                },
                {
                    "code": "F3.5", "title": "Checking an import before you trust it", "minutes": 8,
                    "objective": "Catch import problems before they reach a report.",
                    "read": """
An import that "worked" can still be wrong. Before anyone relies on new data, check three things.

**1. Coverage.** The periods, entities and accounts you expected are all there. A missing month is easy to miss in a chart and obvious in a list.

**2. Totals.** Compare totals by entity and by month with the source system. Use a figure the client trusts, such as a closing balance or the trial balance, not a figure K-φ produced.

**3. What did not land.** Look at lines rejected or waiting for a mapping. Each one is either a mistake in the file or a mapping to create.

When you find a problem, **fix it at its source**: correct the file or the mapping, then import again. Never type over a total in K-φ to make it match. The audit trail will show it, and the next import will undo it.

Keep a short note for each import: what was loaded, what you checked, what you fixed. It takes two minutes and saves an hour at the first review.
""",
                    "try": "Take a ledger export you have and run the three checks on it: coverage, totals, and what would not land.",
                    "points": [
                        "Check coverage, totals, and what did not land.",
                        "Compare with a figure the client trusts.",
                        "Fix at the source; never type over a total.",
                    ],
                },
            ],
            "check": [
                {"q": "After an import, the group total is short by exactly one month of revenue. What is the most likely cause?",
                 "options": ["A rounding setting", "A missing month in the file", "The wrong theme"],
                 "answer": 1, "why": "A gap of exactly one period points to coverage. Check the months before anything else."},
                {"q": "A total in K-φ differs from the trial balance. What do you do?",
                 "options": ["Adjust the total in K-φ", "Find the cause in the file or mapping, fix it, import again", "Ignore it if the difference is small"],
                 "answer": 1, "why": "Fix at the source. A manual adjustment is undone by the next import and shows in the audit trail."},
                {"q": "A balance is missing for one bank this morning. What do you check first?",
                 "options": ["Whether the bank authorisation has expired", "The entity's currency", "The user's role"],
                 "answer": 0, "why": "Expired bank authorisations are the most common reason for a missing balance."},
            ],
        },
        {
            "code": "F4", "title": "Working safely",
            "lessons": [
                {
                    "code": "F4.1", "title": "Reading the audit trail", "minutes": 6,
                    "objective": "Answer who changed what, and when.",
                    "read": """
Every change in K-φ is recorded: who made it, what changed, and when. Approvals are recorded too, with the approver and the time.

Use the audit trail to:

- **Trace a figure** back to the import or the edit that produced it.
- **Answer a reviewer** who asks why a forecast moved since last week.
- **Check an approval** really happened before a change took effect.
- **See what an extension wrote**, with the extension and version that wrote it.

Read it like a ledger: filter by user, by period or by object, then read down in time order. If a change has no explanation, ask the person who made it the same day; memories fade fast.
""",
                    "try": "In the demo, find the audit trail and filter it by user and by period.",
                    "points": [
                        "Every change and every approval is recorded.",
                        "Filter by user, period or object, then read in order.",
                        "Extensions' writes carry the extension and its version.",
                    ],
                },
                {
                    "code": "F4.2", "title": "What you never do in a client tenant", "minutes": 5,
                    "objective": "Know the few rules that protect the client, and you.",
                    "read": """
A short list. Breaking any of these can cost a client money and a certified builder their certificate.

- **Never share a login**, including with an assistant or a colleague.
- **Never approve your own change.**
- **Never type over a figure** to make it match; fix its source.
- **Never leave test data** in a live tenant. Use the demo or a test tenant.
- **Never loosen a control** (two signers, dual control) without the client's written decision.
- **Never promise what K-φ does not do.** If you are unsure, ask before you say yes.

When in doubt, stop and ask the client's approver. A delay of an hour is always cheaper than an unexplained change.
""",
                    "try": "Write down the one rule on this list you have seen broken in a real project, and how it could have been avoided.",
                    "points": [
                        "No shared logins, no self-approval, no typed-over figures.",
                        "Test in the demo or a test tenant, never in a live tenant.",
                        "Controls change only on the client's written decision.",
                    ],
                },
            ],
            "check": [
                {"q": "A client asks you to switch payments to one signer to go faster. What do you do?",
                 "options": ["Do it, the client asked", "Ask for the decision in writing from the client's approver, and advise against it", "Refuse to work with the client"],
                 "answer": 1, "why": "Controls change only on a written decision. Advise, record, and let the client decide."},
                {"q": "You need to test an import format. Where do you do it?",
                 "options": ["In the client's live tenant, then delete the data", "In the demo or a test tenant", "In the client's tenant on a weekend"],
                 "answer": 1, "why": "Test data never goes into a live tenant."},
            ],
        },
    ],
    "lab": "Practise in the K-φ demo: sample companies with FP&A and Cash data. It needs no account and nothing you do is saved.",
    "exam": {
        "title": "Exam: set up Halden Trading",
        "report": [
            ["pass", "Entities and currencies", "3 of 3 entities, currencies match"],
            ["pass", "Roles and approver", "Preparer cannot approve; Tom Ashby is approver"],
            ["fail", "Ledger totals by entity and month", "Halden Négoce SAS, March: 412,300.00 EUR expected, 824,600.00 found. A period appears twice; see lesson F3.5"],
            ["fail", "Seeded problem resolved at source", "Not resolved: the duplicate period is still in the imported file"],
            ["pass", "Audit trail", "Changes by the candidate, in a plausible order"],
        ],
        "situation": "Halden Trading is starting on K-φ. Your exam tenant is empty apart from the company profile.",
        "tasks": [
            "Create the three entities with their currencies: Halden Trading Inc. (USD), Halden Trading Ltd (GBP), Halden Négoce SAS (EUR).",
            "Create two users: Maya Chen, Group Controller, who prepares changes; and Tom Ashby, CFO, who approves them. Name the right person as governance approver.",
            "Import the general ledger file provided (24 months, three entities).",
            "Find the one problem in the import and resolve it at its source.",
            "In the submission form, say in five lines at most what the problem was and how you resolved it.",
        ],
        "checks": [
            "Entities exist with the right currencies",
            "Preparer cannot approve; approver is set; no user holds both duties",
            "Ledger totals by entity and month match the answer key",
            "Seeded problem resolved at its source",
            "Audit trail shows the candidate's changes in a plausible order",
        ],
    },
}
