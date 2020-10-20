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

    #####
    ##  Task 2 : JPL Mars Space Imgs
    #####

    #####
    ##  Task 3 : Mars Facts
    #####

    #####
    ##  Task 4 : Mars Hemispheres
    #####
