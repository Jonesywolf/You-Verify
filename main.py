from turtle import title
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from cred_utils import login
from form_filler import fill_form

if __name__ == "__main__":
    # TODO test headless mode, verify the form filler worked using the certificate, 
    # screenshot the certificate and send it via email, add exception handling
    opts = Options()
    # opts.set_headless()
    browser = Firefox(options=opts)
    browser.get("https://ucheck.utoronto.ca/")
    if browser.title == "My Thrive Health":
        fill_form(browser)
    # If we are prompted to sign in, we get redirected to: 
    # https://idpz.utorauth.utoronto.ca/idp/profile/SAML2/Redirect/SSO?execution=e1s1
    elif browser.title == "weblogin idpz | University of Toronto":
        login(browser)
        fill_form(browser)
    else:
        print("Unexpected page title, you might have been redirected somewhere unexpected.")
    quit()