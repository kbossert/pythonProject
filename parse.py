
import os
import sys
from io import StringIO
from lxml import etree
from pkg_resources import resource_stream

def parse():
    # The ead3 RNG file has a validation error on an invalid attribute on the origination element
    files = ['data/testfiles/ead3_valid_rng.xml', 'data/testfiles/ead3_valid_xsd.xml', 'data/testfiles/ead_2002_valid_dtd.xml', 'data/testfiles/ead_2002_valid_xsd.xml']
    files = ['data/testfiles/ead_2002_valid_dtd.xml']
    files = ['data/testfiles/x.xml']

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

            tree = etree.ElementTree(root)
            for e in root.iter():
                print(tree.getpath(e), e.text)

        except etree.XMLSyntaxError as e:
            print("Not well-formed XML: %s", e)

    return

parse()