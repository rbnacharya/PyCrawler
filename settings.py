import logging
import yaml

DATABASE_ENGINE = "sqlite"		# sqlite or mysql
DATABASE_NAME = "PyCrawler"		# Database name
DATABASE_HOST = "/PyCrawler.db"	# Host address of mysql server or file location of sqlite db
DATABASE_PORT = ""				# Port number as a string. Not used with sqlite
DATABASE_USER = ""				# Not used with sqlite
DATABASE_PASS = ""				# Not used with sqlite

CONFIG_FILE="../config/settings.yml"
ES_CLUSTER_NAME=""
ES_HOST_NAME=""
ES_PORT=""
ES_INDEX_NAME=""
ES_TYPE_NAME_SEARCH=""
ES_TYPE_NAME_CRAWLED=""

def getSettings():
	stream=open(CONFIG_FILE,"r")
	docs=yaml.load(stream)
	global ES_CLUSTER_NAME, ES_HOST_NAME,ES_PORT,ES_INDEX_NAME,ES_TYPE_NAME_SEARCH,ES_TYPE_NAME_CRAWLED
	ES_CLUSTER_NAME=docs["cluster_name"]
	ES_HOST_NAME=docs["host_name"]
	ES_PORT=docs["http_port"]
	ES_INDEX_NAME=docs["index_name_default"]
	ES_TYPE_NAME_SEARCH=docs["type_name_search"]
	ES_TYPE_NAME_CRAWLED=docs["type_name_crawler"]



DEBUG = True 					# Whether or not to show DEBUG level messages
USE_COLORS = True 				# Whether or not colors should be used when outputting text

LOGGING = {						# dictConfig for output stream and file logging
	'version': 1,              
    'disable_existing_loggers': False,

	'formatters': {
		'console': {
			'format': '[%(asctime)s] %(levelname)s::%(module)s - %(message)s',
		},
		'file': {
			'format': '[%(asctime)s] %(levelname)s::(P:%(process)d T:%(thread)d)::%(module)s - %(message)s',
		},
	},

	'handlers': {
		'console': {
			'class': 'ColorStreamHandler.ColorStreamHandler',
			'formatter':'console',
			'level': 'DEBUG',
			'use_colors': USE_COLORS,
		},
		'file': {
			'class': 'logging.handlers.TimedRotatingFileHandler',
			'formatter':'file',
			'level': 'INFO',
			'when': 'midnight',
			'filename': 'pycrawler.log',
			'interval': 1,
			'backupCount': 0,
			'encoding': None,
			'delay': False,
			'utc': False,
		},
	},

	'loggers': {
		'crawler_logger': {
			'handlers': ['console', 'file'],
			'level': 'DEBUG' if DEBUG else 'INFO',
			'propagate': True,
		},
	}
}   
