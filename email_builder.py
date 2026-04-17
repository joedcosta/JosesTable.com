"""
JoEs TaBLe Barcelona — Email Template Builder
==============================================
Generates all 10 branded HTML email templates.
Run: python email_builder.py
Output: /emails/ folder with one .html file per template.

Cloudinary base: https://res.cloudinary.com/djzg1ulup/image/upload/
All images served via f_auto,q_auto (auto WebP + compression).
"""

import os

# ── Asset URLs ─────────────────────────────────────────────────────────────
CDN = "https://res.cloudinary.com/djzg1ulup/image/upload/f_auto,q_auto"
BANNER  = f"{CDN}/v1749463257/Email_Banner_2025_jzslzd.jpg"
MID_IMG = f"{CDN}/v1749621762/email_footer_01_xcvupq.png"
FOOTER  = f"{CDN}/v1776457850/email_footer_insta_r9jr11.jpg"
LOGO    = f"{CDN}/v1749542864/LOGO_JT_512_lyqyl6.png"
WA      = "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"

TERMS   = "https://joestable.clandestino.kitchen/terms"
WA_LINK = "https://wa.me/+447818727657"
MAPS    = "https://maps.app.goo.gl/xnAjfafJDvbwBBbG9"

# ── CSS ────────────────────────────────────────────────────────────────────
CSS = """body{margin:0;padding:0;background:#f4f4f0;font-family:Georgia,'Times New Roman',serif}
.wrap{max-width:520px;margin:0 auto;background:#fff}
img{display:block;border:0}a{color:#1a1a1a}
.logo-block{text-align:center;padding:20px 30px 14px}
.logo-tag{font-family:Arial,sans-serif;font-size:9px;letter-spacing:4px;color:#888;text-transform:uppercase;display:block}
.logo-main{font-size:42px;font-weight:900;color:#1a1a1a;letter-spacing:2px;line-height:1;font-family:Georgia,serif;display:block}
.logo-url{font-family:Arial,sans-serif;font-size:9px;letter-spacing:3px;color:#888;text-transform:uppercase;display:block;margin-top:4px}
.sal{text-align:center;padding:18px 40px 6px;font-size:22px;color:#1a1a1a}
.intro{text-align:center;padding:0 40px 16px;font-size:14px;color:#555;line-height:1.7}
.det{margin:0 36px;border-top:1px solid #ddd;border-bottom:1px solid #ddd;padding:16px 0}
.det-h{font-family:Arial,sans-serif;font-size:10px;font-weight:bold;color:#1a1a1a;letter-spacing:1px;text-transform:uppercase;margin-bottom:12px}
.det-r{font-size:13px;color:#333;margin-bottom:6px;line-height:1.5}
.body{padding:16px 36px;font-size:13px;color:#444;line-height:1.8}
.cta{text-align:center;padding:8px 36px 20px}
.cta-l{font-family:Arial,sans-serif;font-size:10px;letter-spacing:2px;color:#1a1a1a;text-decoration:underline}
.cta-b{font-family:Arial,sans-serif;font-size:11px;font-weight:bold;letter-spacing:2px;color:#1a1a1a;display:block;margin-top:5px}
.sp{padding:14px 36px;font-size:9px;color:#aaa;text-align:center;font-family:Arial,sans-serif;line-height:1.7;border-top:1px solid #eee}
.ft{padding:14px 20px;border-top:1px solid #eee;display:flex;align-items:center;gap:12px}
.ft-r{font-family:Arial,sans-serif;font-size:10px;color:#888;line-height:1.9}
.ft-r a{color:#888;text-decoration:none}
.tag{text-align:center;font-family:Arial,sans-serif;font-size:7px;letter-spacing:2px;color:#bbb;text-transform:uppercase;padding:6px 0 12px}
.btn{display:inline-block;background:#1a1a1a;color:#fff !important;font-family:Arial,sans-serif;font-size:11px;letter-spacing:2px;padding:13px 30px;text-decoration:none;text-transform:uppercase}"""


