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
driver.get('https://www.pcgamesn.com/overwatch-2/tier-list')

# find the table
table = driver.find_element(By.TAG_NAME, 'table')

# find all rows within the table
rows = table.find_elements(By.TAG_NAME, 'tr')

# find the names in the location
names = driver.find_elements(By.TAG_NAME, 'td')

# initialize an empty list to store the table data
table_data = []

# iterate over rows
for row in rows:
    # find all cells within each row
    cells = row.find_elements(By.TAG_NAME, 'td')
    # extract text from each cell and store in a row_data list
    row_data = [cell.text for cell in cells]
    # append the row_data to the table_data list
    table_data.append(row_data)

# print(table_data[0])
# print(table_data[0][0], table_data[0][1])
# print(table_data[1:])
# row_groups = table_data[1:]
# print(table_data[1:][0][1])
#
# # print the tiers
# for i in row_groups:
#     print(i[0])

#create a list to store the character_data after everything
character_data_list = []

# save the names
with open('exercise5.csv', 'w') as f:

    # write the header
    f.write(table_data[0][0] + "," + table_data[0][1])

    # skip the header and access the data in each row
    for row in table_data[1:]:
        # For every row, the character tier is going to be the first item. We can still define the tier down below.
        for entry in row[1:]:
            tier = row[0]
            # Split the string into an array
            heroes = entry
            heroes = heroes.split(",")
            # character_data = {tier: i for i in heroes}
            for hero in heroes:
                character_data = {tier: hero}
                print(character_data, "-- added to list")
                character_data_list.append(character_data)
        # concatenate all items in row[1] into a single string
        cell_content = str([i for i in row[1:]])
        # remove the brackets and get the text of the entire entry as a string
        joined_content = ''.join(row[1:])
        # print(joined_content)

        # write to the CSV file
        f.write("\n" + row[0] + "," + str(joined_content))

    # for name in names:
    #     f.write("," + name.text)

# scraping logic...

# release the resources allocated by Selenium and shut down the browser
driver.quit()

print(character_data_list)

with open('character_data_list.txt', 'w') as f:
    for character in character_data_list:
        f.write(str(character) + '\n')