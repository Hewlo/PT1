import os
from datetime import datetime

project_directory = os.getcwd()
new_file_path = os.path.join(project_directory, 'abc.txt')
now = datetime.now()
dt_string = now.strftime('%Y/%m/%d %H:%M:%S')
if not os.path.exists(new_file_path):
    txt_file = open(new_file_path, 'w')
else:
    txt_file = open(new_file_path, 'a')

content = '''
This is a scheduled task created on
'''
txt_file.write(content + dt_string)
txt_file.close()