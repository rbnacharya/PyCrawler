from elasticsearch import Elasticsearch

class ecConnect:
	def __init__(self):
		self.es=Elasticsearch([{"host":"localhost"}])

	def connect(self):
		#todo
	def addPage(self,data):
		# write data to es
	def addLinks(self,urls):
		#todo
	def isCrawled(self,url):
		#todo
	def close(self):
		#todo
		