import sys
import os
import pprint


def main():
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    filepath = './input_file'
    input_array = []
    fuel_array = []

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ### Read the input into an array of integers
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            input_array = [int(h_pos) for h_pos in line.split(',')]
    
    max_pos = find_max_pos(input_array)
    fuel_array = [0 for x in range(max_pos)]

    ### Go through all the pos (for 0 to max_pos)
    ### and get the sum of all steps for each pos
    for j in range(len(fuel_array)):
        min_fuel = 9999999
        sum = 0
        for i in range(len(input_array)):
            sum += abs(input_array[i] - j)
        if min_fuel > sum:
            min_fuel = sum
            fuel_array[j] = min_fuel
    
    ### Find the minimum fuel value in the array
    min_fuel = 9999999
    for i in range(len(fuel_array)):
        if fuel_array[i] < min_fuel:
            min_fuel = fuel_array[i]
    
    print("================================================================")
    # pp.pprint(fuel_array)
    print("Result: {}".format(min_fuel))

### Find the maximum position in the input array
def find_max_pos(array):
    max_pos = 0
    for pos in array:
        if pos > max_pos:
            max_pos = pos
    return max_pos

if __name__ == '__main__':
    main()