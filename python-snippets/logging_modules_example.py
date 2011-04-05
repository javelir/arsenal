import os, sys, datetime
import logging
from logging.handlers import SMTPHandler

def using_log_file():
    LOG_FILENAME = 'my-log-file'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical error message')


    print '***********************************************'
    print '** log file contents:'
    print '***********************************************'
    with file(LOG_FILENAME,'rb') as f:
        print f.read()
    print '***********************************************'
    os.remove(LOG_FILENAME)

# timv: this thing doesn't work super well..
def email_logger():
    my_logger = logging.getLogger('my-logger')
    
    smtp = 'localhost'
    my_logger.addHandler(SMTPHandler(smtp, 
                                     'tim.f.vieira@gmail.com', 
                                     'tim.f.vieira@gmail.com', 
                                     'testing critical message system.'))
    my_logger.critical('critical message from your script.')
    


def quick_start_log(log_fn=None, mode='w', level=logging.DEBUG, 
                    fmt='%(asctime)s|%(name)s|%(levelname)s| %(message)s'):
    """
    simplest basicConfig wrapper, open log file and return default log handler
    """

    if log_fn is None:
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d_%H%M%S')
        log_fn = '%s.%s.log' % (sys.argv[0], ts)

    logging.basicConfig(level=level,
                        format=fmt,
                        filename=log_fn,
                        filemode=mode)

    logger = logging.getLogger('main')
    if mode.lower() == 'a':
        logger.info('---=== START ===---')

    return logger


def quick_start_example():
    log = quick_start_log()
    log.info('message')
    log.fatal('exit')
