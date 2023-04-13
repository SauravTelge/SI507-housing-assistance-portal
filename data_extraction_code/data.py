
# # import all the required libraries
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC #error handling
# from selenium.common.exceptions import TimeoutException #timeout if not found
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# # initialise chrome driver
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = r"C:\chromedriver.exe"

# y='https://www.4icu.org/us/a-z/'
# driver = webdriver.Chrome('C:\\Users\\Saurav Telge\\chromedriver.exe')
# driver.get(y)


# driver.set_window_size(1920, 1080)
# # all_univ = []
# # all_towns = []
# # all_ranks = []
# # final_dict = {}
# all_data = []
# while (True):
#     i = 0
    
#     # all_univ.append() 
#     # all_towns.append()
#     # all_ranks.append()
#     temp_dict={'univ_name':driver.find_elements(By.XPATH, f"/html/body/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[2]/a").get_attribute("innerHTML"),
#      'town':driver.find_elements(By.XPATH, f"/html/body/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[3]").get_attribute("innerHTML"),
#      'rank':driver.find_elements(By.XPATH, f"/html/body/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[1]/b").get_attribute("innerHTML")
#      }
#     all_data.append(temp_dict)
#     i +=1
#     if 
# print(all_data)


# import all the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #error handling
from selenium.common.exceptions import TimeoutException #timeout if not found
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
   
    univ.append([univ_name,univ_town,univ_rank])

# sort the list of list according to country names
univ.sort()
# store all the details in a csv
with open("universities.csv", 'w') as myfile:
    for row in univ:
        for x in row:
            myfile.write(str(x) + ',')
        myfile.write('\n')
