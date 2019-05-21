import os
import re
import csv
import json
import collections
from bs4 import BeautifulSoup
import xmltodict
import xml.etree.ElementTree

#функция чистит массив от лишних тэгов и превращает в строку
def cleaner(mass):
    strtext = str(mass).strip('[]')
    strtext = re.sub('<lb.*?></lb>\n', '', strtext)
    strtext = re.sub('</[pl]>', '', strtext)
    strtext = re.sub('<[pl] .*?>\n', '', strtext)
    strtext = re.sub('<c> </c>\n', '', strtext)
    text = '\n'.join(strtext.split(', '))
    text = re.sub(', ', '', text)
    text = re.sub('\n\n', '\n', text)
    return text

#функция разбивает текст на предложения
def splitter(text):
    dots = re.sub('<pc.*?>\.</pc>', '<pc>',  text)
    qmarks = re.sub('<pc.*?>\?</pc>', '<pc>', dots)
    emarks = re.sub('<pc.*?>!</pc>', '<pc>', qmarks)
    cleanerver = re.sub('\n\n', '\n', emarks)
    spltext = cleanerver.split('<pc>')
    return spltext

# функция разделяет текст на слова, а слова превращает в словарики с данными
def makesent(bigtable, text, ind):
    phrase = ''
    for s in text:
        print(s)
        s = s.split('\n')
        try:
            phrase += re.search('>(.*?)<', s[0]).group(1)
            for i,w in enumerate(s[1:]):
                try:
                    entry = re.search('>(.*?)<', w).group(1)
                    if w[1:3] == 'pc':
                        phrase += entry
                    elif w[1] == 'w':
                        phrase += ' '+entry
                except AttributeError:
                    eee = 1
        except AttributeError:
            eee = 1
    print(phrase)
    print(ind)
    if len(phrase) > 1:
        bigtable[ind] = phrase
        ind += 1
    return bigtable, ind

def text_drop(text, name): #unused
    file = './processed/'+name+'.txt'
    with open (file, 'a', encoding='utf-8') as f:
        f.write(text)

def main():
    bigtable = {}
    path = './_texts'
    files = os.listdir(path)
    for file in files:
        table = {}
        ind = 0
        text = []
        name = path+'/'+file
        with open(name, encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'lxml')
        body = soup.find('body')
        for sp in body.find_all('sp'):
            ps = sp.find_all('p')
            ls = sp.find_all('l')
            #pcs = sp.find_all('pc')
            lines = cleaner(ls)
            phrases = cleaner(ps)
            sentences = lines + phrases
            spltext = splitter(sentences)
            table, ind = makesent(table, spltext, ind)
            #text.append(sentences)
        #entities[file[:-4]] = text
        bigtable[file[:-4]] = table
    with open('sentences_ids.json', 'w', encoding='utf-8') as f:
        json.dump(bigtable, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()