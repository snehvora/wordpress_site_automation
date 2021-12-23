from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from paragraph import ndtv_movie_paragraph
from tags import tags
from check import sorting
import re




chrome_options = Options()   
chrome_options.add_argument("--headless")

driver=webdriver.Chrome(executable_path='chromedriver',chrome_options=chrome_options)

def ndtv_movie_news_scraper():
    driver.get("https://www.ndtv.com/world-news")
    heading_data = sorting()
    post_list=[]
    post_info=[]
    news_title = []
    com_data = []
    post_list1=[]

    alphabet_regular_expression = re.compile("[^a-zA-Z0-9]")              
    news=driver.find_elements_by_xpath("//h2[@class='newsHdng']/a")
    for i in news:
        post_list.append(i.get_attribute('href'))
        string_without_non_alphabet3 = re.sub(alphabet_regular_expression,"",i.get_attribute('innerText'))
        news_title.append(string_without_non_alphabet3)
            
    print(news_title)        
    print(heading_data)
    for i in heading_data:
        if(i not in news_title):
            heading_data.remove(i)
    print(heading_data)

    result = set(news_title) - set(heading_data)
    res = list(result)
    
    print(res)
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
        heading=driver.find_elements_by_xpath("//div[@class='sp-ttl-wrp']/h1")
        paragraph=ndtv_movie_paragraph(post)
        paragraphs.append(paragraph)
        image=driver.find_elements_by_xpath("(//div[@class='ins_instory_dv_cont']/img)[1]")
        for h in heading:
            headings.append(h.get_attribute('innerText'))
            categories.append('world news')
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

    # del post_info2
    del post_info,post_list,news_title
    return post_info1


