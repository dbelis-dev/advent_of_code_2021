import sys
import os

def main():
    filepath = './input_file'
    cols = 12
    rows = 1000
    input_array = [[0 for i in range(cols)] for j in range(rows)]

    read_array_in(filepath, cols, input_array)

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    oxygen_gen_rating = calculate_result(input_array, 'Oxygen')
    co2_scrub_rating = calculate_result(input_array, 'CO2')
    print("Result {}".format(oxygen_gen_rating * co2_scrub_rating))

def calculate_result(input_array, rating_type):
    one_array = []
    zero_array = []
    final_array = input_array
    cols = len(final_array[0])
    rows = len(final_array)
    for col in range(cols):
        for row in range(rows):
            bit = final_array[row][col]
            if int(bit) == 0:
                # move to 0 array
                zero_array.append(final_array[row])
            else:
                # move to 1 array
                one_array.append(final_array[row])
        if rating_type == 'Oxygen':
            if len(one_array) >= len(zero_array):
                final_array = one_array
            else:
                final_array = zero_array
        else:
            if len(one_array) >= len(zero_array):
                final_array = zero_array
            else:
                final_array = one_array            
        one_array = []
        zero_array = []
        rows = len(final_array)
        if len(final_array) == 1:
            break
    
    rating = ""
    for digit in final_array[0]:
        if int(digit) > 0:
            rating += "1"
        else:
            rating += "0"
    binary = rating
    rating_decimal = 0
    for digit in binary:
        rating_decimal = rating_decimal*2 + int(digit)
    print("Rating Type {}".format(rating_type))
    print("Binary {} - Decimal {}".format(binary, rating_decimal))
    return rating_decimal

def read_array_in(filepath, cols, input_array):
    row = 0;
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            fill_array(cols, row, line, input_array)
            row += 1

def fill_array(cols, row, line, input_array):
    for col in range(cols):
        char_in = line[col]
        if char_in == '\n':
            print("End of line")
            return
        input_array[row][col] = char_in

if __name__ == '__main__':
    main()