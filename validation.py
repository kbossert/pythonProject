
# code initiated from https://github.com/bloomonkey/ead-toolbox
# keep this one in mind for more detailed validation https://github.com/UAlbanyArchives/EADValidator

# Formats to consider
# EAD (2002)
# EAD 3
# EAD with embedded pdf reference
# MARC -> MARCXML -> MODS
# PDF (with properties and without)
# HTML (with JSON, schema.org)
# HTML (without JSON, presumedly nonstandard)
# Standard Office Tools (Word, Excel, PowerPoint, heck maybe Notepad)

from lxml import etree
from pkg_resources import resource_stream

class ValidationFiles:
    EAD_2002_DTD = 'data/schemas/ead.dtd'
    EAD_2002_XSD = 'data/schemas/ead.xsd'
    EAD_2002_RNG = 'data/schemas/ead.rng'
    EAD_3_DTD = 'data/schemas/ead3.dtd'
    EAD_3_XSD = 'data/schemas/ead3.xsd'
    EAD_3_RNG = 'data/schemas/ead3.rng'

class EADValidation():
    "Schema validation containing various EAD variations"

    # Set up the validation file
    def __init__(self, validation_file):
        if validation_file == ValidationFiles.EAD_3_XSD:
            with resource_stream(__name__, validation_file) as fh:
                xmlschema_doc = etree.parse(fh)
                self._dtd = etree.XMLSchema(xmlschema_doc)
        elif validation_file == ValidationFiles.EAD_2002_DTD:
            with resource_stream(__name__, validation_file) as fh:
                self._dtd = etree.DTD(validation_file)
        elif validation_file == ValidationFiles.EAD_3_RNG:
            with resource_stream(__name__, validation_file) as fh:
                xmlschema_doc = etree.parse(fh)
                self._dtd = etree.RelaxNG(xmlschema_doc)
        elif validation_file == ValidationFiles.EAD_2002_XSD:
            with resource_stream(__name__, validation_file) as fh:
                xmlschema_doc = etree.parse(fh)
                self._dtd = etree.XMLSchema(xmlschema_doc)
        elif validation_file == ValidationFiles.EAD_2002_RNG:
            with resource_stream(__name__, validation_file) as fh:
                xmlschema_doc = etree.parse(fh)
                self._dtd = etree.RelaxNG(xmlschema_doc)
        elif validation_file == ValidationFiles.EAD_3_DTD:
            with resource_stream(__name__, validation_file) as fh:
                self._dtd = etree.DTD(validation_file)
        else:
            # Add other formats as examples are found
            print("EAD format not found")

    @property
    def dtd(self):
        return self._dtd

    @property
    def errors(self):
        "Get any errors that occurred while validating"
        return self.dtd.error_log.filter_from_errors()

    def validate(self, ead):
        return self.dtd.validate(ead)


def validate():
    xml_error_count = 0
    dtd_error_count = 0
    dtd_error_file_count = 0
    # The ead3 RNG file has a validation error on an invalid attribute on the origination element
    files = ['data/testfiles/ead3_valid_rng.xml', 'data/testfiles/ead3_valid_xsd.xml', 'data/testfiles/ead_2002_valid_dtd.xml', 'data/testfiles/ead_2002_valid_xsd.xml']
    files = ['data/testfiles/bailey.xml']

    for filepath in files:
        # Check for well-formedness by attempting to parse the file
        validation_file = ValidationFiles.EAD_2002_DTD
        try:
            with open(filepath) as fh:
                try:
                    ead = etree.parse(fh)
                except etree.XMLSyntaxError as e:
                    print("Not well-formed XML: %s", e)
                    xml_error_count += 1
                    continue

            with open(filepath) as fh:
                xml = fh.read()
                if 'ead3.xsd' in xml:
                    validation_file = ValidationFiles.EAD_3_XSD
                elif 'ead3.rng' in xml:
                    validation_file = ValidationFiles.EAD_3_RNG
                elif 'ead.xsd' in xml:
                    validation_file = ValidationFiles.EAD_2002_XSD
                elif 'ead.rng' in xml:
                    validation_file = ValidationFiles.EAD_2002_RNG

        except IOError as e:
            # Log non existent file
            print("%s: %s", str(e.args[1]), filepath)
            continue

        # Validate the file
        validator = EADValidation(validation_file)
        if validator.validate(ead):
            print("SUCCESS! %s PASSED %s",
                         filepath,
                         validator.__class__.__doc__)
        else:
            print('\n'.join([str(e) for e in validator.errors]))
            # Increment DTD error count
            dtd_error_count += len(validator.errors)
            dtd_error_file_count += 1
            continue

    # Print a summary of any errors
    if xml_error_count:
        print("XML errors = {0}".format(xml_error_count))

    if dtd_error_count:
        print("Files with EAD DTD errors = {0}"
                     "".format(dtd_error_file_count)
                     )
        print("Total EAD DTD errors = {0}"
                     "".format(dtd_error_count)
                     )
    print(xml_error_count + dtd_error_file_count)
    return


validate()
