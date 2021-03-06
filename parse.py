
import os
import sys
from io import StringIO
from lxml import etree
from pkg_resources import resource_stream

def parse():
    # The ead3 RNG file has a validation error on an invalid attribute on the origination element
    files = ['data/testfiles/ead3_valid_rng.xml', 'data/testfiles/ead3_valid_xsd.xml', 'data/testfiles/ead_2002_valid_dtd.xml', 'data/testfiles/ead_2002_valid_xsd.xml']
    files = ['data/testfiles/ead_2002_valid_dtd.xml']
    # files = ['data/testfiles/x.xml']

    for filepath in files:
        # Check for well-formedness by attempting to parse the file

        ead = None
        dtd = True

        try:
            with open(filepath) as fh:
                xml = fh.read()
                if 'ead.xsd' in xml or 'ead3.xsd' in xml or 'ead.rng' in xml or 'ead3.rng' in xml:
                    dtd = False
                    start = xml.find('ead')
                    end = xml.find('>', start)
                    y = xml[0:start + 3]
                    z = xml[end:len(xml)]
                    xml = y + z
                    ead = etree.parse(StringIO(xml))

            if dtd:
                with open(filepath) as fh:
                    ead = etree.parse(fh)

            root = ead.getroot()
            print(root.find("archdesc/did/unittitle").text)



                    # for element in root.iter():
                    #     for name, value in sorted(element.items()):
                    #         print('%s = %r' % (name, value))
                    #     print("%s - %s" % (element.tag, element.text))

            # tree = etree.ElementTree(root)
            # for e in root.iter():
            #     print(tree.getpath(e), e.text)

        except etree.XMLSyntaxError as e:
            print("Not well-formed XML: %s", e)

    return

def xsd():

    x = etree.XMLSchema(file='data/schemas/ead.xsd')
    parser = etree.XMLParser(schema=x)
    tree = etree.parse('data/testfiles/ead_2002_valid_xsd.xml', parser)
    root = tree.getroot()
    namespaces = {'ns': 'data/schemas/ead.xsd'}

    # tree = etree.ElementTree(root)
    # for e in root.iter():
    #     print(tree.getelementpath(e), e.text)
    p = "{urn:isbn:1-931666-22-9}"
    search = p + 'archdesc/' + p + 'did/' + p + 'unittitle'
    print(root.find(search).text)
    # print(root.find("{urn:isbn:1-931666-22-9}archdesc/{urn:isbn:1-931666-22-9}dsc/{urn:isbn:1-931666-22-9}c[3]/{urn:isbn:1-931666-22-9}c[102]/{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}unittitle").text)

    # table = root.find('{urn:isbn:1-931666-22-9}archdesc/{urn:isbn:1-931666-22-9}dsc/{urn:isbn:1-931666-22-9}c[3]/{urn:isbn:1-931666-22-9}c[102]/{urn:isbn:1-931666-22-9}did/{urn:isbn:1-931666-22-9}unittitle')

    items = iter(root.xpath('//ns:eadheader/filedesc/titlestmt/titleproper/text()',
                            namespaces=namespaces))
    # for title in zip(*[items] * 2):
    #     print(title)
    for title in items:
        print(title)


parse()
xsd()