# ── Shell ──────────────────────────────────────────────────────────────────
def shell(content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>JoEs TaBLe Barcelona</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">

<img src="{BANNER}" width="520" alt="JoEs TaBLe Barcelona" style="width:100%">

<div class="logo-block">
  <span class="logo-tag">Conceptional Fine Dining</span>
  <span class="logo-main">JoEs TaBLe</span>
  <span class="logo-url">WWW.JOSESTABLE.COM</span>
</div>

{content}

<div class="sp">
  We request a valid payment method on file to confirm your request and help prevent no-shows.
  After successfully completing your request you'll receive a confirmation and your reservation is secured.<br>
  By acknowledging this you automatically accept our<br>
  <a href="{TERMS}" style="color:#555;font-weight:bold">Terms of use and Privacy Policy</a><br>
  Joe &amp; Team
</div>

<div class="ft">
  <img src="{LOGO}" width="52" height="52" alt="JoEs TaBLe" style="border-radius:50%;width:52px;height:52px">
  <div class="ft-r">
    <a href="mailto:booking@josestable.com">&#9993;&nbsp; booking@josestable.com</a><br>
    <a href="tel:+447818727657">&#9742;&nbsp; +44 7818 727 657</a><br>
    <a href="{MAPS}">&#9679;&nbsp; 08001 Barcelona</a><br>
    <a href="https://www.josestable.com">&#9675;&nbsp; josestable.com</a>
  </div>
</div>

<img src="{FOOTER}" width="520" alt="" style="width:100%">
<div class="tag">Conceptual Fine Dining &nbsp;·&nbsp; One Table &nbsp;·&nbsp; Emblematic Location &nbsp;·&nbsp; Vanguard Cuisine</div>

</div>
</body>
</html>"""


def wa_block():
    return f"""<div class="cta">
  <a href="{WA_LINK}" class="cta-l">Contact us anytime</a>
  <span class="cta-b">JoEs TaBLe Barcelona</span>
  <a href="{WA_LINK}" style="display:block;width:36px;margin:8px auto 0">
    <img src="{WA}" width="36" height="36" alt="WhatsApp">
  </a>
</div>"""


# ── Templates ──────────────────────────────────────────────────────────────

def T1(name="Guest"):
    """Missing information — sent when form is incomplete."""
    return shell(f"""
<div class="sal">Dear {name},</div>
<div class="intro">Thank you for your reservation request.</div>
<div class="body">We noticed your request was either incomplete or interrupted. To finalise your booking, please confirm:</div>
<div class="det">
  <div class="det-h">Details needed:</div>
  <div class="det-r">&#9679; Date of Reservation:</div>
  <div class="det-r">&#9679; Number of Guests:</div>
  <div class="det-r">&#9679; Food allergies / Dietary requirements:</div>
  <div class="det-r">&#9679; Wine Pairing: (Standard / Iberico / Seleccion / None)</div>
  <div class="det-r">&#9679; WhatsApp number (for day-of coordination):</div>
</div>
<div class="body">Thank you,<br>Joe &amp; Team</div>
{wa_block()}""")


def T2(name, day, date_str, pax, dietary, wine, stripe_link):
    """Date available — please confirm and pay €20 retention."""
    return shell(f"""
<div class="sal">Dear {name},</div>
<div class="intro">Welcome to Joe's Table Barcelona.<br><em>A gastronomic vanguard, offering private dining experiences in exclusive pop-up locations throughout the city center.</em></div>
<div class="det">
  <div class="det-h">Please confirm your reservation:</div>
  <div class="det-r"><strong>Date:</strong> {day}, {date_str}</div>
  <div class="det-r"><strong>Time:</strong> 7.30pm – 10.30pm (19:30 – 22:30 CET)</div>
  <div class="det-r"><strong>Guests:</strong> {pax}</div>
  <div class="det-r"><strong>Tasting menu:</strong> a Culinary Journey</div>
  <div class="det-r"><strong>Food allergies:</strong> {dietary}</div>
  <div class="det-r"><strong>Wine Pairings:</strong> {wine}</div>
</div>
<div class="body">To secure your spot, please confirm and register a valid payment method. This helps us protect against no-shows and guarantees your place at the table.</div>
<div class="cta" style="padding:16px 36px">
  <a href="{stripe_link}" class="btn">CONFIRM RESERVATION</a>
</div>
<div class="body"><strong>Booking terms and Cancellation policy:</strong><br>Our TC's are visible on our website under <a href="{TERMS}">Terms &amp; Conditions</a> for your perusal.</div>
{wa_block()}""")


def T4(name, day, date_str, pax, dietary, wine):
    """Confirmed reservation."""
    return shell(f"""
<div class="sal">Dear {name},</div>
<div class="intro">Thank you very much,<br><strong>your reservation is now confirmed.</strong></div>
<div class="det">
  <div class="det-h">Your reservation details:</div>
  <div class="det-r"><strong>Date:</strong> {day}, {date_str}</div>
  <div class="det-r"><strong>Time:</strong> 7.30pm – 10.30pm (19:30 – 22:30 CET)</div>
  <div class="det-r"><strong>Guests:</strong> {pax}</div>
  <div class="det-r"><strong>Tasting menu:</strong> a Culinary Journey</div>
  <div class="det-r"><strong>Food allergies:</strong> {dietary}</div>
  <div class="det-r"><strong>Wine Pairings:</strong> {wine}</div>
</div>
<div class="body"><strong>Booking terms and Cancellation policy:</strong><br>Our TC's are visible on our website under <a href="{TERMS}">Terms &amp; Conditions</a> for your perusal.</div>
<img src="{MID_IMG}" width="520" alt="" style="width:100%">
<div class="body">Welcome to Joe's Table Barcelona.<br><br>A gastronomic vanguard, offering private dining experiences hosted in exclusive pop-up locations throughout the city center. Please note that the exact location of the pop-up venue will be sent to all guests at noon on the day of the event. Please ensure your contact details are up to date.</div>
<div class="body" style="padding-top:0">Thank you,<br>Joe &amp; Team</div>
{wa_block()}""")


def T5(name, requested_date, alternatives):
    """Date unavailable — offer alternatives."""
    alt_lines = "\n".join(
        f'  <div class="det-r">&#9679; {a}</div>' for a in alternatives
    )
    return shell(f"""
<div class="sal">Dear {name},</div>
<div class="intro">Thank you for your reservation request.</div>
<div class="body">Unfortunately, <strong>{requested_date}</strong> is not currently available. We would be happy to welcome you on one of the following alternative dates:</div>
<div class="det">
  <div class="det-h">Alternative dates:</div>
{alt_lines}
</div>
<div class="body">Please let us know if any of these work for you and we will send everything needed to complete your reservation immediately.<br><br>Joe &amp; Team</div>
{wa_block()}""")


def T7(name, within_window=True):
    """Cancellation confirmed."""
    msg = (
        "Your reservation has been cancelled at no charge. We hope to welcome you again on a future visit to Barcelona."
        if within_window else
        "As your cancellation falls outside our 7-day free cancellation window, the retention fee is non-refundable per our Terms &amp; Conditions. We hope to have the opportunity to welcome you in the future."
    )
    return shell(f"""
<div class="sal">Dear {name},</div>
<div class="intro">Thank you for letting us know.<br>We are sorry to hear that your plans have changed.</div>
<div class="body">{msg}</div>
<div class="body">We hope to welcome you again soon.<br><br>Joe &amp; Team</div>
{wa_block()}""")


def T8(name, address, postcode, maps_link, meeting_note=""):
    """Day-of venue reveal — send before noon."""
    note = f'<div class="det-r" style="margin-top:8px"><em>{meeting_note}</em></div>' if meeting_note else ""
    return shell(f"""
<div class="sal">Dear {name},</div>
<div class="intro"><strong>We are excited to have you with us tonight.</strong><br>Please take note of tonight's pop-up address.</div>
<div class="det">
  <div class="det-h">Meeting Point / Pop-Up</div>
  <div class="det-r"><strong>{address}</strong><br>{postcode} Barcelona</div>
  {note}
  <div class="det-r" style="margin-top:10px"><strong>Please be on time: 7:30pm (19:30 CET)</strong></div>
  <div class="det-r"><a href="{maps_link}">Open in Google Maps →</a></div>
</div>
<div class="det" style="margin-top:16px">
  <div class="det-h">Notes</div>
  <div class="det-r"><strong>Dress code:</strong> Casual smart</div>
  <div class="det-r"><strong>Payment:</strong> Cash preferred. Card payments carry a 5% supplement.</div>
</div>
<div class="body"><strong>Booking terms and Cancellation policy:</strong><br>Our TC's are visible on our website under <a href="{TERMS}">Terms &amp; Conditions</a> for your perusal.</div>
{wa_block()}""")


def T9(name, date_str, line_items, total, payment_note="Payment settled at the venue / via Stripe."):
    """Post-event receipt."""
    rows = "\n".join(
        f'  <div class="det-r">{desc} &nbsp;&nbsp;&nbsp; &euro;{amt:.2f}</div>'
        for desc, amt in line_items
    )
    return shell(f"""
<div class="sal">Dear {name},</div>
<div class="intro">Thank you for joining us —<br>it was a genuine pleasure hosting you.</div>
<div class="det">
  <div class="det-h">JoEs TaBLe Barcelona — Receipt</div>
  <div class="det-r"><strong>Date:</strong> {date_str}</div>
  <div style="height:8px"></div>
{rows}
  <div style="border-top:1px solid #ddd;margin:12px 0 8px"></div>
  <div class="det-r"><strong>Total &nbsp;&nbsp;&nbsp; &euro;{total:.2f}</strong></div>
  <div class="det-r" style="font-size:11px;color:#999;margin-top:6px">{payment_note}<br>This receipt is for your reference. JoEs TaBLe operates as a private pop-up dining concept.</div>
</div>
<div class="body">We hope to welcome you again next time you are in Barcelona.</div>
{wa_block()}""")


def T10(name, review_link):
    """Post-event review / testimonial request."""
    return shell(f"""
<div class="sal">Dear {name},</div>
<div class="intro">I hope you arrived home well after your evening with us.</div>
<div class="body" style="text-align:center">It would mean a great deal if you could take a moment to share your experience. Your words help others discover Joe's Table and support what we are building here.</div>
<div class="cta" style="padding:16px 36px">
  <a href="{review_link}" class="btn">LEAVE A REVIEW</a>
</div>
<div class="body" style="text-align:center;font-size:12px;color:#666">And if there is anything we can do even better next time, I would love to hear it personally.</div>
<div class="body" style="padding-top:0">Thank you again. It was a privilege to have you at our table.<br><br>Joe</div>
{wa_block()}""")


def TC1(name, date_str, pax, menu_sub, surcharge, total, deposit):
    """Corporate — first response with pricing."""
    return shell(f"""
<div class="sal">Dear {name},</div>
<div class="intro">Welcome to Joe's Table Barcelona.<br><em>A gastronomic vanguard offering private dining experiences at exclusive locations throughout the city center.</em></div>
<div class="det">
  <div class="det-h">Booking Summary — {date_str}</div>
  <div class="det-r"><strong>Private Venue Rental:</strong> &nbsp;&nbsp;&nbsp; &euro;400.00</div>
  <div class="det-r"><strong>Tasting Menu ({pax} guests &times; &euro;120 pp):</strong> &nbsp;&nbsp;&nbsp; &euro;{menu_sub:.2f}</div>
  <div class="det-r"><strong>Service &amp; Payment Surcharge (5%):</strong> &nbsp;&nbsp;&nbsp; &euro;{surcharge:.2f}</div>
  <div style="border-top:1px solid #ddd;margin:12px 0 8px"></div>
  <div class="det-r"><strong>Subtotal &nbsp;&nbsp;&nbsp; &euro;{total:.2f}</strong></div>
  <div class="det-r" style="font-size:11px;color:#999">VAT 21% invoiced separately by the venue host</div>
</div>
<div class="body">
  <strong>Payment terms:</strong> To secure your reservation, a 30% deposit of <strong>&euro;{deposit:.2f}</strong> is required within 3 business days. The remaining balance — plus wine pairings and VAT — is due on or before the event.<br><br>
  <strong>Wine pairings:</strong> from &euro;48 per person, ordered in advance.<br><br>
  <strong>Cancellation:</strong> Free up to 7 days before the event. The 5% surcharge is non-refundable.<br><br>
  For full details: <a href="{TERMS}">Terms &amp; Conditions</a>
</div>
<div class="body" style="padding-top:0">We look forward to the possibility of hosting your team.<br><br>Joe &amp; Team</div>
{wa_block()}""")


def TC2(name, company, date_str, pax, dietary_note, menu_sub, surcharge, total, deposit, balance, stripe_link, free_cancel_date):
    """Corporate — formal deposit invoice with payment link."""
    note = f" ({dietary_note})" if dietary_note else ""
    return shell(f"""
<div class="sal">Dear {name},</div>
<div class="intro">Thank you for confirming — we very much look forward to hosting you and your team.</div>
<div class="det">
  <div class="det-h">Proforma Invoice — {date_str}</div>
  <div class="det-r"><strong>Client:</strong> {company}</div>
  <div class="det-r"><strong>Guests:</strong> {pax}{note}</div>
  <div style="height:8px"></div>
  <div class="det-r">Private Venue Rental &nbsp;&nbsp;&nbsp; &euro;400.00</div>
  <div class="det-r">Tasting Menu ({pax} &times; &euro;120 pp) &nbsp;&nbsp;&nbsp; &euro;{menu_sub:.2f}</div>
  <div class="det-r">Service &amp; Payment Surcharge (5%) &nbsp;&nbsp;&nbsp; &euro;{surcharge:.2f}</div>
  <div style="border-top:1px solid #ddd;margin:12px 0 8px"></div>
  <div class="det-r"><strong>Subtotal &nbsp;&nbsp;&nbsp; &euro;{total:.2f}</strong></div>
  <div class="det-r" style="font-size:11px;color:#999">VAT 21% invoiced by venue host &nbsp;|&nbsp; Wine pairings added to final invoice</div>
</div>
<div class="body"><strong>30% Deposit to confirm: &euro;{deposit:.2f}</strong><br>Balance due on or before event: &euro;{balance:.2f} + wine + VAT</div>
<div class="cta" style="padding:12px 36px 20px">
  <a href="{stripe_link}" class="btn">PAY DEPOSIT — &euro;{deposit:.2f}</a>
</div>
<div class="body">
  Free cancellation until: <strong>{free_cancel_date}</strong><br>
  The 5% surcharge is non-refundable.<br><br>
  Once the deposit is received we will confirm all details and communicate the venue address promptly.
</div>
<div class="body" style="padding-top:0">Joe &amp; Team</div>
{wa_block()}""")


# ── Build all template stubs ───────────────────────────────────────────────
if __name__ == "__main__":
    os.makedirs("emails", exist_ok=True)

    templates = {
        "T1_missing_info":   T1(),
        "T2_please_confirm": T2("[Name]", "[Day]", "[DD Month YYYY]", "Group of [X]", "[dietary]", "[wine]", "[STRIPE_LINK]"),
        "T4_confirmed":      T4("[Name]", "[Day]", "[DD Month YYYY]", "Group of [X]", "[dietary]", "[wine]"),
        "T5_unavailable":    T5("[Name]", "[requested date]", ["[Alternative 1]", "[Alternative 2]", "[Alternative 3]"]),
        "T7_cancellation":   T7("[Name]", within_window=True),
        "T8_venue_reveal":   T8("[Name]", "[Street Address]", "08001", "[MAPS_LINK]", "[Staff name] will meet you there."),
        "T9_receipt":        T9("[Name]", "[DD Month YYYY]", [("8-Course Tasting Menu ([X] guests)", 0.00)], 0.00),
        "T10_review":        T10("[Name]", "[REVIEW_LINK]"),
        "TC1_corporate":     TC1("[Name]", "[DD Month YYYY]", 8, 960.00, 68.00, 1428.00, 428.40),
        "TC2_invoice":       TC2("[Name]", "[Company]", "[DD Month YYYY]", 8, "1 vegetarian", 960.00, 68.00, 1428.00, 428.40, 999.60, "[STRIPE_LINK]", "[DD Month YYYY]"),
    }

    for name, html in templates.items():
        path = f"emails/{name}.html"
        with open(path, "w") as f:
            f.write(html)
        print(f"✓ {path}")

    print(f"\nAll {len(templates)} templates built in /emails/")
