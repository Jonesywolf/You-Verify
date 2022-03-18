from smtplib import SMTPAuthenticationError
import yagmail

def send_email(badge_img_path, gmail_addr, gmail_app_pass=None):
    badge_img_path = badge_img_path if badge_img_path.endswith(".png") else badge_img_path + ".png"
    badge_img_path = badge_img_path if badge_img_path.startswith("screenshots/") else "screenshots/" + badge_img_path

    if gmail_app_pass:
        yag = yagmail.SMTP(gmail_addr, gmail_app_pass)
    else:
        yag = yagmail.SMTP(gmail_addr)
    try:
        yag.send(
            to=gmail_addr,
            subject="YouVerify - Your UCheck Badge",
            contents="See attached.", 
            attachments=badge_img_path,
        )
    except ValueError:
        print("""Invalid gmail username or password, or you might not have set up an application specific password yet.\nTo set one up, see: https://support.google.com/accounts/answer/185833""")
