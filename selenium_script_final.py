from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Setup Firefox options to automatically allow location access in browser
options = Options()
options.set_preference("geo.prompt.testing", True)
options.set_preference("geo.prompt.testing.allow", True)

# Initialize the WebDriver with Firefox and the specified options
with webdriver.Firefox(options=options) as driver:
    # Navigate to the website
    url = "https://gridmybusiness.com/"
    driver.get(url)

    # Wait for the login button to be clickable
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='cursor-pointer ng-star-inserted']"))).click()
    except TimeoutException:
        print("Login button not found or not clickable within timeout.")

    # Wait for the email input to be visible
    try:
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='mb-4 auth-input mx-auto'] input[placeholder='Your Email']")))
        email_input.send_keys('luke@websitetransformers.co.uk')
    except TimeoutException:
        print("Email input not found within timeout.")

    # Wait for the password input to be visible
    try:
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='mb-4 auth-input mx-auto'] input[placeholder='Your Password']")))
        password_input.send_keys('7h2FB5%lKMr2')
    except TimeoutException:
        print("Password input not found within timeout.")

    # Find and click the submit button for login
    try:
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='w-full rounded text-white bg-primary text-white font-bold reduce-to-14-below-375']")))
        submit_button.click()
    except TimeoutException:
        print("Submit button not found or not clickable within timeout.")

    # Attempt to find and interact with the specified element
    try:
        element_to_interact = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mat-icon.notranslate.black-60.material-icons.mat-icon-no-color")))
        element_to_interact.click()
    except TimeoutException:
        print("Specified element not found or not clickable within timeout.")
    except Exception as e:
        print(f"Failed to interact with the specified element: {e}")

    # Click the button with the CSS selector "button.bg-accent:nth-child(1)"
    try:
        button_to_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-accent:nth-child(1)")))
        button_to_click.click()
    except TimeoutException:
        print("Button not found or not clickable within timeout.")

    # Input address into the element with the given CSS selector
    css_selector_for_input = ".location-input"
    address_to_input = "Star House 95 ,High Road, Benfleet, Essex, England, SS7 5LN"
    try:
        address_input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector_for_input)))
        address_input_field.send_keys(address_to_input)
    except TimeoutException:
        print("Address input field not found within timeout.")

    # Wait for 10 seconds before clicking the next button
    time.sleep(10)

    # Click the next button with the CSS selector "button.black-87"
    try:
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.black-87")))
        next_button.click()
    except TimeoutException:
        print("Next button not found or not clickable within timeout.")

    # Wait to visually confirm the actions before the browser closes
    time.sleep(30)
        # Click the next button with the CSS selector "button.black-87"
   

    # Click the element with the CSS selector "div.ng-star-inserted:nth-child(4)"
    try:
        element_to_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ng-star-inserted:nth-child(4)")))
        element_to_click.click()
    except TimeoutException:
        print("Element with CSS selector 'div.ng-star-inserted:nth-child(4)' not found or not clickable within timeout.")

    # Wait to visually confirm the actions before the browser closes
    time.sleep(30)
        # Click the element with the CSS selector "div.ng-star-inserted:nth-child(4)"
    try:
        search_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Insert search query']")))
        search_input.send_keys("architect")
    except TimeoutException:
        print("Search input field not found within timeout.")
    time.sleep(30)

  # Click the button with the CSS selector "button[id='scan-now'] span"
    try:
        scan_now_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#scan-now > span:nth-child(1)")))
        scan_now_button.click()
    except TimeoutException:
        print("Scan Now button not found or not clickable within timeout.")
    
    # Add any additional actions here...

    # Optional: Wait to visually confirm the actions before the browser closes
    time.sleep(40)
     # Click the button with the CSS selector "button.flex:nth-child(4)"
    try:
        button_to_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".flex.items-center.justify-center.export-button")))
        button_to_click.click()
    except TimeoutException:
        print("Button not found or not clickable within timeout.")
    
    # Add any additional actions here...

    # Optional: Wait to visually confirm the actions before the browser closes
    time.sleep(30)
    try:
        clickable_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".w-48"))
        )
        clickable_element.click()
    except TimeoutException:
        print("Element with CSS selector '.w-48' not found or not clickable within timeout.")
    
    # Add any further actions here

    # This is optional; adjust the sleep time as necessary for visual confirmation or debugging
    # import time
    time.sleep(30)




