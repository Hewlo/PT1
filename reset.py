import shutil
import os
from os import remove

for items in os.listdir(os.getcwd()):
    item_path = os.getcwd() + r'/' + items
    file, file_extension = os.path.splitext(items)
    if items == 'resource':
        backup_path = os.getcwd() + r'\\' + 'resource (1)'
        shutil.rmtree(item_path)
        shutil.copytree(backup_path, item_path)
    if file_extension == '.txt' or file_extension == '.zip':
        remove(items)