# You Verify

Fills out a form automatically, **use at your own risk**.

## Installation

First, make sure you have the Firefox browser and python 3 installed. Then, install all the required python dependencies with pip using:

`pip install -r requirements.txt`

Then run `main.py` like any other python file.

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