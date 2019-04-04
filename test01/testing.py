import xml.etree.ElementTree as ET
tree = ET.parse('Ado.xml')
root = tree.getroot()

#print(root[1][1].tag)
for act in root[1][1]:
    for scene in act[1:]:
        for part in scene:
            if str(part.tag)[-3:] == '}sp':
                for speech in part:
                    if str(speech.tag)[-2:] == '}p' or str(speech.tag)[-2:] == '}l':
                        for s in speech:
                            print(s.tag, s.attrib)
                            if s.tag[-1] == 'w':
                                print()







