import logging , duallog , sys , os
sys.path.insert(0, os.path.abspath(".."))

def get_loggerObject():
    duallog.setup('Logs')
    logger = logging.getLogger()
    return logger

logger = get_loggerObject()

def main():

    pass

