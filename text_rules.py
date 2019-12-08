#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jerry Bai'


class Rule:
    """
    Rules to detect if content match a type
    """

    def __init__(self):
        self.type = ""

    def match(self, block):
        pass

    def mark(self, block, handler):
        handler.start(self.type)
        handler.feedback(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    """
    Heading of file, a single line with less than 70 characters and not ended with ':'
    """

    def __init__(self):
        self.type = "heading"

    def match(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'


class TitleRule(HeadingRule):
    """
    Title of file, first heading of text
    """

    def __init__(self):
        self.type = "title"
        self.title_flag = True

    def match(self, block):
        if not self.title_flag:
            return False
        self.title_flag = False
        return HeadingRule.match(self, block)  # Suspend


class ListItemRule(Rule):
    """
    List item starts with '-'. When formatting these items, '-' should be removed first
    """

    def __init__(self):
        self.type = "listitem"

    def match(self, block):
        return block[0] == '-'

    def mark(self, block, handler):
        handler.start(self.type)
        handler.feedback(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(Rule):
    """
    List contains the whole consecutive list items
    """

    def __init__(self):
        self.type = "list"
        self.inside = False

    def match(self, block):
        return True

    def mark(self, block, handler):
        if not self.inside and ListItemRule.match(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.match(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ParagraphRule(Rule):
    """
    Paragraph is all blocks which could not match above rules
    """

    def __init__(self):
        self.type = "paragraph"

    def match(self, block):
        return True
