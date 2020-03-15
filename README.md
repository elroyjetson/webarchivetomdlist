# webarchivetomdlist
Parses webarchive binary plist and MHTML files to create a markdown checklist index.

This is simply a proof of concept so that I can save web pages offline in a single file archive, generate a checklist in markdown to index each file.

The parsing of a single file archive can be done on Linux/Windows/MacOS using Chromium based browser by saving as a Webpage, Single File.  This creates an archive with all assets as an [MTHML](https://en.wikipedia.org/wiki/MHTML) file which is a multi-part mime file similar to an email message.

Usage: mhtml.py <archive name>

After completion, a new line will be added to the ril.md file with the title and original url for the archive.


Safari on MacOS uses the [webarchive binary plist](https://en.wikipedia.org/wiki/Webarchive) file format to save webpages offline.

Usage: webarchive.py <archive name>

After completion, a new line will be added to the ril.md file with the title and original url for the archive.


It is best to run this as a cron batch or systemd service with find in order to update the reading list from time to time.  

Add the following find command changing the -mtime and location of the parser and ril.md list as appropriate.

```
find . -name "*.mhtml" -mtime -1d -exec ./mhtml.py {} >> ril.md \;

-mtime uses the following codes for times

s       second
m       minute (60 seconds)
h       hour (60 minutes)
d       day (24 hours)
w       week (7 days)
```
