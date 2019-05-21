import re
name = './_texts/Ado.xml'
with open(name, encoding='utf-8') as f:
    text = f.read()
sps = re.findall('<sp.*?>.*?/<sp>', text, flags=re.DOTALL)
for sp in sps:
    print(sp)
    ps = re.findall('<p.*?>.*?/<p>', text, flags=re.DOTALL)
    ls = re.findall('<l.*?>.*?/<l>', text, flags=re.DOTALL)
    pcs = re.findall('<pc.*?>.*?/<pc>', text, flags=re.DOTALL)
    print(ps)
