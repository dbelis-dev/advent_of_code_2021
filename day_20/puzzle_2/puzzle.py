import sys
import os
import pprint

iterations = 50
rows = 100
cols = 100
padding = (iterations + 1) * 2
aug_rows = rows + padding
aug_cols = cols + padding
pattern_array = []
image_array = [['.' for x in range(aug_cols)] for y in range(aug_rows)]
output_array = [['.' for x in range(aug_cols)] for y in range(aug_rows)]

def main():
    global image_array, output_array
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    filepath_image = './input_file'
    filepath_pattern = './input_file-pattern'

    if not os.path.isfile(filepath_image):
        print("File path {} does not exist. Exiting...".format(filepath_image))
        sys.exit()
    if not os.path.isfile(filepath_pattern):
        print("File path {} does not exist. Exiting...".format(filepath_pattern))
        sys.exit()

    ### Read the input into an array of integers
    read_image_in(filepath_image)
    read_pattern_in(filepath_pattern)

    print_image(image_array)
    for k in range(iterations):
        output_array = [['.' for x in range(aug_cols)] for y in range(aug_rows)]
        for y in range(aug_rows):
            for x in range(aug_cols):
                pixel = calculate_output_pixel(x,y)
                output_array[y][x] = pattern_array[pixel]
        print_image(output_array)
        image_array = output_array.copy()


    print("================================================================")
    print("Result: {}".format(count_light_pixels()))

def count_light_pixels():
    counter = 0
    for y in range(aug_rows):
        for x in range(aug_cols):
            if output_array[y][x] == '#':
                counter += 1
    return counter

def calculate_output_pixel(x_, y_):
    x_min = x_ - 1
    if x_ - 1 < 0:
        x_min = 0
    x_max = x_ + 1
    if x_ + 1 > aug_cols - 1:
        x_max = aug_cols - 1
    y_min = y_ - 1
    if y_ - 1 < 0:
        y_min = 0
    y_max = y_ + 1
    if y_ + 1 > aug_rows - 1:
        y_max = aug_rows - 1
    str_bin = ''
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if image_array[y][x] == '.':
                str_bin += '0'
            else:
                str_bin += '1'
    return int(str_bin,2)

### Iterate over the lines in the file
def read_image_in(filepath):
    with open(filepath, 'r') as fp:
        row = int(padding / 2)
        for line in fp.readlines():
            line = line.rstrip()
            for col in range(int(padding / 2), len(line)+int(padding / 2)):
                char_in = line[col - int(padding / 2)]
                image_array[row][col] = char_in
            row += 1

### Iterate over the lines in the file
def read_pattern_in(filepath):
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            line = line.rstrip()
            for col in range(len(line)):
                pattern_array.append(line[col])

def print_image(array):
    for row in array:
        for col in row:
            print(col, end='')
        print()
    print()


if __name__ == '__main__':
    main()