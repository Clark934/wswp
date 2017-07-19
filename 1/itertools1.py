# -*- coding: utf-8 -*-

import itertools
from download import download
def iteration():
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-%d' %page
        html = download(url)
        if html is None:
            break
        else:
            pass

if __name__ == '__main__':
    iteration()
