import glob

target = glob.glob
file_match = target('*.txt')
print(file_match)
file_match = target('file[0-9][0-9].txt')
print(file_match)

#Returns every content matching .txt in every folder in the project directory
file_match = target('**/*.txt', recursive=True)
print(file_match)

#Returns folders in the project directory
file_match = target('**/', recursive=True)
print(file_match)