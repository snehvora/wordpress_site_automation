from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import math
import smtplib


chrome_options = Options()   
chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-popup-blocking")


wd=webdriver.Chrome(chrome_options=chrome_options)


username = "admin"
password = "admin123"
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
    post_links = []
    categorys = []
    all_data = []
    post_seo_score = []
    tags = []    
    time.sleep(3)
    #Post Title
    j=0
    for num in range(num_posts):
        j+=1
        time.sleep(3)
        element = wd.find_element_by_xpath("//table[@class='wp-list-table widefat fixed striped table-view-list posts']")
        element.click()

        #Post Title
        post_titles = element.find_elements_by_xpath("//table[@class='wp-list-table widefat fixed striped table-view-list posts']/tbody/tr/td/strong/a")
        for post_title in post_titles:
            post_title_data.append(post_title.get_attribute('innerText'))
        
        #Post links
        post_titles_links = element.find_elements_by_xpath("//table[@class='wp-list-table widefat fixed striped table-view-list posts']/tbody/tr/td/strong/a")
        for post_title_l in post_titles_links:
            post_links.append(post_title_l.get_attribute('href'))

        
        #Category
        cate = element.find_elements_by_xpath("//table[@class='wp-list-table widefat fixed striped table-view-list posts']/tbody/tr/td[@class='categories column-categories']/a")
        for category in cate:
            categorys.append(category.get_attribute('innerText'))
        
        #Post SEO Score
        post_seo = element.find_elements_by_xpath("//table[@class='wp-list-table widefat fixed striped table-view-list posts']/tbody/tr/td/span[starts-with(@class, 'rank-math-column-display seo-score ')]/strong")
        for seo_score in post_seo:
            data = seo_score.get_attribute('innerText')
            post_seo_score.append(data[:2])

        
        #Tags of Post
        post_tags = element.find_elements_by_xpath("//td[@class='tags column-tags']")
        for all_tag in post_tags:
            tags.append(all_tag.get_attribute('innerText'))


        if(j<num_posts):
            element = wd.find_element_by_xpath("(//a[@class='next-page button'])[2]")
            element.click()

    for i in zip(post_title_data, post_links, categorys, post_seo_score, tags):
        all_data.append(i)    
    return all_data

def dashboard():
    data = post_report()
    seo_prob = []
    tag_prob = []
    for i in data:
        seo = i[3]
        if(int(seo) <= 30):
            seo_prob.append(i[1])
        if(i[4] == "—\nNo tags"):
            tag_prob.append(i[1])
    


    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    print("Send Request For Login...")
    s.starttls()
    print("Hand Saking")
    s.login("s...@gmail.com", "P...d")
    print("Login...")
    message = """\
    Subject: Site Problem Detection

    Here is the list of SEO Score Problems:"""+ str(seo_prob) +"""Here is the list of Tag Score Problems:.""" + str(tag_prob) +"""."""

    s.sendmail("sneh.vora135@gmail.com", "jeelpatel27602@gmail.com", message)
    print("Mail Send Sucessfully!!!")
    s.quit()

dashboard()


