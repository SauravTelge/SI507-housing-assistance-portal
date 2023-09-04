# import all the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #error handling
from selenium.common.exceptions import TimeoutException #timeout if not found
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
# initialise chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = r"C:\chromedriver.exe"
univ=[]

y=f'https://www.4icu.org/us/a-z/'
driver = webdriver.Chrome('C:\\chromedriver.exe')
driver.get(y)
driver.set_window_size(1920, 1080)
wait = WebDriverWait(driver, 250)
# count the number of universities on the page
cnt= driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/table/tbody").get_attribute("outerHTML")
count1 = cnt.count('<tr>')
print(count1)
for i in range(1,count1+1):

    
    univ_name=driver.find_element(By.XPATH,f"/html/body/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[2]/a").get_attribute("innerHTML")
    univ_town=driver.find_element(By.XPATH,f"/html/body/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[3]").get_attribute("innerHTML")
    univ_rank=driver.find_element(By.XPATH,f"/html/body/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[1]/b").get_attribute("innerHTML")
   
    univ.append({'university name':univ_name,'university town':univ_town,'university rank':univ_rank})

# store all the details in a CSV
with open("universities.csv", 'w') as myfile:
    for row in univ:
        for x in row:
            myfile.write(str(x) + ',')
        myfile.write('\n')

# store all the details in a JSON
with open("./json_files/universities.json", 'w') as myfile:
    myfile.write(json.dumps(univ,indent = 4))

with open('./json_files/universities.json','r') as myfile:  
  data = json.load(myfile)  
print(data)

