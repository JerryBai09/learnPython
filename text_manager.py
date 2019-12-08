#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jerry Bai'

import sys

from text_parser import Parser
from text_rules import *
from text_handler import Handler


class HTMLRender(Handler):
    """
    Mark a text file to HTML format
    """

    def start_document(self):
        print('<html><head><title>...</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2>')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul>')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)

    def sub_url(self, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))

    def sub_mail(self, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))

    def feedback(self, data):
        print(data)

class HtmlParser(Parser):
    """
    Parse plain text with basic html rules
    """

    def __init__(self, handler):
        super(HtmlParser, self).__init__(handler)
        self.addRules(ListRule())
        self.addRules(ListItemRule())
        self.addRules(TitleRule())
        self.addRules(HeadingRule())
        self.addRules(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


def main():
    handler = HTMLRender()
    parser = HtmlParser(handler)

    parser.parse(sys.stdin)


if __name__ == '__main__':
    main()
