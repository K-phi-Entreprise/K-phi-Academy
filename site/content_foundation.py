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
            "code": "S0", "title": "Set up your practice company",
            "lessons": [
                {
                    "code": "S0.1", "title": "Your practice company and its three entities", "minutes": 5,
                    "objective": "Open your own practice company and give it its three entities, each in its own currency.",
                    "read": """
Every lesson in this academy happens in **your practice company**: your own copy of Halden Trading, a distribution group that is moving to K-φ. It is a K-φ company of its own, separate from the account you signed in with, so nothing you do here touches real books.

It starts the way a client's company starts on day one: **empty**. Only the six bank accounts are there, because banks are connected, not typed in, and five of them already carry their statements. Everything else you bring in yourself, from the files the academy gives you, in four steps. Files imported by hand are the quick way to start and to learn what each import does; chapter F5 shows how a client runs, with nobody importing anything:

1. **The entities**, in this lesson.
2. **The ledger**, 23 months of it (S0.2).
3. **A bank statement**, for the one account still without its history (S0.3).
4. **The open receivables and payables** (S0.4).

Halden Trading has three legal companies. Each keeps its books in its own currency:

| Code | Company | Currency |
|---|---|---|
| HTUS | Halden Trading Inc. | USD |
| HTUK | Halden Trading Ltd | GBP |
| HTFR | Halden Négoce SAS | EUR |

The codes matter: the ledger file uses them on every line. An entity created with the wrong currency stays wrong in every report that converts it.
""",
                    "try": "In your practice company, open Configuration from the FP&A home and create the three entities with exactly these codes, names and currencies.",
                    "points": [
                        "Your practice company is yours alone, separate from your own K-φ account.",
                        "It starts empty, like a client on day one.",
                        "Each entity has a code and a currency: the ledger relies on both.",
                    ],
                },
                {
                    "code": "S0.2", "title": "Import the ledger", "minutes": 8,
                    "objective": "Bring 23 months of general ledger into K-φ, once, and check that every company-month landed.",
                    "read": """
The ledger file holds **November 2024 to September 2026** for the three companies: one balanced journal per company per month, about 3,000 lines, with the entity, business unit, account, debit, credit, currency and third party on each line.

Import it from **File import** on the FP&A home. K-φ reads the columns, shows you a preview with the totals of debits and credits, and saves it as one version.

Two things to watch:

- **Once only.** Importing the same file twice doubles every figure. If it happens, delete the extra version and keep one.
- **The totals.** Debits equal credits in the preview. If they do not, the file did not land as it should.

October 2026 is not in this file. It arrives later, in lesson F3.1, the way a new month arrives at a client.
""",
                    "try": "In your practice company, download the ledger file below and import it with File import. Then open the P&L and check that the 23 months are there.",
                    "points": [
                        "One file, one import, one version.",
                        "Debits equal credits before you save.",
                        "Twice is the most common mistake: delete the extra version.",
                    ],
                },
                {
                    "code": "S0.3", "title": "Import a bank statement", "minutes": 5,
                    "objective": "Load eleven months of movements into the one account that has none yet: Barclays Operating.",
                    "read": """
The six accounts are already there, with their balance on 31 October 2026, the way a bank connection would show them:

| Bank | Account | Company |
|---|---|---|
| JPMorgan Chase | Operating, Payroll | Halden Trading Inc. |
| Barclays | Operating, Reserve | Halden Trading Ltd |
| BNP Paribas | Operating, Payroll | Halden Négoce SAS |

Five of them already hold their history, from **December 2025 to October 2026**: customer receipts, supplier payments, payroll, tax, the loan, and the transfers between the group's own accounts. **Barclays Operating** has none yet. Its statement is the file below, in the format banks send: **camt.053**, the ISO 20022 end-of-day statement.

A camt.053 carries three things a spreadsheet does not:

| In the file | What K-φ does with it |
|---|---|
| The account's **IBAN** | files the statement in its account, without asking |
| The **opening and closing balances** | checks that opening plus the movements equals closing, and says so |
| The bank's **reference** for each movement | recognises a movement already imported, so a second import doubles nothing |

1. In Cash, press **Import a statement** and choose the file.
2. K-φ says how many movements it imported, into which account, and that the balances reconcile.
3. Press Check below.

A CSV statement works too, but it names no account: K-φ then asks which one it is for, and a statement in the wrong account is the mistake to avoid. The balances would still add up, but each company's cash would be wrong.

Pick the statement, not the ledger: a ledger file in Import a statement is refused, with a message saying it is a ledger.
""",
                    "try": "In your practice company, download the Barclays Operating camt.053 below and import it from Import a statement in Cash.",
                    "points": [
                        "Accounts come from the bank; history comes from the statements.",
                        "A camt.053 names its IBAN and its balances: it files and reconciles itself. A CSV does neither.",
                        "The ledger's cash on each month end equals the bank balance that day.",
                    ],
                },
                {
                    "code": "S0.4", "title": "Import the open receivables and payables", "minutes": 7,
                    "objective": "Bring in the invoices still open on 31 October 2026, each in its direction.",
                    "read": """
Two files: what customers still owe Halden Trading (**receivables**) and what it still owes its suppliers (**payables**), as at 31 October 2026. Each line has its direction, its company, its customer or supplier, its dates and its open amount.

Import both from the **AR/AP import** in Cash. K-φ maps the columns for you; check the direction before you save.

A few documents are between two group companies: the management fee the subsidiaries owe Halden Trading Inc. They carry the partner company in **Intercompany partner**. K-φ flags them intercompany, so they are left out of the group's cash forecast and matched on both sides.
""",
                    "try": "In your practice company, download the two invoice files below and import them with the AR/AP import in Cash, receivables as receivables and payables as payables.",
                    "points": [
                        "Receivables and payables are imported in their own direction.",
                        "Intercompany documents name the partner company.",
                        "With the ledger, the banks and the invoices in, your company is set up.",
                    ],
                },
            ],
        },
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
                    "try": "In your practice company, switch between the workspaces with the tabs at the top of the left panel.",
                    "points": [
                        "K-φ is one system of record for FP&A, Cash and Build.",
                        "Data comes in once and is reused across workspaces.",
                        "Custom logic is built inside K-φ, next to the data it uses.",
                    ],
                },
                {
                    "code": "F1.2", "title": "A tour of the interface", "minutes": 7,
                    "objective": "Find your way around: workspace tabs, left panel, and both sides of the top bar.",
                    "read": """
The interface has four fixed areas.

1. **The workspace tabs** at the top of the left panel: FP&A and CASH, plus BUILD once Build is turned on for the account. You switch by clicking. Pointing at a tab does nothing.
2. **The left panel** lists the pages of the selected workspace, and only those.
3. **The left of the top bar** says what you are looking at.
4. **The right of the top bar** says who you are, and holds the tools.

**The left of the top bar**, from left to right:

| Item | What it does |
|---|---|
| Page name and **?** | the page you are on; **?** opens its help |
| **All clear** | the financial checks on your data pass; it turns amber or red with a count when they do not, and a click lists them |
| **Period** | the month you are reading |
| **Entities** | one company, several, or all of them |
| **BU** and **TP** | business unit and third party. **Optional**: a client that does not report by them leaves them on All |
| **Group** or **Company** | Group reads everything in the group currency; Company reads each company in its own currency |
| **Currency** and **1 · K · M** | the display currency, and units, thousands or millions |

These selectors apply in FP&A and Cash alike: change the entity on one page and the next page follows.

**The right of the top bar**, from left to right:

| Item | What it does |
|---|---|
| **Company badge** | the company you are signed into, in pink. In the academy it reads ACAD-… Halden Trading. Check it before you change anything |
| **Role** | your role in that company: OWNER, ADMIN, EDITOR or VIEWER |
| **The bell** | notifications: finished imports, sync results, approvals waiting for you |
| **Sync all** | refreshes every connected data source in turn; its progress shows in the button, the detail goes to the bell |
| **New window** | opens K-φ in a second window with the same session, to see two pages side by side |
| **Auto-scroll** | when on, the page scrolls as the pointer reaches its edge |
| **Full screen** | hides the browser around K-φ |
| **Light or dark** | switches the theme |
| **Sign out** | the red arrow, last on the right |

On a narrow screen, the buttons fold into **More actions** (⋯).

Every dialog is a K-φ dialog, never a browser pop-up, so if you see a raw browser box, report it. Everything should stay readable in both themes; if something doesn't, that is a bug worth reporting.

The theme is a choice of yours, kept in your browser: switching it changes nothing for your colleagues and nothing in the data. The exercise below asks you to switch to light mode, so you have seen every screen of the lesson in both.
""",
                    "try": "In your practice company, switch to light mode with the \u263C button at the top right. Read the company badge and your role, set the entity selector to Halden Trading Ltd, then open a page in FP&A and one in Cash and check that the filter follows you. Switch back to dark afterwards if you prefer it: the check only needs to see you switch once.",
                    "points": [
                        "Left of the top bar: what you are looking at. Period, entities, view, currency, units.",
                        "Business unit and third party are optional selectors.",
                        "Right of the top bar: the company you are in, your role, the bell and the tools.",
                        "Light or dark is yours alone, kept in your browser.",
                    ],
                },
                {
                    "code": "F1.3", "title": "Tenants, entities and reporting axes", "minutes": 8,
                    "objective": "Know how a client is modelled, so you set it up right the first time.",
                    "read": """
**Tenant.** One client account. Everything lives inside it: users, data, extensions. Tenants never see each other, which is why every lab and every exam in this academy runs on a tenant of its own.

**Entities.** The legal companies of the group. Each entity has its own currency. A group with a US, a UK and a French company has three entities in USD, GBP and EUR.

**Reporting axes.** Beside entities, K-φ can report by two optional axes:

- **Business unit**, for brands, divisions or product lines;
- **Third party**, for customers and suppliers.

Both are optional. A client that does not read its business by unit, or does not book its customers and suppliers on the ledger lines, leaves the BU and TP selectors on All, and nothing is lost.

The same axes run through FP&A and Cash. A customer is the same third party in the ledger and in the open receivables, so a DSO can be traced to the invoices behind it.

Two setup decisions are hard to change later, so take them early with the client:

| Decision | Ask |
|---|---|
| Entity list | Which legal companies are in scope, now and within a year? |
| Business units | How does management actually read the business? |

A wrong entity list shows up everywhere downstream: consolidated totals, intercompany, cash pools.
""",
                    "try": "In your practice company, open the entity selector and note the three companies and their currencies. Then find the customer that buys from all three, in FP&A and in Cash.",
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
                    "try": "In your practice company, invite a made-up colleague as a viewer (any address ending in @example.com; no mail is sent) and read what a viewer cannot change. Then, on paper, give five people of a client team you know one of the four roles each.",
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
                    "try": "In your practice company, open Cash, Payments, Payment rights and read who can prepare, approve and sign, and each signer's limit.",
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
                    "try": "In your practice company, download the October 2026 ledger below and import it with File import. Then open the P&L for October and drill into one line until you reach the ledger lines behind it.",
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
                    "try": "In your practice company, open Cash, Φ Setup, Data sources and note what is connected and which entity each source feeds.",
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
                    "try": "In your practice company, open the bank accounts and note which entity each belongs to and how they are grouped.",
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
                    "try": "In your practice company, open Data sources and look at the Google Sheets section. Think of one sheet a client of yours could connect.",
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
                    "try": "In your practice company, run the three checks on the October import from F3.1: coverage, totals, and what would not land. Then take a ledger export of your own and do the same.",
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
                    "try": "In your practice company, find the audit trail and filter it by user and by period.",
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
                 "options": ["In the client's live tenant, then delete the data", "In your practice company or a test tenant", "In the client's tenant on a weekend"],
                 "answer": 1, "why": "Test data never goes into a live tenant."},
            ],
        },
        {
            "code": "F5", "title": "Connect it for good",
            "lessons": [
                {
                    "code": "F5.1", "title": "From a file to a feed", "minutes": 6,
                    "objective": "Choose how each kind of data should reach K-φ, and know why a file imported by hand is only the start.",
                    "read": """
You set up your practice company with files, by hand. That is the quick way to start, and the right way to learn what each import does. It is not how a client runs: nobody imports twelve files every month end, and nobody can say afterwards which file it was.

Data reaches K-φ four ways. Use the first that fits:

| Route | When | Who keeps it running |
|---|---|---|
| **A connector** | The bank, QuickBooks, Xero, Sage: K-φ has a built-in connection | Nobody: it runs on its schedule |
| **An endpoint** | Another system with an API: an ERP, a TMS, a CRM. The Copilot's connection assistant connects it from a recipe, or the system pushes to K-φ's API | Nobody: it runs on its schedule |
| **A synced Google Sheet** | Data people keep by hand: the budget, a forecast, FX rates, a list of mappings | The team that edits the sheet; K-φ loads each change |
| **A file, by hand** | A one-off: the history at go-live, a correction | You, every time: avoid it for anything that repeats |

Whatever the route, the data lands in the same places through the same checks: the ingest contract. A ledger line from an ERP, from a sheet or from a file is checked the same way, and the same line sent twice is replaced, never added twice.

The test of a good set-up is simple: **at the next month end, does anyone have to do anything?** If the answer is yes, write down who, and why.
""",
                    "try": "For your practice company, write down which route each source should take at a real client: the ledger, the bank, the invoices, the budget, the FX rates.",
                    "points": [
                        "A file by hand is for the start and for one-offs.",
                        "Connector first, then endpoint, then a synced sheet.",
                        "The test: the next month end needs nobody.",
                    ],
                },
                {
                    "code": "F5.2", "title": "The Copilot's connection assistant", "minutes": 8,
                    "objective": "Connect a system from its recipe, with its key in the vault, and put it on a schedule.",
                    "read": """
The K-φ Copilot (the φ button at the bottom right) holds two assistants that set up connections. Neither calls a model: they follow a recipe, step by step, so what they do is the same every time.

**The connection assistant** (type `/connect` and the system's name) walks a recipe:

1. **The address and the secrets.** A secret goes into a password field that sends it straight to the vault. It is never in the chat, never in the history, never shown again. Never paste a key into the chat itself.
2. **The test.** The assistant calls the system and says what it found: which objects it can read.
3. **The mapping.** For each object, the assistant proposes which field becomes which K-φ field (the contract), shows a sample mapped and checked, and waits for you to approve. Read the sample: the date, the amount and its sign, the company.
4. **The schedule.** An approved mapping runs on its recipe's schedule (Halden ERP: every night at 02:00 UTC). Each run reads from where the last one stopped.

Every step is recorded in the audit trail under your name; every scheduled run under "schedule". A run that fails twice in a row e-mails the owners and admins.

Your practice company has its own Halden ERP, a test system the academy hosts: its address and key are below. Connect it and run its test. **Do not approve a mapping in the practice company**: it already has this ledger, from your files. You will approve them in the exam.
""",
                    "try": "In your practice company, open the Copilot, type /connect halden-erp, give it the address and the key below, and let it test the connection.",
                    "points": [
                        "/connect <system>: a recipe, step by step, no model.",
                        "Secrets go to the vault, never into the chat.",
                        "Approve the mapping only after reading the sample.",
                    ],
                },
                {
                    "code": "F5.3", "title": "A Google Sheet that loads itself", "minutes": 8,
                    "objective": "Register a sheet in the contract's layout and let K-φ load each change.",
                    "read": """
Some data is kept by people, in a spreadsheet: the budget, a forecast, the FX rates the treasurer agrees with the bank. Keep it there. K-φ reads the sheet; it never writes to it.

1. **Name each tab after what it holds**: `FX`, `GL - Budget 2026`, `TRA - Main bank`, `INV`. The columns are the contract's fields (the developers page lists them).
2. **Share the sheet** as "Anyone with the link can view". K-φ needs no Google account.
3. **Register it** in the Copilot: `/connect`, then Google Sheets, then the link. The sheet assistant shows each tab and what it becomes.
4. **Tick "Load into K-φ each time the sheet changes."** K-φ reads the sheet every few minutes; when it has changed, it checks every row and loads it. A row that fails is reported with its tab, its line and its field, and nothing of that tab is stored until it passes.

A budget in a sheet lands as a **Budget version** of the ledger (version type Budget), next to the actuals, so the P&L and the variance read it like any version.
""",
                    "try": "Download the FX rates file below. In Google Sheets, import it into a new sheet, name the tab FX, share it by link, then register it with the sheet assistant, with “Load into K-φ each time the sheet changes” ticked.",
                    "points": [
                        "Tabs named after the contract objects; columns are its fields.",
                        "Shared by link, read only; K-φ never writes to it.",
                        "Each change loads itself; a bad row is named, nothing half-stored.",
                    ],
                },
                {
                    "code": "F5.4", "title": "The developers page, an API key and Postman", "minutes": 8,
                    "objective": "Call K-φ from outside with a key that holds only what the job needs.",
                    "read": """
When a system has no recipe yet, it talks to K-φ directly: its developers push data to K-φ's API, or read from it.

- **The developers page** (k-phi.com/developers) describes every call, and `/api/v1/openapi.json` describes them for tools. **Postman** imports it: File, Import, paste the link. Every call is then ready, with its parameters.
- **An API key** is made in Admin, API keys. Give it the **scopes the job needs and nothing more**: a dashboard that reads the P&L needs `read:gl`; an ERP that pushes the ledger needs `write:data`. Never an owner's session, never one key for everything.
- **The key is shown once.** Keep it in the system that uses it, or in a password manager; never in an e-mail, a ticket or a chat.
- **Every call is recorded** under the key's label, and the key's last use shows in Admin, API keys. A key nobody uses any more is revoked.

To push data, the same contract applies: `POST /api/v1/contract_ingest` with the object (GL, INV, BAL, TRA, FX) and its rows, the same checks and the same "same id, replaced" rule as a connection or a sheet.
""",
                    "try": "Create an API key with read:gl only. In Postman, import k-phi.com/api/v1/openapi.json, set the key as the bearer token, and call GET /api/v1/me.",
                    "points": [
                        "openapi.json into Postman: every call ready.",
                        "One key per job, only the scopes it needs.",
                        "Shown once, kept in the system, revoked when unused.",
                    ],
                },
                {
                    "code": "F5.5", "title": "Month end, without you", "minutes": 6,
                    "objective": "Know what a set-up that runs by itself looks like, and how you prove it to the client.",
                    "read": """
The set-up is done when the client's month end needs nobody. Before you hand over, check:

- **Every source is on a schedule** (connections) or loads on change (sheets), and you know when it runs.
- **Nothing is imported by hand** in the last month: the audit trail shows the runs under "schedule", not under a person.
- **Failures reach someone.** The owners and admins are e-mailed when a run fails twice; tell the client who they are.
- **The duties hold.** The person who prepares changes is not the one who approves them, and dual control is on: a connection or a mapping is a change like any other.

Then answer the client's questions from what arrived: the month's EBITDA, the cash, the customers who pay late, the budget gap. If you can answer them without touching a file, the set-up works.

Write the client a short note: where each figure comes from, how often it is refreshed, and who to call when a run fails. That note is part of the hand-over.
""",
                    "try": "Write the three-line note you would give Halden's CFO about your practice company: where each figure comes from, and what happens at the next month end.",
                    "points": [
                        "Scheduled, loads on change, no import by hand.",
                        "Failures reach a named person.",
                        "A short note to the client is part of the hand-over.",
                    ],
                },
            ],
            "check": [
                {"q": "The FP&A team keeps the budget in a Google Sheet they edit every week. How should it reach K-φ?",
                 "options": ["Exported to a file and imported each week", "A synced Google Sheet that loads each change", "Typed into K-φ by the controller"],
                 "answer": 1, "why": "Data people keep by hand stays where they keep it; K-φ loads each change."},
                {"q": "The connection assistant asks for the ERP's key. Where does it go?",
                 "options": ["Into the chat, so the Copilot can use it", "Into the key field, which sends it to the vault", "Into the CFO note"],
                 "answer": 1, "why": "A secret goes to the vault and is never shown again; never into the chat."},
                {"q": "A dashboard only reads the P&L. Which API key does it get?",
                 "options": ["An owner key", "A key with read:gl only", "A key with every scope, to be safe"],
                 "answer": 1, "why": "One key per job, with only the scopes it needs."},
            ],
        },
    ],
    "lab": "Practise in your own practice company, a copy of Halden Trading. It starts empty: in chapter S0 you set it up from the academy's files, the entities, the ledger, the bank statements and the invoices.",
    "exam": {
        "title": "Exam: answer the CFO, with data that arrived by itself",
        "situation": "Halden's CFO: \u201cNobody here should import a file again. The ledger and the invoices come from our ERP, the budget lives in a Google Sheet the FP&A team edits. Set it up so that month end needs nobody, then answer my questions about November.\u201d Your exam company has its three entities and nothing else. Its Halden ERP holds the books to 31 October; you close November when your set-up is ready.",
        "tasks": [
            "Put the duties in place: invite Maya Chen as an editor and Tom Ashby as an admin (Admin, Users; no mail is sent), make Tom the only approver and turn on Dual Admin Approval (Admin, Governance). (F2)",
            "Connect the Halden ERP with the Copilot: /connect halden-erp, then the address and the key shown on this page. Approve a mapping of JournalLines to the ledger (GL) and of OpenItems to AR/AP (INV). Let the first sync bring October in. (F5.2)",
            "Put the budget in a Google Sheet: import budget-2026.csv, name the tab \u201cGL - Budget 2026\u201d, share it by link, register it with the sheet assistant and tick \u201cLoad into K-\u03c6 each time the sheet changes\u201d. (F5.3)",
            "Press Check my exam company until the set-up shows PASS. Then press Close November: the ERP publishes November and the night runs your own schedules. You import nothing.",
            "Read the CFO's message: FP&A cuts December's revenue budget of Halden Trading Ltd by 10%. Change it in your sheet, as FP&A would, then press Run tonight's schedules. (F5.5)",
            "Answer the CFO's questions from K-\u03c6, and write the note: where each figure comes from, and what happens at the next month end. Then submit."
        ],
        "checks": [
            "Maya prepares, Tom approves, dual control is on",
            "The ERP is connected, mapped and on its schedule; October is in the books",
            "The budget sheet is registered, loads itself, and is a Budget version",
            "November arrived through the schedule, with no import by anyone",
            "FP&A's change to December arrived from the sheet",
            "At least 4 of the CFO's 6 questions are right: EBITDA, the budget gap, the ledger cash, the dividend, the customer most overdue, December's budget",
            "The note names the sources and how often they run"
        ],
        "report": [
            ["pass", "Users and duties", "Maya prepares, Tom approves, dual control is on."],
            ["pass", "The ERP, connected and on schedule", "Connected, mapped, scheduled daily; October is in the books."],
            ["pass", "The budget, a sheet that loads itself", "The sheet is registered, loads itself, and \u201cBudget 2026\u201d is a budget version."],
            ["fail", "November arrived by itself", "November is in K-\u03c6, but not through the schedule: a sync started by hand is still you. The test is that the month comes in without anyone."],
            ["pass", "FP&A's change arrived by itself", "The cut is in K-\u03c6, loaded by the sheet itself."],
            ["pass", "The CFO's questions", "5 of 6 right; not right: the dividend."],
            ["pass", "Your note to the CFO", "Sources and schedule named."]
        ]
    },
}
