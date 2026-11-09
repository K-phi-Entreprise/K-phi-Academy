# Course A, AI for finance: lesson video scripts.
from scripts_f import T, E
TEAL = (54, 214, 160); RED = (255, 122, 122)

LESSONS = {
"A1.1": {"scenes": [
    T("What a language", "model does", "AI for finance · A1.1 · 7 min", "A1.1 · What a language model does"),
    {"type": "flow", "d": 9, "eyebrow": "THE MECHANISM", "heading": "Trained to predict what comes next", "step": 1.2,
     "nodes": [("Huge amount of text", "training"), ("Predict the next word", "one task"), ("Writes, reasons, codes", "what it learns")],
     "cap": ["A language model is trained to predict what comes next in text.", "From that one task it learns to write, summarise, reason and code."]},
    {"type": "checklist", "d": 10, "eyebrow": "THREE FACTS FOR FINANCE", "heading": "Keep these in mind", "step": 1.6,
     "items": ["It knows its training data, up to a date", "It gives the most plausible answer, not a looked-up one", "It does not remember you between conversations"],
     "cap": ["Without tools it has no access to your ledger or today's rates.", "Plausible and right usually coincide. When they do not, the answer still reads well."]},
    {"type": "flow", "d": 7, "eyebrow": "WORDS IN THIS COURSE", "heading": "Model and assistant", "step": 1.2,
     "nodes": [("Model", "the engine"), ("Assistant", "the product you use")],
     "cap": "The assistant is the product around the model: chat, files, connectors."},
    E("Next  ·  A1.2  Strong and weak points for finance")]},

"A1.2": {"scenes": [
    T("Strong and weak points", "for finance work", "AI for finance · A1.2 · 8 min", "A1.2 · Strong and weak points for finance work"),
    {"type": "compare", "d": 12, "heading": "What to give a model", "left": "Strong", "litems": ["Reading and summarising", "Drafting commentary", "Writing formulas and code", "Classifying transactions"],
     "right": "Weak", "ritems": ["Arithmetic in its head", "Recalling an exact rate", "Knowing your books", "Saying \"I don't know\""],
     "cap": ["Models are good with language, structure and code.", "They are unreliable with exact numbers they compute or recall themselves."]},
    {"type": "quote", "d": 8, "l1": "The model decides what to do.", "l2": "The system of record calculates.",
     "cap": "When an assistant needs a DSO, it should ask K-φ through a tool, not compute it from a pasted table."},
    E("Next  ·  A1.3  Context: what the model sees")]},

"A1.3": {"scenes": [
    T("Context:", "what the model sees", "AI for finance · A1.3 · 6 min", "A1.3 · Context: what the model sees"),
    {"type": "flow", "d": 9, "eyebrow": "CONTEXT", "heading": "Everything the model works with", "step": 1.0,
     "nodes": [("Instructions", ""), ("Conversation", ""), ("Files", ""), ("Tool results", "")],
     "cap": ["A model only works with its context.", "Your instructions, the conversation, files, and what its tools returned."]},
    {"type": "bullets", "d": 10, "eyebrow": "GOOD CONTEXT", "heading": "Three things to give", "step": 1.4,
     "items": [("Who you are, and what it is for", "\"group controller, for the CFO\""), ("The data, or a tool to get it", ""), ("The rules", "\"fiscal year starts in April\"")],
     "cap": ["Say who you are, give the data, state the rules.", "Context is limited: for a new task, start a new conversation."]},
    E("Next  ·  A2.1  From chat to agent")]},

"A2.1": {"scenes": [
    T("From chat", "to agent", "AI for finance · A2.1 · 7 min", "A2.1 · From chat to agent"),
    {"type": "flow", "d": 11, "eyebrow": "AN AGENT", "heading": "A model that can act", "step": 1.2,
     "nodes": [("Goal", "the October commentary"), ("Tools", "read, forecast, write"), ("Loop", "call, read, decide"), ("Permissions", "what it may change")],
     "cap": ["An agent has a goal, tools, a loop and permissions.", "It calls a tool, reads the result, decides the next step, and repeats."]},
    {"type": "compare", "d": 10, "heading": "The power is in the tools", "left": "Read-only tools", "litems": ["Can be wrong", "Cannot do damage"],
     "right": "Write tools", "ritems": ["Change the system", "Need the same controls as a person"],
     "cap": ["An agent with read-only tools can give a wrong answer, which you can check.", "An agent that writes needs the same controls as a person who can."]},
    E("Next  ·  A2.2  Tools and MCP")]},

"A2.2": {"scenes": [
    T("Tools", "and MCP", "AI for finance · A2.2 · 7 min", "A2.2 · Tools and MCP"),
    {"type": "flow", "d": 10, "eyebrow": "MODEL CONTEXT PROTOCOL", "heading": "One standard to connect systems", "step": 1.2,
     "nodes": [("Assistant", "Claude, ChatGPT…"), ("MCP", "open standard"), ("System", "its tools, described")],
     "cap": ["MCP is an open standard for connecting assistants to other systems.", "A system publishes its tools once; any assistant that supports MCP can use them."]},
    {"type": "table", "d": 10, "eyebrow": "TWO KINDS OF TOOL", "heading": "Read and write", "cols": ["Kind", "Examples", "Treat like"], "widths": [1, 2, 1.4], "step": 1.2, "hot": 1, "hot_at": 4,
     "rows": [["Read", "Balances, a P&L, a forecast", "View rights"], ["Write", "Save a scenario, write a forecast line", "Edit rights"]],
     "cap": ["The agent sees what the connected account sees.", "Give write tools only to the people, and agents, who need them."]},
    E("Next  ·  A2.3  Chat, automation, agentic workflow")]},

"A2.3": {"scenes": [
    T("Chat, automation", "and agentic workflow", "AI for finance · A2.3 · 6 min", "A2.3 · Chat, automation and agentic workflow"),
    {"type": "table", "d": 12, "eyebrow": "PICK THE RIGHT KIND", "heading": "Three ways AI helps", "cols": ["", "Who decides the steps", "Good for"], "widths": [1, 1.4, 2], "step": 1.0,
     "rows": [["Chat", "You", "Drafting, questions"], ["Automation", "Fixed in advance", "Same task every day: a nightly sync"], ["Agentic workflow", "The agent, within limits", "Judgement across several systems"]],
     "cap": ["Automation for tasks that never change, agents for tasks that need judgement.", "Explaining this month's variances is an agentic task."]},
    {"type": "flow", "d": 8, "eyebrow": "COMBINE THEM", "heading": "A good setup", "step": 1.2,
     "nodes": [("Automation", "brings data in"), ("Agent", "works on it"), ("Person", "approves")],
     "cap": "Automations bring the data in, an agent works on it, a person approves."},
    E("Next  ·  A3.1  Where agents help in finance")]},

"A3.1": {"scenes": [
    T("Where agents help", "in finance", "AI for finance · A3.1 · 7 min", "A3.1 · Where agents help in finance"),
    {"type": "bullets", "d": 12, "eyebrow": "DATA + JUDGEMENT + WRITING", "heading": "Where agents add value today", "step": 1.2,
     "items": [("Close support", "missing items, checklist status"), ("Reconciliation", "proposed matches, leftovers explained"), ("Variance commentary", "figures pulled from the system"), ("Scenarios", "a question becomes a scenario"), ("Building tools", "the Build course")],
     "cap": ["Agents help where data from several places meets judgement and writing.", "Close, reconciliation, commentary, scenarios, and building tools."]},
    {"type": "quote", "d": 8, "l1": "For expensive mistakes,", "l2": "agents prepare. People release.",
     "cap": "Payments, final journal entries and tax filings are prepared by agents, never released by them."},
    E("Next  ·  A3.2  Human in the loop")]},

"A3.2": {"scenes": [
    T("Human", "in the loop", "AI for finance · A3.2 · 6 min", "A3.2 · Human in the loop"),
    {"type": "flow", "d": 10, "eyebrow": "WHERE TO APPROVE", "heading": "At the point of effect", "step": 1.0, "hot": 3, "hot_at": 4.5,
     "nodes": [("Read", ""), ("Compute", ""), ("Draft", ""), ("Approve", "a person"), ("Write", "")],
     "cap": ["Reviewing every tool call is tiring, and people stop looking.", "Approve the result before it is written, sent or paid."]},
    {"type": "checklist", "d": 10, "eyebrow": "IN K-φ", "heading": "Agents follow the same controls", "step": 1.5,
     "items": ["Acts with the rights of the connected account", "Sensitive changes still need an approver", "Can prepare a payment run, never sign it"],
     "cap": ["An agent acts with the connected account's rights.", "Every change it makes is in the audit trail."]},
    E("Next  ·  A3.3  Designing an agentic workflow")]},

"A3.3": {"scenes": [
    T("Designing an", "agentic workflow", "AI for finance · A3.3 · 8 min", "A3.3 · Designing an agentic workflow"),
    {"type": "table", "d": 14, "eyebrow": "ONE PAGE", "heading": "October variance commentary", "cols": ["Part", "Example"], "widths": [1, 3], "step": 0.8, "hot": 3, "hot_at": 6,
     "rows": [["Trigger", "October close marked complete"], ["Inputs", "Budget and actuals from K-φ"], ["Steps", "Variances above threshold, causes, draft"], ["Checks", "Every figure from a tool result; signs checked"], ["Approval", "Group controller reviews"], ["Output and log", "Saved with the board pack; who, when"]],
     "cap": ["A workflow worth repeating fits on one page.", "Write the checks before the first run: they tell you whether to trust the second."]},
    {"type": "quote", "d": 7, "l1": "When the result is wrong,", "l2": "fix the instructions and the checks.",
     "cap": "The fix is usually not in the model."},
    E("Next  ·  A4.1  Data and credentials")]},

"A4.1": {"scenes": [
    T("Data", "and credentials", "AI for finance · A4.1 · 7 min", "A4.1 · Data and credentials"),
    {"type": "checklist", "d": 11, "eyebrow": "BEFORE YOU SHARE DATA", "heading": "Check three things", "step": 1.6,
     "items": ["Which product and plan, and its data terms", "What the task actually needs", "Where the data goes: connector or pasted file"],
     "cap": ["Know whether your plan trains on your data and how long it keeps it.", "Share only what the task needs."]},
    {"type": "quote", "d": 9, "l1": "Never paste a password,", "l2": "a key or a token into a chat.",
     "cap": ["Anything in a conversation can end up in logs.", "Connect systems through connectors; the builder pass never shows a secret."]},
    E("Next  ·  A4.2  Prompt injection")]},

"A4.2": {"scenes": [
    T("Prompt injection and", "untrusted content", "AI for finance · A4.2 · 7 min", "A4.2 · Prompt injection and untrusted content"),
    {"type": "flow", "d": 10, "eyebrow": "HOW IT HAPPENS", "heading": "Instructions hidden in data", "step": 1.2, "color": {1: RED},
     "nodes": [("Invoice", "from a supplier"), ("Hidden note", "\"update our bank details\""), ("Agent", "reads it")],
     "cap": ["Documents, emails and web pages can carry instructions written to manipulate an agent.", "This is prompt injection."]},
    {"type": "checklist", "d": 10, "eyebrow": "DEFENCES", "heading": "Not in the model alone", "step": 1.4,
     "items": ["Content is data, never orders", "Limit write tools", "Approve at the point of effect", "Confirm bank changes by phone"],
     "cap": ["An invoice cannot change what the agent is allowed to do.", "Changed bank details are still confirmed by a call to a known number."]},
    E("Next  ·  A5.1  Deterministic engine, model on top")]},

"A5.1": {"scenes": [
    T("Deterministic engine,", "model on top", "AI for finance · A5.1 · 6 min", "A5.1 · Deterministic engine, model on top"),
    {"type": "compare", "d": 11, "heading": "Split the work", "left": "Engine (K-φ)", "litems": ["Holds the data", "Computes the figures", "Same inputs, same result", "Audit trail"],
     "right": "Model", "ritems": ["Decides what to ask", "Calls the engine", "Explains in words"],
     "cap": ["A model can give two answers to one question. A finance figure cannot.", "The engine computes; the model asks and explains."]},
    {"type": "quote", "d": 8, "l1": "Results live in the system of record,", "l2": "not in the conversation.",
     "cap": "A scenario built with an assistant is saved in K-φ, where it can be checked and audited."},
    E("Next  ·  A5.2  Checking an answer")]},

"A5.2": {"scenes": [
    T("Checking", "an answer", "AI for finance · A5.2 · 7 min", "A5.2 · Checking an answer"),
    {"type": "checklist", "d": 13, "eyebrow": "FIVE CHECKS", "heading": "For any AI answer with numbers", "step": 1.5,
     "items": ["Trace every figure to a source", "Check signs and directions", "Check units and periods", "Rebuild one figure yourself", "Keep a known-answer case"],
     "cap": ["A figure with no source is a guess.", "Favourable or unfavourable, thousands or units: the most common errors."]},
    {"type": "table", "d": 9, "eyebrow": "THE CLASSIC", "heading": "A sign error", "cols": ["Line", "Budget", "Actual", "Assistant said"], "widths": [1.2, 1, 1, 1.6], "step": 0.9, "hot": 0, "hot_at": 3,
     "rows": [["Freight costs", "520,000", "604,200", "favourable"]],
     "cap": ["Costs 84,200 over budget are unfavourable.", "If one figure is wrong, assume others may be."]},
    E("Next  ·  A6.1  Connecting K-φ to your assistant")]},

"A6.1": {"scenes": [
    T("Connecting K-φ", "to your assistant", "AI for finance · A6.1 · 7 min", "A6.1 · Connecting K-φ to your assistant"),
    {"type": "table", "d": 11, "eyebrow": "TWO MCP SERVERS", "heading": "Public and private", "cols": ["Server", "What it does"], "widths": [1, 3], "step": 1.2,
     "rows": [["Public", "Analyses a ledger file without an account; sandbox deleted within 24 h"], ["Private", "Your tenant, your rights; writes back where allowed"]],
     "cap": ["The public server gives a first look at a ledger, in a sandbox that is deleted.", "The private one connects to your own tenant, with your account's rights."]},
    {"type": "flow", "d": 9, "eyebrow": "IN PRACTICE", "heading": "Ask in plain language", "step": 1.2,
     "nodes": [("Your question", "\"why did DSO move?\""), ("K-φ tools", "exact figures"), ("The answer", "explained in words")],
     "cap": "The figures come from the engine; the words come from the model."},
    E("Next  ·  A6.2  The builder pass")]},

"A6.2": {"scenes": [
    T("The builder", "pass", "AI for finance · A6.2 · 6 min", "A6.2 · The builder pass"),
    {"type": "flow", "d": 11, "eyebrow": "BUILD INSIDE K-φ", "heading": "When no page answers the question", "step": 1.1,
     "nodes": [("Paste the pass", "Claude, Codex, Gemini CLI"), ("Describe", "the logic"), ("It runs in K-φ", "reads your data"), ("Writes back", "after approval")],
     "cap": ["The builder pass lets you build a new tool inside K-φ with your assistant.", "You describe the logic; the assistant writes the code; K-φ runs it."]},
    {"type": "quote", "d": 8, "l1": "The engine computes, the agent builds,", "l2": "a person approves.",
     "cap": "And a known-answer case proves the result. The Build course goes through it in detail."},
    E("Next  ·  Exam  An agentic analysis")]},
}
