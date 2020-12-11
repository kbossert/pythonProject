
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

class EAD2002DTDValidator():
    "Validation according to the EAD 2002 DTD."

    # DTD
    def __init__(self):
       with resource_stream(__name__, 'data/schemas/ead.dtd') as fh:
           self._dtd = etree.DTD(fh)

    # RNG
#    def __init__(self):
#        with resource_stream(__name__, 'data/schemas/ead.rng') as fh:
#            xmlschema_doc = etree.parse(fh)
#            self._dtd = etree.RelaxNG(xmlschema_doc)

    # XSD
#    def __init__(self):
#        with resource_stream(__name__, 'data/schemas/ead.xsd') as fh:
#            xmlschema_doc = etree.parse(fh)
#            self._dtd = etree.XMLSchema(xmlschema_doc)

    @property
    def dtd(self):
        "Get the DTD."
        return self._dtd

    @property
    def errors(self):
        "Get any errors that occurred while validating"
        return self.dtd.error_log.filter_from_errors()

    def validate(self, ead):
        return self.dtd.validate(ead)

class EAD2002XSDValidator():
    "Validation according to the EAD 2002 DTD."

    # DTD
    def __init__(self):
       with resource_stream(__name__, 'data/schemas/ead.dtd') as fh:
           self._dtd = etree.DTD(fh)

    # RNG
#    def __init__(self):
#        with resource_stream(__name__, 'data/schemas/ead.rng') as fh:
#            xmlschema_doc = etree.parse(fh)
#            self._dtd = etree.RelaxNG(xmlschema_doc)

    # XSD
#    def __init__(self):
#        with resource_stream(__name__, 'data/schemas/ead.xsd') as fh:
#            xmlschema_doc = etree.parse(fh)
#            self._dtd = etree.XMLSchema(xmlschema_doc)

    @property
    def dtd(self):
        "Get the DTD."
        return self._dtd

    @property
    def errors(self):
        "Get any errors that occurred while validating"
        return self.dtd.error_log.filter_from_errors()

    def validate(self, ead):
        return self.dtd.validate(ead)

class EAD2002RNGValidator():
    "Validation according to the EAD 2002 DTD."

    # DTD
    def __init__(self):
       with resource_stream(__name__, 'data/schemas/ead.dtd') as fh:
           self._dtd = etree.DTD(fh)

    # RNG
#    def __init__(self):
#        with resource_stream(__name__, 'data/schemas/ead.rng') as fh:
#            xmlschema_doc = etree.parse(fh)
#            self._dtd = etree.RelaxNG(xmlschema_doc)

    # XSD
#    def __init__(self):
#        with resource_stream(__name__, 'data/schemas/ead.xsd') as fh:
#            xmlschema_doc = etree.parse(fh)
#            self._dtd = etree.XMLSchema(xmlschema_doc)

    @property
    def dtd(self):
        "Get the DTD."
        return self._dtd

    @property
    def errors(self):
        "Get any errors that occurred while validating"
        return self.dtd.error_log.filter_from_errors()

    def validate(self, ead):
        return self.dtd.validate(ead)

class EAD3DTDValidator():
    "Validation according to the EAD 2002 DTD."

    # DTD
    def __init__(self):
       with resource_stream(__name__, 'data/schemas/ead.dtd') as fh:
           self._dtd = etree.DTD(fh)

    # RNG
#    def __init__(self):
#        with resource_stream(__name__, 'data/schemas/ead.rng') as fh:
#            xmlschema_doc = etree.parse(fh)
#            self._dtd = etree.RelaxNG(xmlschema_doc)

    # XSD
#    def __init__(self):
#        with resource_stream(__name__, 'data/schemas/ead.xsd') as fh:
#            xmlschema_doc = etree.parse(fh)
#            self._dtd = etree.XMLSchema(xmlschema_doc)

    @property
    def dtd(self):
        "Get the DTD."
        return self._dtd

    @property
    def errors(self):
        "Get any errors that occurred while validating"
        return self.dtd.error_log.filter_from_errors()

    def validate(self, ead):
        return self.dtd.validate(ead)

class EAD3XSDValidator():
    "Validation according to the EAD3 XSD."

    # XSD
   def __init__(self):
       with resource_stream(__name__, 'data/schemas/ead.xsd') as fh:
           xmlschema_doc = etree.parse(fh)
           self._dtd = etree.XMLSchema(xmlschema_doc)

    @property
    def dtd(self):
        "Get the DTD."
        return self._dtd

    @property
    def errors(self):
        "Get any errors that occurred while validating"
        return self.dtd.error_log.filter_from_errors()

    def validate(self, ead):
        return self.dtd.validate(ead)

class EAD3RNGValidator():
    "Validation according to the EAD3 RNG."

    #RNG
    def __init__(self):
        with resource_stream(__name__, 'data/schemas/ead3.rng') as fh:
            xmlschema_doc = etree.parse(fh)
            self._dtd = etree.RelaxNG(xmlschema_doc)

    @property
    def dtd(self):
        "Get the DTD."
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
    files = ['data/testfiles/ead3_valid_rng.xml']
    is_xsd = False

    for filepath in files:
        # Check for well-formedness by attempting to parse the file
        try:
            with open(filepath) as fh:
                try:
                    ead = etree.parse(fh)

                    # XSD check from Brian's GitHub code https://github.com/eadhost/eadator
                    ead2002ns = ead.xpath("//*[namespace-uri()='urn:isbn:1-931666-22-9']")
                    if ead2002ns:
                        is_xsd = True

                except etree.XMLSyntaxError as e:
                    print("Not well-formed XML: %s", e)
                    # Increment XML error count
                    xml_error_count += 1
                    # Skip to next file
                    continue
        except IOError as e:
            # Log non existent file
            print("%s: %s", str(e.args[1]), filepath)
            # Skip to next file
            continue

        validator = EAD3RNGValidator()
        if validator.validate(ead):
            print("SUCCESS! %s PASSED %s",
                         filepath,
                         validator.__class__.__doc__)
        else:
            print('\n'.join([str(e) for e in validator.errors]))
            # Increment DTD error count
            dtd_error_count += len(validator.errors)
            dtd_error_file_count += 1
            # Skip to next file
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
