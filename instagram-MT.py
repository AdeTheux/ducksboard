#!/usr/bin/env python

__author__      = "Arnaud de Theux"
__web__         = "http://arnaud.detheux.org"
__twitter__     = "@AdeTheux"

"""This is a python script that reads an Instagram hashtag feed, parses it and randomly extracts a picture's URL. This URL is then sent to Ducksboard via an image widget. We update this script every hour via a cron tab."""

import urllib
import random
from xml.dom.minidom import parseString
import sys
import os



###Fetches the Instagram RSS
f = urllib.urlopen("http://instagr.am/tags/mondialtelecom/feed/recent.rss")
s = f.read()
f.close()

#Finds the link of the image and strips the unnecessary junk
randomimg = random.randint(1,40)
dom = parseString(s)
xmlTag = dom.getElementsByTagName('link')[randomimg].toxml()
xmlDataName=xmlTag.replace('<link>','').replace('</link>','')

randomimg1 = random.randint(1,40)
dom = parseString(s)
xmlTag1 = dom.getElementsByTagName('link')[randomimg1].toxml()
xmlDataName1=xmlTag1.replace('<link>','').replace('</link>','')

randomimg2 = random.randint(1,40)
dom = parseString(s)
xmlTag2 = dom.getElementsByTagName('link')[randomimg2].toxml()
xmlDataName2=xmlTag2.replace('<link>','').replace('</link>','')

#Send the link to the Ducksboard
command = "curl -u TOKEN:ignored -d '{\"value\": {\"source\": \"%s\"}}' https://push.ducksboard.com/values/72863/ " % xmlDataName
command1 = "curl -u TOKEN:ignored -d '{\"value\": {\"source\": \"%s\"}}' https://push.ducksboard.com/values/72864/ " % xmlDataName1
command2 = "curl -u TOKEN:ignored -d '{\"value\": {\"source\": \"%s\"}}' https://push.ducksboard.com/values/72865/ " % xmlDataName2

print command
print command1
print command2
os.system(command)
os.system(command1)
os.system(command2)