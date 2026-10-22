# Lumova store handoff

Status as of 2026-10-22. Written so a new session can continue without the old chat.

## Goal
Launch a Shopify dropshipping store (brand: Lumova, domain: lumovaco.com) with organic content only (Higgsfield for video and photos). No ad spend. Original ask: an AI dropshipping setup in the style of Davie Fogarty's "I Helped a Complete Stranger Build an AI Ecom Store" video (youtube.com/watch?v=MxjwiA7cCpI; transcript could not be fetched, YouTube rate-limits), thinking like an e-commerce executive (Davie Fogarty, Jordan Welch, Bia Heza, Hormozi). Deadline pressure: sites and supplier outreach were wanted the same night (10pm+).

## User preferences (keep following)
- Talk like to a fifth grader: short, plain, bullet points, condensed. The user also asked for strict token-efficient mode at one point.
- The user is time-poor and wants the agent to act autonomously and only ask big decisions. They offered passwords; do not accept passwords or tokens in chat. Use environment secrets.
- The user wants the agent to test everything itself before reporting, and to be honest about what is unverified.
- Margin standard is 70% net, held firmly. Prefer complete kits where the customer needs nothing else.

## History in one paragraph
Earlier sessions (not in this repo) built a master product list of refill products and a "dropshipping marketing brain" (see the claude.ai artifact "Master Product List", ad-library research via Meta Ad Library: Muravai shower filters ran 376 days, Helios sink filter 109 days). This session narrowed to shower filter + razor, found the friend's store "Luminyx" (single-blade women's razor, $45, reportedly six figures a month) as the layout reference, bought lumovaco.com (about 200 `.com` names were checked; many were taken), researched CJ listings through the user's local browser session, built two product pages in Shopify, and hit the limits below.

## Sourcing rules
- Plan: find products on AliExpress or Alibaba, fulfill through ZenDrop; use CJ Dropshipping as another source. ZenDrop is installed on the store (a "Zendrop" shipping profile exists) but the account has no active plan, so its catalog is paywalled.
- Order samples before any ads. Contact suppliers only after margin is confirmed.
- CJ blocks crawlers with a human-verification page. A crawler user agent returns the page, but that is spoofing; do not do it. Use the user's logged-in browser session.
- AliExpress search pages are readable by plain fetch (price, sold count, rating); item pages are blocked.

## Store state
- Shopify store `wrpnhp-8d`. Storefront is password-locked. All products are DRAFT.
- Theme work lives in an UNPUBLISHED theme "Lumova Build" (id `gid://shopify/OnlineStoreTheme/188222406904`), duplicated from live Horizon. Live theme is untouched.
- Custom files in that theme: `sections/lumova-landing.liquid`, `assets/lumova.css`, `assets/lumova.js`, and one product template per product (`templates/product.lumova-*.json`). Page style is modeled on a friend's single-product razor store (pastel bands, arch hero, circled headline word, "choose your" cards), with our own colors and copy.
- Shopify connector limits: it cannot change the storefront password, payments test mode, shipping rates that use conditions, or shop policies (missing `write_legal_policies`). It cannot publish themes.

## Products
| Product | Price | Landed cost | Net margin | Source |
|---|---|---|---|---|
| Shower Complete Set: handheld head, 1.5 m hose, chrome arm adapter with holder, thread tape, 5 cartridges | $59.99 | $15.12 ($3.19 + $11.93 shipping) | 71.4% | CJ CJYD2842575, Suit 12 |
| Showerhead + 5 cartridges, no hose | $44.99 | $10.26 | 73.6% | CJ Suit 1 |
| Shower refill 3-pack | $19.99 (raise to $22.99 for 70%) | $5.83 | 66% | CJ |
| Razor set: rose gold razor, stand, 10 blades, kraft box | $44.99 | $10.89 | 72.2% | CJ CJBJPFTX00401 variant |

Shopify product ids: shower `15431900332280`, razor `15431900430584`.
Archived (below 70%): blemish patches, face/brow razors, eye patches.
Margin rule: 70% net after Shopify's 2.9% + 30c fee, shipping included in landed cost. Max landed cost = 0.271 x price - 0.30.

## Claims rules
- No chlorine, fluoride, skin, acne, or health claims. Cartridge material is unverified.
- The razor is light (about 56 g). Never say "weighted". Standard 43 x 22 mm double-edge blades fit.
- Shipping copy: 7 to 15 business days. Free US shipping.
- Do not use supplier text overlays ("Cross-Border", "Drop Shipping") or stock-model photos.

