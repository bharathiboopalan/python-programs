# Web spider

from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse

class LinkExtractor(HTMLParser):
	# override handle_starttag of HTMLParser to extract <a> tags from html
	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for (key, value) in attrs:
				if key == 'href':
					newUrl = parse.urljoin(self.baseUrl, value)
					# store extracted link
					self.links = self.links + [newUrl]

	# extract links from a url
	def extractLinks(self, url):
		self.links = []
		self.baseUrl = url
		response = urlopen(url)
		# Only parse html pages
		if response.getheader('Content-Type')=='text/html':
			htmlBytes = response.read()
			htmlString = htmlBytes.decode("utf-8")
			self.feed(htmlString)
			return htmlString, self.links
		else:
			return "",[]

def spider(url, word, maxPages):
	urls = [url]
	numVisits = 0
	while numVisits < maxPages and urls != []:
		numVisits = numVisits +1
		url = urls[0]
		urls = urls[1:]
		try:
			print(numVisits, "Visiting:", url)
			parser = LinkExtractor()
			data, links = parser.extractLinks(url)
			urls = urls + links
		except:
			print("Link extraction failed")

