
# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)

def scrape_all():
    
    # Initiate headless driver for deployment
    browser = Browser('chrome', executable_path='chromedriver', headless=True)
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary.
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
        }
    browser.quit()
    return data

def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    # Convert the browser html to a soup object then quit the browser.
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    
    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
         # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None
    return news_title, news_p
    

# Featured Images
def featured_image(browser):

    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    # Parse the resulting html with BeautifulSoup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    # Find the relative image url
    img_url_rel = img_soup.select_one('figure.lede a img').get('src')
    img_url_rel
    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    return img_url

def mars_facts():
    
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None
    
    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())

# Challenge
# Collect Information of the Mars Hemispheres ~ All Hemisphere Images.
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

def hemispheres(browser):
    
    # The URL where we are looking for the 4 hemisphere images of Mars.
    url = (
        "https://astrogeology.usgs.gov/search/"
        "results?q=hemisphere+enhanced&k1=target&v1=Mars"
    )
    browser.visit(url)
    
    # Loop through the images on the site, click the link, look for the css element, 
    # return the image link for each image.
    hemisphere_image_urls = []
    for i in range(4):
        # Find the css element in the loop
        browser.find_by_css("a.product-item h3")[i].click()
        hemi_data = scrape_hemisphere(browser.html)
        # Append hemisphere image to a list
        hemisphere_image_urls.append(hemi_data)
        # Go back until loop finishes
        browser.back()
    return hemisphere_image_urls

def scrape_hemisphere(html_text):
    
    # Using BeautifulSoup, parse html text
    hemi_soup = BeautifulSoup(html_text, "html.parser")
    # add try/except to account for any errors
    try:
        title_elem = hemi_soup.find("h2", class_="title").get_text()
        sample_elem = hemi_soup.find("a", text="Sample").get("href")
    except AttributeError:
        # Image error will return None, to indicate there is either no image or no title for an image URL.
        title_elem = None
        sample_elem = None
    # Put image URL and text into a dictionary.
    hemispheres = {
        "title": title_elem,
        "img_url": sample_elem
    }
    return hemispheres

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())



