import shutil
import os

project_directory = os.getcwd()
destination_folder = os.path.join(project_directory, 'sample')
print(os.listdir(project_directory))

for files in os.listdir(project_directory):
    source_file_path = os.path.join(project_directory, files)
    file_name, file_extension = os.path.splitext(source_file_path)
    if file_extension == '.txt':
        destination_file_path = os.path.join(destination_folder, files)
        print('Move from {} to {}'.format(source_file_path, destination_file_path))
        shutil.move(source_file_path,destination_file_path)

folder_contents = os.listdir(project_directory)
print(folder_contents)