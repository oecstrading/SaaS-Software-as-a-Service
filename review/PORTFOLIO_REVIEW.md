# OECS Software Portfolio Review

Reviewed 10 November 2026. Scope: 42 original GitHub marketplace listings plus five browser-saved additions (47 total).

## Executive finding

The portfolio contains potentially useful business applications, demonstrators, marketing websites and feasibility documents. It cannot responsibly be described as 47 independently verified production SaaS products. Fifteen original /apps/ launch paths returned 404. The other 27 original routes served the company web-app shell; the company portfolio supplied the actual destinations.

There are 36 matching public launch destinations, nine exact editions not recovered and two access-restricted destinations. Existing listing names are retained for traceability, including original compliance claims in names; names are not endorsements. No production-readiness certification is given.

## Scope and evidence

GET checks established HTTP reachability only. Public source, application bundles and rendered interface text were inspected as available. FaMaaS IFRS demo setup opened its sample dashboard. QuickBooks Cleanup loaded 25 sample accounts and showed a validation preview with 14 steps. The financial framework studio interface was labelled local/single-tenant and flagged an unbalanced initial TB. An authenticated payroll workspace was viewed without running payroll or changing records. No private employee, payroll or patient records are reproduced.

Live payment processing, actual QuickBooks writes, external messages, statutory correctness, production tenancy, backups and full end-to-end functionality were not tested. Missing evidence or a bare HTTP 403 is a limitation, not proof of a defect. Published engineering return figures were not independently recalculated. This is technical/commercial screening, not financial, legal, clinical or regulatory certification.

## Commercial priorities

Focus on FaMaaS, QuickBooks Cleanup, Audit Studio and payroll for controlled acceptance tests. This is an analyst judgment based on workflow visibility and business use, not a comparative valuation. Validate a bounded workflow, delivery costs and customer demand before subscription pricing. Keep feasibility/proposal work separate from operational software. Consolidate the MLS/Realtors aliases and duplicate/module offers.

Suggested sequence: first 30 days—recover exact editions and prepare synthetic acceptance tests; days 31–60—prove persistence, isolation, integration failure handling and recovery; days 61–90—run a customer pilot, measure outcomes and support effort, then agree pricing. Timeline is illustrative.

## Platform changes

Rebuilt the catalogue with search, sector/status filters, sorting, individual assessments, comparisons of up to three apps, browser-local shortlist, shareable assessment links, email draft inquiries and printable review. Removed simulated Google sign-in/admin controls and iframe launch behavior. Five browser-saved additional listings were recovered into the published data. Original local-storage URL overrides no longer supersede published links. Repository-local apps/ compatibility pages resolve to the correct assessment. Historical root-absolute GitHub Pages paths lie outside this repository. index1.html now redirects to the canonical catalogue. No underlying app backend was changed.

## Individual assessments

### 01. Antillia Platform

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Helps overseas buyers compare Caribbean properties and organize due diligence.

**Observed:** The current company landing page links directly to antillia.online; the destination serves property discovery and evidence-confidence content.

**Gap:** Individual listing provenance, advisor credentials, lead delivery and vault permissions were not verified.

**Acceptance test:** Trace one published listing to source documents, route a test inquiry and confirm private documents cannot be read by another user.

**Commercial route:** Broker-led onboarding and property intelligence subscription.

