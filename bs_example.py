# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

def scrape(html):
    soup = BeautifulSoup(html,"lxml")
    tr = soup.find(attrs={'id':'places_area__row'}) # locate the area row
    # 'class' is a special python attribute so instead 'class_' is used
    td = tr.find(attrs={'class':'w2p_fw'})  # locate the area tag
    area = td.text  # extract the area contents from this tag
    return area

if __name__ == '__main__':
    html = urllib2.urlopen('http://example.webscraping.com/places/default/view/United-Kingdom-239').read()
    print scrape(html)
