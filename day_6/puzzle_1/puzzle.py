import sys
import os
import pprint


def main():
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    filepath = './input_file'
    input_array = []
    max_days = 80

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ### Read the input into an array of integers
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            input_array = [int(fish) for fish in line.split(',')]
    ### Pretty-Print the array
    # pp.pprint(input_array)
    ### Iterate over the number of days
    for days in range(max_days):
        calc_next_day(input_array)

    print("Fish count: {}".format(len(input_array)))

def calc_next_day(array):
    for i in range(len(array)):
        if array[i] == 0:
            array[i] = 6
            array.append( 8 )
            continue
        if array[i] > 0:
            array[i] -= 1


if __name__ == '__main__':
    main()