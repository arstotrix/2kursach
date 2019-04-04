#from collections import OrderedDict
import json
#from pprint import pprint as pp
with open ('tags.tsv', encoding='utf-8') as f:
    text = f.read().split('\n')
tags = {}
for t in text:
    t=t.split('\t')
    tags[t[0]]=t[1]
with open("tags.json", 'w', encoding="utf-8") as f:
    json.dump(tags, f, ensure_ascii=False, indent=2)


