from lxml import html
from lxml import xml
import requests
import re

def main():
	page = requests.get('https://en.wiktionary.org/wiki/Category:en:Parts_of_speech')
	tree = html.fromstring(page.content)

	divs = tree.xpath('//div[@class="mw-category-group"]/ul/li/span')

	for x in divs:
		if x.text != None and not re.match(r'^[_\W]+$', x.text):
			print(x.text)

main()
