import subprocess
import os

command = '/bin/tar'
project_directory = os.getcwd()

zip_file_path = os.path.join(project_directory, 'project.tar')
subprocess.call([command, '-xvf', zip_file_path])