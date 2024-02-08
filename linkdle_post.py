import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to chromedriver.exe
chromedriver_path = 'chromedriver.exe'

# Setup the service
service = Service(executable_path=chromedriver_path)

# Start the WebDriver
driver = webdriver.Chrome(service=service)

# Open LinkedIn
driver.get('https://www.linkedin.com')

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'session_key')))

# Log in
username = driver.find_element(By.ID, "session_key")
password = driver.find_element(By.ID, "session_password")
username.send_keys("YOUR_USERNAME")
password.send_keys("YOUR_PASSWORD")
driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button").click()

# Wait for the home page to load
WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CLASS_NAME, 'share-box-feed-entry__trigger--v2')))

# Click on the "Start a post" button


# Upload an image
image_input = driver.find_element(By.XPATH, "//input[@accept='image/*']")
image_path = "path_to_your_image.png"  # Replace this with the path to your image file
image_input.send_keys(image_path)

# Enter title
title_input = driver.find_element(By.XPATH, "//input[@placeholder='Add title']")
title_input.send_keys("Your Title Here")

# Enter description
description_input = driver.find_element(By.XPATH, "//div[@role='textbox']")
description_input.send_keys("Your Description Here")

# Click on the "Post" button
driver.find_element(By.XPATH, "//button[contains(text(), 'Post')]").click()

# Wait for the post to be uploaded
time.sleep(145)

# Close the browser
driver.quit()
