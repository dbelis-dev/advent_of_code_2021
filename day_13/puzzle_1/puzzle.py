import sys
import os
import pprint

max_x = 0
max_y = 0
coords_array = []
folds_array = []
paper_array = []
sec_array = []
counter = 0

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

    paper_array = [['.' for i in range(max_x + 1)] for j in range(max_y + 1)]
    print_paper()

    calculate_fold(0)

    print("================================================================")
    print("Result: {}".format(counter))


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

def fill_array_folds(line):
    drop1, drop2, fold = line.split(' ')
    dir_, div_ = fold.split('=')
    folds_array.append([dir_, int(div_)])

def print_paper():
    for x_, y_ in coords_array:
        paper_array[y_][x_] = '#'

def calculate_fold(index):
    dir_, div_ = folds_array[index]
    if dir_ == 'y':
        ## perform UP fold
        top_min_y = 0
        top_max_y = div_
        bottom_min_y = div_ + 1 
        bottom_max_y = max_y + 1
        print(dir_, div_, "UP")
        perform_up_fold(top_min_y, top_max_y, bottom_min_y, bottom_max_y)
    else:
        ## perform LEFT fold
        left_min_x = 0
        left_max_x = div_
        right_min_x = div_ + 1 
        right_max_x = max_x + 1
        print(dir_, div_, "LEFT")
        perform_left_fold(left_min_x, left_max_x, right_min_x, right_max_x)

def perform_up_fold(top_min_y, top_max_y, bottom_min_y, bottom_max_y):
    mirror = 2
    global counter
    global sec_array
    for j in range(bottom_min_y, bottom_max_y):
        for i in range(max_x + 1):
            if paper_array[j][i] == '#':
                paper_array[j - mirror][i] = '#'
        mirror += 2
    for j in range(top_min_y, top_max_y):
        for i in range(max_x + 1):
            if paper_array[j][i] == '#':
                counter += 1
    ## print top paper
    sec_array = [[paper_array[j][i] for i in range(max_x + 1)] for j in range(top_max_y)]

def perform_left_fold(left_min_x, left_max_x, right_min_x, right_max_x):
    mirror = 2
    global counter
    global sec_array
    for i in range(right_min_x, right_max_x):
        for j in range(max_y + 1):
            if paper_array[j][i] == '#':
                paper_array[j][i - mirror] = '#'
        mirror += 2
    for i in range(left_min_x, left_max_x):
        for j in range(max_y + 1):
            if paper_array[j][i] == '#':
                counter += 1
    ## print left paper
    sec_array = [[paper_array[j][i] for i in range(left_max_x)] for j in range(max_y + 1)]


if __name__ == '__main__':
    main()