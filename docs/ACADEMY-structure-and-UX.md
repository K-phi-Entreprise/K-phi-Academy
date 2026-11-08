# K-φ Academy: structure and learner experience

> Update 8 Nov 2026: a course A, "AI for finance" (what a model is, agents, MCP, agentic workflows, safety, verifying AI output, K-φ with AI), is now required on every path right after Foundation. Credentials are AI-Ready Finance Practitioner and AI-Ready Finance Consultant. FP&A and Cash each gained an assistant lesson (P3.4, C2.4). The live site is the reference for the current syllabus.

Draft, 7 November 2026. Replaces the flat module pages as the master structure; their content moves into the lessons below.

## 1. Structure

**Path > Course > Chapter > Lesson.**

- A **lesson** is 5 to 12 minutes and teaches one thing.
- A **chapter** groups 3 to 5 lessons and ends with an ungraded self-check.
- A **course** ends with a lab (practice, unlimited) and an exam (graded by the checker).
- A **path** is a set of courses leading to a credential.

### Paths

| Path | Courses | Credential |
|---|---|---|
| Foundation | F | Foundation |
| FP&A Specialist | F + FP&A | FP&A |
| Cash Specialist | F + Cash | Cash |
| Builder | F + Build | Build |
| **Consultant** | F + FP&A + Cash + Build + Implementation | **K-φ Certified Consultant** |

Client finance staff typically take Foundation plus one specialist path. Consultants take the full path.

## 2. Syllabus

### Course F: Foundation (about 2 h)

| Chapter | Lessons |
|---|---|
| F1. Welcome to K-φ | F1.1 What K-φ is: one system of record for FP&A, Cash and Build · F1.2 Tour of the interface · F1.3 Tenants, entities, business units, third parties |
| F2. Access and governance | F2.1 Users and roles · F2.2 Governance approvers and dual control · F2.3 Segregation of duties and two-factor authentication |
| F3. Bringing data in | F3.1 Importing a general ledger · F3.2 Accounting connectors · F3.3 Bank connections · F3.4 Sheets, files and Data sources · F3.5 Checking an import before you trust it |
| F4. Working safely | F4.1 Reading the audit trail · F4.2 What you never do in a client tenant |
| Lab and exam | Set up Halden Trading: entities, users, approver, ledger import, one seeded problem |

### Course FP&A (about 4 h)

| Chapter | Lessons |
|---|---|
| P1. From ledger to statements | P1.1 P&L year to date, cumulative balance sheet · P1.2 Drilling down to ledger lines · P1.3 Distributions and retained earnings |
| P2. KPIs and covenants | P2.1 The KPI set and their formulas · P2.2 Working capital: DSO, DPO, DIO, trailing windows · P2.3 Covenants and headroom |
| P3. Budget and versions | P3.1 Versions and what they freeze · P3.2 Creating a budget from actuals · P3.3 Budget versus actuals |
| P4. Forecasting | P4.1 Forecast rules and deterministic replay · P4.2 Collections and disbursements: ledger or open invoices · P4.3 Run-rate assumptions, opt-in · P4.4 Stating assumptions |
| P5. Scenarios | P5.1 Building a scenario · P5.2 Presenting the difference: profit, cash, headroom |
| P6. Valuation | P6.1 Inputs measured from the books · P6.2 Projection and extrapolation · P6.3 Football field and the report |
| P7. Reporting | P7.1 The board pack and why it calculates nothing · P7.2 Reconciling what you present |
| Lab and exam | Statements, a forecast version, an FX scenario, one seeded misclassification |

### Course Cash (about 4 h)

| Chapter | Lessons |
|---|---|
| C1. Bank structure | C1.1 Accounts by entity and by pool · C1.2 Header accounts and reserves · C1.3 Daily balances and history |
| C2. Transactions | C2.1 Categorisation rules · C2.2 Reviewing what remains · C2.3 Intercompany movements |
| C3. Cash position | C3.1 The cash worksheet · C3.2 Presenting the position |
| C4. Receivables and payables | C4.1 One data model with FP&A · C4.2 Direction and intercompany rules · C4.3 Import mappings · C4.4 Reconciliation and tolerances |
| C5. Cash forecast | C5.1 What the forecast combines · C5.2 Category rules and versions · C5.3 Funding needs and overdraft windows |
| C6. Payments and controls | C6.1 Payment runs and approvals · C6.2 Two signers by default |
| Lab and exam | Pools, categorisation, intercompany invoices, a 13-week forecast, one seeded double count |

### Course Build (about 4 h)

| Chapter | Lessons |
|---|---|
| B1. Why build inside the system of record | B1.1 Bespoke logic next to the data, not beside it · B1.2 What an extension can and cannot touch |
| B2. The builder pass | B2.1 Pasting the pass into your LLM · B2.2 Working in small steps · B2.3 The default dashboard and widgets |
| B3. Data | B3.1 Reading tenant data through the API · B3.2 The Data library · B3.3 Variables and Copy for an LLM · B3.4 Licensed data stays with the client |
| B4. Writing back | B4.1 Write-back into Cash · B4.2 Approval before the first write · B4.3 What the audit trail records |
| B5. Verifying AI-built logic | B5.1 Building a known-answer case · B5.2 Signs, dates, units, quotes · B5.3 Checking what was written, not what was shown · B5.4 Keeping the test with the extension |
| B6. Publishing | B6.1 Functions as APIs · B6.2 Community listing, opt-in · B6.3 Ownership and buyout |
| Lab and exam | FX forward valuation extension with write-back and approval, one seeded inverted quote |

