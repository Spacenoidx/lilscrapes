from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# enable headless mode in Selenium
options = Options()
options.add_argument('--headless=new')

# initialize an instance of the chrome driver (browser)
driver = webdriver.Chrome(
    options=options,
    # other properties...
)

# visit your target site
driver.get('https://scrapingclub.com/')
exercise_cards = driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div[1]/h5', /html/body/div[3]/div[2]/div/div[2]/div[1]/h5)

with open('exercise.txt', 'w') as f:
    for card in exercise_cards:
        f.write(card.text + '\n')

# scraping logic...

# release the resources allocated by Selenium and shut down the browser
driver.quit()
