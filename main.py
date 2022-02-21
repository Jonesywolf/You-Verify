from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from cred_utils import login
from form_filler import fill_form, verify_form_completion

if __name__ == "__main__":
    opts = Options()
    # No UI by default:
    opts.headless = True
    browser = Firefox(options=opts)
    
    browser.get("https://ucheck.utoronto.ca/")
    if browser.title == "My Thrive Health":
        fill_form(browser)
        if verify_form_completion(browser):
           print("Form completion successful")
        else:
            print("Form completion failed") 
    # If we are prompted to sign in, we get redirected to: 
    # https://idpz.utorauth.utoronto.ca/idp/profile/SAML2/Redirect/SSO?execution=e1s1
    elif browser.title == "weblogin idpz | University of Toronto":
        print("Redirected to sign in page")
        login(browser)
        fill_form(browser)
        if verify_form_completion(browser):
           print("Form completion successful")
        else:
            print("Form completion failed") 
    else:
        print("Unexpected page title, you might have been redirected somewhere unexpected.")
    
    print("Quitting browser session...")
    quit()