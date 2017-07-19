# -*- coding: utf-8 -*-

import urllib2
import re


def scrape1(html):
    area = re.findall('<td class="w2p_fw">(.*?)</td>',html)
    return area

def scrape2(html):
    area = re.findall('<td class="w2p_fw">(.*?)</td>',html)[1]
    return area

def scrape3(html):
    area = re.findall('<tr id="places_area__row"><td class="w2p_fl"><label for="places_area" id="places_area__label">Area: </label></td><td class="w2p_fw">(.*?)</td>',html)
    return area


def scrape4(html):
    area = re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)[0]
    return area


if __name__ == '__main__':
    html = urllib2.urlopen('http://example.webscraping.com/places/default/view/United-Kingdom-239').read()
    scrape = scrape4
    print scrape(html)
