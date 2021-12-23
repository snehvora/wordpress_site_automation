from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import math

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

def post_report():
    login()
    time.sleep(5)
    element = wd.find_element_by_xpath("(//div[@id='adminmenuwrap']/ul/li/a)[2]")
    element.click()

    
    element = wd.find_element_by_xpath("(//span[@class='count'])[1]")
    num_posts = element.get_attribute("innerText")
    num_posts = num_posts[1:-1]
    num_posts = int(num_posts)
    num_posts = num_posts/20
    num_posts = math.ceil(num_posts)
    if(num_posts > 5):
        num_posts = 5
       

    post_title_data = []
    categorys = []
    all_data = []
    time.sleep(3)
    #Post Title
    j=0
    for num in range(num_posts):
        j+=1
        time.sleep(3)
        element = wd.find_element_by_xpath("//table[@class='wp-list-table widefat fixed striped table-view-list posts']")
        element.click()

        post_titles = element.find_elements_by_xpath("//table[@class='wp-list-table widefat fixed striped table-view-list posts']/tbody/tr/td/strong/a")
        for post_title in post_titles:
            post_title_data.append(post_title.get_attribute('innerText'))

        
        #Category
        cate = element.find_elements_by_xpath("//table[@class='wp-list-table widefat fixed striped table-view-list posts']/tbody/tr/td[@class='categories column-categories']/a")
        for category in cate:
            categorys.append(category.get_attribute('innerText'))
        

        if(j<num_posts):
            element = wd.find_element_by_xpath("(//a[@class='next-page button'])[2]")
            element.click()

    for i in zip(post_title_data, categorys):
        all_data.append(i)    
    return all_data


def sorting():
    data = post_report()
    world_heading = []
    alphabet_regular_expression = re.compile("[^a-zA-Z0-9]")
    for i in data:
        if('world news'==i[1].lower()):
            string_without_non_alphabet = re.sub(alphabet_regular_expression,"",i[0])
            world_heading.append(string_without_non_alphabet)
    wd.close()
    del data
    return world_heading

