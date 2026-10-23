# Suppliers, listings, and margin math

## Margin rule
Net margin = (price - landed cost - (2.9% x price + $0.30)) / price. Landed cost = product + US shipping. Target 70%. Max landed cost for 70% = 0.271 x price - 0.30:
$29.99 -> $7.83 | $39.99 -> $10.54 | $44.99 -> $11.89 | $59.99 -> $15.96 | $69.99 -> $18.67.
Returns, refunds, chargebacks and sample costs are not included (plan 3-8%).

## Live products (checked in Shopify 2026-10-23)
| Product | Variant | Price | Landed | Net margin |
|---|---|---|---|---|
| Lumova Handheld Shower Set (id 15431900332280, renamed 2026-10-22) | Complete Set (showerhead + hose + arm adapter + 5 cartridges) | $59.99 | $15.12 | 71.4% |
| same | Showerhead + 5 cartridges (no hose) | $44.99 | $10.26 | 73.6% |
| same | Refill 3-Pack | $22.99 (was $19.99 when this session built it; the parallel session changed it) | $5.83 | about 70% |
| Lumova Single-Blade Safety Razor (id 15431900430584) | Rose Gold Set (razor + stand + 10 blades) | $44.99 | $10.89 | 72.2% |
Archived: patches (15431903838456), face/brow razors (15431903871224), eye patches (15431903936760), and "Lumova Shower + Razor Bundle" $99.99 (15436976750840, created by the parallel session, archived/cancelled).

## CJ Dropshipping
- Shower listing: https://www.cjdropshipping.com/product/replacement-shower-filter-for-held-showerhead---high-output-shower-water-filter-to-remove-chlorine-fluoride-and-hard-water-p-2604190751231614300.html (SKU CJYD2842575). Listing title claims chlorine, fluoride, hard water removal; the page shows no cartridge material or proof, so we make no filtration claims.
  - Suit 1 $1.73 + $8.53 ship ($10.26): complete handheld showerhead (gunmetal ABS, silicone massage nozzles, three settings, 25.5 cm, 210 g) + 5 cartridges + retail box. No hose, no bracket, no tape.
  - Suit 9/10/11 add a 1.5 m hose; Suit 11 also has a bracket and 5 filters ($2.90) but no adapter for the shower arm.
  - **Suit 12** $3.19 + $11.93 ship = $15.12: head + 1.5 m hose + chrome shower-arm adapter with built-in holder + thread tape + 5 cartridges (per the supplier kit photo). Suit 12 is what we sell as the Complete Set.
  - Cartridges alone: 3 for $0.56 + $5.27 ship ($5.83).
  - Unverified: adapter thread size, how the holder mounts, cartridge material, any manual. Image 2 of the listing says "Labeling" and "Drop Shipping Available" (supplier may offer custom labels).
  - Other CJ shower listings: Beauty Dechlorinating Dual Filter Shower Head ($8.79 + $10.11), Skin Care Shower Head w/ Replaceable Cartridge ($6.47 + $16.76, magnetic/oversize restriction).
- Razor listing: https://www.cjdropshipping.com/product/manual-vintage-razor-mens-razor-metal-gift-p-C6958D60-3561-4AA1-AC23-8D32F5B4313D.html (SKU CJBJPFTX00401). Rose Gold + 10 blades $5.80 + $6.35; Rose Gold + stand variant $3.97 + $6.92 ($10.89). Photos show the stand set as "+10 blades" in a kraft box (about 210 g total); the plain razor is about 56 g, 10.3 cm, carbon steel handle, alloy blades, single poly-bag packaging; standard 43 x 22 mm blades. Variants with 20 blades, 2 and 3 packs, chrome and gunmetal finishes, an exfoliating glove and a toiletry bag also appear in the photos. The rose gold head looks engraved with a supplier mark (confirm or ask for an unbranded head). The razor is not weighted.
- Things CJ did not have (searched many terms): star hydrocolloid pimple patches, manual brow/dermaplane razors, hydrogel eye patches in 60-120 count (only a branded ZOZU 60-piece jar, 0/5 supplier, $0.65 + $8.14), heatless curl sets, facial sculpting kits (gua sha + roller + headband), shower brush sets under 600 g, razor + mitt + bag bundles, satin bonnet bundles. Pet 2-in-1 bath glove: $9.18 + $3.00 = $12.18 (single tool, China only).
- Silk-style 4-piece sleep set (satin pillowcase, eye mask, hair ring, hair band): $5.81 + $6.07 (GOFO+, US warehouse, 98 units) = $11.88; 66% at $39.99, needs $44.99 for 70%. Rejected.
- CJ shows a "Human verification" page to scripted clients. Only requests spoofing Googlebot or Facebook's crawler got the real page; do not use that. Use the user's logged-in browser.

## AliExpress (search pages readable by plain fetch; item pages blocked)
- Shower cartridges 10-pack $6.03, 1,000+ sold: https://www.aliexpress.com/item/3256813019235590.html
- Safety razor with 5 blades $12.10, 4,000+ sold: https://www.aliexpress.com/item/3256808998701921.html
- Star pimple patches, 240 count $1.58, 10,000+ sold: https://www.aliexpress.com/item/3256810137297432.html
- Eyebrow razors 40 pcs $7.36, 10,000+ sold: https://www.aliexpress.com/item/3256810033150120.html
- Eye masks 60 pcs $8.48, 10,000+ sold: https://www.aliexpress.com/item/3256807619235142.html
- Heatless curl rod $5.12-5.84, 5,000-10,000+ sold; hair towel wrap $6.87, 50,000+ sold; pet glove $2-4, 10,000+ sold.
- Estimated margins for the cheap items were 58-65% after shipping and fees. Patches/brow razors/eye patches were dropped for that reason (and pages archived).

## ZenDrop
- Installed on the store (a "Zendrop" shipping profile with free worldwide shipping exists). The account has no active plan, so the catalog redirects to a paywall. User's stated sourcing plan: find on AliExpress/Alibaba, fulfill via ZenDrop; ZenDrop was said to be best for manufacturer quality.

## Master product list from the earlier session
Artifact "Master Product List" (https://claude.ai/artifact/N5HMPysMFo6Eh8tvUEXiAR): refill products scored by demand and ad run time (sink filter 83, premium shower filter 79, private-label cartridges 70, spin scrubber 66, pet bath filter 66, others lower). Selection criteria used: recurring refill, ad longevity (30+ days), no battery, not regulated, low returns, easy 5-second video, private label possible, 70%+ margin.

## Higgsfield
Connector sees 8 unrelated cinematic videos from 2026-10-19, no product stills. Image prompts are in org/prompts/higgsfield-prompts.md.
