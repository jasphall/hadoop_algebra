#!/usr/bin/python
import sys

LEFT_SET_SYMBOL = 'A'


def main():
    current_key = None
    current_value = set()

    for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')

        if key != current_key:
            if len(current_value) == 1 and current_value.pop() == LEFT_SET_SYMBOL:
                print(str(current_key) + '\t' + str(current_key))

            current_key = key
            current_value = set([value])
        else:
            current_value.add(value)

    if len(current_value) == 1 and current_value.pop() == LEFT_SET_SYMBOL:
        print(str(current_key) + '\t' + str(current_key))

main()