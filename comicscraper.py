import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## enable headless mode in Selenium
options = Options()
options.add_argument('--headless')

## initialize an instance of the chrome driver (browser)
driver = webdriver.Chrome(
    options=options,
# other properties...
)

driver.get('https://readcomiconline.li/Comic/Showcase/Issue-22?id=43363')

#reveal status code
time.sleep(5)
print(driver.title)


# ## scraping logic
# count = 0
# pagestoscrape = input('How many pages do you want to scrape? ')
# pagestoscrape = int(pagestoscrape)
#
# while pagestoscrape > count:


#scrape every link on the page
# comicpages = driver.find_elements(By.CLASS_NAME, 'noreferrer')
# comic = [page.text for horse in horses]
# for horse in horses:
#     with
