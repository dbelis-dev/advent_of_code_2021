import sys
import os
import pprint
from datetime import datetime


def main():
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    filepath = './input_file'
    input_array = [int(0) for i in range(9) ]
    max_days = 256
    count_ = 0

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ### Read the input into an array of integers
    with open(filepath, 'r') as fp:
        line = fp.readline()
        for fish in line.split(','):
            input_array[int(fish)] += 1

    ### Pretty-Print the array
    # pp.pprint(input_array)
    ### Iterate over the number of days
    for days in range(max_days):
        calc_next_day(input_array)
    ### Sum up all the elements
    for i in range(len(input_array)):
        count_ += input_array[i]
        
    print("Fish count: {}".format(count_))

def calc_next_day(array):
    regen =  array[0]
    for i in range(1, len(array)):
        array[i-1] = array[i]
        array[i] = 0
    array[6] += regen
    array[8] += regen


if __name__ == '__main__':
    main()