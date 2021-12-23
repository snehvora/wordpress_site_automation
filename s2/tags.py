from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options() 
chrome_options.add_argument("--headless") 
# tagss=[]

driver=webdriver.Chrome(executable_path='chromedriver',chrome_options=chrome_options)

def tags(heading):
    driver.get("https://www.google.com/")

    elements=driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
    elements.send_keys(str(heading))
    elements.send_keys(Keys.ENTER)

    tags_list=[]
    tags=driver.find_elements_by_xpath("//div[@class='s75CSd']")
    for tag in tags:
        tags_list.append(tag.get_attribute('innerText'))

    return tags_list 
