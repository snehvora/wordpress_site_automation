from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from paragraph import ndtv_fashion_paragraph
from tags import tags
import time
from check import sorting
import re



chrome_options = Options()   
chrome_options.add_argument("--headless")

driver=webdriver.Chrome(executable_path='chromedriver',chrome_options=chrome_options)


#NDTV FASHION
def ndtv_fashion_scraper():
    driver.get("https://www.hindustantimes.com/lifestyle/fashion")
    heading_data = sorting()
    post_list=[]
    post_info=[]
    news_title = []
    post_list1=[]

    
    news=driver.find_elements_by_xpath("(//h2[@class='hdg3']/a)[position() >= 2 and position() < 12]")
    alphabet_regular_expression = re.compile("[^a-zA-Z0-9]")
    for i in news:
        post_list.append(i.get_attribute('href'))
        string_without_non_alphabet3 = re.sub(alphabet_regular_expression,"",i.get_attribute('innerText'))
        news_title.append(string_without_non_alphabet3)

    print(news_title)
    print(post_list)
    for i in heading_data:
        if(i not in news_title):
            heading_data.remove(i)
    

    result = set(news_title) - set(heading_data)
    res = list(result)
    

    for i in res:
        index = news_title.index(i)
        post_list1.append(post_list[index])
        


    #data from posts
    headings=[]
    paragraphs=[]
    images=[]
    categories=[]
    tags_list=[]

    for post in post_list1:
        driver.get(post)
        heading=driver.find_elements_by_xpath("//h1[@class='hdg1']")
        paragraph=ndtv_fashion_paragraph(post)
        paragraphs.append(paragraph)
        image=driver.find_elements_by_xpath("(//div[@class='fullStory tfStory']/figure/span/img)[1]")
        for h in heading:
            headings.append(h.get_attribute('innerText'))
            categories.append('Fashion')
            t=tags(h.get_attribute('innerText'))
            tags_list.append(t)

        for i in image:
            images.append(i.get_attribute('src'))

    for i in zip(headings,paragraphs,images,tags_list,categories):
        post_info.append(i)
    
    del headings,paragraphs,images,tags_list,categories

    i=0
    post_info1=[]
    while i < len(post_info):
        if(".jpg" in post_info[i][2]):
            post_info1.append(post_info[i])
        i+=1

    del post_info,post_list,news_title
    
    return post_info1

