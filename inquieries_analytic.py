import json
import re
entries = {}
quantity = {}

with open('tags2.txt', encoding='utf-8') as f:
    text = f.read()
tags = []
for t in text.split('\n'):
    tags.append(t.split('\t')[0])
#print(tags)

with open('database_corrected.json', encoding='utf-8') as f:
    entities = json.load(f)
ind = 0
for entity in entities:
    text = entities[entity]
    for speech in text:
        for phrase in speech:
            sentence = speech[phrase]
            n = 0
            for i, wrd in enumerate(sentence[1:]):
                prev = sentence[i-1]
                next = sentence[i]
                #print(prev)
                #print(next)
                if next['ana'] == '#xx' and next['gotcommas'] == False:
                    #print(prev)
                    #print(next)
                    if prev['ana'] in tags and prev['lemma'] != 'do' and prev['lemma'] != 'be':
                        #print(prev)
                        n += 1
                        collocation = prev['word']+' '+next['word']
                        ind += 1
            if n > 0:
                entries[phrase] = sentence
                phrase = re.sub(',', '<comma>', phrase)
                line = str(ind) + ',' + phrase + ',' + collocation + '\n'
                with open('entries_analytic.tsv', 'a', encoding='utf-8') as f:
                    f.write(line)
                #if n > 1:
                #    quantity[n] = sentence
                #print(sentence)

print(len(entries))
#print(quantity)


'''with open('entries.json', 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)'''
