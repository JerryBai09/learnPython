#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jerry Bai'


def lines(file):
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line.replace('\n', ' '))
        elif block:
            yield ''.join(block).strip()
            block = []


if __name__ == '__main__':
    with open('test_input.txt', 'r') as f:
        for block in blocks(f):
            print(block)
