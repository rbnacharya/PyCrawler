#from query import CrawlerDb
from content_processor import ContentProcessor
from settings import LOGGING
import settings
from esConnector import esConnect
from http_request import RequestHTTP
import sys, urlparse, urllib2, shutil, glob, robotparser
import logging, logging.config
import traceback
import ready_queue

# ===== Init stuff =====

# db init
#cdb = CrawlerDb()
#cdb.connect()

# content processor init
processor = ContentProcessor(None, None, None)
http_req=RequestHTTP()
# logging setup
logging.config.dictConfig(LOGGING)
logger = logging.getLogger("crawler_logger")

#esInit
esc=esConnect()

# robot parser init
robot = robotparser.RobotFileParser()

if len(sys.argv) < 2:
	logger.info("Error: No start url was passed")
	sys.exit()

l = sys.argv[1:]
toCrawl=l[0];
#cdb.enqueue(l)

def crawl():
#	global http_req
	logger.info("Starting (%s)..." % sys.argv[1])
	esc.connect()
	while True:
		url = ready_queue.stripURL(toCrawl)
		http_req.setURL(url)
		if not http_req.can_fetch():
			break
		if not http_req.can_follow():
			break
				
		# if esConnect.isCrawled(url):
		# 	break
		# # if cdb.checkCrawled(url):
		# 	continue
		if url is False:
			break
		status=0
		#print http_req.request("heee")
		http_req.request()
		status = http_req.get_status()
		if status != 200:
			break
		data = http_req.get_data()

		processor.setInfo(str(url), status, data)
		ret = processor.process()
		if status != 200:
			break
		linkedTo = []
		
		#toDo: check if it is already crawled
		# for q in ret:
		# 	if not cdb.checkCrawled(q):
		# 		add_queue.append(q)

		processor.setInfo(str(url), status, data)
		linkedTo = processor.process()
		l = len(linkedTo)
		#logger.info("Got %s status from %s (Found %i links)" % (status, url, l))
		esc.addPage(processor.getDataDict())
		# if l > 0:
		# 	cdb.enqueue(add_queue)	
		# cdb.addPage(processor.getDataDict())
		processor.reset()
		break

	logger.info("Finishing...")
	#cdb.close()
	logger.info("Done! Goodbye!")

if __name__ == "__main__":
	try:
		crawl()
	except KeyboardInterrupt:
		logger.error("Stopping (KeyboardInterrupt)")
		sys.exit()
	except Exception, e:
		logger.error("EXCEPTION: %s " % e)
		traceback.print_exc()
	
