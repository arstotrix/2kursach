import json
words = 0
sentences = 0
speeches = 0
with open('database_corrected.json', encoding='utf-8') as f:
    entities = json.load(f)
for entity in entities:
    speeches += len(entities[entity])
    for sent in entities[entity]:
        sentences += len(sent)
        for s in sent:
            words += len(sent[s])
print('speeches: ', speeches)
print('sentences: ', sentences)
print('words: ', words)