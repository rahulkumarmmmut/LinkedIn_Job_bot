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


# Wait for job listings to load
time.sleep(5)

# Find all job listing elements by their common class name
job_listings = driver.find_elements(By.CSS_SELECTOR, 'li.jobs-search-results__list-item')[:20]  # Take the first 20 job listings

for job_listing in job_listings:
    # Scroll into view and click the job listing
    driver.execute_script("arguments[0].scrollIntoView();", job_listing)
    job_listing.click()
    time.sleep(2)

    try:
        # Click on the 'Easy Apply' button
        easy_apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button--top-card')
        easy_apply_button.click()
        time.sleep(2)

        # Click on the 'Next' button
        next_button = driver.find_element(By.XPATH, "//button[@aria-label='Continue to next step']")
        next_button.click()
        time.sleep(2)

        # Check for 'Submit Application' button
        try:
            submit_button = driver.find_element(By.XPATH, "//button[@aria-label='Submit application']")
            submit_button.click()
        except NoSuchElementException:
            # If the 'Submit Application' button is not there, check for another 'Next' button
            try:
                next_button = driver.find_element(By.XPATH, "//button[@aria-label='Continue to next step']")
                # If there's another next button, close the application
                close_button = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
                close_button.click()
            except NoSuchElementException:
                print("Neither Submit nor Next button found, maybe already applied or other issue.")
    except NoSuchElementException:
        print("Easy Apply button not found, might not be an easy apply job.")

    # Return to the job listings page or close the job detail modal if necessary
    driver.get("https://www.linkedin.com/jobs/search/?keywords=Security%20Analyst&location=United%20States")
    time.sleep(2)

# ... [rest of your code] ...
