import sys
import os
import math

def main():
    filepath = './input_file'
    counter = 0
    current_value = 0

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath) as fp:
        for depth in fp:
            if int(depth) > current_value:
                counter += 1
            current_value = int(depth)

    print("Number of increaces: {}".format(counter-1))

if __name__ == '__main__':
    main()
