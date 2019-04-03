import re
import json
dict = {}
i = 0
with open('Ado.xml', encoding='utf-8') as f:
    text = f.read()
words = re.findall('<w.*?</w>', text, flags=re.DOTALL)
#print(words)
for w in words[:1000]:
    word = re.search('>.*?<', w).group()[1:-1]
    data = re.search('<w.*?>', w).group()
    i+=1
    print(word, data)
print(i)
    #print(word)





#for w in words:
    #print(w)
    #word = re.search('>.?*<', w).group()
    #print(word)
#    w = w.split('')
#    for item in w:

