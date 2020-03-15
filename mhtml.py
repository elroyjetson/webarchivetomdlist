#!/usr/bin/env python3

# Use to parse meta info from Chrome/Chromium mhtml files

# find . -name "*.mhtml" -mtime -1d -exec ./mhtml.py {} >> ril.md \;
# Create a crontab or systemd entry
# set path to the script and the reading list
# set the time to include so that you only get new items
# -mtime uses the following codes
# s       second
# m       minute (60 seconds)
# h       hour (60 minutes)
# d       day (24 hours)
# w       week (7 days)

import sys

file = sys.argv[1]

with open(file) as fp:
    head = [next(fp) for x in range(3)]

title = head[2].split(": ")[1]
url = head[1].split(": ")[1]

print("- [ ] [{}]({})".format(title.strip(), url.strip()))