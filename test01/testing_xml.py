import xml.etree.ElementTree as ET
tree = ET.parse('Ado.xml')
root = tree.getroot()

#print(root.tag) #tag = idk wtf this is
#print(root.attrib) #attributes i guess

#print(root[1][1].tag)
for word in root[1][1].findall('div'):
    print(word)


