from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the target URL
url = "https://quotes.toscrape.com/search.aspx"
driver.get(url)
# Define a wait time
wait = WebDriverWait(driver, 10)

# Wait for the dropdown to be present and clickable
author_dropdown = wait.until(EC.presence_of_element_located((By.ID, "author")))

# Use Select to interact with the dropdown
select_author = Select(author_dropdown)

# Select "Albert Einstein" by visible text
select_author.select_by_visible_text("Albert Einstein")

# Wait for the dropdown to be present and clickable
tag_dropdown = wait.until(EC.presence_of_element_located((By.ID, "tag")))

# Use Select to interact with the dropdown
select_tag = Select(tag_dropdown)

# Select "Albert Einstein" by visible text
select_tag.select_by_visible_text("music")

check = wait.until(EC.element_to_be_clickable((By.NAME, "submit_button")))
check.click()

soup = driver.page_source
citation = BeautifulSoup(soup, "html.parser")

print(citation.find("span", class_="content").text.strip())

# Optional: If there is a submit button or other interaction needed after selecting
time.sleep(2)  # Allow time to see the selection

# Close the browser when done
driver.quit()








