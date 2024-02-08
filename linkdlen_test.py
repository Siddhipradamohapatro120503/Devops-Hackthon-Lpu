from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv()

chrome_driver_path = "chromedriver.exe"

s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)
url = "https://linkedin.com/"

driver.get(url=url)
time.sleep(2)

email = driver.find_element(By.ID, "session_key")
password = driver.find_element(By.ID, "session_password")

email.send_keys(os.getenv('Gmail'))
password.send_keys(os.getenv('Pass'))
time.sleep(2)
login = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/button")
time.sleep(2)
login.click()
time.sleep(60)


Post_uplode= driver.find_element(By.CLASS_NAME, 'share-box-feed-entry__trigger')
Post_uplode.click()
time.sleep(2)

# image_input = driver.find_element(By.CLASS_NAME, "share-promoted-detour-button")
# image_path = "output.png"  # Replace this with the path to your image file
# image_input.send_keys(image_path)

def description_input(Input_dsicription):
    description_input = driver.find_element(By.CLASS_NAME, "ql-editor")
    description_input.send_keys(Input_dsicription)
    time.sleep(5)


driver.find_element(By.XPATH, "//button[contains(text(), 'Post')]").click()

time.sleep(100)

# media_button = driver.find_element(By.CLASS_NAME,"share-promoted-detour-button__icon-container")
# media_button.click()

# Wait for the media modal to load
# time.sleep(2)

# # Find the input element for media upload
# input_element = driver.find_element(By.CLASS_NAME,"artdeco-button")

# # Provide the path to your image file
# image_path = 'C:\Users\siddh\OneDrive\Desktop\Devops Project_ lpu\Devops-Hackthon-Lpu\output.png'

# # Upload the image file
# input_element.send_keys(image_path)

# # Wait for the image to be uploaded
# time.sleep(5)

# sign_in_button = driver.find_element(by=By.CLASS_NAME, value="nav__button-secondary")

# sign_in_button.click()

# email_field = driver.find_element(by=By.NAME, value="session_key")
# email_field.send_keys("XXXX@gmail.com")

# password_field = driver.find_element(by=By.ID, value="password")
# password_field.send_keys("XXXXX")

# sign_in = driver.find_element(by=By.CSS_SELECTOR, value="form button")
# sign_in.send_keys(Keys.ENTER)

# apply_job_posts = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# for listing in apply_job_posts:
#     print("Clicked Easy_apply confirmed")
#     listing.click()
#     time.sleep(3)

#     try:
#         # apply button field
#         apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
#         apply_button.click()
#         time.sleep(5)

#         # phone number field
#         phone_number = driver.find_element(by=By.CLASS_NAME, value="fb-single-line-text__input")
#         if phone_number.text == "":
#             phone_number.send_keys("1234567899")

#         # Cancel and discard button
#         cancel_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
#         cancel_button.click()

#         discard_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")
#         discard_button.click()

#     except NoSuchElementException:
#         print("No Application button available, skipped")
#         continue

# driver.quit()