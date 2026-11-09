# Cash course: lesson video scripts.
from scripts_f import T, E
from scripts_p import S
M = lambda code, mins: f"Cash · {code} · {mins} min"
RED = (255, 122, 122); TEAL = (54, 214, 160)

LESSONS = {
"C1.1": {"scenes": [
    T("Accounts by entity", "and by pool", M("C1.1", 7), "C1.1 · Accounts by entity and by pool"),
    {"type": "compare", "d": 9, "heading": "Two views of the same accounts", "left": "By entity", "litems": ["One legal company each", "What auditors read"], "right": "By pool", "ritems": ["Managed together", "What treasury reads"],
     "cap": ["Every account belongs to one entity.", "Accounts managed together form a pool."]},
    S("bank_accounts", ["Name accounts so people recognise them.", "Payment-provider accounts stay out of the bank list."], d=8),
    E("Next  ·  C1.2  Header accounts and reserves")]},
"C1.2": {"scenes": [
    T("Header accounts", "and reserves", M("C1.2", 6), "C1.2 · Header accounts and reserves"),
    {"type": "flow", "d": 10, "eyebrow": "A POOL", "heading": "One header holds the reserve", "step": 1.1, "hot": 1, "hot_at": 3,
     "nodes": [("GBP collections", ""), ("Header", "HSBC GBP main"), ("GBP payments", "")],
     "cap": ["The header receives the sweeps or funds the others.", "Transfers inside a pool are internal: never income, never spending."]},
    E("Next  ·  C1.3  Daily balances and history")]},
"C1.3": {"scenes": [
    T("Daily balances", "and history", M("C1.3", 5), "C1.3 · Daily balances and history"),
    S("bank_dash", ["K-φ stores each account's balance day by day.", "Any past position can be rebuilt: month end, a covenant date, a hard week."], d=9),
    {"type": "quote", "d": 7, "l1": "A flat line after a renewal", "l2": "may be a gap, not a quiet week.", "cap": "Check missing days were filled after a connection is renewed."},
    E("Next  ·  C2.1  Categorisation rules")]},
"C2.1": {"scenes": [
    T("Categorisation", "rules", M("C2.1", 7), "C2.1 · Categorisation rules"),
    S("bank_tx", "A position is only useful when each transaction has a category.", d=7),
    {"type": "bullets", "d": 10, "eyebrow": "WRITE RULES FROM THE LARGEST FLOWS", "heading": "In this order", "step": 1.2,
     "items": [("Payroll and tax", "regular, easy to match"), ("Ten largest customers and suppliers", ""), ("Financing", "loans, interest, facilities"), ("Intercompany", "group names and accounts")],
     "cap": ["Rules match counterparty, reference or amount pattern.", "Start with the largest, most regular flows."]},
    E("Next  ·  C2.2  Reviewing what remains")]},
"C2.2": {"scenes": [
    T("Reviewing", "what remains", M("C2.2", 5), "C2.2 · Reviewing what remains"),
    {"type": "compare", "d": 9, "heading": "For each line in review", "left": "One-off", "litems": ["Categorise it once"], "right": "Comes back", "ritems": ["Write or adjust a rule"],
     "cap": ["Review on a fixed rhythm, daily or weekly.", "A growing \"Other\" category is a review that is not happening."]},
    E("Next  ·  C2.3  Intercompany movements")]},
"C2.3": {"scenes": [
    T("Intercompany", "movements", M("C2.3", 7), "C2.3 · Intercompany movements"),
    {"type": "flow", "d": 10, "eyebrow": "FOR THE GROUP, NOTHING HAPPENED", "heading": "250,000 USD from Inc. to Ltd", "step": 1.2, "color": {1: TEAL},
     "nodes": [("Halden Trading Inc.", "pays out"), ("Intercompany", "both sides"), ("Halden Trading Ltd", "receives")],
     "cap": ["Counted as ordinary flows, both sides inflate the group's receipts and payments.", "Categorise and match both sides as intercompany."]},
    {"type": "checklist", "d": 8, "eyebrow": "MATCHING", "heading": "Check", "step": 1.4,
     "items": ["Same amount, after conversion", "Close dates", "Cash in transit at month end"],
     "cap": "A transfer leaving on the 30th and arriving on the 2nd is cash in transit."},
    E("Next  ·  C2.4  Rule suggestions with an assistant")]},
"C2.4": {"scenes": [
    T("Rule suggestions", "with an assistant", M("C2.4", 6), "C2.4 · Rule suggestions with an assistant"),
    {"type": "flow", "d": 9, "eyebrow": "THE ASSISTANT PROPOSES", "heading": "You approve what runs", "step": 1.2,
     "nodes": [("Uncategorised lines", ""), ("Grouped by pattern", "assistant"), ("Proposed rules", "with examples"), ("You create", "after review")],
     "cap": "An assistant is good at finding the patterns in uncategorised lines."},
    {"type": "checklist", "d": 9, "eyebrow": "REVIEW BEFORE ANY RULE RUNS", "heading": "Three checks", "step": 1.4,
     "items": ["Too broad? \"PAYMENT\" catches half the bank", "Intercompany: group companies only", "Payroll lines: share only what is needed"],
     "cap": "The assistant proposes; the rules you approve are what run."},
    E("Next  ·  C3.1  The cash worksheet")]},
"C3.1": {"scenes": [
    T("The cash", "worksheet", M("C3.1", 7), "C3.1 · The cash worksheet"),
    S("bank_position", ["A chart on top, a pivot-style report below.", "Rows and columns are yours: entity, account, category, period."], d=10, zoom=1.15),
    {"type": "quote", "d": 7, "l1": "Use the same weekly views,", "l2": "every week.", "cap": "Agree two or three views with the treasurer, so the numbers compare."},
    E("Next  ·  C3.2  Presenting the position")]},
"C3.2": {"scenes": [
    T("Presenting", "the position", M("C3.2", 5), "C3.2 · Presenting the position"),
    {"type": "checklist", "d": 10, "eyebrow": "THREE LINES FOR MANAGEMENT", "heading": "Same layout every time", "step": 1.5,
     "items": ["Cash today, by entity and in total", "What changed, and why", "What is coming: the lowest point and when"],
     "cap": "State the exchange rates and their date when you convert currencies."},
    E("Next  ·  C4.1  One data model with FP&A")]},
"C4.1": {"scenes": [
    T("One data model", "with FP&A", M("C4.1", 6), "C4.1 · One data model with FP&A"),
    {"type": "compare", "d": 10, "heading": "Payer and payee swap", "left": "Receivable", "litems": ["Our entity is the payee", "The third party pays us"], "right": "Payable", "ritems": ["Our entity is the payer", "We pay the third party"],
     "cap": ["Invoices use the same entity, business unit and third-party selectors as FP&A.", "The same customer links its invoices to its ledger account."]},
    S("ar_aging", "From a DSO to the customers behind it.", d=7),
    E("Next  ·  C4.2  Direction and intercompany rules")]},
"C4.2": {"scenes": [
    T("Direction and", "intercompany rules", M("C4.2", 7), "C4.2 · Direction and intercompany rules"),
    {"type": "flow", "d": 10, "eyebrow": "HOW K-φ DECIDES", "heading": "From the two parties on the document", "step": 1.2, "color": {2: TEAL},
     "nodes": [("Group company paid", "receivable"), ("Group company pays", "payable"), ("Both in the group", "intercompany")],
     "cap": ["A third party that does not exist yet is created.", "When the direction looks wrong, check the parties' names first."]},
    E("Next  ·  C4.3  Import mappings")]},
"C4.3": {"scenes": [
    T("Import", "mappings", M("C4.3", 5), "C4.3 · Import mappings"),
    {"type": "flow", "d": 9, "eyebrow": "TEACH K-φ ONCE", "heading": "Unknown party, one question", "step": 1.2, "color": {2: RED},
     "nodes": [("Unrecognised party", ""), ("Asked once", "which company?"), ("Remembered", "right or wrong")],
     "cap": ["When no party is recognised, the import asks once and remembers.", "A wrong answer is remembered too: check the first import carefully."]},
    E("Next  ·  C4.4  Reconciliation and tolerances")]},
"C4.4": {"scenes": [
    T("Reconciliation", "and tolerances", M("C4.4", 6), "C4.4 · Reconciliation and tolerances"),
    {"type": "table", "d": 10, "eyebrow": "EACH INVOICE SHOWS", "heading": "Status, payment, match", "cols": ["Invoice", "Status", "Paid on", "Reconciled"], "widths": [1.4, 1, 1, 1], "step": 1.0, "hot": 2, "hot_at": 4,
     "rows": [["INV-2041", "Paid", "2026-10-03", "Yes"], ["INV-2052", "Partly paid", "2026-10-11", "Partly"], ["INV-2077", "Open", "", "No"]],
     "cap": ["Matching follows a tolerance in percent or amount.", "Keep it narrow: wide tolerances match the wrong payments."]},
    E("Next  ·  C5.1  What the forecast combines")]},
"C5.1": {"scenes": [
    T("What the cash", "forecast combines", M("C5.1", 7), "C5.1 · What the forecast combines"),
    {"type": "flow", "d": 10, "eyebrow": "FOUR INPUTS", "heading": "Precise near, budget far", "step": 1.0,
     "nodes": [("Banks", "starting point"), ("Open invoices", "due dates"), ("Budget, ledger", "mapped to cash"), ("Known movements", "tax, loans, dividends")],
     "cap": ["Banks and invoices are precise for the coming weeks; the budget takes over further out.", "Treasury usually reads 13 weeks, week by week."]},
    E("Next  ·  C5.2  Category rules and versions")]},
"C5.2": {"scenes": [
    T("Category rules", "and versions", M("C5.2", 6), "C5.2 · Category rules and versions"),
    {"type": "quote", "d": 9, "l1": "One saved rule per category.", "l2": "Same inputs, same forecast.",
     "cap": ["When the forecast moves, an input or a rule changed, and both are recorded.", "Write down why each rule was chosen: \"Payroll: budget, paid on the 25th\"."]},
    E("Next  ·  C5.3  Funding needs and overdraft windows")]},
"C5.3": {"scenes": [
    T("Funding needs and", "overdraft windows", M("C5.3", 7), "C5.3 · Funding needs and overdraft windows"),
    {"type": "checklist", "d": 10, "eyebrow": "FOR EACH WINDOW", "heading": "Three answers", "step": 1.5,
     "items": ["How much, at the lowest point", "From when to when (the end can be open)", "How to fund it"],
     "cap": ["When an entity's forecast goes below zero, K-φ shows a funding need with its window.", "A transfer, a facility drawing, or a delayed payment."]},
    S("pay_funding", "Read funding needs per entity: a group surplus does not pay one company's suppliers.", d=8),
    E("Next  ·  C6.1  Payment runs and approvals")]},
"C6.1": {"scenes": [
    T("Payment runs", "and approvals", M("C6.1", 6), "C6.1 · Payment runs and approvals"),
    S("pay_runs", ["A run picks the invoices, the beneficiaries and the paying account.", "Then it goes for approval and signature."], d=9),
    {"type": "quote", "d": 8, "l1": "A new or changed beneficiary", "l2": "is paid 24 hours after approval.", "cap": "Use that time: confirm the change by phone, on a known number."},
    E("Next  ·  C6.2  Two signers by default")]},
"C6.2": {"scenes": [
    T("Two signers", "and their limits", M("C6.2", 5), "C6.2 · Two signers by default"),
    {"type": "flow", "d": 9, "eyebrow": "ENFORCED BY K-φ", "heading": "Preparer, approver, two signers", "step": 1.0,
     "nodes": [("Prepare", ""), ("Approve", ""), ("Sign", "within a limit"), ("Sign", "within a limit")],
     "cap": ["The preparer can neither approve nor sign; the approver cannot sign.", "Every signer has a limit. A tenant with a single user cannot pay."]},
    S("pay_rights", "A change to anyone's payment rights takes effect only when a second admin confirms it.", d=8, zoom=1.5, focus=(600, 150, 1320, 410), label="Payment rights"),
    E("Next  ·  Exam  Position, invoices and forecast")]},
}
