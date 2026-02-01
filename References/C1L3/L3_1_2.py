import shutil
import os


project_directory = os.getcwd()

new_file_path = os.path.join(project_directory, 'abc.txt')
print('Files to be created:', new_file_path)
if not os.path.exists(new_file_path):
    txt_file = open(new_file_path, 'w')
else:
    txt_file = open(new_file_path, 'a')

content = '''
This is a sample content to be written to the text file.
1 - My name is John.
2 - I am student of Administrative Scripting.
3 - I will become a Python developer once I finish this course.
'''

txt_file.write(content)
txt_file.close()
folder_contents = os.listdir(project_directory)