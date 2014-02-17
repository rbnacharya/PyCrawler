from elasticsearch import Elasticsearch
import settings
import constants

class ecConnect:
	def __init__(self):

	def connect(self):
		self.es=Elasticsearch([{"host":settings.ES_HOST_NAME}])
		#todo
	def addPage(self,data):
		datae={'link':data[constants.LINK],'status':data[constants.STATUS],'title':data[constants.TITLE],
		'body':data[constants.BODY],'size':data[constants.SIZE],'linkTo':data[constants.LINKSTO],
		"addedOn":data[constants.VISITEDON]}
		write_data(datae,settings.ES_TYPE_NAME_SEARCH)
		# write data to es
		#todo
	def addVisited(self,data):
		datae={'link':data[constants.LINK],'addedOn':data[constants.VISITEDON]}
		write_data(datae,settings.ES_TYPE_NAME_CRAWLED)
		
	def isCrawled(self,url):
		# check if it is crawled
		
	def write_data(self,data,type):
		self.es.index(index=settings.ES_INDEX_NAME,doc_type=type,body=data)

		
	def connect(self):
		self.es=Elasticsearch([{"host":settings.ES_HOST_NAME}])
		#todo
	def addPage(self,data):
		datae={'link':data[constants.LINK],'status':data[constants.STATUS],'title':data[constants.TITLE],
		'body':data[constants.BODY],'size':data[constants.SIZE],'linkTo':data[constants.LINKSTO],
		"addedOn":data[constants.VISITEDON]}
		write_data(datae,settings.ES_TYPE_NAME_SEARCH)
		# write data to es
		#todo
	def addVisited(self,data):
		datae={'link':data[constants.LINK],'addedOn':data[constants.VISITEDON]}
		write_data(datae,settings.ES_TYPE_NAME_CRAWLED)
		
	def isCrawled(self,url):
		# check if it is crawled
		
	def write_data(self,data,type):
		self.es.index(index=settings.ES_INDEX_NAME,doc_type=type,body=data)

		
	def connect(self):
		self.es=Elasticsearch([{"host":settings.ES_HOST_NAME}])
		#todo
	def addPage(self,data):
		datae={'link':data[constants.LINK],'status':data[constants.STATUS],'title':data[constants.TITLE],
		'body':data[constants.BODY],'size':data[constants.SIZE],'linkTo':data[constants.LINKSTO],
		"addedOn":data[constants.VISITEDON]}
		write_data(datae,settings.ES_TYPE_NAME_SEARCH)
		# write data to es
		#todo
	def addVisited(self,data):
		datae={'link':data[constants.LINK],'addedOn':data[constants.VISITEDON]}
		write_data(datae,settings.ES_TYPE_NAME_CRAWLED)
		
	def isCrawled(self,url):
		# check if it is crawled
		
	def write_data(self,data,type):
		self.es.index(index=settings.ES_INDEX_NAME,doc_type=type,body=data)

		