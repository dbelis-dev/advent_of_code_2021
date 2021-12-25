import sys
import os
import pprint

min_x = 0
min_y = 0
max_x = 139
max_y = 137
deep_array = [] #[['.' for x in range(max_x)] for y in range(max_y)]
next_step = True

def main():
    global pp
    global deep_array, max_x, max_y, next_step
    pp = pprint.PrettyPrinter(indent=4)
    filepath = './input_file'

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ### Read the input into an array of integers
    read_array_in_template(filepath)
    print_array(deep_array)

    step = 0
    while next_step:
        next_step = False
        step += 1
        print("=== Step {}".format(step))
        y_ = min_y
        while y_ < max_y:
            x_ = min_x
            while x_ < max_x:
                if check_adjacent(x_, y_, '>'):
                    next_step = True
                    x_ += 1
                x_ += 1
            y_ += 1
        # print_array(deep_array)
        for y in range(max_y):
            for x in range(max_x):
                if deep_array[y][x] == '*':
                   deep_array[y][x] = '.'
        x_ = min_x
        while x_ < max_x:
            y_ = min_y
            while y_ < max_y:
                if check_adjacent(x_, y_, 'v'):
                    next_step = True
                    y_ += 1
                y_ += 1
            x_ += 1
        # print_array(deep_array)
        for y in range(max_y):
            for x in range(max_x):
                if deep_array[y][x] == '*':
                   deep_array[y][x] = '.' 
    print()
    print_array(deep_array)

    print("================================================================")
    # print("Result: {}".format(max-min))


def check_adjacent(x, y, direction):
    # global min_x, min_y
    # print(x, y)
    next_x = x
    next_y = y

    if direction == '>':
        next_x = x + 1
        # print("Checking RIGHT {},{}".format(next_x, y))
        if next_x == len(deep_array[0]):
            # print(" Wrapping on X")
            next_x = min_x
    if direction == 'v':
        next_y = y + 1
        # print("Checking DOWN {},{}".format(x, next_y))
        if next_y == len(deep_array):
            # print(" Wrapping on Y")
            next_y = min_y
    
    # print("Testing NEXT {},{}".format(next_x, next_y))
    if deep_array[next_y][next_x] == '.' and deep_array[y][x] == direction:
        ## move to next right
        # print("    Moving {} to {},{}".format(direction, next_x, next_y))
        deep_array[y][x] = '*'
        deep_array[next_y][next_x] = direction
        return True
    
    return False

### Iterate over the lines in the file
def read_array_in_template(filepath):
    global initial_template
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            line = line.rstrip()
            row = []
            for char in line:
                row.append(char)
            deep_array.append(row)

### Pretty-print the array
def print_array(array):
    for i in array:
        for j in i:
            print(j, end='')
        print()


if __name__ == '__main__':
    main()