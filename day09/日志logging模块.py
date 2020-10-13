import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


fh = logging.FileHandler('test.log',encoding='utf-8')
fh.setLevel(logging.INFO)

ch = logging.StreamHandler()
formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s[%(lineno)d]: %(message)s')


fh.setFormatter(formatter1)
ch.setFormatter(formatter2)

logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')
