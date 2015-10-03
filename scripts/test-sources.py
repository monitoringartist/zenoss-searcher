#!/usr/bin/env python

import os, sys, requests, json, re
files = [
  '../sources/zenoss-wiki.json',
]

ecode = 0

for file in files:    
    with open(file) as data_file:
        data = json.load(data_file)
        print '=== FILE: %s (%d projects) ===' % (file, len(data))
        if len(data) < 100:
            print 'Problem with parsing data for ' + file
            ecode = 1
        for id in data:
           try:
               s = requests.get(data[id]['url'])
               if s.status_code != 200:
                  print "File: %s, project %s" % (file, data[id]['name'])
                  print '  url - ' +  data[id]['url']
                  print '  ' + str(s)
                  ecode = 1

           except Exception as e:
               print "File: %s, project %s" % (file, data[id]['name'])
               print '  url - ' +  data[id]['url']
               print '  ' + str(e)
               ecode = 1

sys.exit(ecode)
