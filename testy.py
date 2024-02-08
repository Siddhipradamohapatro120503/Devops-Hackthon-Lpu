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

# Use implicit or explicit waits instead of time.sleep()
# For example, using implicit wait:
# driver.implicitly_wait(10)

# Or using explicit wait:
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "element_id")))

# Close the browser after 10 seconds
time.sleep(10)
driver.quit()
