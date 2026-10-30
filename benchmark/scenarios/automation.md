# Scenario: automation

## Opening message
automate my invoices somehow, i'm drowning in them

## Hidden intent card
- Freelance photographer; receives supplier invoices (incoming, not ones they send) as PDF attachments by email (Gmail) from about 5 regular suppliers.
- Wants each PDF saved to Google Drive in a folder per month.
- Wants amount, supplier, date, due date extracted into a Google Sheet.
- Invoices over 500 EUR must be flagged.
- Weekly summary every Monday to Telegram: what's due this week.
- Already runs n8n self-hosted on a small server and wants to use it.
- NEVER pay anything automatically.
- Suppliers sometimes send the same invoice twice; duplicates must not be added twice.
- Their tax advisor gets the Drive folder; filenames should be YYYY-MM-DD_supplier_amount.pdf.
## Things the user does NOT know or care about
- how PDF extraction works technically, n8n node names
