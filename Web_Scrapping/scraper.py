# import urllib to work with URLs
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    # the __init__ method uses a website to extract as a parameter
    def __init__(self, site):
        self.site = site
    # the scraper class has a method called scrape that you can
    #  whenever to retrieve data from any passed site

    # the urlopen() function sends a request to a website and returns
    #  a response object in which its HTML code is stored, along with
    #   additional data. The response of the function. read () returns
    #   the HTML of the Response object. All the HTML for the website is
    #   in the html variable.

    # Add code in the scrape function which creates a BeautifulSoup object,
    #  and pass the html variable and the 'html.parser' string as a parameter
    # the BeautifulSoup object does all the hard work and parses the HTML.
    #  can now add code to the scrape function that calls the find_all method
    #   on the BeautifulSoup object.
    # Pass 'a' as the parameter and the method will return all the URLs the
    #  website is linked to in the HTML code downloaded.
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all('a'):
            url = tag.get('href')
            if url is None:
                continue
            if 'articles' in url:
                print('\n' + url)

    # the find_all method returns an iterable containing the tag objects found.
    #  each time around the for loop, the variable receives the value of a new
    #   Tag object. Each Tag object has many different instance variables, but I
    #    just want the value of the href instance variable, which contains each URL.
    # this can be retrieved by calling the get method and passing 'href' as a parameter.
    # Finally, verify that the URL variable contains data; that it contains the string
    #  'articles' (don't want to print internal links); and if so, print it.

news = 'https://news.google.com/'
Scraper(news).scrape()


