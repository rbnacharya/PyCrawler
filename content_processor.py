from multiprocessing import Pool
import re, sys, logging, string
import constants
from datetime import date

from ready_queue import ready_queue

logger = logging.getLogger("crawler_logger")



def stripPunctuation(text):
	pattern = re.compile(r'[^\w\s]')
	return pattern.sub(' ', text)

def stripScript(text):
	pattern = re.compile(r'<script.*?\/script>')
	return pattern.sub(' ', text)

class ContentProcessor:
	
	def __init__(self, url, status, text):
		self.links = {}
		self.text = text
		self.size = 0
		self.url = url
		self.status = status

	def setText(self, text):
		self.text = text
		self.size = len(text)

	def setUrl(self, url):
		self.url = url

	def setStatus(self, status):
		self.status = status

	def setInfo(self, url, status, text):
		self.url = url
		self.status = status
		self.text = text
		self.size = len(text)

	def reset(self):
		self.links = {}
		self.text = None
		self.head = None
		self.body = None
		self.title = None
		self.size = 0
		self.status = None

	
	
	def remove_html_tags(self, data):
		p = re.compile(r'<.*?>')
		return p.sub('', data)

	def findnth(self, haystack, needle, n):
		parts = haystack.split(needle, n)
		if len(parts) <= n:
			return -1
		return len(haystack)-len(parts[-1])-len(needle)

	# returns the queue from processBody
	def process(self):
		text_lower = self.text.lower()
		self.title = self.text[text_lower.find('<title')+6:text_lower.find('</title>')]
		self.head = self.text[text_lower.find('<head')+5:text_lower.find('</head>')]
		self.body = self.text[text_lower.find('<body'):text_lower.find('</body>')]
		self.text = stripPunctuation(self.remove_html_tags(stripScript(self.body)))

		self.links=ready_queue(self.url, self.body)
		return self.links

	
	def getDataDict(self):
		todayDate=date.today()
		return {constants.LINK:self.url,constants.STATUS:self.status,constants.TITLE:self.title,
		constants.BODY:self.text,constants.SIZE:self.size,constants.LINKSTO:self.links,
		constants.VISITEDON :todayDate}
	