### Course I: Implementation (about 2 h, Consultant path only)

| Chapter | Lessons |
|---|---|
| I1. Scoping | I1.1 Discovery questions · I1.2 Data inventory: what lives where |
| I2. Running the project | I2.1 Tenant setup plan · I2.2 Parallel run over two closes · I2.3 Go-live checklist |
| I3. Handover | I3.1 Training the client's users · I3.2 Documentation and known-answer tests · I3.3 Support and escalation to K-φ |
| Capstone | Review of the candidate's four exam tenants as one implementation, plus a go-live checklist submitted for Halden Trading |

## 3. Lesson format

Every lesson has the same layout, so learners know where to look.

1. **Objective:** one sentence.
2. **Video:** 2 to 4 minutes, screen recording with voice. Captions and transcript.
3. **Read:** the explanation, with screenshots.
4. **Try it:** one action to do in the learner's lab tenant, opened beside the lesson.
5. **Key points:** three bullets.
6. **Resources:** downloadable files where relevant (dataset, templates, checklists).

Chapters end with a **self-check** of three or four questions. It is ungraded and only tells the learner whether to revisit a lesson.

## 4. Learner experience

### Screens

| Screen | What it shows |
|---|---|
| **Catalogue** | The five paths, each with duration, audience, credential and a "Start" button |
| **Learner home** | Current course and next lesson ("Resume"), progress per course, badges earned, expiry dates |
| **Course page** | Outcomes, prerequisites, duration, chapter list with progress, lab and exam status |
| **Lesson player** | Left: chapter tree with ticks. Centre: the lesson. Right or bottom: "Open lab". Top: progress bar and time left. Previous and Next |
| **Lab** | The learner's own practice tenant, persistent, with a "Reset lab" button |
| **Exam** | Rules, "Start exam" (creates a fresh tenant), the brief, a submission form, then the checker report check by check |
| **Certificate** | Badge, holder, level, platform version, dates, verify link, "Add to LinkedIn", PDF download |
| **Directory** | Public list of active certificates, filter by country and credential |
| **Verify page** | Public, one per certificate, status valid, expired or revoked |

### Rules

- **Public reading, login for doing.** Lessons can be read without an account, which helps search and lets buyers see what "certified" covers. Labs, progress, exams and certificates need a login.
- **The login is a K-φ account.** Every learner becomes a K-φ user with a lab tenant. The academy is also an acquisition channel.
- **Resume anywhere.** Progress is saved per lesson; the learner home always offers "Resume".
- **Mobile.** Lessons and videos work on a phone. Labs and exams are desktop only, and say so.
- **No timer on exams.** Each exam tenant stays open 72 hours. Attempts follow the Phase 0 rules.
- **Accessibility.** Captions and transcripts for every video, keyboard navigation, readable in light and dark themes.
- **Brand.** K-φ palette (navy, neon yellow #E6FF00), the "K-φ" mark, the aurora used once, on the certificate.

### The exam flow

1. Learner clicks "Start exam". A fresh tenant is created with a variant of the dataset.
2. The brief opens beside the tenant.
3. The learner works, with any tools and any LLM.
4. The learner submits the form: requested figures and a short note.
5. The checker runs and returns a report: each check passed or failed, with the reason.
6. Pass: certificate issued, verify page live, "Add to LinkedIn" offered. Fail: the report shows what to revisit, and the next attempt opens after 24 hours.

## 5. Build or buy the platform

| Option | For | Against |
|---|---|---|
| Hosted e-learning platform (course builder with video, progress, certificates) | Fast to set up; video hosting, progress tracking and certificates included | Exams still need our own checker and tenants; a second login; another brand; a monthly fee |
| **Own academy, on K-φ** (recommended) | One login, which is the K-φ account; labs and exams are native; every learner becomes a user; full control of the brand | We build progress tracking, the lesson player and video hosting |

Recommendation: our own, kept simple. Lessons are Markdown pages in the K-phi-academy repo, rendered by the site. Progress, labs, exams and certificates live in K-φ, behind the normal login. Videos go on a video host with an embeddable player and captions.

## 6. Production plan

| Step | Content | Effort |
|---|---|---|
| 1 | Write all lessons (text and screenshots), around 75 lessons | 4 to 5 days, Claude drafts, Vincent reviews |
| 2 | Record videos: 2 to 4 minutes each, screen and voice | The slow part. Start with Foundation and Build |
| 3 | Academy site: catalogue, course pages, lesson player, public reading | 3 to 4 days |
| 4 | Learner accounts, progress, labs (inside K-φ) | 3 to 4 days |
| 5 | Exams, checkers, submission form, certificates, verify pages (Phase 2 of the plan) | 5 to 7 days |
| 6 | Directory, LinkedIn button, renewal | 2 days |

**Pilot shortcut:** the five pilot consultants can start with steps 1 and 5 only: lessons as pages, no videos, labs and exams run by hand. Videos and the player follow once the pilot shows which lessons are hard.
