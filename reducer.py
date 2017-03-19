#!/usr/bin/python

import sys


def main():

    current_key = None

    for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')

        if key != current_key:
            print(str(key) + '\t' + str(value))
            current_key = key

main()