from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open URL
driver.get("https://www.saucedemo.com/")

try:
    # Wait for username input field to be visible
    username_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )

    # Send keys to username input field
    username_input.send_keys("standard_user")

    # Wait for password input field to be visible
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )

    # Send keys to password input field
    password_input.send_keys("secret_sauce")

    # Wait for login button to be clickable
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )

    # Click login button
    login_button.click()

    # Wait for the entire page to load
    WebDriverWait(driver, 20).until(
        lambda driver: driver.execute_script('return document.readyState') == 'complete'
    )

    # Get title of the webpage
    title = driver.title
    print("Title:", title)

    # Get current URL of the webpage
    current_url = driver.current_url
    print("Current URL:", current_url)

    # Extract entire contents of the webpage
    page_source = driver.page_source

    # Save page source to a text file
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(page_source)

finally:
    # Close the browser
    driver.quit()
