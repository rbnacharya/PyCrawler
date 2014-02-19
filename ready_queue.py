import re, urlparse

linkregex = re.compile('<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>')

queue = []
def ready_queue(address, html):
	global queue
	url = urlparse.urlparse(str(address))
	links = linkregex.findall(html)
	for link in links:
		if link.startswith("/"):
			addQueue('http://'+url[1]+link)
		elif link.startswith("http") or link.startswith("https"):
			addQueue(link)
		elif link.startswith("#"):
			continue
		else:
			addQueue(urlparse.urljoin(url.geturl(),link))
	return queue

def addQueue(item):
	item=stripURL(item)
	if(item not in queue):
		queue.append(item)
def stripURL(item):
	if(item[len(item)-1]=="/"):
		return item[0:len(item)-1]
	return item