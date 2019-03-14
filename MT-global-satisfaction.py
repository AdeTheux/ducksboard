#!/usr/bin/env python

"""Fetches the satisfaction score of Zendesk spokes and gathers it in one spot. Then uses the Ducksboard API to display it on pins."""

__author__      = "Arnaud de Theux"
__web__      = "http://arnaud.detheux.org"
__twitter__      = "@AdeTheux"

from urllib import urlopen
import urllib
import sys
import os

#spoke online
good = 0
bad  = 0

data = urlopen("https://mtonline.zendesk.com/satisfaction.json").readlines()[0]
good = data.count('1')
bad  = data.count('0')

#spoke wholesale
good1 = 0
bad1  = 0

data = urlopen("https://mtwhl.zendesk.com/satisfaction.json").readlines()[0]
good1 = data.count('1')
bad1  = data.count('0')

#spoke servicedesk
good2 = 0
bad2  = 0

data = urlopen("https://mtservicedesk.zendesk.com/satisfaction.json").readlines()[0]
good2 = data.count('1')
bad2  = data.count('0')

#spoke telenet
good3 = 0
bad3  = 0

data = urlopen("https://mttelenet.zendesk.com/satisfaction.json").readlines()[0]
good3 = data.count('1')
bad3  = data.count('0')

#spoke virgin
good4 = 0
bad4  = 0

data = urlopen("https://mtvirgin.zendesk.com/satisfaction.json").readlines()[0]
good4 = data.count('1')
bad4  = data.count('0')

#spoke trial
good5 = 0
bad5  = 0

data = urlopen("https://mttrial.zendesk.com/satisfaction.json").readlines()[0]
good5 = data.count('1')
bad5  = data.count('0')


#addition
sum_good = good + good1 + good2 + good3 + good4 + good5
sum_bad = bad + bad1 + bad2 + bad3 + bad4 + bad5

#ducksboard API
command = "curl -u TOKEN:ignored -d '{\"value\": %d}' https://push.ducksboard.com/values/44214/" % sum_good
command2 = "curl -u TOKEN:ignored -d '{\"value\": %d}' https://push.ducksboard.com/values/44215/" % sum_bad

print command
os.system(command)
print command2
os.system(command2)