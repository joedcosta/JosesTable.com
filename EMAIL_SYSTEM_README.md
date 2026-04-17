# JoEs TaBLe — Email System

Branded HTML email templates for all guest communications.

## Setup

No dependencies. Pure Python 3.

```bash
python email_builder.py
```

Generates `/emails/` folder with 10 ready-to-send HTML files.

## Templates

| File | Template | When to use |
|---|---|---|
| `T1_missing_info.html` | T-1 | Form incomplete — request missing details |
| `T2_please_confirm.html` | T-2 | Date available — send Stripe confirmation link |
| `T4_confirmed.html` | T-4 | Booking confirmed after deposit |
| `T5_unavailable.html` | T-5 | Requested date unavailable — offer alternatives |
| `T7_cancellation.html` | T-7 | Guest cancels — acknowledge per policy |
| `T8_venue_reveal.html` | T-8 | Day-of — send before noon with venue address |
| `T9_receipt.html` | T-9 | Post-event receipt (24h after) |
| `T10_review.html` | T-10 | Post-event review request (48–72h after) |
| `TC1_corporate.html` | T-C1 | Corporate first response with pricing |
| `TC2_invoice.html` | T-C2 | Corporate deposit invoice with Stripe link |

## Image Assets (Cloudinary — auto WebP via f_auto,q_auto)

| Asset | Cloudinary path |
|---|---|
| Banner | `f_auto,q_auto/v1749463257/Email_Banner_2025_jzslzd.jpg` |
| Mid image | `f_auto,q_auto/v1749621762/email_footer_01_xcvupq.png` |
| Footer strip | `f_auto,q_auto/v1776457850/email_footer_insta_r9jr11.jpg` |
| Logo circle | `f_auto,q_auto/v1749542864/LOGO_JT_512_lyqyl6.png` |

## Usage

Claude drafts every email by calling the relevant function with real guest data, then saves as a Gmail draft. Joe reviews and sends.

Example — confirmed booking:
```python
html = T4(
    name="Mohit",
    day="Sunday",
    date_str="17 May 2026",
    pax="Group of 2",
    dietary="none",
    wine="none",
)
```
