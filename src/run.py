import logging , duallog

def get_loggerObject():
    duallog.setup('Logs')
    logger = logging.getLogger()
    return logger

def main():
    get_loggerObject()

if __name__ == '__main__':
    main()

