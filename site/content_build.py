# Build course content. Every lesson describes what the app does on staging, checked against the engine
# (blocks/builder, lib/data-library.js, lib/variables.js), not plans.
from content_fpa import L, Q

COURSE = {
    "id": "build", "code": "B", "title": "Build", "badge": "Build", "duration": "About 4 hours", "status": "available",
    "audience": "Builders, analysts who automate, consultants.", "prereq": "Agentic finance, MCP, Data foundation",
    "summary": "Build extensions with your own LLM, use the Data library, write back under governance, and prove the AI got it right.",
    "outcomes": [
        "Decide when a need belongs in a BUILD, and what a BUILD can and cannot reach.",
        "Build pages, a dashboard and functions from your LLM with a Builder pass, in small checked steps.",
        "Combine the account's data with public series and your own variables, under their licences.",
        "Write back under dual control, and prove with known answers that what the AI built is right.",
    ],
    "lab": "Practise in your own practice company, a copy of Halden Trading, with its own BUILD workspace: you are its builder, and what you build stays a preview in that company.",
    "chapters": [
        {"code": "B1", "title": "Why build inside the system of record", "lessons": [
            L("B1.1", "Bespoke logic next to the data", 7,
              "Recognise the needs a BUILD is for, and the ones it is not.",
              """
Every finance team has logic no product ships: a margin-call model for a commodity trader, retainage on construction jobs, a covenant computed the way one bank defines it. That logic usually lives in a spreadsheet beside the system, fed by exports.

A BUILD puts that logic **inside** K-φ, next to the data K-φ already holds:

- **The data is already there and already clean.** Ledger, statements, bank balances, invoices, forecasts and budgets come from K-φ, with the same figures as every other screen. Nothing is exported or re-keyed.
- **The agent writes the code, you write the rule.** You describe the logic in your own words; your LLM writes the pages and functions against the K-φ API. You check the result (chapter B5).
- **The result lives in K-φ.** Pages sit in the BUILD workspace, follow the top bar's filters, and can feed CASH.

What a BUILD is not for:

- **A generic need.** If every client needs it, it belongs in K-φ itself, not in one client's BUILD.
- **A tool on its own.** A BUILD that reads none of the account's data is just an app; build it anywhere.

The test: the logic is specific to this business, and it needs the data K-φ already holds.
""",
              "In your practice company, open the BUILD workspace and read its menu: the Dashboard first, then Manage and the Data library. Note what is there before anything is built.",
              ["A BUILD holds logic specific to one business.", "It reads the data K-φ already holds; nothing is exported.", "A need every client shares belongs in K-φ itself."]),
            L("B1.2", "What an extension can and cannot touch", 7,
              "Know the limits the server enforces on every BUILD.",
              """
K-φ has three workspaces: FP&A, CASH and BUILD. A BUILD is built **on top of** K-φ, never inside it. Its code runs apart from the engine and reaches the account only through the K-φ API, with a credential limited to that one account.

The limits are enforced by the server, not by the code you write:

- **One account.** The account comes from the credential, never from the request. A BUILD cannot reach another company's data, even by mistake.
- **Scopes.** An extension can hold at most these rights: read the ledger, cash and forecasts; read the Data library and write the account's variables; write scenarios, its own store and, if granted, its own cash forecast lines; read and deploy its own code.
- **Never.** No ledger import, no change to the account's configuration, no change to FP&A or CASH pages. Bank statements and posted entries are never written by a BUILD.
- **A switch.** Turn the extension off, or revoke its key, and the next call is refused.

Every call an extension makes is recorded: which capability, the answer, how long it took. An admin reads that log in BUILD > Manage.

So when a client asks "can the AI break our books?", the answer is no: it can only reach what its scopes allow.
""",
              "In your practice company, open BUILD > Manage and read the scopes of your BUILD. Which of them lets it put lines in the cash forecast? Type it.",
              ["A BUILD reaches one account, through the API only.", "Scopes are enforced by the server.", "It never writes the ledger, bank statements or configuration."]),
        ], "check": [
            Q("A client wants a page that shows the weather in Paris, with no link to their figures. Is that a good BUILD?", ["Yes, any page can be a BUILD", "No: it uses none of the account's data, so it can be built anywhere", "Only if an admin approves it"], 1, "A BUILD earns its place by combining specific logic with the data K-φ already holds."),
            Q("Can an extension post entries to the ledger?", ["Yes, with the right scope", "No: no scope allows it, and the server refuses it", "Only during the trial"], 1, "Ledger import is never among an extension's scopes. The limit is enforced by the server."),
        ]},
        {"code": "B2", "title": "The builder pass", "lessons": [
            L("B2.1", "Pasting the pass into your LLM", 8,
              "Start a build from a Builder pass, safely.",
              """
A **Builder pass** is how your LLM gets to work on the account's BUILD. In BUILD > Manage, a builder clicks **Builder pass**: K-φ copies a link. Paste it into a chat with an assistant that can run code (Claude, for example), then say what you want built.

Behind the link, your LLM reads a brief: the API address, the credential, the scopes, the rules for pages, and how to deploy. There is no repository, token or setup for you to handle: K-φ keeps the code and deploys it.

What protects the account:

- **Only builders can create a pass.** An admin names a builder, and a second admin confirms it (chapter B4). A builder sees the whole account, so a user limited to some entities cannot be one.
- **A pass lasts 7 days.** Creating a new one revokes the previous one, and a pass stops at once when its builder loses the right.
- **Treat it like a password.** Paste it only into your own chat. Anyone holding the link can build until it expires or is revoked.

If your assistant reports that its requests are refused before reaching K-φ, its code tool is not allowed to reach K-φ's address: add it to the allowed domains in your assistant's settings.
""",
              "In your practice company, create a Builder pass, paste it into a new chat in your assistant, and ask: \"Which K-φ account is this, and what scopes do you have?\" Compare the answer with BUILD > Manage.",
              ["A pass is a link your LLM reads; K-φ deploys the code.", "Only builders create passes; a pass lasts 7 days.", "Keep it private: it works for whoever holds it."]),
            L("B2.2", "Working in small steps", 7,
              "Build in steps you can check, and undo one that went wrong.",
              """
An LLM builds well when each request is small and checked before the next one. A good rhythm:

1. **Say what you want, in business words.** "A page listing jobs with the retainage held back, by customer."
2. **Let it say what it will change** before it deploys. The pass asks your LLM to do this.
3. **Check the page in K-φ.** Open BUILD, compare a figure with the screen it comes from.
4. **Then ask for the next thing.** One page, one table or one function at a time.

Every deploy is a **version**. In BUILD > Manage > Versions you see each version with its one-line description, and **Restore** puts the BUILD back to an earlier one. A restore is itself recorded, so nothing is lost.

When something goes wrong, do not ask the LLM to "fix everything". Restore the last good version, then ask again, smaller.
""",
              "In your practice company, ask your assistant for one page that lists Halden's bank accounts with their balances. Then ask for a second change, for example a new title. Restore the first version, from BUILD > Manage > Versions or by asking your assistant, and check that the page is back as it was.",
              ["One small request at a time, checked in K-φ.", "Every deploy is a version you can restore.", "Restore, then ask again, smaller."]),
            L("B2.3", "The default dashboard and widgets", 6,
              "Use the Dashboard every BUILD starts with.",
              """
Every BUILD starts with a **Dashboard**, first in its menu. It is a board of K-φ widgets that the team drags from a catalogue, with no code:

- **FP&A:** KPI tile, Statement, Margins, Working-capital days, Budget versus actual, K-φ forecast.
- **CASH:** Cash flow, Bank balances and their history, Cash forecast and low point, Receivables aging, Top overdue, Invoices due by week.
- **Risk:** FX rate, Covenant gauge and panel.
- A **Note** for text.

Each widget flips to the table behind it, and the table exports. The widgets show K-φ's own figures, so they always match the other screens.

Everything else in the menu is a custom page, written by your LLM, and stays empty until its logic is defined. Start with the Dashboard: often the first need is answered by widgets alone, and the custom pages are kept for what no widget does.
""",
              "In your practice company, add the Bank balances widget and the Receivables aging widget to the Dashboard, then flip one of them to its table.",
              ["The Dashboard comes with every BUILD.", "Widgets show K-φ's figures and flip to their table.", "Custom pages are for what no widget does."]),
        ], "check": [
            Q("You create a new Builder pass while an older one is still valid. What happens to the older one?", ["Both stay valid", "The older one is revoked", "The older one becomes read-only"], 1, "One pass at a time: creating a new one revokes the previous one."),
            Q("Your LLM deployed a page that broke a table that worked before. What is the best next step?", ["Ask it to fix everything at once", "Restore the last good version, then ask again in a smaller step", "Delete the BUILD"], 1, "Every deploy is a version. Restore, then make a smaller request."),
        ]},
        {"code": "B3", "title": "Data", "lessons": [
            L("B3.1", "Reading tenant data through the API", 8,
              "Read the account's figures the way K-φ computes them.",
              """
A BUILD reads the account through the K-φ API: who is calling and with which scopes (`/me`), the versions, the statements, the bank position, forecasts, invoices. The full list is in the API description your LLM reads from the pass.

Three rules keep a BUILD right:

- **Show figures as K-φ gives them.** Never recompute a figure K-φ already computed: a net income or a DSO rebuilt from raw lines will drift from the statement the CFO reads.
- **Follow the top bar.** Every BUILD page follows K-φ's top bar: version, entities, business unit, trading partner, consolidation, currency and units. A page that ignores it shows the group when the user selected one company.
- **Name the version.** Statements depend on the version (the closing) you ask for. A figure without its version cannot be checked.

When your LLM shows a figure, ask it which call and which version it came from. That answer is what you check against the screen.
""",
              "In your practice company, ask your assistant for Halden Trading Ltd's net income for September 2026, through the API. Check it against FP&A > P&L for the same month and company, then type it.",
              ["Read figures from the API; never recompute them.", "Every page follows the top bar.", "A figure is checked with its version."]),
            L("B3.2", "The Data library", 7,
              "Use public market and macro series with their source and licence.",
              """
**BUILD > Data library** is a catalogue of market, macro and public series: reference FX rates and interest rates from the European Central Bank, US series from FRED, and country indicators from the World Bank.

Each series shows:

- its **source** and its **licence**;
- the date of its **latest point**;
- how it is **refreshed** (daily series about every day, monthly and annual ones weekly), and whether the last refresh worked.

A BUILD reads a series through the same API as the account's data, so a page can put a margin call next to the curve it depends on. Every value comes with its source and, when the licence asks for it, the attribution text.

Before using a series, check its latest point. A daily series whose last point is a week old is a feed problem, not a quiet market.
""",
              "In your practice company, open BUILD > Data library, find the ECB's euro reference rate against the US dollar, and enter the date of its latest point.",
              ["Each series carries its source and licence.", "Check the date of the latest point before using it.", "BUILD reads series through the same API."]),
            L("B3.3", "Variables and Copy for an LLM", 8,
              "Load the account's own reference data and hand it to your LLM.",
              """
Some reference data is the client's own: a price list, a freight rate, a forward curve from their broker, a margin rate from their clearing house. In K-φ these are **variables**: series the account defines, read as `var.CODE` beside the public ones.

Variables are defined in CASH > Φ Setup > Data sources, and read in BUILD > Data library beside the public series. A variable gets its points through three doors, all into the same store:

- **A sheet or a file:** a tab named `VAR` (variable, date, key, value), or `VAR - BRENT` with dates down and values or tenors across.
- **Its endpoint:** the API defines a variable and loads its points, all or none.
- **Your LLM:** the same calls, through the pass or the MCP.

A point is a date, a key and a value. The key is empty for one value a day, or a tenor (3M, 10Y) for a curve.

**Copy for an LLM**, on the Data library and in Data sources, copies every series and variable with its latest value and how to read it. Paste it into your chat: your LLM then knows what exists, and does not invent a series.
""",
              "In your practice company, create a variable FREIGHT_RATE and load at least three monthly points, from a VAR tab or by asking your assistant. Then use Copy for an LLM and check that the variable is in the text.",
              ["Variables are the account's own reference series.", "Three doors, one store: sheet, endpoint, LLM.", "Copy for an LLM stops the LLM from inventing series."]),
            L("B3.4", "Licensed data stays with the client", 6,
              "Respect what each source allows.",
              """
Data comes with terms. The Data library shows each series' licence, and the engine follows it:

- **Open and attribution series** (ECB, FRED, World Bank) are stored once and shared. When the source asks for attribution, its text travels with every answer.
- **The account's own data** (its variables, its sheets and files) is **client-owned**: it stays in the account and is never served to anyone else.

Market data under a commercial licence (a terminal, an exchange feed) is not in the library. When a client needs it, they load it as their own variables, under their own licence, and it stays in their account. The same goes for sites whose terms forbid reuse: they are deliberately absent.

For a consultant, the rule is simple: never carry one client's variables into another client's BUILD, and never put licensed data in a page or function other people can call.
""",
              "In your practice company, open the Data library and check the licence of the FREIGHT_RATE variable you created. What does it say about who can read it?",
              ["The library shows each series' licence.", "The client's own data never leaves its account.", "Commercial feeds come in as the client's variables, under its licence."]),
        ], "check": [
            Q("Your LLM computes DSO itself from raw invoice lines and gets 71 days; the KPI page shows 73. What should the BUILD show?", ["71, since the LLM computed it from the lines", "73, the figure K-φ computed, read through the API", "The average of both"], 1, "Never recompute a figure K-φ already computed: show what the API gives, so the BUILD matches every other screen."),
            Q("A client loads its broker's forward curve as a variable. Who can read it?", ["Every K-φ account, like public series", "Only that account", "Anyone with the series code"], 1, "Variables are client-owned: they stay in the account and are never served to anyone else."),
        ]},
        {"code": "B4", "title": "Writing back", "lessons": [
            L("B4.1", "Write-back into Cash", 8,
              "Let a BUILD feed the cash forecast, within its limits.",
              """
A BUILD becomes part of treasury when its results reach CASH. With the **write:cash** scope, an extension can put **its own lines** in CASH > Cash forecasts: committed movements on a bank account and a day, for example the margin calls a model expects, or the retainage released when a job closes.

How these lines behave:

- **Tagged.** Each line carries the BUILD's name. The Cash worksheet, the CASH forecast and Claude in K-φ read them at once, and everyone sees where they came from.
- **Deleted, never edited.** A person can delete a BUILD's line, not change it. To change it, change the logic and let the BUILD write again.
- **All or nothing.** A write either saves every row or none, and says which row was refused and why. With "replace", the BUILD first removes the lines it wrote before: a forecast it recomputes never piles up.
- **Gone with the right.** Withdraw write:cash, or switch the extension off, and its lines leave every forecast at once.

A BUILD page can also sit in CASH > Forecast instead of BUILD, and a BUILD can set funding needs, the minimum to keep on each account, in CASH > Move > Funding needs.

Nothing here touches bank statements or the ledger: the BUILD writes forecasts, not facts.
""",
              "In your practice company, ask your assistant to put one forecast line from your BUILD: a payment of 25,000 GBP on Halden Trading Ltd's Operating account, on the 15th of next month. Then find it in CASH > Cash forecasts with your BUILD's name on it.",
              ["A BUILD writes its own forecast lines, tagged with its name.", "People delete them; only the BUILD rewrites them.", "Forecasts only: never statements or the ledger."]),
            L("B4.2", "Approval before the first write", 7,
              "Know which BUILD changes need a second person.",
              """
The changes that widen what a BUILD can do are under **dual control**: one admin proposes, a second confirms. The proposer can never confirm their own request.

They are:

- **naming a builder**, with or without the right for BUILD to write to CASH;
- **changing an extension**: switching it on, changing its scopes (adding write:cash, for example), its address or its limits;
- **registering an extension**;
- **issuing a server key**.

The second person is an approver of the account, from the roles already set in Admin > Governance; they approve or reject in Governance or in BUILD > Manage, and are told by email. An account with a single admin has no second person: K-φ confirms instead.

So before a BUILD's first line reaches the cash forecast, two people have agreed that it may: one who asked, one who confirmed. When you implement for a client, name the approver before the build starts, not on the day the first write is needed.
""",
              "In your practice company, open the audit trail and find who confirmed that you became a builder. In a client's account with two admins, who would have had to confirm it?",
              ["Widening a BUILD needs a second person.", "The proposer never confirms their own request.", "A single-admin account is confirmed by K-φ."]),
            L("B4.3", "What the audit trail records", 6,
              "Answer an auditor's questions about a BUILD.",
              """
Every step of a BUILD's life is in the account's audit trail, with who and when:

- **Rights:** a builder named or removed, a request proposed, confirmed, rejected or reminded, seats changed.
- **Credentials:** a Builder pass created, a server key issued or revoked.
- **Code:** each deploy with its one-line description, each restore of an earlier version.
- **Settings:** an extension created or changed, its secrets set (the names, never the values), the Copilot switched on for it.
- **Writes:** a function that changes data, called and by whom.

Beside it, the **call journal** in BUILD > Manage lists every API call the extension made: capability, answer, time taken.

An auditor's three questions have direct answers: who could change this logic (the builders and their approvals), what changed and when (the versions and deploys), and what it wrote (the tagged lines and the write calls).
""",
              "In your practice company, open the audit trail and find the Builder pass you created in B2.1, then the deploy from B2.2.",
              ["Rights, credentials, code, settings and writes are all recorded.", "Secrets are recorded by name, never by value.", "The call journal lists every API call."]),
        ], "check": [
            Q("A treasurer edits the amount of a line your BUILD put in the cash forecast. What happens?", ["The amount changes", "It is refused: a BUILD's line can be deleted, not changed", "The BUILD is switched off"], 1, "A BUILD's lines can be deleted by a person, never edited: the BUILD rewrites them from its logic."),
            Q("An admin proposes to give an extension the write:cash scope. Who can confirm it?", ["The same admin", "A second approver of the account, or K-φ for a single-admin account", "Any builder"], 1, "Dual control: the proposer never confirms their own request."),
        ]},
        {"code": "B5", "title": "Verifying AI-built logic", "lessons": [
            L("B5.1", "Building a known-answer case", 8,
              "Prove a calculation with a case whose answer you already know.",
              """
You do not read the code to know it is right. You test it with a **known-answer case**: inputs small enough to compute by hand, and the answer written down **before** the BUILD runs.

For a margin-call model, for example:

- one contract, one price move, one margin rate;
- the call you expect, computed on paper or in a spreadsheet you trust;
- then the same inputs in the BUILD.

Good cases are small and cover the edges: a price move of zero (no call), a move just below the threshold, a move in the other direction, two contracts that offset.

If the BUILD's answer differs, do not let the LLM "explain" the difference away. Either your case is wrong, and you correct it, or the logic is, and you ask for a fix with the case attached.
""",
              "Write a known-answer case for adding 20% VAT to a net amount: three inputs, including zero and a negative credit note, with the expected outputs. Ask your assistant for a BUILD page that takes a net amount and shows the VAT and the gross amount, then enter your three inputs.",
              ["Write the expected answer before the BUILD runs.", "Small cases that cover the edges.", "A difference means the case or the logic is wrong: find which."]),
            L("B5.2", "Signs, dates, units, quotes", 7,
              "Check the four places AI-built finance logic most often goes wrong.",
              """
Most errors in finance logic written by an LLM fall in four places:

- **Signs.** Is an outflow negative? Is a credit balance shown as a positive liability? K-φ's API states its conventions: check that the BUILD keeps them.
- **Dates.** Value date or booking date? Month end or calendar day? Is the last day of the month in or out?
- **Units.** Thousands or units, percent or decimal (5 or 0.05), one currency or several added together without conversion.
- **Quotes.** EUR/USD at 1.08 means one euro costs 1.08 dollars; inverted, every conversion is wrong by the same factor. Curves quoted in percent per year, not per month.

For each of the four, pick one figure in the BUILD and trace it to its source in K-φ or the Data library. One traced figure per risk catches most mistakes before a user does.
""",
              "In your practice company, pick one amount on a BUILD page and trace it: which API call, which version, which sign convention, which unit.",
              ["Signs, dates, units and quotes cause most errors.", "Trace one figure per risk to its source.", "Check the conventions the API states."]),
            L("B5.3", "Checking what was written, not what was shown", 6,
              "Verify a write by reading it back from K-φ.",
              """
A page can show the right figure and still have written the wrong one, or written nothing. When a BUILD writes, check the write itself:

- **Read back from K-φ**, not from the BUILD: the lines in CASH > Cash forecasts, with their amount, date, account and currency.
- **Count them.** The number of lines written should match the number the logic produced.
- **Run it twice.** With "replace", a second run must leave the same lines, not double them.

The BUILD's own message ("12 lines saved") is a claim. The lines in CASH are the fact.
""",
              "In your practice company, run the write from B4.1 a second time with \"replace\", then check in CASH > Cash forecasts that there is still exactly one line from your BUILD.",
              ["Read the write back from K-φ, not from the page.", "Count the lines.", "A second run must not double them."]),
            L("B5.4", "Keeping the test with the extension", 6,
              "Make the known-answer case part of the BUILD.",
              """
A test kept in a notebook is lost the day someone else changes the BUILD. Keep it **with** the extension.

K-φ helps for functions: each function declares an **example**, an input with its expected output, and K-φ refuses a deploy whose example does not fit the function's schemas. Put your known-answer case there: it is the function's test, and it is what the developer page shows to anyone who calls it.

For pages and writes, ask your LLM to keep a short test file in the BUILD that lists each known-answer case and how to run it, and to run it before every deploy. After a restore, run it again.

The rule for a consultant handing over a BUILD: no logic without its known-answer case, and no case without the person who confirmed the expected answer.
""",
              "In your practice company, ask your assistant to declare a function add_vat with your known-answer case from B5.1 as its example, and deploy. Then ask it to deploy an example whose output is text instead of a number: K-φ refuses it.",
              ["Keep each known-answer case in the BUILD.", "A function's example is its test, checked at deploy.", "Run the tests again after a restore."]),
        ], "check": [
            Q("Your BUILD says \"12 lines saved\". How do you verify the write?", ["Trust the message", "Read the lines back in CASH > Cash forecasts and count them", "Ask the LLM if it is sure"], 1, "The message is a claim; the lines in K-φ are the fact."),
            Q("A conversion uses EUR/USD 1.08 the wrong way round. What do you see?", ["Nothing: the rate is the same", "Every converted amount is wrong by the same factor", "Only the totals are wrong"], 1, "An inverted quote makes every conversion wrong by the same factor: trace one figure to catch it."),
        ]},
        {"code": "B6", "title": "Publishing", "lessons": [
            L("B6.1", "Functions as APIs", 8,
              "Turn the logic you built into an API the client's other tools call.",
              """
Any reusable logic in a BUILD (a calculation, an allocation, a rule, a check) belongs in a **function**. K-φ serves each function as an API at `/api/v1/fn/<name>`, so the account can call it from its other systems, Excel, a sheet or another tool.

A function declares, in the BUILD:

- its **name** and a one-line **summary**;
- its **input** and **output**, as schemas: K-φ checks the input before calling and the output after;
- whether it **writes** (changes data) or only reads;
- an **example** input and output: its test (lesson B5.4).

K-φ signs every call it forwards to the BUILD, and the BUILD refuses any call without a valid signature. The function's address is public; the signature is what proves the call came from K-φ.

Tell the user in their words: "allocate_cash is now callable from your other tools: it takes a date and returns the split by entity."
""",
              "In your practice company, ask your assistant to list the account's functions through the API, and check that add_vat shows its summary, schemas and example. A practice BUILD lists functions but does not run them: they run on a client's own BUILD service.",
              ["Reusable logic goes in a function.", "K-φ checks inputs and outputs against the schemas.", "Every call is signed by K-φ."]),
            L("B6.2", "Who can call a function", 6,
              "Give the right key to the right caller.",
              """
A function is called with an API key of the account. An admin creates keys in Settings > API keys and chooses their scopes:

- **run:build** calls the functions that only read.
- **run:build:write** also calls the functions that change data. An admin grants it deliberately, and each call is recorded in the audit trail.

Give each caller its own key: one for the Excel workbook, one for the ERP, one for a sheet. When one caller stops, revoke its key; the others keep working.

A Builder pass can call its own functions to test them, but it is not a key to hand to another system: it expires in 7 days and belongs to its builder.
""",
              "In your practice company, create a key named \"Excel VAT\" with the run:build scope only. Which of your functions can it call?",
              ["run:build reads; run:build:write also changes data.", "One key per caller, revoked on its own.", "A Builder pass is for building, not for other systems."]),
            L("B6.3", "Claude in K-φ uses your BUILD", 6,
              "Let the team use the BUILD from K-φ's own assistant.",
              """
When an admin switches it on in BUILD > Manage, Claude in K-φ can use the BUILD:

- **open its pages** on the person's screen ("show me the margin calls");
- **read what the BUILD stores** for the account;
- **call its functions**, with the same checks as any caller.

A function that changes data never runs from the assistant on its own: Claude in K-φ says what it will do, and it runs only when the person clicks **Confirm**.

This is where a BUILD pays off for the team: the logic one builder wrote becomes something every user can ask for in plain words, inside K-φ, with the figures K-φ already holds.
""",
              "In your practice company, switch the BUILD on for Claude in K-φ in BUILD > Manage, then ask it to open your bank accounts page.",
              ["Claude in K-φ opens BUILD pages, reads its data and calls its functions.", "A function that writes waits for the person's Confirm.", "One builder's logic, usable by the whole team."]),
        ], "check": [
            Q("An ERP must call a function that writes cash lines. Which key?", ["A Builder pass", "Its own key with run:build:write", "Any key with run:build"], 1, "Writing functions need run:build:write, granted deliberately, on a key of the ERP's own."),
            Q("A user asks Claude in K-φ to run a function that changes data. What happens?", ["It runs at once", "Claude says what it will do; it runs when the person clicks Confirm", "It is refused"], 1, "A function that writes waits for the person's confirmation."),
        ]},
    ],
    "exam": {
        "title": "Exam: one build, start to finish",
        "situation": "The exam of the K-φ Builder path. You get an exam company: Halden with its three companies, 23 months of ledger and its banks, and its own BUILD. The CFO wants the corporate tax on the third quarter in the cash forecast: for each company, 25% of its net income for July to September 2026, paid on 15 December 2026 from its Operating account, in its currency. Your assistant builds it with a Builder pass; you check it. Every step is something you did in a lesson; the lesson is named at the end of the step. Allow about an hour.",
        "tasks": [
            "Start: press Start exam on the right, then Open my exam company. Its BUILD is in the menu, with you as its builder.",
            "The page: in BUILD > Manage, create a Builder pass and paste it into your assistant. Ask for a page \"Tax payments\" that shows, for each company, its net income for July to September 2026 read through the API, and the tax at 25%. Check one company against FP&A > P&L. (B2.1, B3.1)",
            "A rollback: ask for a change to the page, restore the version before it, then ask for one more change, so a new version sits on top of the restored one. (B2.2)",
            "The function: have the tax logic declared as a function too, with a known-answer case as its example, for instance a net income of 100,000 giving a tax of 25,000. (B5.4)",
            "The payments: ask your assistant to write one payment per company to the cash forecast, then run it a second time with \"replace\". Check in CASH > Cash forecasts that there is exactly one line per company. (B4.1, B5.3)",
            "The key: in Settings > API keys, create a key for the system that will call your function, with the run:build scope only. (B6.2)",
            "Check: press Check my exam company. Every step shows PASS, or says what is missing.",
            "Answer and submit: the tax Halden Trading Ltd will pay on 15 December 2026, as your page shows it, in GBP. Type the amount only, then submit.",
        ],
        "checks": [
            "Your BUILD has a page of its own, deployed",
            "A version was restored, and a new one deployed on top of it",
            "A function is declared with its known-answer example",
            "One tax payment per company on 15 December 2026, from each Operating account, at 25% of the quarter's net income",
            "A key with run:build only, for the function's callers",
            "The tax of Halden Trading Ltd you typed is right",
        ],
        "report": [
            ["pass", "A BUILD page", "Your BUILD menu shows \"Tax payments\"."],
            ["pass", "A rollback, then a new version", "\"Restored version 1: tax page\", then 1 version deployed after it."],
            ["pass", "A function with its known-answer example", "Function quarter_tax, with its example: K-φ checked it at deploy."],
            ["fail", "The tax payments in the cash forecast", "6 lines for 3 companies: a second run added instead of replacing. Write with \"replace\"."],
            ["pass", "A key for the function's callers", "Key \"ERP tax\": run:build only."],
            ["pass", "The figure on your page", "Right: 23,070.91 GBP."],
        ],
    },
}
