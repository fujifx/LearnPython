import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

'''
** What is Web Scraping **
> When a program or script pretends to be a browser and retrieves web pages,
look at those web pages, extract information, and then looks at more web pages.
> Search engines scrape web pages - we call this "spidering web" or "web crawling"

** Why Scrape? **
> Pull data - particularly social data - who links to who?
> Get your own data back out of some systems that has no "export capability"
> Monitor a site for new information
> Spider the web to make a database for search engine

** Scraping Web Pages
> There is some controversy about web page scraping and some sites are bit snippy about it
> Republishing copyrighted information is not allowed
> Violating terms of service is not allowed

Install the below package
pip install beautifulsoup4
'''

url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')   # 'html' variable gonna be in bytes/ UTF-8, but BeautifulSoup intelligently
                                            # parses (by dealing with all imperfections and inconsistencies in the HTML byte array)
                                            # provides an object. Check out the doc for more details

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))