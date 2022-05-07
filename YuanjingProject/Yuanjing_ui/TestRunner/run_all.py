import logging
# …Ë÷√root logger
logger = logging.getLogger()
logger.setLevel(level=logging.ERROR)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(levelname)s'))
logger.addHandler(ch)

logger.error(11)

p = logging.getLogger('foo')
p.setLevel(level=logging.ERROR)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(levelname)s'))
p.addHandler(ch)
p.error(22)