import sys
import os
import pprint

sum_basin = 0

def main():
    global pp
    pp = pprint.PrettyPrinter(indent=2)
    filepath = './input_file'
    global rows
    global cols
    rows = 100
    cols = 100
    input_array = [[0 for j in range(cols)] for i in range(rows)]
    sec_array = [[9 for j in range(cols)] for i in range(rows)]
    bassin_array = []
    sum_depths = 0
    global sum_basin

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ### Read the input into an array of integers
    read_array_in(filepath, input_array)
    
    ### Find all the low points in the array and
    ### and calculate to risk level and total
    sum_depths = find_low_points(input_array, sec_array, sum_depths)

    for i in range(rows):
    # i = 0
        for j in range(cols):
            if sec_array[i][j] < 9:
                ## Claculate basin for this low point
                sum_basin = 1
                calculate_basin_for_point(i, j, input_array, sec_array)
                bassin_array.append(sum_basin)
    
    # pp.pprint(sec_array)
    print("================================================================")
    bassin_array.sort()
    total = 1
    for i in range(len(bassin_array) - 3, len(bassin_array)):
        total *= bassin_array[i]
        print("Max Basin Size: {}".format(bassin_array[i]))
    
    print("Result: {}".format(total))


def calculate_basin_for_point(row, col, array, sec_array):
    global sum_basin
    low_pos = array[row][col]
    ## Check for the values below
    if row+1 < rows:
        for i in range(row + 1, rows):
            if array[i][col] > low_pos and array[i][col] < 9 and sec_array[i][col] != 10:
                sec_array[i][col] = 10
                sum_basin += 1
                calculate_basin_for_point(i, col, array, sec_array)
            else:
                break
    ## Check for the values to the right
    if col+1 < cols:
        for j in range(col + 1, cols):
            if array[row][j] > low_pos and array[row][j] < 9 and sec_array[row][j] != 10:
                sec_array[row][j] = 10
                sum_basin += 1
                calculate_basin_for_point(row, j, array, sec_array)
            else:
                break
    ## Check for the values above
    if row > 0:
        for i in range(row - 1, -1, -1):
            if array[i][col] > low_pos and array[i][col] < 9 and sec_array[i][col] != 10:
                sec_array[i][col] = 10
                sum_basin += 1
                calculate_basin_for_point(i, col, array, sec_array)
            else:
                break
    ## Check for the values to the right
    if col > 0:
        for j in range(col - 1, -1, -1):
            if array[row][j] > low_pos and array[row][j] < 9 and sec_array[row][j] != 10:
                sec_array[row][j] = 10
                sum_basin += 1
                calculate_basin_for_point(row, j, array, sec_array)
            else:
                break

def find_low_points(input_array, sec_array, sum_depths):
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
    return sum_depths

### Iterate over the lines in the file
def read_array_in(filepath, array):
    row = 0;
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            fill_array(row, line, array)
            row += 1

### Read each char and add it to the array
def fill_array(row, line, array):
    for col in range(cols):
        char_in = line[col]
        if char_in == '\n':
            print("End of line")
            return
        array[row][col] = int(char_in)

if __name__ == '__main__':
    main()