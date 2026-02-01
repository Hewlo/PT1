import shutil
import os
import zipfile

project_directory = os.getcwd()
backup_folder_directory = os.path.join(project_directory, 'samplecopy')
zip_file_name = 'sample.zip'

with zipfile.ZipFile(zip_file_name, mode='w') as archive:
    for files in os.listdir(backup_folder_directory):
        zip_file_directory = os.path.join(backup_folder_directory, files)
        archive.write(zip_file_directory, arcname=files)
print(os.listdir(project_directory))

