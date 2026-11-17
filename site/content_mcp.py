# Course M: MCP, K-φ in your AI assistant (owner, 2026-11-17: "for AI foundation path: add a course on MCP.
# explain what a public vs a private MCP offers, applied for K-phi. propose to test the public MCP (create a GL
# and upload it). validate with a QCM").
from content_fpa import L, Q

COURSE = {
    "id": "mcp", "code": "M", "title": "MCP: K-φ in your AI assistant", "badge": "MCP", "duration": "About 45 minutes", "status": "available",
    "audience": "Everyone on the AI Foundation path, after Agentic finance.", "prereq": "Agentic finance",
    "summary": "The two doors K-φ opens to AI assistants: the public MCP, for anyone and any ledger, and the private MCP, for your own company with your rights.",
    "outcomes": [
        "Explain what MCP is, in one sentence a CFO understands.",
        "Tell what K-φ's public MCP offers, and what it never does.",
        "Tell what K-φ's private MCP offers, and how its access is controlled.",
        "Analyse a ledger with the public MCP, and know which door fits which need.",
    ],
    "lab": "Practise with your own AI assistant (Claude, ChatGPT or another that takes connectors) and a ledger file: the one of your practice company, or one you make.",
    "chapters": [
        {"code": "M1", "title": "Two doors into K-φ", "lessons": [
            L("M1.1", "What MCP is", 5,
              "Say what MCP is and why it matters in finance.",
              """
**MCP, the Model Context Protocol**, is a common way for an AI assistant to find and call another system's **tools**. A system that speaks MCP publishes a list of what it can do (“give the P&L”, “analyse this ledger”), with what each tool needs. The assistant reads the list, picks the tool, calls it, and reports the answer.

Why it matters in finance:

- **The figure comes from the system, not from the model.** When an assistant gives you an EBITDA through K-φ's MCP, K-φ's engine computed it; the model reports it. That is the difference between a figure you can audit and one the model made up (course Agentic finance, A5).
- **One connection, any assistant.** Claude, ChatGPT and other assistants that take MCP connectors all reach the same K-φ tools. You do not rebuild anything when you change assistant.
- **The system decides what is allowed.** The tools a server offers, and the rights of the credential behind them, are set on K-φ's side, not in the conversation.

K-φ has **two** MCP servers, for two different needs: the **public** one and the **private** one. The next two lessons take them in turn.
""",
              "In your AI assistant, open its list of connectors (or integrations) and find where you would add one. Do not add anything yet.",
              ["A protocol for an assistant to call a system's tools.", "The figure comes from the system, not the model.", "K-φ has two servers: public and private."]),
            L("M1.2", "The public MCP: any ledger, no account", 7,
              "Know what the public MCP offers, to whom, and what it never does.",
              """
K-φ's **public MCP** is listed in the assistants' directories under the name **K-φ** (in Claude: claude.ai/directory/k-phi). Anyone adds it in two clicks. It needs **no K-φ account, no key, no approval**.

**What it does.** You give it a general ledger (a trial balance or an ERP export: CSV, TSV or Excel, from SAP, QuickBooks, Xero, Sage or any other) and it returns:

- the **statements**: P&L, balance sheet, cash flow;
- **30 KPIs** with their formulas and thresholds: margins, EBITDA, DSO, DPO, DIO and the others;
- **bank covenants**: DSCR, debt to EBITDA, interest coverage, with their status;
- a **cash forecast** per company and per business unit, with the DSO and DPO observed in the ledger;
- a **report link** to the full interactive analysis.

**How the file gets there.** A ledger is often too big for a chat. The assistant asks the public MCP for an **upload link**; you drop the file on that page; the assistant then fetches the analysis. Only when the ledger is already text in the conversation does the assistant send it directly.

**What it never does.**

- **It never touches a K-φ company.** Each file is analysed in an **isolated sandbox**, deleted within **24 hours** unless you claim it into an account.
- **It does not consolidate.** A file with several companies is **summed as it is**: no currency conversion, no intercompany elimination. Read each company in its own currency.
- **It does not compute in the model.** The figures are the engine's, traceable to the ledger lines.

**Who it is for.** A prospect who wants to see what K-φ makes of their books before signing; a consultant who receives a ledger and wants a first reading in minutes; anyone checking a figure without setting up a company.
""",
              "Add the K-φ connector to your assistant from its directory. You will use it in M2.1.",
              ["No account, no key: any ledger, from the directory.", "Statements, 30 KPIs, covenants, forecast, a report link.", "A sandbox, deleted within 24 hours; no consolidation."]),
            L("M1.3", "The private MCP: your company, your rights", 7,
              "Know what the private MCP reaches and how access to it is controlled.",
              """
K-φ's **private MCP** is the whole application served to your assistant: **your** company, with its versions, statements, forecast, scenarios and budgets. Its address is your K-φ address followed by **/mcp** (for example https://k-phi.com/mcp).

**What it offers.** Tools that **read** (the P&L, the balance sheet, cash flow, KPIs, the forecast, variances, the ledger versions, the accounts) and tools that **write** (save a scenario, create a budget version, set a flow rule). An assistant connected to it answers “why did October's margin drop?” from your own books, and saves the scenario you agree on into K-φ.

**How you connect it.** Two ways:

1. **Sign in as yourself.** Add K-φ as a custom connector with its /mcp address: the assistant sends you to K-φ's sign-in, and the connection then carries **your** rights.
2. **An API key.** In Admin, AI tab, API keys, an owner creates a key with the scopes the job needs. **mcp:tools** gives every read scope and nothing else; **mcp:write** adds the write scopes. K-φ shows the connector settings to copy next to the key.

**How it stays safe.**

- **One company.** A credential reaches the company it belongs to, never another.
- **Scopes.** A key that only reads cannot change anything, whatever the conversation asks.
- **Every call is recorded** in K-φ's audit trail, under the key's label or the user who signed in. “The assistant did it” is never an answer: the trail says which credential did.
- **The rules of the company still apply.** A change that needs a second admin's approval waits for one.

**Public or private?** The public MCP answers “what does K-φ make of this ledger?” for anyone. The private MCP answers “what is happening in my company, and can we act on it?” for the people of that company.
""",
              "In your practice company, open Admin, AI tab, API keys, and read the scopes a key can hold. Note which ones mcp:tools includes. Create nothing.",
              ["Your company: read and write tools.", "Sign in as yourself, or a key with the right scopes.", "One company, scopes, every call in the audit trail."]),
        ], "check": [
            Q("What does an assistant need to use K-φ's public MCP?", ["A K-φ API key", "Nothing but the K-φ connector from its directory", "An owner's approval"], 1, "The public MCP is open: no account, no key."),
            Q("Where does the private MCP's EBITDA come from?", ["The model's arithmetic", "K-φ's engine", "The last chat"], 1, "Through either server, the engine computes and the model reports."),
            Q("An assistant must only read your figures. Which key?", ["One with mcp:tools", "One with mcp:write", "The owner's password"], 0, "mcp:tools holds every read scope and nothing that writes."),
        ]},
        {"code": "M2", "title": "Try it", "lessons": [
            L("M2.1", "Analyse a ledger with the public MCP", 12,
              "Get K-φ's analysis of a ledger from your assistant, and read it critically.",
              """
**1. Have a ledger.** Any general ledger works: one line per posting with a date, a company, an account, a description, a debit, a credit and a currency. Take the ledger file of your practice company (lesson S0.2), or make one in a spreadsheet: a few dozen lines over two or three months are enough. Make it balance: every month, debits equal credits.

**2. Ask your assistant.** With the K-φ connector added (M1.2), attach nothing yet and write: “Analyse my general ledger with K-φ.” The assistant calls the public MCP and gives you an **upload link**.

**3. Drop the file on that page.** One step, a few seconds, nothing to fill in. Come back to the conversation.

**4. Read what comes back.** The assistant shows the summary (statements, KPIs, covenants, forecast) and the **report link**. Open the report.

**5. Check it.** Pick three figures and trace them:

- **Revenue of one month**: sum the revenue lines of that month in your file. Same figure?
- **One KPI**: the report gives its formula; recompute it from two statement lines.
- **A company in another currency**, if your file has one: its figures are in its own currency, and the group total adds them as they are.

If a figure differs, the file usually explains it: a sign convention, a missing month, an account in the wrong class. That reading is the skill, not the button.

Your file sits in a sandbox and is deleted within 24 hours. Nothing reaches your practice company.
""",
              "Run the five steps with your practice ledger or one you made, and trace three figures from the report back to the file.",
              ["Ask, get an upload link, drop the file.", "Statements, KPIs, covenants, forecast, a report.", "Trace three figures back to the file."]),
            L("M2.2", "Which door, when", 5,
              "Choose the right door for a request, and say why.",
              """
| Request | Door | Why |
|---|---|---|
| “What would K-φ make of our ledger?” (before any contract) | **Public** | No account; a sandbox that disappears |
| A consultant gets a client's export and wants a first reading today | **Public** | Minutes, no set-up, nothing kept |
| “Why did our October margin drop?” | **Private** | It needs your company's versions and history |
| “Save this as a scenario”, “create Budget 2027 v2” | **Private**, a credential that may write | Writes are recorded and follow the company's rules |
| A dashboard tool that only reads figures every morning | **Private**, a key with read scopes | One key per job, only what it needs |
| “Consolidate our three companies in USD” | **Private** (K-φ's consolidation) | The public MCP sums as it is, without conversion |

Two habits whichever the door:

- **The number is the engine's.** If an assistant gives a figure it did not get from a tool, ask it for the source.
- **No secret in a conversation.** A key goes in the connector's settings, never in a message.
""",
              "For each request in the table, say aloud which door and why, before reading the answer column.",
              ["Public: any ledger, first reading, nothing kept.", "Private: your company, history, actions.", "Figures from the engine; no secret in a chat."]),
        ], "check": [
            Q("You uploaded a ledger through the public MCP. What happens to it?", ["It joins your practice company", "It is analysed in a sandbox, deleted within 24 hours unless claimed", "It is kept forever"], 1, "The public MCP never touches a K-φ company."),
            Q("A request to consolidate three companies in USD. Which door?", ["Public", "Private", "Either"], 1, "The public MCP sums as it is; consolidation is K-φ's, in your company."),
        ]},
    ],
    "exam": {
        "title": "Exam: ten questions on K-φ's two MCP doors",
        "situation": "No company to set up: ten multiple-choice questions on what the public and the private MCP offer, how they are reached, and which fits which need. Eight right answers pass.",
        "tasks": [
            "Start: press Start exam on the right. The questions appear once the exam has started.",
            "Answer the ten questions: one choice each. Chapter M1 has every answer; M2.1 shows them at work.",
            "Submit: the result comes at once, with the numbers of any question not right."
        ],
        "checks": [
            "Eight of the ten answers are right"
        ],
        "report": [
            ["pass", "Your answers", "9 of 10 right (not right: question 5)."]
        ]
    },
}
