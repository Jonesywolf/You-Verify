from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def screenshot_page(browser, page_img_path):
    badge_elem_header = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "status-0-0"))
    )
    badge_elem_child = badge_elem_header.find_element(By.XPATH, "..")
    badge_elem = badge_elem_child.find_element(By.XPATH, "..")
    
    print("Taking a screenshot of the page...")
    page_img_path = page_img_path if page_img_path.endswith(".png") else page_img_path + ".png"
    page_img_path = page_img_path if page_img_path.startswith("screenshots/") else "screenshots/" + page_img_path
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
    page_img_path = page_img_path if page_img_path.endswith(".png") else page_img_path + ".png"
    page_img_path = page_img_path if page_img_path.startswith("screenshots/") else "screenshots/" + page_img_path
    im = Image.open(page_img_path)
    im = im.crop((int(x), int(y), int(width), int(height)))
    
    badge_img_path = badge_img_path if badge_img_path.endswith(".png") else badge_img_path + ".png"
    badge_img_path = badge_img_path if badge_img_path.startswith("screenshots/") else "screenshots/" + badge_img_path
    im.save(badge_img_path)
    print(f"Saved to {badge_img_path}.")

def save_screenshots(browser, badge_img_path, page_img_path):
    badge_elem = screenshot_page(browser, page_img_path)
    screenshot_badge(badge_img_path, page_img_path, badge_elem)
    
    #TODO add default image paths to gitignore