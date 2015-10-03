python gen-source-wiki.py > ../sources/zenoss-wiki.json
DATE=`date +"%Y-%m-%d %H:%M:%S"`
sed -i -e "s/Updated on .*\./Updated on $DATE./g" ../index.html
