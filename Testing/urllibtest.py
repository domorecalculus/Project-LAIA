#!/usr/bin/env python3


from urllib.request import *

website = urlopen('https://en.wiktionary.org/wiki/arborescent')

print(website.read().decode('utf-8'))
