from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import uniform

def start_survey(browser):
    # Wait for start survey button to appear
    check_in_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa-id='check-in-button']"))
    )
    check_in_btn.click()
    
def answer_question(browser, input_id_suffix):
    # Wait for answer button to appear
    answer_inputs = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, f"[id$={input_id_suffix}]"))
    )
    # Input isn't clickable, so click its parent element instead
    last_answer_input = answer_inputs[-1]
    last_answer_lbl = last_answer_input.find_element(By.XPATH, "..")
    last_answer_lbl.click()
    
def submit_survey(browser):
    submit_btn = browser.find_element(By.CLASS_NAME, "MuiButton-containedPrimary")
    submit_btn.click()
    
def fill_form(browser):
    start_survey(browser)
    answer_input_id_suffixes = [
        "yes",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no"
    ]
    for input_id_suffix in answer_input_id_suffixes:
        answer_question(browser, input_id_suffix)
        time.sleep(uniform(1, 3)) # seconds
        # TODO Make a delay function
    
    submit_survey(browser)
    # TODO remove this delay:
    time.sleep(uniform(3, 5)) # seconds
    