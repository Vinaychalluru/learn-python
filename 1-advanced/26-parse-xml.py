# XML
#     - Root
#     - Child
#     - XML Document
#     - Elements
#     - Attributes
#     - Value

# In built Module - ElementTree

import xml.etree.ElementTree as et
import traceback

# Consists of functions which parses XML document
class XMLParser:
    def __init__(self, pFileName):
        self.tree = et.parse(pFileName)
        self.root = self.tree.getroot()
        print(f"Parsed XML Doc {pFileName}\n"
        f"The Root: {self.root.tag}")

    def displayAllChild(self):
        print("\nTo Display All Child & Sub-Elements ...")
        for vChild in self.root:  # for i in list
            print(f"\nChild : {vChild.tag} | Attrib : {vChild.attrib}")
            for vSubChild in vChild:
                print(f"SubChild : {vSubChild.tag} | Text : {vSubChild.text} | Attrib : {vSubChild.attrib}")

    def loopSpecficChildren(self, pChildName):
        print("\nTo Display Specific Child: ", pChildName)
        for vChild in self.root.iter(pChildName):
            print(f"\nChild : {vChild.tag} | Attrib : {vChild.attrib}")


    def fetchChildOnDemand(self, pChildName):
        print(f"\nTo Fetch & Display Specific Child Tags: {pChildName}")
        for vChild in self.root.findall(pChildName):
            vRank = vChild.find('rank').text
            vYear = vChild.find('year').text
            vName = vChild.get('name')

            print(f"\n{vName} had ranking - {vRank} in the year {vYear}")

    def updateRankOfCountry(self, pIncVal, vOutputFileName):
        print("\nAdd Element & Sub-Element")
        for vRank in self.root.iter('rank'):
            vRank.text = str(int(vRank.text) + pIncVal)
            vRank.set('updated', 'yes')
            # Adding element & sub-elements
            vNewElement = et.Element('survey')
            vNewSubElement = et.SubElement(vNewElement, 'date')
            vNewSubElement.text = '2018-07-01'
            vNewSubElement = et.SubElement(vNewElement, 'place')
            vNewSubElement.text = 'India'
            vRank.append(vNewElement)

        self.tree.write(vOutputFileName)
        print("\nOutput file is generated")


def main():
    vFileName = "../assets/sample-xml.xml"
    vOutputFileName = "../assets/output/parse-xml-output.xml"
    objXMLP = XMLParser(vFileName)
    objXMLP.displayAllChild()
    objXMLP.loopSpecficChildren('neighbor')
    objXMLP.fetchChildOnDemand('country')
    objXMLP.updateRankOfCountry(1, vOutputFileName)


try:
    xml_doc = et.parse("../assets/sample-xml.xml")  # XML Document
    xml_doc_root = xml_doc.getroot().tag

    xml_str = '<?xml version="1.0"?><data><title>Xml Parsing</title></data>'
    xml_str_root = et.fromstring(xml_str).tag

    # Print XML root using f-string
    print(f"The root of XML Document is '{xml_doc_root}'")
    print(f"The root of XML String is '{xml_str_root}'")

    main()

except Exception as e:
    traceback.print_exc()
else:
    print("No Exceptions Occurred")
