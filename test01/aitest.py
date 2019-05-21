lines = ['young', 'blood', 'young', 'blood', 'punchdrunken', 'youngblood']
for l in lines:
    with open('testt.txt', 'a', encoding='utf-8') as f:
        f.write(l)