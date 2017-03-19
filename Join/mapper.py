#!/usr/bin/python

import sys

R_NAME = 'Orders'
S_NAME = 'Customers'
JOIN_COLUMN_R = 2
JOIN_COLUMN_S = 1


def main():

    for line in sys.stdin:
        line = line.strip()
        elements = line.split('\t')
        name_column = elements[0]

        if name_column == R_NAME:
            join_column = elements[JOIN_COLUMN_R]
            elements.remove(name_column)
            elements.remove(join_column)
            print(str(join_column) + '\t(' + str(R_NAME) + ',' + str(elements) + ')')

        else:
            if name_column == S_NAME:
                join_column = elements[JOIN_COLUMN_S]
                elements.remove(name_column)
                elements.remove(join_column)
                print(str(join_column) + '\t(' + str(S_NAME) + ',' + str(elements) + ')')

main()
