from bs4 import BeautifulSoup
import os

for root, dirs, files in os.walk('.'):
    names = files
for name in names:
    if name.endswith('.xml'):
        stats =  name.strip('.xml')
        with open(name, encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), 'lxml')
        if not soup.find('p')== None:
            stats += ' p is present'
        if not soup.find('l') == None:
            stats += ' l is present'
        print(stats)
