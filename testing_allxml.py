import xml.etree.ElementTree as ET
import json
import xmltodict
import os
import re

path = './_texts'
try:
    os.mkdir('./processed')
except FileExistsError:
    print('File already exists')
#csvname = 'sentences.csv'
files = os.listdir(path)
for file in files:
    name = path+'/'+file
    with open(name, encoding='utf-8') as f:
        text = f.read()
    pieces = re.findall('<sp.*?>.*?</sp>', text, flags=re.DOTALL)
    #print(pieces)
    for p in pieces:
        print(p)
        o = xmltodict.parse(p)
        print(type(o))
            #with open('test1.json', 'w', encoding='utf-8') as f:
                #json.dump(o, f, ensure_ascii=False, indent=2) # '{"e": {"a": ["text", "text"]}}'


