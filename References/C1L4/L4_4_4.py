import configparser
import os
import re
from random import randint

project_directory = os.getcwd()
config_file = os.path.join(project_directory, 'config.txt')
parser = configparser.ConfigParser()

if not os.path.exists(config_file):
    config = open('config.txt','w')
    text = '''[personal_information]
    name = John
    age = {}
    
    [grades]
    english = {}
    maths = {}
    '''.format(randint(6,80),randint(0, 100), randint(0,100))
    text = re.sub(' ', '', text, flags=re.MULTILINE)
    config.write(text)
    config.close()
else:
    config = open('config.txt', 'r')

parser.read(config_file)
name = parser.get('personal_information', 'name')
age = parser.get('personal_information', 'age')
english = parser.get('grades', 'english')
maths = parser.get('grades', 'maths')

print('''Personal information:
Name : {}
Age : {}

Grades:
English : {}
Maths : {}'''.format(name, age, english, maths))

config.close()