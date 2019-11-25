#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jerry Bai'

import sys
import re
import os


def format(comment):
    # match <comment> </comment>
    content = ""
    if comment:
        for line in comment:
            content += '* '
            content += line
            content += '\n'
    return content


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        f.seek(0)
        text = f.read()
        emphasis_pattern = r'<comment>([\w\W]*?)</comment>'
        comment_mark = re.search(emphasis_pattern, text)
        comment = []
        if comment_mark:
            comment = comment_mark.group(1).strip().split('\n')
        else:
            print("comment not found")
        content = format(comment)
        prefix_comment = r"/**************************************\n"
        postfix_comment = r"**************************************/"
        content = prefix_comment + content + postfix_comment
        text = re.sub(emphasis_pattern, content, text)
        temp_file = ""
        if text:
            temp_file = sys.argv[1] + "_bak"
            with open(temp_file, 'w') as format_file:
                format_file.write(text)
        else:
            print("No output text")

        if temp_file:
            os.system(r'mv %s %s' % (temp_file, sys.argv[1]))
        else:
            print("No format execution")