

# Web-Scraping-to-HTML-with-Database
This program uses Web Scraping with Jupyter Notebooks, MongoDB, PyMongo, Flask, and Splinters - all in order to render data on a dashboard and store it in a MongoDB database.

![alt text](https://github.com/riggiobill/Web-Scraping-to-HTML-with-Database/blob/main/Screenshots/App%20Screenshot%201.png?raw=true)

![alt text](https://github.com/riggiobill/Web-Scraping-to-HTML-with-Database/blob/main/Screenshots/App%20Screenshot%202.png?raw=true)



To perform this task, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines the steps required.



## Step 1 - Scraping

* Scraped data for the application using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Created a Jupyter Notebook file called `mission_to_mars.ipynb` and used this to complete all scraping and analysis tasks. The following outlines what data needed to be scraped.


### NASA Mars News

* Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text. Assigned the text to variables that can be referenced later.



### JPL Mars Space Images - Featured Image

* Visited the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable called `featured_image_url`.

* Made sure to find the image url to the full size `.jpg` image.

* Made sure to save a complete url string for this image.



### Mars Facts

* Visited the Mars Facts webpage [here](https://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string.
 

### Mars Hemispheres

* Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* Found the image urls to the full resolution image.

* Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.


- - -

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Converted Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all scraping code from above and return one Python dictionary containing all of the scraped data.

* Created a route called `/scrape` that will import `scrape_mars.py` script and call `scrape` function.

  * Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` that will query Mongo database and pass the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements.

- - -

### Copyright

Trilogy Education Services © 2020. All Rights Reserved.
