import os
import re
import json
from bs4 import BeautifulSoup

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

# функция разделяет текст на слова, а слова превращает в словарики с данными, и делает словарь с чистыми предложениями
def wordify(text):
    sentences = {}
    for s in text:
        sentence = []
        phrase = ''
        s = s.split('\n')
        for elem in s:
            if not elem.startswith('<'):
                s.remove(elem)
        if len(s) > 0:
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
                except AttributeError:
                    eee = 1
        if sentence!=[]:
            sentences[phrase] = sentence
    return sentences

#unused
def text_drop(text, name):
    file = './processed/'+name+'.txt'
    with open (file, 'a', encoding='utf-8') as f:
        f.write(text)

def main():
    entities = {}
    path = './_texts'
    files = os.listdir(path)
    for file in files:
        mark = 0
        text = []
        name = path+'/'+file
        with open(name, encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'lxml')
        body = soup.find('body')
        for sp in body.find_all('sp'):
            ps = sp.find_all('p')
            ls = sp.find_all('l')
            lines = cleaner(ls)
            phrases = cleaner(ps)
            sents = lines + phrases
            spltext = splitter(sents)
            sentences = wordify(spltext)
            text.append(sentences)
        entities[file[:-4]] = text
    with open('database_corrected.json', 'w', encoding='utf-8') as f:
        json.dump(entities, f, ensure_ascii=False, indent=2)
    words = 0
    speeches = 0
    sentences = 0
    for entity in entities:
        speeches += len(entities[entity])
        for sent in entities[entity]:
            sentences += len(sent)
            for s in sent:
                words += len(sent[s])
    print('speeches: ', speeches)
    print('sentences: ', sentences)
    print('words: ', words)

if __name__ == "__main__":
    main()