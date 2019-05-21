import re
from json import load, dump
import os
from bs4 import BeautifulSoup

def body_out(fname): #достаём тело из текста
    with open(fname, encoding= 'utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
    body = soup.find('body')
    return body

def names(start_path): #ходим по папке и достаём имена
    for root, dirs, files in os.walk(start_path):
        names = files
    return names

def src_main(names): #достаём имена, ссылка на другую функцию
    titles = []
    for name in names:
        if name.endswith('.xml'):
            src_bodies(name)
            name = name.strip(".xml")
            titles.append(name)
    return titles

def src_bodies(name): #достаём тело и работаем с ними
    body = body_out(name)
    ps = body.findall('p')
    return

def main():
    src(names('.'))







if __name__ == "__main__":
    main()
