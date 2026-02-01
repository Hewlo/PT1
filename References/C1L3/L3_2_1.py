import shutil
import os

project_directory = os.getcwd()
folder_contents = os.listdir(project_directory)
print(folder_contents)

existing_file_path = os.path.join(project_directory, 'abc.txt')
duplicate_file_path = os.path.join(project_directory, 'abcCopy.txt')
shutil.copy(existing_file_path,duplicate_file_path)

folder_contents = os.listdir(project_directory)
print(folder_contents)