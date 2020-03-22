# Mission_to_Mars
Web scrape information about Mars for analysis and create an app to display analysis.

# Project Overview
Using web scraping to gather the latest data about the planet Mars by pulling data from multiple websites, storing it in a database then presenting the collected data on a webpage.


## Objective

Created several files which were all used to create the web page for visualization of the results:

	- In Jupyter Notebook, create a dataframe to hold a table of facts about the planet Mars.
	
	- In VS Code created an html file to identify the elements and classes to scrape.
	
	- In VS Code created a file execute the scraping of the websites selected.
	
	- In VS Code created a file using FLASK to create a web page with the results of the scraping.
	
Finally, create a portfoio.

Steps:

	1. Use Splinter and ChromeDriver to automate web scraping for Mars data by identifying the HTML tags, 
	using Chrome DevTools, to identify information we want to gather.
	
	2. Use BeautifulSoup to parse and extract the Mars data. 
	
	3. Use MongoBD to store data retrieved for easy access.
	
	4. Use Flask visualize scraping results.
	
	5. Create Portfolio
	
	- Selected one of the templates provided and customized the html and css files to create my own portfolio.
	
	
  Images:
  
  ![alt_text](https://github.com/Al-Huneidi/Mission_to_Mars/blob/master/screenshots/Portfolio_1.png)
  
  ![alt_text](https://github.com/Al-Huneidi/Mission_to_Mars/blob/master/screenshots/Portfolio_2.png)
  
  ![alt_text](https://github.com/Al-Huneidi/Mission_to_Mars/blob/master/screenshots/Portfolio_3.png)
  
  ![alt_text](https://github.com/Al-Huneidi/Mission_to_Mars/blob/master/screenshots/Portfolio_4.png)


Sites scraped:

	- https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

	- https://mars.nasa.gov/news/
	

# Challenge
Pull high-resolution images of Mars hemisphere and use DevTool to find the proper elements to scrape.  Update the Mongo database with the new data and later the design of the web app to accommodate these images.

## Objectives

	- Use BeautifulSoup and Splinter to automate a web browser and scrape hit-resolution images.

	- Use a MongoDB to store data from the web scrape.

	- Update the web application and Flask to display the data from the web scrape.

	- Use Bootstrap to style the web app.

