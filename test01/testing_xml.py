import xml.etree.ElementTree as ET
tree = ET.parse('Ado.xml')
root = tree.getroot()

#print(root.tag) #tag = idk wtf this is
#print(root.attrib) #attributes i guess

#print(root[1][1].tag)
for act in root[1][1]:
    #print(r.tag, r.attrib)
    for scene in act[1:]:
        print(scene.tag, scene.attrib)
        for part in scene:
            if str(part.tag) == '{http://www.tei-c.org/ns/1.0}sp':
                print(part.tag, part.attrib)



