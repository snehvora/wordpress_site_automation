from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

file_path = "C:/Users/Lenovo/Downloads/codebeautify.txt"
if os.path.isfile(file_path):
        os.remove(file_path)


chrome_options = Options()   
#chrome_options.add_argument("--headless")


driver=webdriver.Chrome(executable_path='chromedriver',chrome_options=chrome_options)

def unique_data(paras):
    list3=[]
    driver.get("https://codebeautify.org/paraphrasing-tool")
    for para in paras:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except:
            pass
        
        elements = driver.find_element_by_xpath("(//div[@class='viewerEditor ace_editor ace-tm']/textarea)[1]")
        elements.send_keys(str(para))
        
        time.sleep(2)
        elements=driver.find_element_by_xpath("//input[@id='defaultaction']")
        elements.click()

        time.sleep(5)

        elements=driver.find_element_by_xpath("(//input[@class='btn span11'])[4]")
        elements.click()

        time.sleep(5)

        try:
            with open(file_path, 'r', encoding='utf-8-sig', errors='ignore') as file_read:
                data = file_read.read()
                data = str(data).capitalize()
                list3.append(str(data))
                file_read.close()
        except:
            driver.refresh()

        try:
            driver.refresh()
        except:
            time.sleep(2)
            driver.refresh()
            
    x = " (Only headlines are taken from a syndicated feed.)"
    list3.append(x)
    return list3
    

