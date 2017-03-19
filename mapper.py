#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def main():

    for line in sys.stdin:
        line = line.strip()
        elements = line.split('\t')
        if len(elements) > 1:
            el = int(elements[1])
            print(str(el) + '\t' + str(el))

main()
