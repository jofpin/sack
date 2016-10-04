"""Use the HTMLParser library to parse HTML files that aren't too bad."""

__all__ = [
    'HTMLParserTreeBuilder',
    ]

try:
    from html.parser import HTMLParser
    CONSTRUCTOR_TAKES_STRICT = True
except ImportError, e:
    from HTMLParser import HTMLParser
    CONSTRUCTOR_TAKES_STRICT = False
from libs.bs4.element import (
    CData,
    Comment,
    Declaration,
    Doctype,
    ProcessingInstruction,
    )
from libs.bs4.dammit import EntitySubstitution, UnicodeDammit

from libs.bs4.builder import (
    HTML,
    HTMLTreeBuilder,
    STRICT,
    )


HTMLPARSER = 'html.parser'

class HTMLParserTreeBuilder(HTMLParser, HTMLTreeBuilder):

    is_xml = False
    features = [HTML, STRICT, HTMLPARSER]

    def __init__(self, *args, **kwargs):
        if CONSTRUCTOR_TAKES_STRICT:
            kwargs['strict'] = True
        return super(HTMLParserTreeBuilder, self).__init__(*args, **kwargs)

    def prepare_markup(self, markup, user_specified_encoding=None,
                       document_declared_encoding=None):
        """
        :return: A 3-tuple (markup, original encoding, encoding
        declared within markup).
        """
        if isinstance(markup, unicode):
            return markup, None, None

        try_encodings = [user_specified_encoding, document_declared_encoding]
        dammit = UnicodeDammit(markup, try_encodings, isHTML=True)
        return (dammit.markup, dammit.original_encoding,
                dammit.declared_html_encoding)

    def feed(self, markup):
        super(HTMLParserTreeBuilder, self).feed(markup)

    def handle_starttag(self, name, attrs):
        self.soup.handle_starttag(name, dict(attrs))

    def handle_endtag(self, name):
        self.soup.handle_endtag(name)

    def handle_data(self, data):
        self.soup.handle_data(data)

    def handle_charref(self, name):
        # XXX workaround for a bug in HTMLParser. Remove this once
        # it's fixed.
        if name.startswith('x'):
            data = unichr(int(name.lstrip('x'), 16))
        else:
            data = unichr(int(name))
        self.handle_data(data)

    def handle_entityref(self, name):
        character = EntitySubstitution.HTML_ENTITY_TO_CHARACTER.get(name)
        if character is not None:
            data = character
        else:
            data = "&%s;" % name
        self.handle_data(data)

    def handle_comment(self, data):
        self.soup.endData()
        self.soup.handle_data(data)
        self.soup.endData(Comment)

    def handle_decl(self, data):
        self.soup.endData()
        if data.startswith("DOCTYPE "):
            data = data[len("DOCTYPE "):]
        self.soup.handle_data(data)
        self.soup.endData(Doctype)

    def unknown_decl(self, data):
        if data.upper().startswith('CDATA['):
            cls = CData
            data = data[len('CDATA['):]
        else:
            cls = Declaration
        self.soup.endData()
        self.soup.handle_data(data)
        self.soup.endData(cls)

    def handle_pi(self, data):
        self.soup.endData()
        self.soup.handle_data(data)
        self.soup.endData(ProcessingInstruction)

