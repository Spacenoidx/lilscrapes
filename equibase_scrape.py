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
driver.get('https://www.equibase.com/static/workout/KEE040324USA-EQB.html')
print(driver.title)
horse_name_entries = driver.find_elements(By.XPATH, '//*[@data-label="Horse Name"]')
with open('exercise3.txt', 'w') as f:
    for name in horse_name_entries:
        f.write(name.text + '\n')

# scraping logic...

# release the resources allocated by Selenium and shut down the browser
driver.quit()
