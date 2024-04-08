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

driver.get('https://news.ycombinator.com/')


## scraping logic
count = 0
pagestoscrape = input('How many pages do you want to scrape? ')
pagestoscrape = int(pagestoscrape)

while pagestoscrape > count:


    #scrape every link on the page
    links = driver.find_elements(By.CLASS_NAME, 'titleline')
    links = [link.text for link in links]
    for link in links:
        print(link)

    # If there are more pages to scrape, click the next button

    if pagestoscrape > count:
        try:
            # wait until the next button is clickable
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'morelink')))

            # click the next button
            next_button = driver.find_element(By.CLASS_NAME, 'morelink')
            next_button.click()
            count += 1
            print('\n \n    Page ' + str(count) + ' successfully scraped')

            time.sleep(count*3)

            continue

        except Exception as error:
            print(error)
            print('no more pages to scrape')
            break



    # print ('Page ' + str(count) + ' scraped')
    # links = driver.find_elements(By.CLASS_NAME, 'titleline')
    # links = [link.text for link in links]
    # for link in links:
    #     print(link)
    #
    # count += 1

## close the browser
driver.quit()

