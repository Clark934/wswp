import urllib2
# -*- coding:utf-8 -*-
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()
