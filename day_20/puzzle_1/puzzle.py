import sys
import os
import pprint


def main():
    global paper_array
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    filepath = './input_file'

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ### Read the input into an array of integers
    read_array_in(filepath)

    print_paper()


    print("================================================================")
    # print("Result: {}".format(counter))


### Iterate over the lines in the file
def read_array_in(filepath):
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            line = line.rstrip()
            if line != '':
                if line[0].isnumeric():
                    fill_array_coords(line)
                else:
                    fill_array_folds(line)

def fill_array_coords(line):
    global max_x, max_y
    x_, y_ = line.split(',')
    coords_array.append([int(x_), int(y_)])
    if max_x < int(x_):
        max_x = int(x_)
    if max_y < int(y_):
        max_y = int(y_)

def print_paper():
    for x_, y_ in coords_array:
        paper_array[y_][x_] = '#'



if __name__ == '__main__':
    main()