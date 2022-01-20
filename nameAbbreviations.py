'''
Small python script that prints
 all abbreviations of first-name/last-name combo.
'''

import sys


def name_abbreviations(first, last):
    ''' Takes two (2) arguments and returns a list of abbriviations.
    \nFirst : String
    \nLast : String
    \nReturn : List
    '''

    abbreviations = []
    for i in range(len(first)):
        for k in range(len(last)):
            if len(first[:i+1]+last[:k+1]) <= 8:
                abbreviations.append(first[:i+1]+last[:k+1])

    return abbreviations


if __name__ == "__main__":
    # Print abbreviations if arguments are provided
    # Otherwise, print usage help
    if len(sys.argv) > 2:
        print("\n".join(name_abbreviations(sys.argv[1], sys.argv[2])))
    else:
        print("\nUsage: "
              + sys.argv[0][len(sys.argv[0])-sys.argv[0][::-1].find('\\'):]
              + " first-name last-name")
