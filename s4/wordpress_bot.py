from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login import login
from login  import wd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from image_downloader import image_downloader
import random
from news_model import ndtv_movie_news_scraper


ndtv_movie_news_data = ndtv_movie_news_scraper()
print(ndtv_movie_news_data)

image = str("C:/Users/Lenovo/Desktop/site_automation/s4/image/1.jpg")
count = 1

ex_links = ["https://en.wikipedia.org/wiki/Entertainment"]


try:
    login()
except:
    wd.close()
    login()
time.sleep(10)
wd.refresh()
for data in ndtv_movie_news_data:
    #clicking new post
    time.sleep(2)
    try:
        elements=wd.find_element_by_xpath("//div[@class='wp-menu-image dashicons-before dashicons-admin-post']")
        elements.click()
    except:
        wd.refresh()
        elements=wd.find_element_by_xpath("//div[@class='wp-menu-image dashicons-before dashicons-admin-post']")
        elements.click()

    #clicking add new
    time.sleep(2)
    try:
        elements=wd.find_element_by_xpath("//a[@class='page-title-action']")
        elements.click()
    except:
        wd.refresh()
        elements=wd.find_element_by_xpath("//a[@class='page-title-action']")
        elements.click()

    #writing heading
    time.sleep(2)
    elements=wd.find_element_by_xpath("//textarea[@class='editor-post-title__input']")
    elements.send_keys(str(data[0]))
    time.sleep(1)

    #add image and caption
    time.sleep(2)
    elements = wd.find_element_by_xpath("(//div[@class='edit-post-header-toolbar__left']/button)[1]")
    elements.click()

    time.sleep(2)
    elements = wd.find_element_by_xpath("//button[@class='components-button block-editor-block-types-list__item editor-block-list-item-image']")
    elements.click()

    time.sleep(2)
    elements = wd.find_element_by_xpath("//button[@class='components-button block-editor-media-placeholder__button is-tertiary']")
    elements.click()
    
    time.sleep(2)
    elements = wd.find_element_by_xpath("//input[@class='block-editor-media-placeholder__url-input-field']")
    elements.send_keys(str(data[2]))
    
    time.sleep(3)
    elements = wd.find_element_by_xpath("//button[@class='components-button block-editor-media-placeholder__url-input-submit-button has-icon']")
    elements.click()

    time.sleep(2)
    elements = wd.find_element_by_xpath("//div[@class='block-editor-block-contextual-toolbar-wrapper']/div/div/div/div/button")
    elements.click()

    time.sleep(2)
    elements = wd.find_element_by_xpath("(//div[@class='components-dropdown-menu__menu']/button)[2]")
    elements.click()

    time.sleep(2)
    elements = wd.find_element_by_xpath("//figcaption[@class='block-editor-rich-text__editable rich-text']")
    elements.send_keys(str(data[0]))
    #paragraph
    for paragraph in data[1]:
        time.sleep(2)
        elements=wd.find_element_by_xpath("(//div[@class='edit-post-header-toolbar__left']/button)[1]")
        elements.click()
        time.sleep(2)
        elements=wd.find_element_by_xpath("//button[@class='components-button block-editor-block-types-list__item editor-block-list-item-paragraph']")
        elements.send_keys(str(paragraph))
    
    elements=wd.find_element_by_xpath("(//div[@class='edit-post-header-toolbar__left']/button)[1]")
    elements.click()

    elements=wd.find_element_by_xpath("//button[@class='components-button block-editor-block-types-list__item editor-block-list-item-separator']")
    elements.click()

    elements=wd.find_element_by_xpath("(//div[@class='edit-post-header-toolbar__left']/button)[1]")
    elements.click()

    time.sleep(3)
    elements=wd.find_element_by_xpath("//button[@class='components-button block-editor-block-types-list__item editor-block-list-item-heading']")
    elements.send_keys(str(" You May Also Like:"))

    time.sleep(1)
    elements=wd.find_element_by_xpath("(//div[@class='edit-post-header-toolbar__left']/button)[1]")
    elements.click()

    elements=wd.find_element_by_xpath("//button[@class='components-button block-editor-block-types-list__item editor-block-list-item-latest-posts']")
    elements.click()

    time.sleep(2)
    elements = wd.find_element_by_xpath("(//div[@class='block-editor-block-contextual-toolbar-wrapper']/div/div/div[@class='block-editor-block-toolbar__slot']/div[@class='components-toolbar-group']/button)[2]")
    elements.click()

    time.sleep(1)
    elements = wd.find_element_by_xpath("(//input[@class='components-form-toggle__input'])[4]")
    elements.click()

    elements = wd.find_element_by_xpath("(//div[@class='components-toolbar']/div/button)[2]")
    elements.click()

    elements=wd.find_element_by_xpath("(//div[@class='edit-post-header-toolbar__left']/button)[1]")
    elements.click()

    elements=wd.find_element_by_xpath("//button[@class='components-button block-editor-block-types-list__item editor-block-list-item-separator']")
    elements.click()
    

    #External Link
    ex_data = ' <a href="'+ random.choice(ex_links) +'" rel="nofollow">Click Here</a>'
    elements=wd.find_element_by_xpath("(//div[@class='edit-post-header-toolbar__left']/button)[1]")
    elements.click()

    elements=wd.find_element_by_xpath("//button[@class='components-button block-editor-block-types-list__item editor-block-list-item-html']")
    elements.send_keys(str(ex_data))

    time.sleep(2)
    elements=wd.find_element_by_xpath("(//div[@class='components-panel__header interface-complementary-area-header edit-post-sidebar__panel-tabs']/ul/li/button)[1]")
    elements.click()
    
    if(count==1):
        time.sleep(4)
        elements=wd.find_element_by_xpath("(//div[@class='components-panel']/div/h2/button)[7]")
        elements.click()
        count = count+1
    
    time.sleep(4)
    elements=wd.find_element_by_xpath("//button[@class='components-button editor-post-featured-image__toggle']")
    elements.click()
    
    time.sleep(3)
    elements=wd.find_element_by_xpath("(//div[@class='media-router']/button)[1]")
    elements.click()

    #downloading image
    time.sleep(2)
    image_downloader(data[2])
    time.sleep(5)
    #uploading image
    input_tag = "//input[starts-with(@id,'html5_')]"
    elements = wd.find_element_by_xpath(input_tag)
    elements.send_keys(image)
    time.sleep(15)
    try:
        elements=wd.find_element_by_xpath("//div[@class='media-toolbar-primary search-form']/button")
        elements.click()
    except:
        time.sleep(6)
        elements=wd.find_element_by_xpath("//div[@class='media-toolbar-primary search-form']/button")
        elements.click()
    
    time.sleep(2)
    elements=wd.find_element_by_xpath("(//div[@class='components-panel__header interface-complementary-area-header edit-post-sidebar__panel-tabs']/ul/li/button)[1]")
    elements.click()
    
    if(count==2):
        time.sleep(2)
        elements=wd.find_element_by_xpath("(//div[@class='components-panel']/div/h2/button)[5]")
        elements.click()
        count = count+1

    #searching category
    time.sleep(2)
    elements = wd.find_element_by_xpath("//input[@class='editor-post-taxonomies__hierarchical-terms-filter']")
    elements.send_keys(str(data[4]))

    #selecting that category
    time.sleep(2)
    input_tag = "//div[@class='components-panel']/div/div/div/div/div/span/input"
    elements = wd.find_element_by_xpath(input_tag)
    elements.click()

    if(count == 3):
        time.sleep(2)
        elements=wd.find_element_by_xpath("(//div[@class='components-panel']/div/h2/button)[6]")
        elements.click()
        count = count+1

    #for inserting tags
    time.sleep(2)
    for tag in data[3]:
        elements = wd.find_element_by_xpath("//input[@class='components-form-token-field__input']")
        elements.send_keys(str(tag))
        elements.send_keys(Keys.ENTER)
    
    time.sleep(3)
    elements=wd.find_element_by_xpath("(//button[@class='components-button has-icon'])[3]")
    elements.click()

    time.sleep(2)
    elements = wd.find_element_by_xpath("//tags[@class='tagify  ']/span")
    elements.send_keys(str(data[0]))
    elements.send_keys(Keys.ENTER)

    # #click on edit snippet
    # time.sleep(3)
    # elements = wd.find_element_by_xpath("//button[@class='components-button rank-math-edit-snippet is-primary']")
    # wd.execute_script("arguments[0].click();", elements)
    
    # time.sleep(2)
    # description = description()
    # elements = wd.find_element_by_xpath("//textarea[@class='components-textarea-control__input css-1l8z26q-StyledTextarea-inputStyleNeutral-inputStyleFocus-inputControl ebk7yr50']")
    # elements.send_keys(str(description))

    # time.sleep(2)
    # elements = wd.find_element_by_xpath("//div[@class='components-modal__content']/div/button")
    # elements.click()

    time.sleep(2)
    elements = wd.find_element_by_xpath("//button[@class='components-button is-pressed has-icon']")
    elements.click()
    
    

    #save 
    time.sleep(2)
    elements = wd.find_element_by_xpath("(//div[@class='edit-post-header__settings']/button)[1]")
    elements.click()
    time.sleep(5)

    elements = wd.find_element_by_xpath("(//div[@class='edit-post-header__settings']/div/button)[2]")
    elements.click()

    #seo score
    element = wd.find_element_by_xpath("//div[@class='score-text']")
    score = element.get_attribute('innerText')[:2]
    score = int(score)
    
    print(score)
    #pubish
    if(score>30):
        time.sleep(3)
        elements = wd.find_element_by_xpath("//button[@class='components-button editor-post-publish-panel__toggle editor-post-publish-button__button is-primary']")
        elements.click()

        time.sleep(3)
        elements = wd.find_element_by_xpath("//button[@class='components-button editor-post-publish-button editor-post-publish-button__button is-primary']")
        elements.click()

        time.sleep(3)
        elements = wd.find_element_by_xpath("(//button[@class='components-button has-icon'])[6]")
        elements.click()  
    
    time.sleep(3)
    elements = wd.find_element_by_xpath("//a[@class='components-button edit-post-fullscreen-mode-close has-icon']")
    elements.click()
    
    time.sleep(4)
    elements = wd.find_element_by_xpath("//a[@class='wp-first-item wp-has-submenu wp-not-current-submenu menu-top menu-top-first menu-icon-dashboard menu-top-last']")
    elements.click()

wd.close()