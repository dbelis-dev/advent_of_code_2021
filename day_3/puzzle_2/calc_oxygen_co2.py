import sys
import os

def main():
    filepath = './input_file'
    cols = 12
    rows = 1000
    input_array = [[0 for i in range(cols)] for j in range(rows)]
    one_array = []
    zero_array = []
    final_array = []
    oxygen_gen_rating = ""
    co2_scrub_rating = ""

    read_array_in(filepath, cols, input_array)

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

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
        if len(one_array) >= len(zero_array):
            final_array = one_array
        else:
            final_array = zero_array
        print("Final_Array {}".format(final_array))
        one_array = []
        zero_array = []
        rows = len(final_array)
        if len(final_array) == 1:
            break

    for digit in final_array[0]:
        if int(digit) > 0:
            oxygen_gen_rating += "1"
        else:
            oxygen_gen_rating += "0"
    binary = oxygen_gen_rating
    oxygen_gen_rating_decimal = 0
    for digit in binary:
        oxygen_gen_rating_decimal = oxygen_gen_rating_decimal*2 + int(digit)
    print("Oxygen {} - Decimal {}".format(binary, oxygen_gen_rating_decimal))

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
        if len(one_array) >= len(zero_array):
            final_array = zero_array
        else:
            final_array = one_array
        print("Final_Array {}".format(final_array))
        one_array = []
        zero_array = []
        rows = len(final_array)
        if len(final_array) == 1:
            break

    for digit in final_array[0]:
        if int(digit) > 0:
            co2_scrub_rating += "1"
        else:
            co2_scrub_rating += "0"
    binary = co2_scrub_rating
    co2_scrub_rating_decimal = 0
    for digit in binary:
        co2_scrub_rating_decimal = co2_scrub_rating_decimal*2 + int(digit)
    print("C02 Scrubbing {} - Decimal {}".format(binary, co2_scrub_rating_decimal))

    print("Result {}".format(oxygen_gen_rating_decimal * co2_scrub_rating_decimal))

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