from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from cred_utils import login
import env_utils
from form_utils import fill_form, verify_form_completion
from screenshot_utils import save_screenshots
from email_utils import send_email

if __name__ == "__main__":
    env_contents = env_utils.load_dotenv()
    gmail_addr = env_utils.load_gmail_addr(env_contents)
        
    opts = Options()
    if env_utils.use_headless_mode(env_contents):
        # No UI by default:
        opts.headless = True
    browser = Firefox(options=opts)
    
    browser.get("https://ucheck.utoronto.ca/")
    if browser.title == "My Thrive Health":
        fill_form(browser)
        if verify_form_completion(browser):
           print("Form completion successful")
           save_screenshots(browser, "badgeImage", "pageImage")
        else:
            print("Form completion failed")
        send_email(gmail_addr, "badgeImage")
    # If we are prompted to sign in, we get redirected to: 
    # https://idpz.utorauth.utoronto.ca/idp/profile/SAML2/Redirect/SSO?execution=e1s1
    elif browser.title == "weblogin idpz | University of Toronto":
        user_creds = env_utils.get_creds(env_contents)
        print("Redirected to sign in page")
        login(browser, user_creds)
        fill_form(browser)
        if verify_form_completion(browser):
           print("Form completion successful")
           save_screenshots(browser, "badgeImage", "pageImage")
        else:
            print("Form completion failed")
        send_email(gmail_addr, "badgeImage")
    else:
        print("Unexpected page title, you might have been redirected somewhere unexpected.")
    
    print("Quitting browser session...")
    quit()