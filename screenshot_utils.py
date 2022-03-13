from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

def fix_img_path(img_path):
    img_path = img_path if img_path.endswith(".png") else img_path + ".png"
    img_path = img_path if img_path.startswith("screenshots/") else "screenshots/" + img_path
    return img_path

def screenshot_page(browser, page_img_path):
    badge_elem_header = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "status-0-0"))
    )
    badge_elem_child = badge_elem_header.find_element(By.XPATH, "..")
    badge_elem = badge_elem_child.find_element(By.XPATH, "..")
    
    print("Taking a screenshot of the page...")
    
    try:
        Path("screenshots/").mkdir()
    except FileExistsError:
        # Screenshots folder already exists
        pass
    else:
        print("Created screenshots folder.")
    
    page_img_path = fix_img_path(page_img_path)
    browser.save_screenshot(page_img_path);
    print(f"Saved to {page_img_path}.")
    return badge_elem

def screenshot_badge(badge_img_path, page_img_path, badge_elem):
    # crop image
    elem_location = badge_elem.location;
    elem_size = badge_elem.size;
    x = elem_location["x"];
    y = elem_location["y"];
    width = x + elem_size["width"];
    height = y + elem_size["height"];
    print("Taking a screenshot of the badge...")
    page_img_path = fix_img_path(page_img_path)
    im = Image.open(page_img_path)
    im = im.crop((int(x), int(y), int(width), int(height)))
    
    badge_img_path = fix_img_path(badge_img_path)
    im.save(badge_img_path)
    print(f"Saved to {badge_img_path}.")

def save_screenshots(browser, badge_img_path, page_img_path):
    badge_elem = screenshot_page(browser, page_img_path)
    screenshot_badge(badge_img_path, page_img_path, badge_elem)
    
    #TODO add default image paths to gitignore