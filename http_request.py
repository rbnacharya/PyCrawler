import urllib2,robotparser,urlparse

robot = robotparser.RobotFileParser()



class RequestHTTP:
	def __init__(self):
		self.init()	
	
	def init(self):
		self.req= None
		self.checkifmodified=True
		self.isModified=True
		self.status=0
		self.requ= None

	def setURL(self,url):
		self.url=url
		self.init()

	def initConnection(self):
		self.req=urllib2.Request(str(self.url))

	def isModifiedSince(self,date_obj):
		self.req.add_header("If-Modified-Since",date_obj)

	def requestInternal(self):
		self.initConnection()
		self.req.add_header('User-Agent', 'ESCrawler 0.0.1')
		try:
			self.requ = urllib2.urlopen(self.req)
		except urllib2.URLError,e:
			pass
			# logger.error("Exception at url: %s\n%s" % (url, e))
		except urllib2.HTTPError, e:
			self.status = e.code
		if self.status == 0:
			self.status = 200
		if self.status == 304:
			self.isModified=False

	def get_status(self):
		return self.status


	def request(self):
		self.initConnection()
		self.requestInternal()

	def isModifiedFlag(self):
		return self.isModified;

	def can_fetch(self):
		u = urlparse.urlparse(self.url)
		robot.set_url('http://'+u[1]+"/robots.txt")
		if not robot.can_fetch('PyCrawler', self.url.encode('ascii', 'replace')):
			return False
		return True

	def can_follow(self):
		if not self.url.startswith('http'):
			return False
		return True

	def get_data(self):
		return self.requ.read()
		

	


		

	