import sys
import os
import pprint

rows = 10
cols = 10
input_array = [[0 for j in range(cols)] for i in range(rows)]
sum_flashes = 0

def main():
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    filepath = './input_file'

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ### Read the input into an array of integers
    read_array_in(filepath, cols, input_array)
    print("Original Input")
    pp.pprint(input_array)
    for k in range(100):
        next_step()

    print("================================================================")
    print("Result: {}".format(sum_flashes))

### Calculate a single step
def next_step():
    for i in range(rows):
        for j in range(cols):
            ## increase every element by one
            input_array[i][j] += 1
    
    found_flashing_oct = False
    while True:
        found_flashing_oct = False
        for i in range(rows):
            for j in range(cols):
                if input_array[i][j] == 10:
                    input_array[i][j] = -1
                    flash_adjacent(i, j)
                    found_flashing_oct = True
        if found_flashing_oct == False:
            break

    zero_energy()
    # print("=== After step ===")
    # pp.pprint(input_array)

### For the particular index, find all adjacent oct
### and increase by 1
def flash_adjacent(pos_i, pos_j):
    start_pos_i = pos_i - 1
    end_pos_i = pos_i + 2
    start_pos_j = pos_j - 1
    end_pos_j = pos_j + 2
    if pos_i - 1  < 0:
        start_pos_i = 0
    if pos_i + 2 > cols - 1:
        end_pos_i = cols
    if pos_j - 1  < 0:
        start_pos_j = 0
    if pos_j + 2 > rows - 1:
        end_pos_j = rows
    for i in range(start_pos_i, end_pos_i):
        for j in range(start_pos_j, end_pos_j):
            ## do not update same element
            if pos_i == i and pos_j == j:
                continue
            # if input_array[i][j] < 10:
            if input_array[i][j] != -1 and input_array[i][j] != 10:
                ## increase by one due to flash
                input_array[i][j] += 1

### Reset to zero all flashed actopuses
def zero_energy():
    global sum_flashes
    for i in range(rows):
        for j in range(cols):
            if input_array[i][j] == -1:
                sum_flashes += 1
                input_array[i][j] = 0

### Iterate over the lines in the file
def read_array_in(filepath, cols, array):
    row = 0;
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            fill_array(cols, row, line, array)
            row += 1

### Read each char and add it to the array
def fill_array(cols, row, line, array):
    for col in range(cols):
        char_in = line[col]
        if char_in == '\n':
            print("End of line")
            return
        array[row][col] = int(char_in)

if __name__ == '__main__':
    main()