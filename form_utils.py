from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from random import uniform

def open_form(browser):
    print("Starting form...")
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
    print("Submitting form...")
    submit_btn = browser.find_element(By.CLASS_NAME, "MuiButton-containedPrimary")
    submit_btn.click()
    print("Form submitted...")
    
def fill_form(browser):
    open_form(browser)
    answer_input_id_suffixes = [
        "yes",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no"
    ]
    print("Filling out form...")
    for input_id_suffix in answer_input_id_suffixes:
        answer_question(browser, input_id_suffix)
        time.sleep(uniform(1, 3)) # seconds
        # TODO Make a delay function
    
    submit_survey(browser)
    
def verify_form_completion(browser):
    # Wait for form completion to appear
    try:
        form_completed_elem = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "lastCheckInLabel"))
        )
        form_completion_success = True
    except TimeoutException:
        form_completion_success = False
    return form_completion_success
    #TODO validate using datetime in time element to ensure the most recent from filling succeeded