# D2D Self-Publishing Pipeline for Hermes Agent

## Overview
Complete workflow from manuscript to published book on Draft2Digital.

## Prerequisites
1. D2D account (create at draft2digital.com)
2. Browser automation via Hermes browser tools
3. Manuscript files (Markdown or DOCX)
4. Cover image (JPEG/PNG, D2D specs: 1600x2400 min for ebook)
5. Book metadata (title, author, description, ISBN, categories, keywords)

## Pipeline Steps

### Phase 1: Manuscript Preparation
1. **Validate manuscript** — check formatting, chapter breaks, front/back matter
2. **Convert to EPUB** — D2D accepts EPUB, DOCX, or PDF
3. **Add ISBN** — D2D provides free ISBN or use your own
4. **Generate cover** — create cover image meeting D2D specs

### Phase 2: D2D Upload (Browser Automation)
1. **Login to D2D** — navigate to draft2digital.com, enter credentials
2. **Create new book** — click "Add New Book"
3. **Fill metadata** — title, author, description, categories, keywords
4. **Upload manuscript** — upload EPUB/DOCX file
5. **Upload cover** — upload cover image
6. **Set pricing** — configure price per marketplace
7. **Select distribution** — choose storefronts (Amazon, Apple, B&N, etc.)
8. **Review & publish** — final review and submit

### Phase 3: Post-Publication
1. **Verify publication** — check that book appears on storefronts
2. **Update backmatter** — add D2D ISBN to backmatter of all books
3. **Update website** — add purchase links to danielryan-author.com
4. **Announce** — post on Twitter/Instagram

## D2D Account Setup (One-Time)
1. Go to draft2digital.com/register
2. Create account with email/password
3. Set pen name: "Daniel Ryan"
4. Complete tax information (W-9 for US authors)
5. Set up payment method (PayPal or direct deposit)

## File Requirements
- **Manuscript**: EPUB preferred, DOCX accepted
- **Cover**: JPEG or PNG, minimum 1600x2400 pixels, 300 DPI
- **ISBN**: D2D provides free ISBN, or use your own
- **Description**: Plain text or basic HTML, 100-4000 characters

## Categories (BISAC)
Middle-Grade Mystery & Detective Stories: JUV000000
Middle-Grade Humor: JUV028000
Middle-Grade Science Fiction: JUV036000

## Keywords (per book)
- Series name
- Character names
- Genre terms
- Age range (middle grade, ages 8-12)
- Comparable titles

## Pricing Strategy
- Ebook: $2.99-$4.99 (sweet spot for middle grade)
- Paperback: $7.99-$12.99 (D2D Print on Demand)
- Free ISBN from D2D (or purchase your own)

## Automation Notes
- D2D has NO public API — must use browser automation
- Browser tools available: browser_navigate, browser_click, browser_type, browser_snapshot
- Login credentials needed (store securely)
- Each book takes ~15-20 minutes to upload via browser
- Can batch upload multiple books in one session

## Integration with Hermes
- Store D2D credentials in memory (encrypted)
- Create cron job to check publication status
- Auto-generate backmatter with purchase links
- Track sales via D2D reports (browser scrape)
