from smtplib import SMTPAuthenticationError
import yagmail

# def store_email_creds(gmail_addr):
#     # Stores credentials in keyring, prompts user for their password
#     yagmail.register(gmail_addr)

def send_email(gmail_addr, badge_img_path):
    badge_img_path = badge_img_path if badge_img_path.endswith(".png") else badge_img_path + ".png"
    badge_img_path = badge_img_path if badge_img_path.startswith("screenshots/") else "screenshots/" + badge_img_path

    yag = yagmail.SMTP(gmail_addr)
    try:
        yag.send(
            to=gmail_addr,
            subject="YouVerify - Your UCheck Badge",
            contents="See attached.", 
            attachments=badge_img_path,
        )
    except ValueError:
        print("Invalid gmail username or password")
