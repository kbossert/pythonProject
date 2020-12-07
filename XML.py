import lxml

# root.find() will navigate down the document tree to find children
# root.xpath() will return a matching element using an XPATH query as a sting
# root.tag will show the element’s name
# root.text will show any text contained by the element
# root.attrib will provide an dictionary of an element’s attributes
# To get an attribute, use root.attib[“attributeName”]
# root.tail will show any text after the element for mixed content

from lxml import etree as ET

# enter a path to the XML file here
windowsPath = "ead.xml"
xmlObject = ET.parse(windowsPath)

# root is the top-level <ead> tag
root = xmlObject.getroot()

collectionName = root.find("archdesc/did/unittitle").text
print("We are working with " + collectionName)
print(root.find("archdesc/did/unitdate").text)
