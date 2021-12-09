import sys
import os
import pprint


def main():
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    filepath = './input_file'
    rows = 100
    cols = 100
    input_array = [[0 for j in range(cols)] for i in range(rows)]
    sec_array = [[9 for j in range(cols)] for i in range(rows)]
    sum_depths = 0

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ### Read the input into an array of integers
    read_array_in(filepath, cols, input_array)

    for i in range(rows):
        for j in range(cols):
            is_minimum = False
            ## Check if above is lower
            if i > 0:
                top = input_array[i-1][j]
                if input_array[i][j] < top:
                    is_minimum = True
                else:
                    continue
            ## Check if below is lower
            if i+1 < rows:
                bottom = input_array[i+1][j]
                if input_array[i][j] < bottom:
                    is_minimum = True
                else:
                    continue
            ## Check if previous is lower
            if j > 0:
                left = input_array[i][j-1]
                if input_array[i][j] < left:
                    is_minimum = True
                else:
                    continue
            ## Check if next is lower
            if j+1 < cols:
                right = input_array[i][j+1]
                if input_array[i][j] < right:
                    is_minimum = True
                else:
                    continue
            if is_minimum:
                sec_array[i][j] = input_array[i][j]
                sum_depths += input_array[i][j] + 1
        # print()
    
    print("================================================================")
    print("Result: {}".format(sum_depths))
    # pp.pprint(sec_array)

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