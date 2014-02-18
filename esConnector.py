from elasticsearch import Elasticsearch
import settings
import constants

class esConnect:
	def __init__(self):
		settings.getSettings()
		print "index"+settings.ES_INDEX_NAME

	def connect(self):
		self.es=Elasticsearch([{"host":settings.ES_HOST_NAME}])

	def addVisited(self,data):
		datae={'link':data['link'],'addedOn':data['addedOn']}
		self.write_data(datae,settings.ES_TYPE_NAME_CRAWLED)
	@staticmethod	
	def isCrawled(url):
		# check if it is crawled
		return False
		
	def connect(self):
		self.es=Elasticsearch([{"host":settings.ES_HOST_NAME}])
		#todo
	def addPage(self,data):
		datae={'link':data[constants.LINK],'status':data[constants.STATUS],'title':data[constants.TITLE],
		'body':data[constants.BODY],'size':data[constants.SIZE],'linkTo':data[constants.LINKSTO],
		"addedOn":data[constants.VISITEDON]}
		self.addVisited(datae)
		self.write_data(datae,settings.ES_TYPE_NAME_SEARCH)
		# write data to es
		
		
	def write_data(self,data,type):
		self.es.index(index=settings.ES_INDEX_NAME,doc_type=type,body=data)

	
		
