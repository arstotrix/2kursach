import xml.etree.ElementTree as ET
import re
tree = ET.parse('Ado.xml')
root = tree.getroot()

#print(root.tag) #tag = idk wtf this is
#print(root.attrib) #attributes i guess

#print(root[1][1].tag)
for act in root[1][1]:
    #print(act.tag, act.attrib)
    for scene in root.findall('w'):
        print(scene.tag)



