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

driver.get('https://www.racingandsports.com.au/form-guide/thoroughbred/australia/echuca/2024-04-08/R1')

#reveal status code
print(driver.title)


# ## scraping logic
# count = 0
# pagestoscrape = input('How many pages do you want to scrape? ')
# pagestoscrape = int(pagestoscrape)
#
# while pagestoscrape > count:


#scrape every link on the page
horses = driver.find_elements(By.CLASS_NAME, 'horseName')
horses = [horse.text for horse in horses]
for horse in horses:
    print(horse)
