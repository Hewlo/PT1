import os
import shutil
import zipfile
from datetime import datetime
import logging
from logging import INFO

#Task D
logging.basicConfig(filename='PI2404P_Joe.txt',filemode='w',
                    format='%(asctime)s, %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(INFO)

project_folder_directory = os.getcwd()
upload_directory = project_folder_directory + r'/resource'
student_submission_directory = upload_directory + r'/student_submission.txt'
now = datetime.now()

#Task A
with open(student_submission_directory, 'r') as content:
    for line in content.readlines():
        if ' ' in line:
            continue
        line = line.rstrip()
        project, owner = line.split(':')
        project_file_directory = upload_directory + r'/' + project
        target_project_file_directory = upload_directory + '/' + owner + '_' + project
        shutil.move(project_file_directory, target_project_file_directory)
        logger.info('Rename file: {} rename to {}'.format(project, owner + '_' + project))

#Task B
date_now = now.strftime('%Y_%m_%d')
split_backup_directory = upload_directory.split(r'/')
backup_folder_name = split_backup_directory[split_backup_directory.index(max(split_backup_directory))]
backup_file_name = date_now + '_' + backup_folder_name
backup_folder_directory = project_folder_directory + r'/' + backup_file_name

if not os.path.exists(backup_folder_directory):
    os.mkdir(backup_folder_directory)
for files in os.listdir(upload_directory):
    files_path = upload_directory + r'/' + files
    shutil.copy(files_path, backup_folder_directory)
logger.info('Backing up folder: {} created'.format(backup_file_name))

#Task C
datetime_now = now.strftime('%Y_%m_%d_%H_%M_%S')
zip_name = '{}_{}.zip'.format(datetime_now, backup_folder_name)
with zipfile.ZipFile(zip_name, 'w') as archive:
    for files in os.listdir(backup_folder_directory):
        files_path = backup_folder_directory + r'/' + files
        archive.write(files_path)
    logger.info('Compressing file {}'.format(zip_name))
    shutil.rmtree(backup_folder_directory)
    logger.info('Removing folder {} removed'.format(backup_file_name))

