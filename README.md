# OECS Software Portfolio

Public portfolio: https://oecstrading.github.io/SaaS-Software-as-a-Service/

42 individual app assessments, corrected destinations, search and filters, three-app comparisons, browser-local inquiry shortlist, email drafts and a printable portfolio review. Rebuilt 10 November 2026.

This repository presents software offerings; it does not host their backends or certify production readiness. An unavailable edition is labelled explicitly. Compatibility pages under this repository’s `apps/` directory resolve to the relevant assessment; historical root-absolute `/apps/` URLs are outside this repository’s control. The alternate `index1.html` redirects to the canonical catalogue.

## Maintain

Edit `catalog.json`, then run:

```sh
python scripts/build-review.py
python scripts/check-catalog.py
node --check app.js
node --check catalog-data.js
```

Optional point-in-time external link check:

```sh
python scripts/check-catalog.py --http
```

GitHub Pages serves the root directly. There are no dependencies or build tools. Deploy the static root on the existing Pages configuration. `catalog-data.js` is generated so the catalogue also works without fetching JSON at runtime. Keep it synchronized using the generator.

## Review and validation

- [Written review](review/PORTFOLIO_REVIEW.md)
- [CSV assessment table](review/assessment.csv)
- [Validation and limits](review/VALIDATION.md)
- [Final URL checks](review/current-link-audit.json)

The shortlist stores only app IDs on the visitor's browser. Contact controls prepare email drafts; the site never claims an email has been sent. There is no simulated login, admin control, server-side form submission or checkout. Source changes to underlying applications are outside this portfolio rebuild.
