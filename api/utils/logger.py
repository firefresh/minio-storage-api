import logging
import os

def get_logger(name='default', level='INFO', log_path=None, log_format = '%(asctime)s - %(levelname)s - %(pathname)s - Line: %(lineno)d - ', prefix=""):
	if log_path is None:
		log_path = os.getenv('LOG_PATH', '/tmp')
	logger = logging.getLogger(name)
	formatter = logging.Formatter(fmt=log_format+str(prefix)+" %(message)s")
	file_handler = logging.FileHandler(log_path + '/' + name + ".log")
	file_handler.setFormatter(formatter)
	logger.handlers = []
	logger.addHandler(file_handler)
	logger.setLevel(level)
	logger.propagate = False
	return logger