Current destination: [https://www.antillia.online/](https://www.antillia.online/)

### 02. Infrastructure PMIS

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Gives lenders and project teams a shared view of budgets, milestones and disbursements.

**Observed:** The published app redirects to pmisforbanks.com. The browser remained on Loading during the initial inspection; its public bundle was retrieved.

**Gap:** A reachable site does not establish working project updates, approvals or portfolio reconciliation.

**Acceptance test:** Create a sandbox project, submit an approved variation and reconcile a staged disbursement to the ledger.

**Commercial route:** Paid discovery followed by one institution pilot.

Current destination: [https://pmisforbanks.com/](https://pmisforbanks.com/)

### 03. FaMaaS - Fixed Assets Management

Status: **Demo tested**. Review scope: Browser sample workflow tested.

**Business value:** Reduces manual asset-register work and depreciation preparation.

**Observed:** Browser test completed the IFRS demo setup and opened a dashboard with 26 sample assets and depreciation navigation.

**Gap:** Marketing customer counts, uptime and 100% compliance claims were not independently evidenced; tenant isolation and accounting results remain untested.

**Acceptance test:** Reconcile five asset examples including disposal and impairment to independently prepared schedules; prove company isolation.

**Commercial route:** Prioritize a controlled accountant-led pilot.

Current destination: [https://fixed-assets-management-system.lovable.app/](https://fixed-assets-management-system.lovable.app/)

### 04. BetterBooks Caribbean for QuickBooks

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Connects Caribbean POS, payroll and VAT work to bookkeeping.

**Observed:** The Better Books Caribbean destination and its public bundle are reachable. Bundle text includes posted-versus-simulated reconciliation and OAuth configuration screens.

**Gap:** Successful token refresh, duplicate prevention and real QuickBooks posting have not been demonstrated.

**Acceptance test:** Post a sandbox sale twice, verify one receipt only, expire the token and reconcile posting totals.

**Commercial route:** Sell implementation plus support after connector acceptance.

Current destination: [https://counter-to-ledger.lovable.app/](https://counter-to-ledger.lovable.app/)

### 05. IFRS & GAAP AI Statement Generator

Status: **Prototype**. Review scope: Browser interface inspected.

**Business value:** Provides a structured trial-balance-to-reporting and audit workpaper workflow.

**Observed:** Browser opened Enterprise Financial Framework Studio, explicitly labelled Single-Tenant / Local. It shows mapping, materiality and completion gates; the initial TB was out of balance and sign-off gates flagged it.

**Gap:** Local administrator UI is not server authentication. Final statements, imports, export accuracy and shared storage were not validated.

**Acceptance test:** Import a balanced synthetic TB, map every account, reconcile all statements and prove sign-off remains blocked for an unbalanced TB.

**Commercial route:** Offer a reviewed local reporting tool before promising hosted multi-user SaaS.

Current destination: [https://ai-ifrs-gaap-financial-statements-generator.lovable.app/](https://ai-ifrs-gaap-financial-statements-generator.lovable.app/)

### 06. EcoChill Proposa-Link

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Helps businesses compare refrigeration and microgrid investment proposals.

**Observed:** Public rendered interface contains asset sizing, a 10-year IRR matrix, entity/currency selection and a proposal approval queue.

**Gap:** Displayed returns and staged PostgreSQL operations do not prove actual savings or durable approval records.

**Acceptance test:** Recalculate NPV and IRR from exported cash flows and verify an approval survives a new session.

**Commercial route:** Paid energy assessment with an editable proposal model.

Current destination: [https://ecochill-proposa-link.lovable.app/](https://ecochill-proposa-link.lovable.app/)

### 07. Belize Blue Economy MRV MIS

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Organizes blue-economy indicators, investment inventory and evidence verification.

**Observed:** Rendered overview includes verification queue, CSV/PDF controls and programme components; initial contributor and capital totals are zero.

**Gap:** Zero totals do not establish a populated government system; evidence provenance and contributor permissions are untested.

**Acceptance test:** Submit synthetic field evidence, reject then approve it, and reconcile the indicator and CSV changes.

**Commercial route:** Commissioned M&E pilot with a named programme owner.

Current destination: [https://belize-blue-economy-mis.lovable.app/](https://belize-blue-economy-mis.lovable.app/)

### 08. Caribbean Finance Hub

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Helps micro-lenders reconcile loan books and monitor arrears.

**Observed:** Current destination is a micro-lending risk engine with ledger input, aging, underwriting, tax bridge and TB import; initial public view contains zero balances.

**Gap:** Zero/default data and visible role choices do not establish server-enforced permissions or valid lending calculations.

**Acceptance test:** Run a synthetic amortization schedule through payment, partial arrears and write-off; reconcile interest and aging.

**Commercial route:** One lender pilot after reconciliation acceptance.

Current destination: [https://carib-glide.lovable.app/](https://carib-glide.lovable.app/)

### 09. Easy Sales Cloud

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Supports retail sales and inventory workflows.

**Observed:** Destination is branded JACS Financials — AI Point of Sale; public bundle contains authentication and role-handling code.

**Gap:** Inventory consistency, offline sync and QuickBooks receipt posting were not verified.

**Acceptance test:** Complete a sale, return and duplicate webhook in a sandbox and reconcile stock, cash and journals.

**Commercial route:** Implementation-led retail pilot.

Current destination: [https://easy-sales-cloud.lovable.app/](https://easy-sales-cloud.lovable.app/)

### 10. VAT Reporter AI

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Helps accountants prepare and review VAT working papers.

**Observed:** Destination and public bundle are reachable; bundle contains an explicit QuickBooks-not-connected path and sample-data wording.

**Gap:** Current country rules, imported input VAT and filing outputs were not tested.

**Acceptance test:** Reconcile a synthetic return with standard, exempt, credit-note and imported-input transactions against independently checked rules.

**Commercial route:** Accountant-assisted preparation service; validate each jurisdiction before a filing claim.

Current destination: [https://vatreporter-ai.lovable.app/](https://vatreporter-ai.lovable.app/)

### 11. Gender and Climate Finance Tagging Platform

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Structures climate-finance tagging, project evidence and reporting.

**Observed:** Published route redirects to gcftportal.org. Public repository contains React pages, server routers and database schema; README identifies a full-stack deployment.

**Gap:** Repository breadth does not prove active integrations, independently verified credits or government acceptance.

**Acceptance test:** Trace one tagged transaction to evidence, approval, exported report and server audit event using isolated tenants.

**Commercial route:** Institutional evidence-management pilot.

Current destination: [https://gcftportal.org/](https://gcftportal.org/)

Matching source: [https://github.com/oecstrading/gcft-global-platform](https://github.com/oecstrading/gcft-global-platform)

### 12. Dominica DOMCREP M&E MIS

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Tracks resilience-programme activities, outputs and evidence.

**Observed:** DOMCREP-branded destination and its application bundle are reachable.

**Gap:** Programme authorization, live records and indicator calculations were not verified.

**Acceptance test:** Create a synthetic result, attach evidence, exercise reviewer approval and verify export totals.

**Commercial route:** Programme-specific implementation and support.

Current destination: [https://dominica-crep-me-mis-system.lovable.app/](https://dominica-crep-me-mis-system.lovable.app/)

### 13. Grenada UBEC Blue Economy M&E

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Gives a blue-economy programme a consistent monitoring workspace.

**Observed:** Grenada UBEC-branded destination and public bundle are reachable.

**Gap:** Source data, role enforcement, programme authorization and reporting acceptance remain unverified.

**Acceptance test:** Reconcile an indicator from baseline to approved result and test another organization cannot read it.

**Commercial route:** Institutional pilot after indicator design review.

Current destination: [https://grenada-ubec-me-project.lovable.app/](https://grenada-ubec-me-project.lovable.app/)

### 14. OECS AI Institute Platform

Status: **Website**. Review scope: Public website and bundle inspection.

**Business value:** Introduces training and incubator services and helps recruit participants.

**Observed:** The Institute website is reachable and identifies virtual incubation and AI education.

**Gap:** A public website does not verify a working LMS, mentorship matching or learner progress records.

**Acceptance test:** Enroll a sandbox learner, complete a module and prove progress persists with appropriate access.

**Commercial route:** Market training and incubation; demonstrate LMS separately.

Current destination: [https://www.theoecsaiinstitute.com/](https://www.theoecsaiinstitute.com/)

### 15. Close Command Hub

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Helps finance teams reconcile subscription flows and document close exceptions.

**Observed:** Rendered page is a specialized SaaS Close Command Deck with Stripe flows, refund demonstration, deferred revenue and QBO export tabs.

**Gap:** The specialized reconciliation deck does not substantiate the broader advertised close-management suite or live Stripe sync.

**Acceptance test:** Reconcile a synthetic annual subscription, fee, refund and month-end recognition through balanced journals.

**Commercial route:** Productize the narrow reconciliation workflow first.

Current destination: [https://close-command-hub.lovable.app/](https://close-command-hub.lovable.app/)

### 16. Executive Portfolio Hub

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Consolidates management views across personal and business entities.

**Observed:** Rendered Meridian dashboard includes multiple entities, ledger rows and balance-sheet summaries.

**Gap:** Displayed portfolio values are interface content, not independently confirmed assets; data feeds and consolidation eliminations were not tested.

**Acceptance test:** Import a synthetic intercompany transaction and verify consolidated elimination and source-to-report reconciliation.

**Commercial route:** Private reporting engagement with controlled data access.

Current destination: [https://wealth-compass-hub-06.lovable.app/](https://wealth-compass-hub-06.lovable.app/)

### 17. QuickBooks Utility Tools

Status: **Demo tested**. Review scope: Browser sample workflow tested.

**Business value:** Helps accountants review duplicate accounts and prepare bulk cleanup actions.

**Observed:** Browser loaded 25 sample accounts. Find duplicates displayed a dry-run preview with 14 steps, including a rejected merge.

**Gap:** Live Desktop bridge, Online OAuth, rollback and actual accounting mutations were not tested. Absolute reversibility and all-error validation claims need evidence.

**Acceptance test:** Use a disposable QuickBooks company to test preview, merge dependencies, export, backup and recovery.

**Commercial route:** Prioritize a supervised beta with backups and an accountant review step.

Current destination: [https://quickbooks-utility-tools.lovable.app/](https://quickbooks-utility-tools.lovable.app/)

### 18. JACS Restaurant Management

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Coordinates restaurant ordering, kitchen activity and POS operations.

**Observed:** Current destination is JAMROCK Restaurant POS; its bundle contains staff PIN/session handling and application workflows.

**Gap:** Payment, kitchen delivery, QR ordering and accounting synchronization were not verified end to end.

**Acceptance test:** Place one test QR order, confirm kitchen delivery, void it and reconcile the receipt and stock movement.

**Commercial route:** One restaurant pilot with a defined support contract.

Current destination: [https://jacs-restaurant-pos-system.lovable.app/](https://jacs-restaurant-pos-system.lovable.app/)

### 19. E-Testing Driver's License

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Supports digitized driver-theory testing administration.

**Observed:** OECS E-Testing destination and bundle are reachable; public bundle includes local storage and demo booking paths.

**Gap:** Official exam approval, identity checks, question security and tamper-resistant result storage were not demonstrated.

**Acceptance test:** Exercise candidate-to-result workflow with synthetic identities and prove a candidate cannot alter score or access another result.

**Commercial route:** Government pilot after identity and examination acceptance.

Current destination: [https://oecs-drivers-license-testing-platform.lovable.app/](https://oecs-drivers-license-testing-platform.lovable.app/)

### 20. eLandSaintLucia

Status: **Access restricted**. Review scope: HTTP access check only.

**Business value:** Could simplify parcel searches and land-record discovery.

**Observed:** The configured eLand destination returned HTTP 403 during the automated check.

**Gap:** Access-blocked is not proof of a missing application; source records, title verification and blockchain/LADM claims cannot be evaluated here.

**Acceptance test:** Provide an authorized test environment, verify a parcel against source records and demonstrate role-based edits and history.

**Commercial route:** Keep as access-restricted and arrange a controlled demonstration.

### 21. JACS Hospice Management Platform

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Could reduce duplicated hospice scheduling and care documentation.

**Observed:** JACS Medical destination and bundle are reachable; bundle contains clinical workflow and demo-seeding paths. No patient records were inspected.

**Gap:** Clinical controls, production data protection, tenancy, backups and operational suitability were not verified.

**Acceptance test:** Use synthetic patients to test care-plan permissions, corrections, exports and recovery with the clinical operator.

**Commercial route:** Institution-led evaluation with synthetic data before live use.

Current destination: [https://jacs-enterprise-medical.lovable.app](https://jacs-enterprise-medical.lovable.app)

### 22. BetterBooks Caribbean Marketing Page

Status: **Website**. Review scope: Public website and bundle inspection.

**Business value:** Explains BetterBooks services and supports lead generation.

**Observed:** A separate BetterBooks marketing destination and bundle are reachable.

**Gap:** This is a marketing page, not another accounting engine. Conversion claims and form delivery remain untested.

**Acceptance test:** Submit an agreed synthetic lead and confirm delivery and owner assignment.

**Commercial route:** Treat as a sales channel for BetterBooks, not a separate SaaS product.

Current destination: [https://better-books-marketing-page.lovable.app/](https://better-books-marketing-page.lovable.app/)

### 23. TV & Radio Financial Management System

Status: **Demo on request**. Review scope: Exact advertised source unavailable.

**Business value:** Could organize advertising revenue, campaign costs and proof-of-play records.

**Observed:** Original company path does not identify the application; current company portfolio config has no real app URL.

**Gap:** No matching application source or functioning destination was established.

**Acceptance test:** Supply the source and demo; reconcile an insertion order to spots delivered, invoice and cash collection.

**Commercial route:** Demo on request until the application is recovered.

### 24. MLS Real Estate Marketplace

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Could centralize property and other asset discovery across the OECS.

**Observed:** Custom-domain destination serves OECS Marketplace. Its public bundle is byte-identical to the OECS Realtors destination.

**Gap:** This appears to be a deployment alias rather than evidence of a separate MLS product; broker data rights and lead routing remain untested.

**Acceptance test:** Trace an authorized listing through search, update, inquiry routing and broker permissions.

**Commercial route:** Consolidate marketplace positioning and confirm listing rights.

Current destination: [https://oecsrealestatemarketplace.com/](https://oecsrealestatemarketplace.com/)

### 25. OECS Realtors Platform

Status: **Accessible · unverified**. Review scope: HTTP and public source inspection.

**Business value:** Connects buyers and sellers of Caribbean properties and other assets.

**Observed:** Lovable destination serves the same title and identical public bundle as the MLS custom-domain deployment.

**Gap:** Do not count this alias as independently delivered SaaS functionality; actual listing and lead operations remain unverified.

**Acceptance test:** Verify listing ownership, moderation, seller contact and stale-listing handling.

**Commercial route:** Use one canonical marketplace and one operating offer.

Current destination: [https://oecs-realtors-platform.lovable.app/](https://oecs-realtors-platform.lovable.app/)

### 26. Wheels Works Auto Shop

Status: **Prototype**. Review scope: Public application bundle inspected.

**Business value:** Demonstrates service booking and vehicle-business operations.

**Observed:** The live Wheels Works destination is branded Smiley Tinting Plus and explicitly labels payment and QuickBooks synchronization as simulated.

**Gap:** Title/positioning differs from a general auto-shop system; live payments, booking concurrency and accounting were not tested.

**Acceptance test:** Race two bookings for the same slot and test a sandbox deposit, refund and accounting reconciliation.

**Commercial route:** Offer a tinting-business demo; validate a pilot before broad auto-shop claims.

Current destination: [https://wheels-works.lovable.app/](https://wheels-works.lovable.app/)

### 27. OECS Trading Platform

Status: **Website**. Review scope: Public website and bundle inspection.

**Business value:** Introduces trading, advisory services and the software portfolio.

**Observed:** The company website and portfolio were inspected; it routes visitors to applications and contact channels.

**Gap:** This is a company website, not evidence of a transactional logistics platform.

**Acceptance test:** Trace a trade inquiry to a named owner and demonstrate any claimed shipment/order workflow separately.

**Commercial route:** Use as the corporate sales channel.

Current destination: [https://oecstrading.com/](https://oecstrading.com/)

### 28. Smiley's Tinting Plus — Business & Inspection Hub

Status: **Prototype**. Review scope: Matching public source inspected.

**Business value:** Shows how a tinting business could coordinate inspections, proposals and accounting views.

**Observed:** Matching GitHub Pages source is Smiley’s Business Hub v12. Source includes simulated Stripe webhook events and client-side payment-link actions.

**Gap:** Sample operations do not establish persistent bookings, AI damage assessment or real payment processing.

**Acceptance test:** Complete an inspection-to-proposal-to-deposit flow in a sandbox and verify persistence and image handling.

**Commercial route:** Controlled service-business demonstration.

Current destination: [https://oecstrading.github.io/Tinting-Business-Platform-plus-Accounting-V11/](https://oecstrading.github.io/Tinting-Business-Platform-plus-Accounting-V11/)

Matching source: [https://github.com/oecstrading/Tinting-Business-Platform-plus-Accounting-V11/blob/main/index.html](https://github.com/oecstrading/Tinting-Business-Platform-plus-Accounting-V11/blob/main/index.html)

### 29. Audit Studio — AI-Powered Audit Platform

Status: **Prototype**. Review scope: Matching public source inspected.

**Business value:** Gives small audit firms a structured engagement and workpaper workspace.

**Observed:** Matching Complete Platform source uses browser localStorage; its FAQ explicitly says cross-device collaboration needs the Phase 2 backend. DeepSeek calls require a configured proxy.

**Gap:** Default demo credentials, browser-side roles and a local hash chain are not hosted identity or an independently immutable audit trail.

**Acceptance test:** Import a synthetic TB, review a workpaper, verify export and restore; separately test backend identity and AI proxy failure.

**Commercial route:** Prioritize a single-workstation pilot, then build shared-service controls.

Current destination: [https://oecstrading.github.io/AI-Financial-Auditor-with-DeepSeek-/](https://oecstrading.github.io/AI-Financial-Auditor-with-DeepSeek-/)

Matching source: [https://github.com/oecstrading/AI-Financial-Auditor-with-DeepSeek-/blob/main/index.html](https://github.com/oecstrading/AI-Financial-Auditor-with-DeepSeek-/blob/main/index.html)

### 30. Caribbean Gas Intelligence — dMRV Monitoring System

Status: **Prototype**. Review scope: Matching public source inspected.

**Business value:** Explains gas monitoring and replenishment workflows to operators and investors.

**Observed:** Matching GitHub Pages document contains a platform/user-guide demonstration. Source has no fetch calls and depicts simulated monitoring/order flows.

**Gap:** No evidence of live sensor ingestion, emergency alarms, payments or dispatched orders was established.

**Acceptance test:** Replay signed sensor readings through alert, operator acknowledgement and a sandbox replenishment event.

**Commercial route:** Sell feasibility and integration work before a monitoring subscription.

Current destination: [https://oecstrading.github.io/Caribbean-Gas-Intelligence-St.-Lucia-Pilot-/](https://oecstrading.github.io/Caribbean-Gas-Intelligence-St.-Lucia-Pilot-/)

Matching source: [https://github.com/oecstrading/Caribbean-Gas-Intelligence-St.-Lucia-Pilot-/blob/main/index.html](https://github.com/oecstrading/Caribbean-Gas-Intelligence-St.-Lucia-Pilot-/blob/main/index.html)

### 31. Antillia Skills Bank — Verified Professionals

Status: **Prototype**. Review scope: Matching public source inspected.

**Business value:** Demonstrates talent discovery, filtering and profile presentation.

**Observed:** Matching source explicitly declares eight demo workers but displays verified-worker claims and a much larger headline count.

**Gap:** Background checks, credential verification, actual worker availability and real client ratings were not evidenced.

**Acceptance test:** Use consented test profiles; verify credentials against source documents and distinguish pending from verified.

**Commercial route:** Recruit a documented pilot cohort before marketplace launch.

Current destination: [https://oecstrading.github.io/Antillia-Skills-Bank/](https://oecstrading.github.io/Antillia-Skills-Bank/)

Matching source: [https://github.com/oecstrading/Antillia-Skills-Bank/blob/main/index.html](https://github.com/oecstrading/Antillia-Skills-Bank/blob/main/index.html)

### 32. Biogas St. Lucia — Northern Pilot (Gros Islet)

Status: **Planning document**. Review scope: Matching engineering source inspected.

**Business value:** Communicates a proposed northern Saint Lucia digester and filling-station design.

**Observed:** Matching source contains engineering tabs and fixed commercial-scale payback/IRR values. It describes a 6 m³ pilot and larger-scale economics.

**Gap:** Fixed displayed figures are scenarios, not operating returns or a validated financial engine; pilot and commercial-scale results must remain separate.

**Acceptance test:** Rebuild cash flows with feedstock, uptime, upgrading, compression, delivery and maintenance assumptions, then independently recalculate returns.

**Commercial route:** Engineering feasibility and investor discussion document.

Current destination: [https://oecstrading.github.io/Biogas-St-Lucia-Filling-Station-Pilot/](https://oecstrading.github.io/Biogas-St-Lucia-Filling-Station-Pilot/)

Matching source: [https://github.com/oecstrading/Biogas-St-Lucia-Filling-Station-Pilot/blob/main/index.html](https://github.com/oecstrading/Biogas-St-Lucia-Filling-Station-Pilot/blob/main/index.html)

### 33. Biogas St. Lucia — Vieux Fort Pilot

Status: **Demo on request**. Review scope: Exact advertised source unavailable.

**Business value:** Could communicate a separate Vieux Fort pilot design and budget.

**Observed:** The advertised local HTML is absent. The recovered northern-pilot source mentions Vieux Fort comparisons but is not the specified Vieux Fort application.

**Gap:** An exact matching source was not established; quoted CAPEX and returns cannot be checked as an app.

**Acceptance test:** Recover the exact design and reconcile mass/energy balance, BoQ and cash-flow assumptions.

**Commercial route:** Keep as demo on request rather than substituting the northern pilot.

### 34. COSMOS Biogas Haiti — Filling Station Pilot

Status: **Planning document**. Review scope: Matching engineering source inspected.

**Business value:** Explains a proposed Haitian biogas filling station and equipment scope.

**Observed:** Matching GitHub Pages source is COSMOS Biogas Filling Station — Engineering Design Package, with equipment, cost and climate sections.

**Gap:** A design document does not demonstrate installed plant, sales, registry issuance or measured emissions.

**Acceptance test:** Validate supplier quotes, gas quality assumptions, plant uptime and cash flows against the engineering design.

**Commercial route:** Commissioned feasibility and procurement planning.

Current destination: [https://oecstrading.github.io/Biogas-Haiti-Filling-Station-Pilot/](https://oecstrading.github.io/Biogas-Haiti-Filling-Station-Pilot/)

Matching source: [https://github.com/oecstrading/Biogas-Haiti-Filling-Station-Pilot/blob/main/index.html](https://github.com/oecstrading/Biogas-Haiti-Filling-Station-Pilot/blob/main/index.html)

### 35. Biogas Haiti — Industrial Division (1,000 m³)

Status: **Demo on request**. Review scope: Exact advertised source unavailable.

**Business value:** Could present the economics and rollout of a larger Haitian digester.

**Observed:** No exact standalone 1,000 m³ industrial-division source was established. The recovered filling-station package has an integration reference only.

**Gap:** A related engineering reference cannot establish the advertised industrial app or its claimed return figures.

**Acceptance test:** Recover the industrial model, reconcile annual production and operating costs, and calculate NPV/IRR from explicit cash flows.

**Commercial route:** Keep exact product unavailable; identify related material separately.

Related material — different edition: [https://oecstrading.github.io/Biogas-Haiti-Filling-Station-Pilot/](https://oecstrading.github.io/Biogas-Haiti-Filling-Station-Pilot/)

### 36. BiogasSTLucia — GCF/CDB Concept Note

Status: **Demo on request**. Review scope: Exact advertised source unavailable.

**Business value:** Supports development of a climate-finance concept note.

**Observed:** An exact 18-section GCF/CDB concept-note file was not established. A related BiogasSTLucia master proposal exists and includes sensor simulation.

**Gap:** Related proposal material is not the advertised exact grant document and does not evidence funding approval.

**Acceptance test:** Recover the exact submission; reconcile budget, financing sources, results framework and supporting evidence.

**Commercial route:** Proposal-development service; demo on request for this edition.

Related material — different edition: [https://oecstrading.github.io/Biogasstlucia/](https://oecstrading.github.io/Biogasstlucia/)

### 37. Rivet & Roan Barber Co. — Booking Platform

Status: **Demo on request**. Review scope: Exact advertised source unavailable.

**Business value:** Could automate barber appointment availability and reduce no-shows.

**Observed:** Advertised local booking HTML is absent and no matching repository was established.

**Gap:** Slot locking, deposits, reminders and waitlist automation cannot be verified.

**Acceptance test:** Recover source, attempt simultaneous bookings and verify sandbox deposit/refund and reminder delivery.

**Commercial route:** Keep off the launch path pending recovery.

### 38. CaribCarbon — Caribbean Climate Asset Marketplace

Status: **Demo on request**. Review scope: Exact advertised source unavailable.

**Business value:** Could help project developers compare climate-asset opportunities.

**Observed:** The exact CaribCarbon app was not found. An older OECS carbon marketplace repository is related material, not a confirmed match.

**Gap:** Country parameters, revenue share, registry integration and tradable assets are unverified.

**Acceptance test:** Recover exact source and reconcile each calculator; trace a project to independent validation and registry records.

**Commercial route:** Demonstration on request; do not imply issued credits or guaranteed income.

Related material — different edition: [https://github.com/oecstrading/OECS-Prototypes](https://github.com/oecstrading/OECS-Prototypes)

### 39. The AI AML/CFT Compliance Auditor — Standalone

Status: **Demo on request**. Review scope: Exact advertised source unavailable.

**Business value:** Could organize AML/CFT controls, deficiencies and workpapers.

**Observed:** Advertised standalone AML/CFT HTML is absent; no exact matching source was established.

**Gap:** Password gating and local attestations would not alone establish regulated access controls or compliance.

**Acceptance test:** Recover source and test import mapping, evidence retention, role isolation and reviewed report output using synthetic cases.

**Commercial route:** Recover and review before selling a compliance product.

### 40. Caribbean Micro-Lending Enterprise Matrix

Status: **Demo on request**. Review scope: Exact advertised source unavailable.

**Business value:** Could support loan aging, underwriting and ledger reporting.

**Observed:** Exact standalone Enterprise Matrix HTML is absent. The recovered Caribbean Finance Hub is a related micro-lending risk-engine destination.

**Gap:** Do not present a related version as the recovered standalone edition; exact calculations and RBAC remain unverified.

**Acceptance test:** Recover exact edition or formally consolidate with Finance Hub after a reconciled loan-book test.

**Commercial route:** Consolidate the product family; related demo only.

Related material — different edition: [https://carib-glide.lovable.app/](https://carib-glide.lovable.app/)

### 41. AI Financial Statement Generator — Audit Platform

Status: **Demo on request**. Review scope: Exact advertised source unavailable.

**Business value:** Could turn a mapped trial balance into reviewed financial statements.

**Observed:** The company portfolio currently points this listing to the same Audit Studio URL as entry 29. An exact standalone generator source was not established.

**Gap:** Duplicate destination is not evidence of a separate four-step generator or its PDF/Excel exports.

**Acceptance test:** Recover the exact module and reconcile position, performance, cash flow, notes and exports from a synthetic TB.

**Commercial route:** Position as a reporting module until separately demonstrated.

Related material — different edition: [https://oecstrading.github.io/AI-Financial-Auditor-with-DeepSeek-/](https://oecstrading.github.io/AI-Financial-Auditor-with-DeepSeek-/)

### 42. JACS Payroll — Caribbean-Compliant Payroll for QuickBooks

Status: **Accessible · unverified**. Review scope: Authenticated interface inspected; no mutations.

**Business value:** Helps Caribbean employers organize payroll, attendance and payslips.

**Observed:** The current OECS HR & Payroll destination opened an authenticated workspace with company selection and payroll navigation. No payroll was run and no private employee details are reproduced here.

**Gap:** Nine-country statutory accuracy, cross-company isolation and live QuickBooks posting were not tested.

**Acceptance test:** Use a synthetic payroll in each supported country; independently verify deductions, approval, payslip and duplicate-safe sandbox posting.

**Commercial route:** Prioritize an accountant-led payroll pilot with versioned country rules.

Current destination: [https://caribbean-payroll-with-quickbooks.lovable.app/](https://caribbean-payroll-with-quickbooks.lovable.app/)

### 43. Project Support for Dominica

Status: **Planning document**. Review scope: Matching public source inspected.

**Business value:** Helps public-sector counterparts review a structured project-development approach.

**Observed:** Matching public source is an expression-of-interest and project-development support hub with phase tasks, results framework, risk matrix and browser-local progress. It explicitly describes the M&E/MRV systems as prototypes not yet deployed in any country.

**Gap:** A proposal workspace does not demonstrate a commissioned institutional MIS or government adoption.

**Acceptance test:** Walk through one synthetic deliverable review, export the results framework and verify what progress persists across devices.

**Commercial route:** Offer project-development consulting with a supporting workspace.

Current destination: [https://oecstrading.github.io/dominica-project-development-support/](https://oecstrading.github.io/dominica-project-development-support/)

Matching source: [https://github.com/oecstrading/dominica-project-development-support/blob/main/index.html](https://github.com/oecstrading/dominica-project-development-support/blob/main/index.html)

### 44. Loyverse Bridge

Status: **Accessible · unverified**. Review scope: Authenticated inventory interface inspected; no mutations.

**Business value:** Could reduce duplicate work between restaurant inventory and accounting systems.

**Observed:** Browser opened the inventory workspace. It asks the user to connect Loyverse and import stores before adding inventory locations, and labels payroll and tables as sample modules.

**Gap:** Multi-store stock consistency, recipe depletion, webhook idempotency and bookkeeping are not verified by a reachable route.

**Acceptance test:** Replay duplicate and out-of-order sale webhooks across two sandbox stores; reconcile recipe depletion, stock and balanced journal entries.

**Commercial route:** One restaurant integration pilot after inventory reconciliation acceptance.

Current destination: [https://loyverse-inventory-bridge.lovable.app/inventory](https://loyverse-inventory-bridge.lovable.app/inventory)

### 45. Generative Legal Chambers

Status: **Prototype**. Review scope: Matching public source inspected.

**Business value:** Demonstrates intake, draft preparation and legal-matter presentation.

**Observed:** Matching public source includes case and invoice views, templated draft generation and client-side actions. Attorney-review and LEDES-download buttons display alerts describing production behavior.

**Gap:** An alert saying a draft was sent is not attorney delivery or e-filing. The source does not establish a working AI service, trust accounting or protected client workspace.

**Acceptance test:** Use a synthetic matter; trace document generation, counsel receipt, permissions and audit history without real filing or agreement execution.

**Commercial route:** Counsel-supervised prototype demonstration; implement protected matter workflows before operational use.

Current destination: [https://oecstrading.github.io/Generative-Lawyers/](https://oecstrading.github.io/Generative-Lawyers/)

Matching source: [https://github.com/oecstrading/Generative-Lawyers/blob/main/index.html](https://github.com/oecstrading/Generative-Lawyers/blob/main/index.html)

### 46. QuickBooks Desktop Bridge to QB Online

Status: **Accessible · unverified**. Review scope: Browser landing page inspected.

**Business value:** Could connect legacy QuickBooks POS Desktop sales to QuickBooks Online.

**Observed:** Browser landing page is specifically QB POS Desktop v19 to QBO, with agent, scheduled sync, OAuth and AI error-handling claims. It offers sign-in and a trial.

**Gap:** This is narrower than a general QuickBooks Desktop migration bridge. Agent installation, token isolation, idempotency and accounting accuracy were not tested.

**Acceptance test:** In disposable POS/QBO companies, sync a sale and refund twice, refresh an expired token and reconcile item, tax and payment mappings.

**Commercial route:** Implementation-led migration/integration pilot; verify the actual source-product scope.

Current destination: [https://qb-bridge-ai-buddy.lovable.app/](https://qb-bridge-ai-buddy.lovable.app/)

### 47. JACS Financial Management System with POS and QB Integration

Status: **Access restricted**. Review scope: HTTP access check only.

**Business value:** Could combine POS operations and bookkeeping in one workflow.

**Observed:** The saved Manus destination returned HTTP 403 during the automated check. A related JACS POS source exists, but exact deployment/version matching was not established.

**Gap:** Restricted access prevents assessing the live app; a related repository is not evidence of this deployment’s current functionality.

**Acceptance test:** Provide authorized test access and complete a synthetic sale, refund, stock update and duplicate-safe QuickBooks sandbox posting.

**Commercial route:** Arrange a controlled demonstration; keep public launch withheld until verified.

## Evidence files

- original-link-audit.json: original 42 GET checks, including body hashes.

- destination-audit.json: actual destinations obtained from the company portfolio and their GET responses.

- github-pages-audit.json: recovered matching demonstration URLs.

- additional-destinations.json: IFRS studio and payroll URLs.

- bundle-audit.json: public bundle URLs and superficial code counts, used only as navigation/inspection aids. Counts of fetch, storage or demo strings are not functionality or security scores.

- supplemental-destinations.json: five browser-saved additions and HTTP checks.

- current-link-audit.json: final destination and related-link GET checks.

- VALIDATION.md: rebuilt catalogue validation and limitations.

All checks are point-in-time. Domain availability and application behavior may change.
