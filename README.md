# You Verify

Fills out a form automatically, **USE AT YOUR OWN RISK**.

## How To Use

### General Setup

First, make sure you have the Firefox or Chrome web browser and python 3 installed. Then, install all the required python dependencies with pip using:

```pip install -r requirements.txt```

Then run `main.py` like any other python file.

In this project's folder, you need to add a `.env` file with the following text in it (updated with your credentials):
```
# UTORID credentials
USERNAME=your_username
PASSWORD=your_password

# Email
GMAIL=your_email_address
# Optionally, uncomment the app password field below or store it in a keyring (default)
# GMAIL_APP_PASS=your_app_password

# Browser settings
HEADLESS_MODE=True
# Supports CHROME or FIREFOX
BROWSER=CHROME
```
This project sends you an email (from yourself) with a screenshot of the survey completion, to access your
gmail account it requires that you set up an **application specific password**. For more details including
how to set one up, see: https://support.google.com/accounts/answer/185833

### Raspberry Pi Instructions

Follow the above instructions under [General Setup]. 

#### Chromedriver & Chromium

Now, Chromium and Chromedriver need to have matching versions for the web scraping portion to work.
Next, run the following commands to remove Chromium then reinstall matching Chromium and Chromedriver versions compiled on ARM [Source](https://stackoverflow.com/questions/65617246/issues-running-selenium-with-chromedriver-on-raspberry-pi-4):
```console
sudo apt purge --remove chromium-browser -y
sudo apt autoremove && sudo apt autoclean -y
sudo apt install chromium-chromedriver
```

#### Update .env Since Keyring Doesn't Work in Cron

Unfortunately, I couldn't get KDE Wallet Manager to work with crontab, so you'll need to uncomment this line (and add your gmail app password) to the `.env` file (or figure out how to do it yourself, and if you do, please let me know):
```
GMAIL_APP_PASS=your_app_password
```

#### Add a .bat File for Running Your Python File

I used a virtual environment for running my script which is optional (you can learn more about setting one up yourself [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/))
TODO

#### Edit your Crontab

TODO

## How it works:

* Use python dot env to parse the user's credentials
* Use selenium and a headless Firefox or Chrome Driver to crawl the webpage and fill out the form
* Screenshot the completion badge and email it to the user using yagmail
* Use a service like crontab or windows task scheduler to run the code every day

## Learning Goals

* Learn how to test web crawlers
* Get better with selenium
* Deploy on Raspberry Pi, automate with crontab to run daily

## Code Division

### Env utils

Handles user credentials from `.env` file.

### Cred Utils

Handles credentials, log in, etc. Called if redirected to sign in page https://idpz.utorauth.utoronto.ca/idp/profile/SAML2/Redirect/SSO?execution=e1s1

### Form utils

Handles filling out the form automatically and submitting it.

### Screenshot utils
Takes screenshots of the page and the survey completion badge.

### Email utils
Handles email sending to the user from using their gmail account.

## To Do:
* add more exception handling
* make printouts optional
* make printouts prettier
* add more options in .env:
* for longer waits for elements to appear
* for debug mode
* path to browser, if necessary
* enable email sending in .env file
* handle env file better, it's kinda janky passing env_contents around
* optionally use keyring instead of .env to store credentials
* squash bug where verification element is screenshotted too early
* Update README.md with instructions for installing browser drivers
