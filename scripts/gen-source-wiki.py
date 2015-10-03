#!/usr/bin/env python

from pyquery import PyQuery as pq
from lxml import etree
import urllib, json, ziconizing

arr = {}
d = pq(url='http://wiki.zenoss.org/All_ZenPacks')
for a in d('.smw-column li a'):

    name = a.text.strip() + ' ZenPack'
    url = 'http://wiki.zenoss.org' + a.get('href')
    arr[name.replace(' ','-')] = {
      'name': name,
      'url': url,
      'keywords': name.lower().replace(' ZenPack','').split(' '),
      'icon':  ziconizing.iconizing(name, name.lower().split(' '))
    }
print json.dumps(arr)

