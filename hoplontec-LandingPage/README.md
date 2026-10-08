# Hoplontec Inc.

A responsive, build-free landing page for Hoplontec Inc. and its Armur brand. Ivory and bottle green, with system fonts and no external dependencies or tracking.

## Preview

Run `python3 -m http.server 8080` in this directory and open http://localhost:8080.

## Publish with GitHub Pages

1. Authenticate with GitHub using `gh auth login`.
2. Create or choose a public repository and push these files to its `main` branch.
3. In the repository's **Settings → Pages**, select **GitHub Actions** as the source.
4. Run the **Deploy landing page** workflow, or push a change to `main`.

The workflow publishes only the public page files and assets. Relative asset paths work on both project and organization Pages URLs. Review GitHub Pages' current usage limits before publishing a business site: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits

## Content

Edit the homepage in `index.html`, the brands directory in `brands.html`, and company information in `company.html`. Add future brands as additional articles inside the brands page’s `.brand-grid`. Edit text and links in these HTML files; colors and layout are in `styles.css`. The Armur artwork in `assets/armur-brand.png` was supplied by the owner and is displayed unchanged. Hoplontec uses a plain text name; no company logo has been supplied. Company details were supplied by the owner. The product description is based on https://armur.org/ and links to that site. Add a company contact email when available. No product availability or company contact address is assumed.

Company subpages: `mission.html`, `values.html`, `careers.html`, and `contact.html`. Values and approach copy are drafts based on the company mission. General and careers enquiries currently use `legal@armur.org`, as specified by the owner. Do not invent job openings. Shared dropdown behavior is in `navigation.js`.

## Contact form

`contact.html` submits directly to FormSubmit over HTTPS and delivers enquiries to `legal@armur.org`. Native required-field and email validation work without JavaScript; FormSubmit provides its confirmation page and default CAPTCHA. No test submission has been sent. Before launch, submit a message yourself and follow the activation email sent to `legal@armur.org`, then send a second message to verify delivery. The form discloses the external processing provider. No API keys or mail credentials are stored in the website.

The careers form in `careers.html` uses the same FormSubmit recipient with a separate careers subject. It collects name, email, area of interest, an optional LinkedIn URL, and an introduction. No careers test enquiry has been sent.
