import random

# import all the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # error handling
from selenium.common.exceptions import TimeoutException  # timeout if not found
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# initialise chrome driver
import json

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--test-type")
options.binary_location = r"C:\chromedriver.exe"
crime = []

y = "https://www.populationu.com/gen/most-dangerous-cities-in-the-us"
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get(y)
driver.set_window_size(1920, 1080)
wait = WebDriverWait(driver, 250)
# count the number of universities on the page
cnt = driver.find_element(By.XPATH, "/html/body/div[6]").get_attribute("outerHTML")
count = cnt.count("<tr>")
print(count)
for i in range(1, count - 1):
    city_name = driver.find_element(
        By.XPATH, f"/html/body/div[6]/table/tbody/tr[{i}]/td[2]"
    ).get_attribute("innerHTML")
    city_state = driver.find_element(
        By.XPATH, f"/html/body/div[6]/table/tbody/tr[{i}]/td[3]"
    ).get_attribute("innerHTML")
    city_rank = driver.find_element(
        By.XPATH, f"/html/body/div[6]/table/tbody/tr[{i}]/td[1]"
    ).get_attribute("innerHTML")
    crimes_per_day = driver.find_element(
        By.XPATH, f"/html/body/div[6]/table/tbody/tr[{i}]/td[11]"
    ).get_attribute("innerHTML")
    crime.append(
        {
            "city name": city_name,
            "State": city_state,
            "City rank": city_rank,
            "Crimes per day": crimes_per_day,
        }
    )
random.shuffle(crime)


# store all the details in a JSON
with open("./json_files/crimes_new.json", "w") as myfile:
    myfile.write(json.dumps(crime, indent=4))

with open("./json_files/crimes_new.json", "r") as myfile:
    data = json.load(myfile)
print(data)
