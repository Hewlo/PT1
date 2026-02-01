import logging
import os

logging.basicConfig(filename='john.log', filemode='w',
                    format='%(asctime)s %(message)s',)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info('Getting current directory')
project_directory = os.getcwd()
logger.info('Current project folder is: {}'.format(project_directory))