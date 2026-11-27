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

Company subpages: `mission.html`, `values.html`, `careers.html`, and `contact.html`. Values and approach copy are drafts based on the company mission. General and careers enquiries currently use `the publisher’s confirmed inbox`, as specified by the owner. Do not invent job openings. Shared dropdown behavior is in `navigation.js`.

## Contact form

`contact.html` submits directly to FormSubmit over HTTPS and delivers enquiries to `the publisher’s confirmed inbox`. Native required-field and email validation work without JavaScript; FormSubmit provides its confirmation page and default CAPTCHA. No test submission has been sent. Before launch, submit a message yourself and follow the activation email sent to `the publisher’s confirmed inbox`, then send a second message to verify delivery. The form discloses the external processing provider. No API keys or mail credentials are stored in the website.

The careers form in `careers.html` uses the same FormSubmit recipient with a separate careers subject. It collects name, email, area of interest, an optional LinkedIn URL, and an introduction. No careers test enquiry has been sent.

## Search visibility

All pages have unique titles, descriptions, and HTTPS canonical URLs. The homepage canonical is `https://hoplontec.io/`; home links use `./`. `sitemap.xml` lists the eight canonical pages, and `robots.txt` references it. The shared packaging script copies both files into deployment output. When adding a page, update the sitemap and the workflow’s public-file list. Armur artwork uses responsive WebP assets; the original PNG is retained as source.

After deployment, the owner should verify the `hoplontec.io` Domain property in Google Search Console using its supplied DNS TXT record, submit `https://hoplontec.io/sitemap.xml`, and inspect the homepage and brands page with URL Inspection. No verification code has been invented or added. Google Analytics is separate from Search Console; indexing and rankings are not guaranteed. Review Page indexing and Core Web Vitals reports when data becomes available.

## NiviLog

`nivilog.html` is the dedicated product page linked from its card in `brands.html`. It is included in the sitemap and copied by the shared packaging script. Copy and artwork are based on the local NiviLog project's README and development previews, reviewed November 24, 2026. The owner confirmed that release is coming soon; the app is presented for adults 18+, with no unverified store links, release date, price, or medical benefit claims. Confirm public-release status and contact details before adding install badges.

NiviLog’s expanded product page uses optimized meal-entry and feeling-overview development screenshots, a three-screen walkthrough, and accessible native FAQ disclosures. Source screenshots are in the local NiviLog project’s `docs/previews`; captions identify them as development examples.

## NiviLog legal pages

The English and Spanish NiviLog legal pages mirror the app sources, privacy version 2026-11-25.5 and terms version 2026-11-25.2. They keep pre-release status and use the public contact form for privacy enquiries. Downloadable rendered Markdown copies are in assets/legal. Keep these copies synchronized using scripts/sync-nivilog-legal.py.

## NiviLog feedback (English and Spanish)

`nivilog-feedback.html` and `nivilog-feedback-es.html` are the app-linked forms. They collect only a required 1–5 satisfaction rating, optional topic/comment, language/product labels and an optional per-submission reference. There is no name/email input, analytics tag, automatic attachment, browser-content storage or private journal connection. Default FormSubmit CAPTCHA remains enabled. Native HTML validation/POST work without JavaScript; JavaScript adds double-click prevention and a random reference displayed on the matching completion page. The completion page does not claim to verify inbox delivery.

**Activation:** open the FormSubmit activation/confirmation email received by the existing form owner. Confirm the inbox and copy the opaque “invisible email” identifier from the supplied `https://formsubmit.co/<id>` endpoint. Put **only the identifier** in `feedback-config.json` as `formId`. Never put the receiving address, a password or an API key there. Empty configuration leaves both forms disabled with an honest notice; malformed configuration fails packaging. The identifier is a public form handle, not a secret. The packaging script injects it and also replaces plain inbox destinations in packaged contact/careers forms. Once the ID is supplied, replace those destinations in the source templates too so new source revisions do not expose the address; already-published Git history is unaffected.

Run `python3 scripts/test_feedback.py`, `node scripts/test-feedback.cjs`, and the existing Pages packaging command. Both Pages workflows run these checks. Publish through the existing main-branch GitHub Pages workflow; no new hosting service or domain is needed. Verify the two public pages and then have the inbox owner make a test submission and confirm receipt. Automated tests never send an email or solve a CAPTCHA.

Hoplontec should restrict inbox access and remove product-feedback messages within 180 days, including controlled copies/exports. FormSubmit documents a 30-day archive; email retention is managed by the inbox owner. Ratings are responses, not verified unique customers. This email flow does not automatically produce the standalone receiver’s satisfaction reports. See https://formsubmit.co/documentation and https://formsubmit.co/privacy.pdf for provider behavior.

**Legal synchronization:** `python3 scripts/sync-nivilog-legal.py /absolute/path/to/NiviLog/assets/legal` renders the current app sources in both languages, using the public contact form as the privacy contact. Update the version constants in that script when app legal versions change. This change uses privacy 2026-11-25.5 and terms 2026-11-25.2, retains pre-release status and adds no analytics to these legal pages. Do not publish personal data, inbox contents, confirmation emails or API keys in this public repository.

The confirmed opaque FormSubmit handle is now configured for both NiviLog feedback languages and the existing contact/careers forms. Current form templates and deployment artifacts use that handle instead of the receiving inbox address. No live test email was sent by automated validation.

The NiviLog page now uses seven owner-supplied iPhone screenshots (IMG_9249–IMG_9255, November 25, 2026), stored as optimized WebP assets with the `20261125` suffix. The full screenshot content is preserved; walkthrough images link to larger copies. Older development previews remain in assets but are no longer displayed on the page.

## NiviLog video demo

The owner-supplied NiviLog-Website-Demo.zip provides the video tour in `assets/nivilog-demo/`, with landscape/portrait MP4s, posters, English captions, transcript, and production credits/licenses. The page selects the portrait edit on initial mobile load, never autoplays, and uses `preload="none"`. All assets are included by the existing assets-copy deployment step.


## NiviLog explainer

The product page also includes the 1 minute 47 second guide at `#explainer`.
Its landscape/mobile MP4s, posters, English captions, chapter track, transcript,
and production credits are in `assets/nivilog-explainer/`. The original 41-second
demo remains at `#demo`. Both use the same female English synthetic narrator.
Native controls, `preload="none"`, and no autoplay keep playback user initiated.
The shared `assets/nivilog-demo/player.js` selects the portrait edit once on mobile
and pauses the other video when playback starts. Without JavaScript, landscape
videos and captions remain usable. Each video has an expandable text transcript.
No external video service or player dependency is added. The existing Pages
workflow copies these assets automatically; the script URL has a content hash so
visitors receive the updated two-player behavior.


The demo and explainer share a two-column layout from 64rem (1024 CSS pixels),
with aligned player rows. They stack below that width. Each keeps its own native
controls, captions and transcript; opening a transcript does not shift the other
player. Portrait source selection on initial phone load is unchanged.
