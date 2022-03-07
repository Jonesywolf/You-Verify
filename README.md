# You Verify

Fills out a form automatically, **USE AT YOUR OWN RISK**.

## How To Use

First, make sure you have the Firefox browser and python 3 installed. Then, install all the required python dependencies with pip using:

```pip install -r requirements.txt```

Then run `main.py` like any other python file.

In this project's folder, you need to add a `.env` file with the following text in it (updated with your credentials):
```
# UTORID credentials
USERNAME=your_username
PASSWORD=your_password

# Email
GMAIL=your_email_address

# Other settings
HEADLESS_MODE = True
```
You can either copy the template above or use and rename the `template.env` file included in the repository.

## How it works:

* Use python dot env to parse the user's credentials
* Use selenium and a headless Firefox Driver to crawl the webpage and fill out the form
* Use a service like crontab or windows task scheduler to run the code every day

## Learning Goals

* Learn how to test web crawlers
* Get better with selenium
* Deploy on Raspberry Pi, automate with crontab to run daily

## Code Division

### Cred Utils

Handles credentials, log in, etc. Called if redirected to sign in page https://idpz.utorauth.utoronto.ca/idp/profile/SAML2/Redirect/SSO?execution=e1s1

### Form filler

Handles filling out the form automatically and submitting it.

## To Do:
* add more exception handling
* make printouts optional
* make printouts prettier
* add more options in .env:
* for longer waits for elements to appear
* for debug mode
* headless mode
* choice of browser
* path to browser, if necessary
* fix email sending using OAuth2
* enable email sending in .env file
* handle env file better, it's kinda janky passing env_contents around
* optionally use keyring instead of .env to store credentials
