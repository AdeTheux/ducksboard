#!/usr/bin/env python

__author__      = "Arnaud de Theux"
__web__ = "http://arnaud.detheux.org"
__twitter__     = "@AdeTheux"

"""This is a python script that  fetches the 10 top tags from your Zendesk account and send them to 2 Ducksboard custom bars graphs. You need to run this script in a cron tab so that it updates the tags from time to time."""

import sys
import os
import random
import httplib2
from xml.dom.minidom import parseStringfrom
from urllib import urlopen
import urllib
from xml.dom.minidom import parseString
import re

###Settings. Replace with your own Zendesk credentials and URL. If you don't use the API token (baaad) just put your password and remove the "/token" part
user           = 'EMAIL/token'
password       = 'TOKEN'
zendesk        = 'http://servicedesk.mondialtelecom.eu/'


###Fetches the tags file
h= httplib2.Http(".cache")
h.add_credentials(user, password)
resp, content = h.request(zendesk+"tags.xml", "GET", headers={'content-type' : 'application/xml'} )
f = urllib.urlopen(zendesk+"tags.xml")
s = f.read()
f.close()

#Displays the top 10 tags (You need to replace [1] by [0] and increment accordingly below. I start from line 1 because I don't want the first tag to be displayed.
#1
dom = parseString(s)
xmlTag = dom.getElementsByTagName('name')[1].toxml()
xmlDataName=xmlTag.replace('<name>','').replace('</name>','')

dom = parseString(s)
xmlTag = dom.getElementsByTagName('count')[1].toxml()
xmlDataTag=xmlTag.replace('<count>','').replace('</count>','')
#2
dom = parseString(s)
xmlTag = dom.getElementsByTagName('name')[2].toxml()
xmlDataName1=xmlTag.replace('<name>','').replace('</name>','')

dom = parseString(s)
xmlTag = dom.getElementsByTagName('count')[2].toxml()
xmlDataTag1=xmlTag.replace('<count>','').replace('</count>','')
#3
dom = parseString(s)
xmlTag = dom.getElementsByTagName('name')[3].toxml()
xmlDataName2=xmlTag.replace('<name>','').replace('</name>','')

dom = parseString(s)
xmlTag = dom.getElementsByTagName('count')[3].toxml()
xmlDataTag2=xmlTag.replace('<count>','').replace('</count>','')
#4
dom = parseString(s)
xmlTag = dom.getElementsByTagName('name')[4].toxml()
xmlDataName3=xmlTag.replace('<name>','').replace('</name>','')

dom = parseString(s)
xmlTag = dom.getElementsByTagName('count')[4].toxml()
xmlDataTag3=xmlTag.replace('<count>','').replace('</count>','')
#5
dom = parseString(s)
xmlTag = dom.getElementsByTagName('name')[5].toxml()
xmlDataName4=xmlTag.replace('<name>','').replace('</name>','')

dom = parseString(s)
xmlTag = dom.getElementsByTagName('count')[5].toxml()
xmlDataTag4=xmlTag.replace('<count>','').replace('</count>','')
#6
dom = parseString(s)
xmlTag = dom.getElementsByTagName('name')[6].toxml()
xmlDataName5=xmlTag.replace('<name>','').replace('</name>','')

dom = parseString(s)
xmlTag = dom.getElementsByTagName('count')[6].toxml()
xmlDataTag5=xmlTag.replace('<count>','').replace('</count>','')
#7
dom = parseString(s)
xmlTag = dom.getElementsByTagName('name')[7].toxml()
xmlDataName6=xmlTag.replace('<name>','').replace('</name>','')

dom = parseString(s)
xmlTag = dom.getElementsByTagName('count')[7].toxml()
xmlDataTag6=xmlTag.replace('<count>','').replace('</count>','')
#8
dom = parseString(s)
xmlTag = dom.getElementsByTagName('name')[8].toxml()
xmlDataName7=xmlTag.replace('<name>','').replace('</name>','')

dom = parseString(s)
xmlTag = dom.getElementsByTagName('count')[8].toxml()
xmlDataTag7=xmlTag.replace('<count>','').replace('</count>','')
#9
dom = parseString(s)
xmlTag = dom.getElementsByTagName('name')[9].toxml()
xmlDataName8=xmlTag.replace('<name>','').replace('</name>','')

dom = parseString(s)
xmlTag = dom.getElementsByTagName('count')[9].toxml()
xmlDataTag8=xmlTag.replace('<count>','').replace('</count>','')
#10
dom = parseString(s)
xmlTag = dom.getElementsByTagName('name')[10].toxml()
xmlDataName9=xmlTag.replace('<name>','').replace('</name>','')

dom = parseString(s)
xmlTag = dom.getElementsByTagName('count')[10].toxml()
xmlDataTag9=xmlTag.replace('<count>','').replace('</count>','')



###Display the ouput on Ducksboard 5 bars
command = "curl -u API_KEY:ignored -d '{\"value\":  %s}' https://push.ducksboard.com/values/ENDPOINT_ID/ " % xmlDataTag
command1 = "curl -u API_KEY:ignored -d '{\"value\":  %s}' https://push.ducksboard.com/values/ENDPOINT_ID/ " % xmlDataTag1
command2 = "curl -u API_KEY:ignored -d '{\"value\":  %s}' https://push.ducksboard.com/values/ENDPOINT_ID/ " % xmlDataTag2
command3 = "curl -u API_KEY:ignored -d '{\"value\":  %s}' https://push.ducksboard.com/values/ENDPOINT_ID/ " % xmlDataTag3
command4 = "curl -u API_KEY:ignored -d '{\"value\":  %s}' https://push.ducksboard.com/values/ENDPOINT_ID/ " % xmlDataTag4
command5 = "curl -u API_KEY:ignored -d '{\"value\":  %s}' https://push.ducksboard.com/values/ENDPOINT_ID/ " % xmlDataTag5
command6 = "curl -u API_KEY:ignored -d '{\"value\":  %s}' https://push.ducksboard.com/values/ENDPOINT_ID/ " % xmlDataTag6
command7 = "curl -u API_KEY:ignored -d '{\"value\":  %s}' https://push.ducksboard.com/values/ENDPOINT_ID/ " % xmlDataTag7
command8 = "curl -u API_KEY:ignored -d '{\"value\":  %s}' https://push.ducksboard.com/values/ENDPOINT_ID/ " % xmlDataTag8
command9 = "curl -u API_KEY:ignored -d '{\"value\":  %s}' https://push.ducksboard.com/values/ENDPOINT_ID/ " % xmlDataTag9
print command
print command1
print command2
print command3
print command4
print command5
print command6
print command7
print command8
print command9
os.system(command)
os.system(command1)
os.system(command2)
os.system(command3)
os.system(command4)
os.system(command5)
os.system(command6)
os.system(command7)
os.system(command8)
os.system(command9)