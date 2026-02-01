import os
import logging
import zipfile
import shutil
from time import strftime

#TASK D
logging.basicConfig(filename='PI2404P_Joe.txt', filemode='w',
                    format= '%(asctime)s: %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel('INFO')

project_directory = os.getcwd()
resource_directory = os.getcwd() + r'/resource'
txt_file_directory = os.getcwd() + r'/resource/student_submission.txt'
# txt_contents = open(txt_file_directory, 'r')

#TASK A
with open(txt_file_directory, 'r') as txt_contents:
    for lines in txt_contents.readlines():
        lines = lines.rstrip('\n')
        if lines == '' or ':' not in lines:
            continue
        project_name, project_owner = lines.split(':')
        file_name, file_extension = os.path.splitext(project_name)
        project_full_name = file_name + '_' + project_owner + file_extension
        target_project_name = resource_directory + r'/{}'.format(project_name)
        try:
            os.rename(target_project_name, resource_directory + r'/{}'.format(project_full_name))
            logger.info('Rename file: {} rename to {}'.format(target_project_name, project_full_name))
        except FileNotFoundError:
            logger.info('Skipped file: {}'.format( project_full_name))

#TASK B
#I don't know how I come up with these.
split_resource_path = resource_directory.split('/')
copy_target_name = split_resource_path[split_resource_path.index(max(split_resource_path))]
backup_folder_directory = os.getcwd() + '/' + strftime('%Y_%m_%d_{}'.format(copy_target_name))
if not os.path.exists(backup_folder_directory):
    shutil.copytree(resource_directory, backup_folder_directory)
    logger.info('Backing up folder: {} created'.format(backup_folder_directory))

#TASK C
with zipfile.ZipFile('{}_{}.zip'.format(strftime('%Y_%m_%d_%H_%M_%S'), copy_target_name),'w') as archive:
    for files in os.listdir(resource_directory):
        file_path = backup_folder_directory + r'/{}'.format(files)
        archive.write(file_path)
    logger.info('Compressing file {}'.format(archive.filename))
    shutil.rmtree(backup_folder_directory)
    logger.info('Removing folder {} removed'.format(backup_folder_directory))