import os
import re
import csv
import json
import collections
from bs4 import BeautifulSoup
import xmltodict
import xml.etree.ElementTree

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

def splitter(text):
    """dels = []
    puncts = str(pcs).strip('[]').split(', ')
    for p in puncts:
        if '>.<' in str(p) or '>!<' in str(p) or '>?<' in str(p):
            dels.append(p)"""
    dots = re.sub('<pc.*?>\.</pc>', '<pc>',  text)
    qmarks = re.sub('<pc.*?>\?</pc>', '<pc>', dots)
    emarks = re.sub('<pc.*?>!</pc>', '<pc>', qmarks)
    cleanerver = re.sub('\n\n', '\n', emarks)
    spltext = cleanerver.split('<pc>')
    return spltext

def wordify(text):
    sentences = []
    for s in text:
        sentence = []
        s = s.split('\n')
        for i,w in enumerate(s):
            wrd = {}
            try:
                wrd['gotcommas'] = False
                if s[i-1][1:3] == 'pc':
                    wrd['gotcommas'] = True
                wrd['ana'] = re.search('ana="(.*?)"', w).group(1)
                wrd['lemma'] = re.search('lemma="(.*?)"', w).group(1)
                wrd['n'] = re.search('n="(.*?)"', w).group(1)
                wrd['xmlid'] = re.search('xml:id="(.*?)"', w).group(1)
                wrd['word'] = re.search('>(.*?)<', w).group(1)
                sentence.append(wrd)
                #print(wrd)
            except AttributeError:
                i+=1
        if sentence!=[]:
            print(sentence)
            sentences.append(sentence)
    return sentences

def main():
    name = './_texts/Ado.xml'
    speeches = []
    # csvname = 'sentences.csv'
    with open(name, encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
    #print(type(soup))
    body = soup.find('body')
    #print(type(body))
    for sp in body.find_all('sp'):
        #print(sp)
        ps = sp.find_all('p')
        ls = sp.find_all('l')
        #pcs = sp.find_all('pc')
        lines = cleaner(ls)
        phrases = cleaner(ps)
        sentences = lines+phrases
        spltext = splitter(sentences)
        text = wordify(spltext)
        speeches.append(text)
    print(speeches)
        #print(spltext)
        # words = sp.find_all('w')

if __name__ == '__main__':
    main()