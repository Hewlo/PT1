import shutil
import os

project_directory = os.getcwd()
print('Project folder path is:', project_directory)

folder_contents = os.listdir(project_directory)
print(folder_contents)

new_folder_path = os.path.join(project_directory, 'sample')
print('New folder path is:', new_folder_path)

if not os.path.exists(new_folder_path):
    os.mkdir(new_folder_path)

folder_contents = os.listdir(project_directory)
print(folder_contents)