## Product hunt result
CJ had no qualifying listing for: heatless curl set, facial sculpting kit, shower brush set, razor + mitt bundle, bonnet set. Only a silk-style sleep set matched, and it misses 70% (66% at $39.99). ZenDrop needs an active plan before its catalog opens. Need 3 more products; none chosen.

## Open items
1. Samples of Suit 12 and the razor set before any ads. Check hose, adapter thread, bracket, cartridge material, and the razor head's possible supplier engraving.
2. Ask CJ about custom branding, unbranded razor head, and photo permission.
3. Original photos from Higgsfield to replace supplier images (prompts were written in chat; shower and razor each need hero, flat-lay, lifestyle, detail, refill/blade shots).
4. Paste refund, shipping, and terms policies in Shopify (drafts were sent as `lumova-policies.md`). Set Standard shipping to $0.
5. Replace the public home address and personal email in the privacy policy with business ones.
6. Install Shopify Subscriptions for refills.
7. Publish "Lumova Build", set products Active, remove the store password.

## Launch gates (all must pass)
1. Crawler clicks every link and button on every page: 0 broken.
2. Test order completes (cart, checkout, confirmation) on desktop and mobile. Plan: 100%-off discount code plus free shipping, so no payment mode is needed.
3. Mobile Lighthouse: performance 80+, accessibility 90+.
4. A reviewer agent that did not build the site passes product pages, navigation, search, policies, and original copy and images, with screenshots and the crawl log.
5. Conversion rate and AOV tracking live. New store: day 0 is the baseline.
Current status: gates 1-4 not run. Store is locked and photos are supplier images.

## How we work
- Agent acts alone on: draft edits, unpublished-theme edits, margin checks, crawls, speed tests, test orders, research tables.
- Agent asks first on: publishing, spending money, prices under 70% margin, supplier outreach, deleting things, anything customers see.
- Access: use a Shopify custom app token stored as an environment secret (`SHOPIFY_ADMIN_TOKEN`), never pasted into chat. Logged-in sites (CJ, ZenDrop, Meta Ad Library, TikTok Creative Center, Google Ads Transparency) run in a local session with the browser; the cloud session writes the prompts and tables.
- Do not bypass bot checks on supplier sites (CJ blocks crawlers; do not spoof a crawler user agent).

## Marketing angles to test
- Shower: the whole setup in one box; about $3 a month in refills; swaps in minutes.
- Razor: cents per blade; less plastic; one blade, one pass.
- Patterns seen at Supply (education, ritual, guarantee) and Starface/Hero (bundles, free gift, TikTok clips).

## Decisions log
- Curated store: two hero kits now; add pages only when a supplier passes 70% net margin.
- Dropped for margin: patches, brow razors, eye patches. Dropped silk sleep set (66% at $39.99).
- Shower sold as a complete set (Suit 12), not head-only, so the customer needs nothing else. Razor sold as a set with stand.
- Razor copy says 10 blades (photos show +10), not 20. Shower copy makes no filtration claims.
- Free US shipping, because the margins already include shipping cost.
- A reviews app slot, product structured data, and a "Save %" badge were added to the page section.

## Tooling findings
- Shopify connector: can read and write products, collections, theme files in an unpublished theme, variants, media (via staged upload + curl), discounts, and run GraphQL. Cannot publish themes, change policies, payments test mode, or the storefront password.
- Image upload path that works: `stagedUploadsCreate`, curl POST to the returned URL with the returned parameters, then `productUpdate(media: ...)` with the `resourceUrl`. Images sent mid-turn in chat are not saved to disk; only images at the start of a user message are.
- Higgsfield connector: 8 unrelated videos exist, no product stills. Prompts for hero, flat-lay, lifestyle, detail, and refill/blade shots were written in chat for the user to run.
- Local scratch files (not in repo): policy drafts `lumova-policies.md`, a one-page summary `lumova-handoff.md`.

## Prompts already handed to the user's local browser session
CJ quality check (exact box contents and image URLs for Suit 12 and the razor variant); ZenDrop/CJ product hunt for complete kits under $10.50 landed with US warehouse priority. Results: nothing qualifying beyond the silk sleep set.

## Next actions for the next session
1. Get Suit 12 image URLs from the user's local session and attach them to the shower product (or use Higgsfield originals).
2. Set up `SHOPIFY_ADMIN_TOKEN` as an environment secret, then set policies, free shipping, navigation, and publish with the user's approval.
3. Run the launch gates: crawl, $0 test order with a 100%-off code, Lighthouse, independent reviewer agent, tracking.
4. Find 3 more products (AliExpress via a paid ZenDrop plan, or other CJ US-warehouse kits).
5. Build marketing angles from the Meta Ad Library, TikTok Creative Center, and Google Ads Transparency Center, using the user's logged-in browser.
