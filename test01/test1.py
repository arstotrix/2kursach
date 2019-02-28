import os
from bs4 import BeautifulSoup
import re
def fread(fn, sep):
    with open (fn, encoding='utf-8') as f:
        text = f.read()
        body = re.search('<body>.*</body>', text, flags = re.DOTALL).group(0)
        print(body)
    return body

def main():
    fread('Ado.xml', '')

if __name__ == '__main__':
    main()
