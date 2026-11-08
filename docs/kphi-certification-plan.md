# K-φ Certified Builder: training path and certification

Implementation plan. Draft, 7 November 2026.

## 1. Why

Mid-market and larger buyers ask three questions before they commit:

1. Will the company still be there tomorrow?
2. Will someone help when something breaks?
3. Is there anyone other than the founder who can implement it?

A certification path answers the third directly and helps with the second. The first needs its own answers (buyout option on extensions, data export, source escrow, a public continuity page), which are outside this plan.

## 2. Principles

- **Graded by the system, not by a person.** Every exam is a hands-on task on a sandbox tenant. A checker reads the result through the API and compares it with an answer key. No multiple choice.
- **Independence.** Certified builders hold no equity and no stake in K-φ. Any revenue they earn from published extensions is disclosed on their profile.
- **Scarce and current.** A real trap in the exam, a published pass rate, 12-month validity, a revocation rule.
- **Portable.** The skill taught is "verifying AI-built finance logic", which is useful beyond K-φ. This framing makes the credential worth the time and opens the door to a neutral co-signer later.
- **No promises.** Certification does not mean leads, work or IP. It means visibility and verified skill.

## 3. Curriculum

One foundation module and three tracks. About 16 hours in total for the full Consultant path; 2 hours for Foundation.

| Module | Covers | Hands-on task (checked automatically) |
|---|---|---|
| 0. Intro and admin | Tenants and entities, users and roles, governance approvers, dual control, audit trail, connectors and imports | Set up a tenant: an entity, two users with the right roles, an approver, one data import |
| 1. FP&A | Ledger to statements, KPIs, budget vs actuals, forecast, scenarios, valuation | Build a forecast and a scenario that match known figures |
| 2. Cash | Bank accounts and feeds, categorisation, cash position, cash forecast, AR/AP, covenants | Categorise a statement; produce a cash position and forecast that match the answer key |
| 3. Build | Builder pass, Data library, write-back into Cash, permissions, change control | Build an extension from a spec, with known answers and one seeded trap |

All four modules use one shared dataset. The Build exam reuses the FP&A and Cash data the candidate has already set up, which demonstrates the core message: custom logic lives inside the system of record.

## 4. Certificates

| Badge | Requirement | Audience |
|---|---|---|
| Foundation | Module 0 | Everyone (prerequisite) |
| FP&A / Cash / Build | Foundation + that track | Specialists, client staff |
| **K-φ Certified Consultant** | Foundation + all three tracks | Implementers |

- A client's own finance staff can stop at Foundation plus one track. This is the "internal builder" level and answers the continuity question from the buyer's side.
- Each certificate is a signed record (holder, level, platform version, date, expiry) with a public page at `academy.k-phi.com/verify/<id>`, showing the checker report and an anonymised summary of the build.
- The pilot cohort gets "Founding Builder #1 to #N", a permanent title with no financial rights.
- A public directory lists active certificates. Expired or revoked records disappear from it but their verify page states the status.

## 5. Where it lives

| Part | Home | Why |
|---|---|---|
| Course pages, verify pages, directory | New repo `K-phi-academy`, GitHub Pages, `academy.k-phi.com` | Same setup as K-phi-deck. No engine deploy, not affected by the production freeze |
| Exam specs, answer keys, checkers, issuing script | New private repo `K-phi-certify` in K-phi-Entreprise | Kept apart from the engine; can be partly open-sourced later so anyone can see how grading works |
| Sandbox tenants | "BUILD by K-φ" ephemeral tenants if live; otherwise demo tenants on staging | Reuses the existing pattern |
| Engine | No change for the pilot | Later changes follow feature branch, staging, main |

## 6. Phases

### Phase 0: decisions (one page, approved by Vincent)

- Names and levels as in section 4.
- Pass rule per module: figures within a set tolerance, write-back correct (amount, sign, date), permissions and dual control held, trap handled.
- Validity 12 months; revocation rule; independence clause.
- The five pilot consultants.

### Phase 1: course content (2 to 3 days)

- Four module pages plus one exam brief per module.
- Vendor-neutral framing for the verification and governance parts.
- Check: Vincent reads the pages on the Pages preview.

### Phase 2: dataset, answer keys and checkers (4 to 6 days)

- One shared fictional dataset: entities, ledger, bank statements, invoices.
- Answer key per module, computed independently of K-φ (spreadsheet).
- Build exam case, smaller than the margin-call demo (for example an FX exposure with a hedge rollover), using the Data library and writing into Cash, with one seeded trap such as a sign convention.
- Four checkers. Each reads a tenant through the API and outputs a JSON report with pass or fail and the reason for each check.
- Proof without reading code: for each module, a reference solution must pass and at least three deliberately broken solutions must fail, each with the reason named. This runs in CI.

### Phase 3: manual pilot with five consultants

- Each consultant gets a sandbox tenant and the exam briefs, and builds with their own LLM (Claude, Codex or Gemini CLI).
- Vincent triggers a checker from a GitHub Action (manual run, tenant ID as input) and receives the report.
- An issuing script creates the signed record, the verify page and the founding number.
- Collect where people got stuck; fix the modules and briefs.
- Publish the first certified names on the site and LinkedIn.

### Phase 4: automation, only after the pilot (about 1 week)

- Self-service sign-up with invite codes, capped at the first 50.
- A "start certification" tool in the BUILD by K-φ MCP; checker runs on submit; certificate issued automatically.
- Directory page, expiry and renewal job (short automated re-test on the current version), revocation, trap rotation each season.
- Compute cap per candidate.
- Verification records move from static files to a small signed API.

### Phase 5: later

- The Build checker as a pre-deploy gate in production BUILD, so an extension can show "passed the checks".
- Extension marketplace with disclosed revenue share.
- A neutral co-signer (treasury association or business school) for the verification and governance module.
- A one-line clause buyers can use in RFPs: "implementation by a K-φ certified builder, verified at academy.k-phi.com".

## 7. Risks

| Risk | Mitigation |
|---|---|
| A badge nobody values | Named founding cohort, public directory, verify pages that are easy to share |
| Implied promises | Never say certified means leads, work or IP; independence clause |
| Compute cost per candidate | Invite codes, cap of 50, compute cap per tenant |
| Answers circulate | Seasonal trap rotation, per-candidate data variations |
| Dilution | Pass rate published, 12-month expiry, revocation |
| Checker wrong | Reference and broken solutions in CI for every module |

## 8. Open points

- Whether "BUILD by K-φ" sandbox tenants are live in time for Phase 2.
- Whether k-phi.com is served by the engine (irrelevant for the pilot, since the academy has its own domain).
- Pricing after the pilot: free for consultants at first, paid for client staff.
