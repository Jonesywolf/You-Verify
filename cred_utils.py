from dotenv import dotenv_values
from selenium.webdriver.common.by import By

import time
from random import uniform

def load_creds(filename=".env"):
    raw_creds = dotenv_values(filename)
    creds = {}
    try:
        creds = {
            "user" : raw_creds["USERNAME"],
            "pass" : raw_creds["PASSWORD"]
        }
    except KeyError:
        print(f"Invalid credential file: {filename}")
    return creds

def fill_username(browser, user_creds):
    if user_creds["user"]:
        username_input = browser.find_element(By.ID, "username")
        username_input.send_keys(user_creds["user"])
    else:
        print("Username not found")

def fill_password(browser, user_creds):
    if user_creds["pass"]:
        pass_input = browser.find_element(By.ID, "password")
        pass_input.send_keys(user_creds["pass"])
    else:
        print("Password not found")

def submit_form(browser):
    submit_btn = browser.find_element(By.NAME, "_eventId_proceed")
    submit_btn.click()

def login(browser):
    user_creds = load_creds()
    if user_creds:
        fill_username(browser, user_creds)
        
        time.sleep(uniform(2, 4)) # seconds
        
        fill_password(browser, user_creds)
        
        # Clear user_creds
        user_creds = None
        
        time.sleep(uniform(2, 4)) # seconds
        
        submit_form(browser)