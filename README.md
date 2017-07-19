# Web Scraping with Python
===========================

一边学习《用Python写网络爬虫》一书，一边对于书中因为事例网站的变化而导致的bug进行修复。

****
### Author:Siyao Chen
### E-mail:siyao.chen92@gmail.com
****
The first bug comes from the websites update.The url input of the 'link_crawler' should be as follows.
`link_crawler('http://example.webscraping.com/places', '/places/default/(index|view)', delay=0, num_retries=1,
              user_agent='BadCrawler')`


This repository contains source code of examples from the book *Web Scraping with Python*, published by Packt Publishing. 
Examples have been tested with Python 2.7 and depend on: 

 * [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) (Ch 2)
 * [lxml](http://lxml.de/) (Ch 2-9)
 * [pymongo](http://api.mongodb.org/python/current/) (Ch 3-5, 9)
 * [PyQt](http://www.riverbankcomputing.co.uk/software/pyqt/intro) / [PySide](https://pypi.python.org/pypi/PySide) (Ch 5)
 * [ghost](http://jeanphix.me/Ghost.py/) (Ch 5)
 * [Selenium WebDriver](http://www.seleniumhq.org/projects/webdriver/) (Ch 5, 9)
 * [mechanize](http://wwwsearch.sourceforge.net/mechanize/) (Ch 6)
 * [PIL](http://www.pythonware.com/products/pil/) / [Pillow](https://python-pillow.github.io/) (Ch 7)
 * [pytesseract](https://github.com/madmaze/pytesseract) (Ch 7)
 * [scrapy](http://scrapy.org/) (Ch 8)
 * [portia](https://github.com/scrapinghub/portia) (Ch 8)
 * [scrapely](https://github.com/scrapy/scrapely) (Ch 8)

This examples will break in future as websites change and dependencies are updated, so [bug reports and patches](https://bitbucket.org/wswp/code/issues?status=new&status=open) are welcome.
