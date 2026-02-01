import shutil
import os

project_directory = os.getcwd()
existing_file_path = os.path.join(project_directory, 'abcCopy.txt')

print('File name to rename from :', existing_file_path)
folder_contents = os.listdir(project_directory)
print(folder_contents)

rename_file_path = os.path.join(project_directory, 'def.txt')
print('File name to rename to :', rename_file_path)
shutil.move(existing_file_path, rename_file_path)

folder_contents = os.listdir(project_directory)
print(folder_contents)