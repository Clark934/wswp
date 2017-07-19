# -*- coding: utf-8 -*-

import itertools
from download import download


def iteration():
    max_errors = 5
    num_errors = 0
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-%d' % page
        html = download(url)
        if html is None:
            num_errors += 1
            if max_errors == num_errors:
                break
        else:
            num_errors = 0


if __name__ == '__main__':
    iteration()
