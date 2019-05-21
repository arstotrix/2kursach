import re
import json
dict = {}
with open('Ado.xml', encoding='utf-8') as f:
    text = f.read()
words = re.findall('<w.*?</w>', text, flags=re.DOTALL)
#print(words)
i = 0
for w in words[:1000]:

    if re.search('n=".*?"', w) and re.search('n=".*?"', w) and re.search('ana=".*?"', w):
        word = re.search('>.*?<', w).group()[1:-1]
        data = re.search('<w.*?>', w).group()
        xmlid = re.search('xml:id=".*?"', w).group()[8:-1]
        lemma = re.search('lemma=".*?"', w).group()[7:-1]
        n = re.search('n=".*?"', w).group()[3:-1]
        ana = re.search('ana=".*?"', w).group()[5:-1]
        i+=1
        print(word, xmlid, n, lemma, ana)
print(i)

    #print(word)





#for w in words:
    #print(w)
    #word = re.search('>.?*<', w).group()
    #print(word)
#    w = w.split('')
#    for item in w:

