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
- **Scopes.** An extension can hold at most these rights: read the ledger, cash and forecasts; write scenarios, its own store and, if granted, its own cash forecast lines; read and deploy its own code.
- **Never.** No ledger import, no change to the account's configuration, no change to FP&A or CASH pages. Bank statements and posted entries are never written by a BUILD.
- **A switch.** Turn the extension off, or revoke its key, and the next call is refused.

Every call an extension makes is recorded: which capability, the answer, how long it took. An admin reads that log in BUILD > Manage.

So when a client asks "can the AI break our books?", the answer is no: it can only reach what its scopes allow.
""",
              "In your practice company, open BUILD > Manage and read the scopes of the extension. Which of them would let it put lines in the cash forecast?",
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
              "In your practice company, ask your assistant for one page that lists Halden's bank accounts with their balances. Then open BUILD > Manage > Versions and find the version it created.",
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
              "In your practice company, ask your assistant for Halden Trading Ltd's net income for the latest version, through the API. Check it against FP&A > P&L for the same version and company, then enter it.",
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
    ],
}
