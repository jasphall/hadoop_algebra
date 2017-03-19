#!/usr/bin/python
import sys


def main():
    current_key = None
    current_relation = None
    current_value = None

    for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')

        value = trim_characters(value, ['(', ')'])

        value_splitted = value.split(',')
        relation = value_splitted[0]
        value_splitted.remove(relation)
        value = value_splitted

        value_res = ''
        for index, v in enumerate(value):
            if index != len(value)-1:
                value_res += v + '\t'
            else:
                value_res += v

        value_res = trim_characters(value_res, ['[', ']'])

        if current_key != key:
            current_key = key
            current_value = value_res
            current_relation = relation
        else:
            if relation != current_relation:
                print(str(key) + '\t(' + str(current_value) + '\t' + str(key) + '\t' + str(value_res) + ')')

def trim_characters(text, characters):
    for char in characters:
        if char in text:
            text = text.replace(char, '')
    return text

main()