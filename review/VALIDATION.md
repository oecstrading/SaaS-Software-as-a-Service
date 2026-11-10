# Validation — 10 November 2026

## Passed

- Data invariants: 47 unique IDs and complete individual assessments; generated browser data matches catalog.json.
- JavaScript syntax: app.js and catalog-data.js passed `node --check`.
- Destination check: all 38 unique launch/related-material URLs responded HTTP 200 at the final check. There are 36 per-listing public launch destinations, nine unavailable exact editions and two restricted editions.
- Browser preview: all 42 original direct assessment routes displayed their corresponding app titles. An unavailable edition offered an app-specific email draft instead of a broken launch.
- Search: a QuickBooks Utility query narrowed results to one; a nonsense query displayed the empty state. Reset restored 42 offerings.
- Status filter: Demo tested narrowed results to two.
- Shortlist: adding an offering updated the saved state and produced an email draft containing its name and review status. No email was sent.
- Comparison: FaMaaS and QuickBooks Utility displayed side-by-side business value, evidence, remaining gaps and acceptance tests.
- Desktop visual inspection: catalogue, typography, summary counts and detail presentation inspected in the browser preview.
- Static compatibility pages: repository-local `apps/*.html` routes map to the corresponding assessment. index1.html redirects to the canonical root.

## Limits

- Catalogue QA does not imply every underlying app feature was tested. Only FaMaaS demo setup and QuickBooks Cleanup sample/validation workflows were exercised as operational sample flows during the app review.
- An authenticated payroll workspace and other public interfaces were observed without executing payroll, payments, QuickBooks mutations or sending notifications.
- No production-readiness certification, security penetration test, statutory calculation certification or financial-model assurance is provided.
- Responsive CSS is supplied; a separate mobile-device browser run was not performed.
- Print behavior is implemented; a full exported PDF was not generated or visually verified.
- Historical root-absolute `https://oecstrading.github.io/apps/...` URLs belong outside this repository's Pages prefix and cannot be repaired by this repository alone. Current catalogue links no longer use them. Compatibility pages support the correct `/SaaS-Software-as-a-Service/apps/...` prefix.
- Email inquiry depends on a configured email application. It is labelled as a draft; there is no server-side submission or delivery claim.
- No underlying app backend, schema, tax engine or third-party deployment was modified.

Five additional listings (43–47) were discovered in the authenticated browser’s old portfolio admin display after the first publication. They were recovered into the published catalogue and individually screened. Four returned HTTP 200; the fifth returned 403.
