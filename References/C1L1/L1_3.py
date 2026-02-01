import subprocess
import os

alacritty = '/bin/alacritty'

project_directory = os.getcwd()
file_path = os.path.join(project_directory, 'sample_output_1_3.txt')

subprocess.call([alacritty, '-e', 'vim', file_path])