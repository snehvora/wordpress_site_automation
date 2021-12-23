from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()   
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-popup-blocking")


wd=webdriver.Chrome(chrome_options=chrome_options)


username = "admin"
password = "Jeelpatel@212121"
login_url = "https://newstheme.krahatfoundation.org/wp-login.php/"


def login():
    wd.get(login_url)

    form = wd.find_element_by_id('loginform')
    form_post_url = form.get_attribute('action')

    # login_url is the current URL
    if login_url != form_post_url:
        wd.get(form_post_url)

    form = wd.find_element_by_id('loginform')
    time.sleep(1)
    ele = wd.find_element_by_xpath("//input[@id='user_login']")
    ele.send_keys(username)
    time.sleep(1)
    ele1 = wd.find_element_by_xpath("//input[@id='user_pass']")
    ele1.send_keys(password)


    elements = wd.find_element_by_xpath("//input[@id='wp-submit']")
    elements.click()



