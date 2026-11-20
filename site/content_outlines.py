# Outlines of the courses still in preparation (titles only), from ACADEMY-structure-and-UX.md.

def C(code, title, lessons):
    return {"code": code, "title": title, "lessons": [{"code": c, "title": t} for c, t in lessons]}

OUTLINES = [
    {"id": "build", "code": "B", "title": "Build", "badge": "Build", "duration": "About 4 hours", "status": "preparing",
     "audience": "Builders, analysts who automate, consultants.", "prereq": "Agentic finance, MCP, Data foundation",
     "summary": "Build extensions with your own LLM, use the Data library, write back under governance, and prove the AI got it right.",
     "chapters": [
        C("B1", "Why build inside the system of record", [("B1.1", "Bespoke logic next to the data"), ("B1.2", "What an extension can and cannot touch")]),
        C("B2", "The builder pass", [("B2.1", "Pasting the pass into your LLM"), ("B2.2", "Working in small steps"), ("B2.3", "The default dashboard and widgets")]),
        C("B3", "Data", [("B3.1", "Reading tenant data through the API"), ("B3.2", "The Data library"), ("B3.3", "Variables and Copy for an LLM"), ("B3.4", "Licensed data stays with the client")]),
        C("B4", "Writing back", [("B4.1", "Write-back into Cash"), ("B4.2", "Approval before the first write"), ("B4.3", "What the audit trail records")]),
        C("B5", "Verifying AI-built logic", [("B5.1", "Building a known-answer case"), ("B5.2", "Signs, dates, units, quotes"), ("B5.3", "Checking what was written, not what was shown"), ("B5.4", "Keeping the test with the extension")]),
        C("B6", "Publishing", [("B6.1", "Functions as APIs"), ("B6.2", "Community listing, opt-in"), ("B6.3", "Ownership and buyout")]),
     ]},
    {"id": "implementation", "code": "I", "title": "Implementation", "badge": "K-φ Agentic Architect", "duration": "About 2 hours", "status": "preparing",
     "audience": "Implementers. Last course of the Agentic Architect path.", "prereq": "Agentic finance, MCP, Data foundation, FP&A, Cash, Build",
     "summary": "Scope, run and hand over a K-φ implementation: discovery, parallel run over two closes, go-live, handover.",
     "chapters": [
        C("I1", "Scoping", [("I1.1", "Discovery questions"), ("I1.2", "Data inventory: what lives where")]),
        C("I2", "Running the project", [("I2.1", "Tenant setup plan"), ("I2.2", "Parallel run over two closes"), ("I2.3", "Go-live checklist")]),
        C("I3", "Handover", [("I3.1", "Training the client's users"), ("I3.2", "Documentation and known-answer tests"), ("I3.3", "Support and escalation to K-φ")]),
     ]},
]

# owner, 2026-11-18: "agentic finance and MCP should be inside AI foundation": every other path starts with the
# whole K-φ AI Foundation (F, A and M), shown as one block on its card
PATHS = [
    {"id": "practitioner", "title": "K-φ AI Foundation", "who": "Everyone starting on K-φ", "courses": ["ai", "mcp", "foundation"], "credential": "K-φ AI Foundation", "hours": "5 h"},
    {"id": "fpa", "title": "K-φ Agentic FP&A", "who": "Controllers and FP&A teams", "base": "practitioner", "courses": ["ai", "mcp", "foundation", "fpa"], "credential": "K-φ Agentic FP&A", "hours": "8 h"},
    {"id": "cash", "title": "K-φ Agentic Treasury", "who": "Treasurers and cash managers", "base": "practitioner", "courses": ["ai", "mcp", "foundation", "cash"], "credential": "K-φ Agentic Treasury", "hours": "8 h"},
    {"id": "builder", "title": "K-φ Builder", "who": "People who build on K-φ with an LLM", "base": "practitioner", "courses": ["ai", "mcp", "foundation", "build"], "credential": "K-φ Builder", "hours": "8 h"},
    {"id": "architect", "title": "K-φ Agentic Architect", "who": "Implementers who design and run K-φ for clients", "base": "practitioner", "courses": ["ai", "mcp", "foundation", "fpa", "cash", "build", "implementation"], "credential": "K-φ Agentic Architect", "hours": "18 h"},
    # owner, 2026-11-20: a vendor-neutral course, built from sessions that use no K-φ material, for continuing education
    {"id": "treasury-ai", "title": "Agentic AI in Treasury", "who": "Treasurers, cash managers and finance teams", "neutral": True, "courses": ["treasury-ai"], "credential": "Agentic AI in Treasury, certificate of completion", "hours": "2.5 h"},
]
