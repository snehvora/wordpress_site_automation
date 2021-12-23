from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from paraphrases import unique_data
from preprocess import preprocess

chrome_options = Options()   
chrome_options.add_argument("--headless")

driver=webdriver.Chrome(executable_path='chromedriver',chrome_options=chrome_options)

#FOOD NEWS SECTION
def ndtv_movie_paragraph(url):
    driver.get(url)

    paras=driver.find_elements_by_xpath("//div[@class='expand-txt']/p")
    l=len(paras)
    print(l)
    list1=[]
    for i in range(1,l+1):
        x_path = "(//div[@class='expand-txt']/p)[{}]".format(i)
        para=driver.find_element_by_xpath(x_path)
        list1.append(para.get_attribute('innerText'))

    
    list3=[]   

    if('' in list1):
        list1.remove('')
    for j in list1:
        j=' '+j
        list3.append(j)
    # for j in list3:
    #     if("Also Read" in j):
    #         list3.remove(j)
    del list1
    list3 = preprocess(list3)
    para_list=unique_data(list3)
 
    return para_list

