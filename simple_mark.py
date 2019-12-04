#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jerry Bai'

import sys, re
from util import blocks


title = True
for block in blocks(sys.stdin):
    # Substitute ** for <em> flag
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    block = re.sub(r'\(http://wwspam\.fu/(.+)\)', r'<a href="http://wwspam\.fu/\1">\1</a>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')

print('</body></html>')

