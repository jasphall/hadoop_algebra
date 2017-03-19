#!/usr/bin/python

import sys


def main():

    current_key = None
    current_value = None
    current_key_counter = 0

    for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')

        if key == current_key:
            current_key_counter += 1
        else:
            if current_key_counter == 2:
                print(str(current_key) + '\t' + str(current_value))
            current_key = key
            current_value = value
            current_key_counter = 1

    if current_key_counter == 2:
        print(str(current_key) + '\t' + str(current_value))

main()