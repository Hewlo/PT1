import shutil
import os

project_directory = os.getcwd()
source_folder_path = os.path.join(project_directory, 'sample')
destination_folder_path = os.path.join(project_directory, 'samplecopy')

print(os.listdir(project_directory))
shutil.copytree(source_folder_path, destination_folder_path)
print(os.listdir(project_directory))