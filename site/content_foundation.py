# Foundation course content. Lessons are Markdown in "read"; everything else is plain text.

COURSE = {
    "id": "foundation",
    "code": "F",
    "title": "Data foundation",
    "badge": "Data foundation",
    "duration": "About 1 hour 45 minutes",
    "status": "available",
    "audience": "Everyone. The third course of the K-φ AI Foundation, after Agentic finance and MCP.",
    "prereq": "Agentic finance, MCP",
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
                    "code": "F5.4", "title": "Push two ledger lines from Postman", "minutes": 8,
                    "objective": "Send data to K-φ from outside, with a key that holds only what the job needs.",
                    "read": """
When a system has no recipe yet, its developers send data to K-φ's API. You try it with Postman: two ledger lines, pushed from outside into your practice company.

1. **Make a key.** In your practice company: Admin, the AI tab, API keys. Label it `Postman`, pick *Choose scopes…*, tick `write:data` and nothing else, press Create. **Copy the key now: it is shown once.**
2. **Import the collection.** Download it under *Check my work* below. In Postman: Import, drop the file. A collection appears with one request, *Post 2 GL lines*, its address already set to your practice company.
3. **Give Postman the key.** Click the collection's name, open *Variables*, paste the key as the value of `api_key`, Save. Nothing goes in *Params*, *Headers* or the URL.
4. **Send.** Open *Post 2 GL lines*, press Send. K-φ answers **200** with `"stored": 2`. **401**: the key is not in `api_key`. **403**: the key lacks `write:data`.

Then open the ledger: October 2026, Halden Trading Ltd, account 1000 debited and 4000 credited by 1,000. Send it again and nothing doubles: the same line id replaces the line.

- **One key per job, with only the scopes it needs**: a dashboard that reads needs `read:gl`, a system that pushes needs `write:data`. Never an owner's session, never one key for everything.
- **The key lives in the system that uses it** or in a password manager, never in an e-mail, a ticket or a chat. Every call is recorded under its label; a key nobody uses any more is revoked.
- **The full API** is on the developers page (k-phi.com/developers): the same push takes invoices, balances, transactions and FX rates (`"object": "INV"`, `"BAL"`, `"TRA"`, `"FX"`), with the same checks as a connection or a sheet.
""",
                    "try": "Make a key with write:data only, import the collection into Postman, paste the key in its api_key variable and send Post 2 GL lines.",
                    "points": [
                        "A key per job, with only the scopes it needs.",
                        "The key in the system, never in a message.",
                        "Same line id, replaced: a re-send never doubles.",
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
    "lab": "Practise in your own practice company, a copy of Halden Trading. It opens set up: the three companies, 23 months of ledger, six banks and the open invoices. This course brings in October 2026 (F3.1) and connects it for good (F5).",
    "exam": {
        "title": "Exam: the K-φ AI Foundation",
        "situation": "The one exam of the K-φ AI Foundation path: it covers Agentic finance, MCP and Data foundation, and passing it gives the K-φ AI Foundation credential. You get an exam company with Halden's three companies and chart of accounts, nothing else. Three set-up steps (2 to 4 below), then two answers. Every step is something you did in a lesson; the lesson is named at the end of the step. Allow about 45 minutes.",
        "tasks": [
            "Start: press Start exam on the right, then Open my exam company. The two files appear on this page.",
            "The ledger, and your template: in the exam company, import halden-ledger-2026.csv. At the column step, press Save Template and name it (for example Halden ledger): that template is your ERP's layout, reused in the next step. Then finish the import as it proposes (one version per month). (F3.1)",
            "Your connector and its two test entries: ERP Connect, Add Connector, mode Push, template: the one you saved (under Saved templates), Save. Press Postman to download its collection. In Postman: Import that file, open \u201c3. Test Ingest (2 rows)\u201d, press Send. K-\u03c6 answers 200. Change nothing in the request. (F5.4)",
            "The third parties: turn the Copilot on (Admin, AI), open it and choose \u26a1 Consultant at its top. Attach third-parties.csv, send /tp /import and apply. The rules land in Settings, Organization, Third Party Rules. (F3.2)",
            "Check: press Check my exam company. Every step shows PASS, or says what is missing. Submit does not count, and uses no attempt, until steps 2 to 4 all pass.",
            "Answer and submit: Halden Trading Ltd's net income at October 2026, year to date, in GBP (Statements, P&L: Entities, Halden Trading Ltd only; Company at the top, so it stays in GBP; the 2026-10 column, last line, Net income). Type the amount only, for example 312450.80. Then ask the Copilot \u201cSummarise Halden's financial situation\u201d, paste its answer, and submit."
        ],
        "checks": [
            "The ledger file is in once, every company and month balanced",
            "Your saved template is the connector's, and its two test entries came in from Postman, balanced",
            "Every customer and supplier is in, with the payment terms of the file",
            "Halden Trading Ltd's net income at October 2026, year to date, is right",
            "The Copilot was asked in the exam company, and its summary quotes your books"
        ],
        "report": [
            ["pass", "The ledger, imported", "1,301 lines, January to October 2026; every company and month balances."],
            ["pass", "Your template, a connector, two test entries", "Template \u201cHalden ledger\u201d, connector \u201cHalden ERP\u201d: the two test entries came in from Postman, balanced, in their own version \u201cAPI_TEST_2026-11\u201d, apart from the books."],
            ["pass", "The third parties", "22 customers and suppliers, each with its payment terms: the cash forecast now times their payments."],
            ["fail", "The net result", "Not right: this is the 2026-09 column: take 2026-10. Statements, P&L: Entities, Halden Trading Ltd only; Company at the top, so the figures stay in GBP; the 2026-10 column, last line, Net income."],
            ["pass", "The Copilot's summary", "The summary comes from your books: its figures match the ledger."]
        ]
    },
}
