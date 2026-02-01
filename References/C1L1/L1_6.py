import subprocess
import os

command = '/bin/tar'
project_directory = os.getcwd()

zip_file_path = os.path.join(project_directory, 'project.tar')
compress_target = './'

subprocess.call([command, '-tvf', zip_file_path])