__author__ = 'rakesh'

import requests
import lxml.html
import urllib
import urlparse
import json
from bs4 import BeautifulSoup

websiteData = {}  #This will be your json data

def extractLinks(url, base):
        '''
        Return links from the website
        :param url: Pass the url
        :param base: this is the base links
        :return: list of links
        '''
        links = [] #it will contain all the links from the website
        try:
            r = requests.get(url)
        except:
            return []
        obj = lxml.html.fromstring(r.text)
        potential_links = obj.xpath("//a/@href")
        links.append(r.url)
        #print potential_links
        for link in potential_links:
            if base in link:
                links.append(link)
            else:
                if link.startswith("http"):
                    links.append(link)

                elif base.endswith("/"):
                    if link.startswith("/"):
                        link = link.lstrip("/")
                        link = base + link
                    else:
                        link = base + link
                    links.append(link)

        return links

def createJson(url):
    '''
    Creating a json object here
    :param url: url from where you want to extract the data
    :return:
    '''
    data = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    letters = soup.find_all('td')
    companyName = letters[1].get_text()  #Company name
    for i in range(len(letters)-1):
        if i % 2 == 0:
            data[letters[i].get_text()] = letters[i+1].get_text()  #creating a dictionary
    websiteData[companyName] = data

def url_fix(s, charset='utf-8'):
    """
    this program is basically to normalize the url since some url contain spaces, comma between them.
    :param s: string of your link
    :param charset:
    :return: normalized link
    """
    if isinstance(s, unicode):
        s = s.encode(charset, 'ignore')
    scheme, netloc, path, qs, anchor = urlparse.urlsplit(s)
    path = urllib.quote(path, '/%')
    qs = urllib.quote_plus(qs, ':&=')
    return urlparse.urlunsplit((scheme, netloc, path, qs, anchor))

def websitePage(website, base):
    '''
    Visiting each page of the website and trying to extract those links and text
    :param website: website url link
    :param base: base of the website will remain constant
    :return:
    '''
    extractedLinks = extractLinks(website, base)
    for line in extractedLinks:
        if 'page' in line.rsplit('/')[-1] or len(line.rsplit('/')[-1]) == 0 or line.rsplit('/')[-1] == '#' or 'companies' in line.rsplit('/')[-1]:
            pass
        else:
            createJson(url_fix(line))

def main():
    '''
    Go over each links in the website and create a JSON file for address. Check out solution.json file
    :return:
    '''
    website = 'http://data-interview.enigmalabs.org/companies/'
    base = 'http://data-interview.enigmalabs.org/'
    for i in range(1, 11):
        if i == 1:
            websitePage(website, base)
        else:
            websitePage(website + '?page={}'.format(i), base)

if __name__ == '__main__':
    main()
    print json.dumps(websiteData)  #json encoding
