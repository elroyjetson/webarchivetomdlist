#!/usr/bin/env python3

# Use to parse meta info from Safari Webarchive files

# find . -name "*.webarchive" -mtime -1d -exec ./test.py {} >> ril.md \;
# Create a crontab or systemd entry
# set path to the script and the reading list
# set the time to include so that you only get new items
# -mtime uses the following codes
# s       second
# m       minute (60 seconds)
# h       hour (60 minutes)
# d       day (24 hours)
# w       week (7 days)

import plistlib, sys
from bs4 import BeautifulSoup

file = sys.argv[1]

with open(file, 'rb') as fp:
    pl = plistlib.load(fp)

url = pl["WebMainResource"]["WebResourceURL"]
html_doc = pl["WebMainResource"]["WebResourceData"]

soup = BeautifulSoup(html_doc, 'html.parser')

title = soup.title.string

print("- [ ] [{}]({})".format(title, url))