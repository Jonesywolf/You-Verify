from selenium.webdriver import Firefox, Chrome, FirefoxOptions, ChromeOptions
from cred_utils import login
import env_utils
from form_utils import fill_form, verify_form_completion
from screenshot_utils import save_screenshots
from email_utils import send_email

def complete_survey(env_contents):
    fill_form(browser)
    if verify_form_completion(browser):
        print("Form completion successful")
        save_screenshots(browser, "badgeImage", "pageImage")
    else:
        print("Form completion failed")
    gmail_addr = env_utils.load_gmail_addr(env_contents)
    gmail_app_pass = env_utils.load_gmail_app_pass(env_contents)
    send_email("badgeImage", gmail_addr, gmail_app_pass=gmail_app_pass)

if __name__ == "__main__":
    env_contents = env_utils.load_dotenv()
    
    if env_utils.get_browser(env_contents) == "FIREFOX":
        print("Using Firefox driver")
        opts = FirefoxOptions()
        #TODO: refactor
        if env_utils.is_headless_mode(env_contents):
            # No UI by default:
            opts.add_argument("--headless")
        browser = Firefox(options=opts)
    elif env_utils.get_browser(env_contents) == "CHROME":
        print("Using Chrome driver, make sure you have the right file for your operating system and browser version.")
        opts = ChromeOptions()
        #TODO: refactor
        opts.add_argument("--no-sandbox")
        if env_utils.is_headless_mode(env_contents):
            # No UI by default:
            opts.add_argument("--headless")
        browser = Chrome(options=opts)
    else:
        print("Unrecognized BROWSER setting in .env, defaulting to Firefox...")
        opts = FirefoxOptions()
        #TODO: refactor
        if env_utils.is_headless_mode(env_contents):
            # No UI by default:
            opts.add_argument("--headless")
        browser = Firefox(options=opts)
    
    browser.get("https://ucheck.utoronto.ca/")
    if browser.title == "My Thrive Health":
        complete_survey(env_contents)
    # If we are prompted to sign in, we get redirected to: 
    # https://idpz.utorauth.utoronto.ca/idp/profile/SAML2/Redirect/SSO?execution=e1s1
    elif browser.title == "weblogin idpz | University of Toronto":
        user_creds = env_utils.get_creds(env_contents)
        print("Redirected to sign in page")
        login(browser, user_creds)
        complete_survey(env_contents)
    else:
        print("Unexpected page title, you might have been redirected somewhere unexpected.")
    
    print("Quitting browser session...")
    quit()