# OECS SaaS catalogue

[View the public catalogue](https://oecstrading.github.io/SaaS-Software-as-a-Service/#catalogue)

## Maintain the catalogue

Sign in to GitHub and [edit catalog.json](https://github.com/oecstrading/SaaS-Software-as-a-Service/edit/main/catalog.json). GitHub requires repository write access to publish edits to this repository. Public visitors can browse the deployed listings. A fork or pull request cannot change the deployed catalogue without an authorized merge.

- **Add** a listing by copying an existing JSON object and assigning a previously unused positive integer ID. Update the title, industry, type, description, technologies, access note and launch URL. Keep `url` consistent with `current_url`.
- **Modify** a listing in place and retain its ID.
- **Remove** a listing's entire JSON object and an adjacent comma if present. Use an empty array if removing all listings.
- Use an absolute HTTPS launch URL, or empty URL fields for a demo by request.
- Commit on `main` or open a pull request. After GitHub Pages deploys, refresh the catalogue and check the listing and launch link.

The public portfolio loads `catalog.json` directly. Use `index.html` for design changes. Keep credentials and private material out of the public repository.
