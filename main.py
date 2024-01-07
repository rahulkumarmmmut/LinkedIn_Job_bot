from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

ACCOUNT_EMAIL = "irahulk2903@gmail.com"
ACCOUNT_PASSWORD = "Rahulkumar2903"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3794953663&f_AL=true&geoId=103644278&keywords=Security%20Analyst&location=United%20States&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

time.sleep(2)
sign_in = driver.find_element(By.CLASS_NAME, value='nav__button-secondary')
sign_in.click()

time.sleep(2)
sign_in_email = driver.find_element(By.NAME, value='session_key')
sing_in_password = driver.find_element(By.NAME, value='session_password')

sign_in_email.send_keys(ACCOUNT_EMAIL)
sing_in_password.send_keys(ACCOUNT_PASSWORD)

sign_in_button = driver.find_element(By.CLASS_NAME, value='btn__primary--large')
sign_in_button.click()


job1 = driver.find_element(By.XPATH, value='//*[@id="ember440"]')
job1.click()

time.sleep(2)

job1_EA = driver.find_element(By.XPATH, value='//*[@id="ember1925"]/span')

time.sleep(1)

Phone_job1 = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3789410477-9-phoneNumber-nationalNumber"]')
Phone_job1.send_keys("123456789")

time.sleep(1)

job1_submit = driver.find_element(By.XPATH, value='//*[@id="ember2170"]/span')
job1_submit.click()




