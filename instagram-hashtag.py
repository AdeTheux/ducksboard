#!/usr/bin/env python

__author__      = "Arnaud de Theux"
__web__         = "http://arnaud.detheux.org"
__twitter__     = "@AdeTheux"

"""This is a python script that reads an Instagram hastag feed, parses it and randomly extracts a picture's URL. This URL is then sent to Ducksboard via an image widget. We update this script every hour via a cron tab."""

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
randomimg = random.randint(1,100)
dom = parseString(s)
xmlTag = dom.getElementsByTagName('link')[randomimg].toxml()
xmlDataName=xmlTag.replace('<link>','').replace('</link>','')

#Send the link to the Ducksboard
command = "curl -u API_KEY:ignored -d '{\"value\": {\"source\": \"%s\"}}' https://push.ducksboard.com/values/ENDPOINT_ID/ " % xmlDataName
print command
os.system(command)