from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser

#####
## Create a function to link the browser and chromedriver and open the browser as a variable object
## This allows the browser object to be accessed later
#####

def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome",**executable_path, headless=False)


#####
## The scrape() function.
#####

def scrape():
    browser = init_browser()


    #####
    ## Initializes the dictionary to store data in
    #####

    mars_dict = {}


    #####
    ##  Task 1 : NASA Mars News
    ##  Using code from mission_to_mars.ipynb, populate the dictionary
    #####
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news = soup.find("div", class_="list_text")
    news_paragraph = news.find("div", class_="article_teaser_body").text
    news_title = news.find("div",class_="content_title").text

    mars_dict["mars_news_title"] = news_title
    mars_dict["mars_news_paragraph"] = news_paragraph
    #--------------------------------------------------------------------------------------------

    #####
    ##  Task 2 : JPL Mars Space Imgs
    ##  Using code from mission_to_mars.ipynb, populate the dictionary
    #####
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Find first featured Mars image
    image = soup.find("img",class_="thumb")["src"]

    # Find image url to full size .jpg image and append to initial url
    image_url = "https://jpl.nasa.gov"+image
    featured_image_url = image_url

    mars_dict["featured_image_url"] = featured_image_url
    #--------------------------------------------------------------------------------------------

    #####
    ##  Task 3 : Mars Facts
    ##  Using code from mission_to_mars.ipynb, populate the dictionary
    #####

    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    facts_pd = pd.read_html(facts_url)
    facts_df = pd.DataFrame(facts_pd[0])

    facts_df.columns=['Attribute','Data']

    # Use Pandas to convert the data into an HTML table string using Pandas .to_html and .replace
    facts_table = facts_df.set_index("Attribute")
    mars_facts = facts_table.to_html(classes = 'mars_facts')
    mars_facts = mars_facts.replace('\n', ' ')

    mars_dict["html_table_string"] mars_facts
    #--------------------------------------------------------------------------------------------

    #####
    ##  Task 4 : Mars Hemispheres
    ##  Using code from mission_to_mars.ipynb, populate the dictionary
    #####

    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemispheres = []

    for x in range (4):
        image_array = browser.find_by_tag('h3')
        image_array[x].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        src = soup.find("img", class_="wide-image")["src"]
        x_url = 'https://astrogeology.usgs.gov'+src
        x_title = soup.find("h2", class_="title").text
        hemi_dict = {"title":x_title,"img url":x_url}
        hemispheres.append(hemi_dict)
        browser.back()

    mars_dict["Mars_img_dict"] = hemispheres
    #--------------------------------------------------------------------------------------------

    # Return mars_dict with all scraped information
    return mars_dict