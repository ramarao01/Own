import logging
import logging.config
log_levels = {
    'critical': logging.CRITICAL,
    'debug':    logging.DEBUG,
    'error':    logging.ERROR,
    'warning':  logging.WARNING,
    'info':     logging.INFO,
}


def setup_logger(log_file_name,level_name='debug'):
	level = log_levels.get(level_name, logging.NOTSET)
	#formatter = logging.Formatter(fmt= ('%(asctime)s : %(module)s : %(name)s : %(levelname)s : %(message)s'))
	formatter = logging.Formatter(fmt= ('%(asctime)s : %(levelname)s : %(message)s'))
	handler = logging.FileHandler(filename=log_file_name, mode='w+')
	handler.setFormatter(formatter)

	logger = logging.getLogger(log_file_name[:-4])
	logger.setLevel(level)
	logger.addHandler(handler)
	return logger