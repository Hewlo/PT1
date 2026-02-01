import os
import shutil

project_directory = os.getcwd()
source_folder_path = os.path.join(project_directory, 'sample')
print(os.listdir(project_directory))

if os.path.exists(source_folder_path):
    shutil.rmtree(source_folder_path)
    print(os.listdir(project_directory))