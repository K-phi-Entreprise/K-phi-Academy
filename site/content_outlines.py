# Outlines of the courses still in preparation (titles only), from ACADEMY-structure-and-UX.md.

def C(code, title, lessons):
    return {"code": code, "title": title, "lessons": [{"code": c, "title": t} for c, t in lessons]}

OUTLINES = [
    {"id": "build", "code": "B", "title": "Build", "badge": "Build", "duration": "About 4 hours", "status": "preparing",
     "audience": "Builders, analysts who automate, consultants.", "prereq": "Foundation, AI for finance",
     "summary": "Build extensions with your own LLM, use the Data library, write back under governance, and prove the AI got it right.",
     "chapters": [
        C("B1", "Why build inside the system of record", [("B1.1", "Bespoke logic next to the data"), ("B1.2", "What an extension can and cannot touch")]),
        C("B2", "The builder pass", [("B2.1", "Pasting the pass into your LLM"), ("B2.2", "Working in small steps"), ("B2.3", "The default dashboard and widgets")]),
        C("B3", "Data", [("B3.1", "Reading tenant data through the API"), ("B3.2", "The Data library"), ("B3.3", "Variables and Copy for an LLM"), ("B3.4", "Licensed data stays with the client")]),
        C("B4", "Writing back", [("B4.1", "Write-back into Cash"), ("B4.2", "Approval before the first write"), ("B4.3", "What the audit trail records")]),
        C("B5", "Verifying AI-built logic", [("B5.1", "Building a known-answer case"), ("B5.2", "Signs, dates, units, quotes"), ("B5.3", "Checking what was written, not what was shown"), ("B5.4", "Keeping the test with the extension")]),
        C("B6", "Publishing", [("B6.1", "Functions as APIs"), ("B6.2", "Community listing, opt-in"), ("B6.3", "Ownership and buyout")]),
     ]},
    {"id": "implementation", "code": "I", "title": "Implementation", "badge": "K-φ Architect", "duration": "About 2 hours", "status": "preparing",
     "audience": "Implementers. Last course of the Architect path.", "prereq": "Foundation, AI for finance, FP&A, Cash, Build",
     "summary": "Scope, run and hand over a K-φ implementation: discovery, parallel run over two closes, go-live, handover.",
     "chapters": [
        C("I1", "Scoping", [("I1.1", "Discovery questions"), ("I1.2", "Data inventory: what lives where")]),
        C("I2", "Running the project", [("I2.1", "Tenant setup plan"), ("I2.2", "Parallel run over two closes"), ("I2.3", "Go-live checklist")]),
        C("I3", "Handover", [("I3.1", "Training the client's users"), ("I3.2", "Documentation and known-answer tests"), ("I3.3", "Support and escalation to K-φ")]),
     ]},
]

PATHS = [
    {"id": "practitioner", "title": "K-φ Practitioner", "who": "Everyone starting on K-φ", "courses": ["foundation", "ai"], "credential": "K-φ Practitioner", "hours": "4 h"},
    {"id": "fpa", "title": "K-φ FP&A Specialist", "who": "Controllers and FP&A teams", "courses": ["foundation", "ai", "fpa"], "credential": "K-φ FP&A Specialist", "hours": "8 h"},
    {"id": "cash", "title": "K-φ Treasury Specialist", "who": "Treasurers and cash managers", "courses": ["foundation", "ai", "cash"], "credential": "K-φ Treasury Specialist", "hours": "8 h"},
    {"id": "builder", "title": "K-φ Builder", "who": "People who build on K-φ with an LLM", "courses": ["foundation", "ai", "build"], "credential": "K-φ Builder", "hours": "8 h"},
    {"id": "architect", "title": "K-φ Architect", "who": "Implementers who design and run K-φ for clients", "courses": ["foundation", "ai", "fpa", "cash", "build", "implementation"], "credential": "K-φ Architect", "hours": "18 h"},
]
