#!/usr/bin/env python
#
# This script goes to the website https://www.tug.org/texlive/debian.html and 
# get the latest debian control file into debian-control-texlive-in.txt
# To use it:
# ```
#   equivs-build debian-control-texlive-in.txt
#   dpkg -i texlive-local_<version>_all.deb
# ```

import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.tug.org/texlive/debian.html")
soup = BeautifulSoup(req.text, 'lxml')

links = ["https://www.tug.org/texlive/{}".format(s['href']) \
    for s in soup.find_all('a') if s['href'].find('files/debian-equivs') > -1]

open('debian-control-texlive-in.txt', 'w').write(requests.get(sorted(links)[-1]).text)
