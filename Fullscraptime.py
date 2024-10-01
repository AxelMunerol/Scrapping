from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time

# Start timer
start_time = time.time()

# Initialize WebDriver
driver = webdriver.Chrome()

# Start on the first page
nbpage = 1
URL = f"https://quotes.toscrape.com/page/{nbpage}/"
driver.get(URL)
page = requests.get(URL)
# Set up a wait time
wait = WebDriverWait(driver, 10)

# Loop through pages
while True:
    # Wait until the "Next" button or page content is present
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup.prettify())

    # Do your scraping work here (extract quotes, authors, etc.)

    # Find the "Next" button
    next_button = driver.find_elements(By.CLASS_NAME, 'next')

    if next_button:
        # Click the "Next" button to go to the next page
        next_button[0].find_element(By.TAG_NAME, "a").click()
        nbpage += 1
        time.sleep(2)  # Wait for 2 seconds before loading the next page
    else:
        # No more "Next" button, break the loop
        break

# Close the browser when done
driver.quit()
# End timer
end_time = time.time()

# Calculate and print the execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.2f} seconds")
