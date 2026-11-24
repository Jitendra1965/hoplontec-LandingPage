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

## Search visibility

All pages have unique titles, descriptions, and HTTPS canonical URLs. The homepage canonical is `https://hoplontec.io/`; home links use `./`. `sitemap.xml` lists the eight canonical pages, and `robots.txt` references it. The shared packaging script copies both files into deployment output. When adding a page, update the sitemap and the workflow’s public-file list. Armur artwork uses responsive WebP assets; the original PNG is retained as source.

After deployment, the owner should verify the `hoplontec.io` Domain property in Google Search Console using its supplied DNS TXT record, submit `https://hoplontec.io/sitemap.xml`, and inspect the homepage and brands page with URL Inspection. No verification code has been invented or added. Google Analytics is separate from Search Console; indexing and rankings are not guaranteed. Review Page indexing and Core Web Vitals reports when data becomes available.

## NiviLog

`nivilog.html` is the dedicated product page linked from its card in `brands.html`. It is included in the sitemap and copied by the shared packaging script. Copy and artwork are based on the local NiviLog project's README and development previews, reviewed November 24, 2026. The owner confirmed that release is coming soon; the app is presented for adults 18+, with no unverified store links, release date, price, or medical benefit claims. Confirm public-release status and contact details before adding install badges.

NiviLog’s expanded product page uses optimized meal-entry and feeling-overview development screenshots, a three-screen walkthrough, and accessible native FAQ disclosures. Source screenshots are in the local NiviLog project’s `docs/previews`; captions identify them as development examples.

## NiviLog legal pages

`nivilog-privacy.html` and `nivilog-terms.html` reproduce the English legal documents from NiviLog `assets/legal/`, versions 2026-11-24.3 and 2026-11-24.2. Publisher/address come from that project; contact is the owner-provided legal@armur.org. Public policy links point to the Hoplontec copy. Both retain a pre-release draft notice. Downloadable rendered Markdown copies are in `assets/legal/`. Update these copies alongside app legal changes; the NiviLog release configuration itself has not been changed.
