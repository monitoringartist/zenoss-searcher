#!/bin/bash

cd /tmp
wget https://github.com/monitoringartist/zenoss-searcher/archive/gh-pages.zip
unzip gh-pages.zip
cp -r zenoss-searcher-gh-pages/* /usr/share/nginx/html
rm -rf /tmp/*
nginx -g 'daemon off;'
