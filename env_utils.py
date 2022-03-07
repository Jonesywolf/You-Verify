from dotenv import dotenv_values
import re

def load_dotenv(filename=".env"):
    print("Loading .env")
    return dotenv_values(filename)

def is_val_true(env_contents, key):
    return env_contents[key].lower() in ('true', '1', 'yes', 'y', 't')

def use_headless_mode(env_contents):
    return is_val_true(env_contents, "HEADLESS_MODE")

def get_creds(env_contents):
    creds = {}
    try:
        creds = {
            "user" : env_contents["USERNAME"],
            "pass" : env_contents["PASSWORD"]
        }
        # Clear sensitive info
        del env_contents["USERNAME"]
        del env_contents["PASSWORD"]
    except KeyError:
        print("Missing UTORID credentials in .env")
        
    return creds

def is_valid_gmail(gmail_addr):
    return re.fullmatch(r"\b[A-Za-z0-9._%+-]+@gmail.com\b", gmail_addr)

def load_gmail_addr(env_contents):
    try:
        gmail_addr = env_contents["GMAIL"]
        if not is_valid_gmail(gmail_addr):
            print("Invalid gmail address in .env")
    except KeyError:
        print("Missing GMAIL address in .env")
    return gmail_addr
    