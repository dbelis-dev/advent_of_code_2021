import sys
import os
import array

def main():
    filepath = './input_file'
    power_array = [0 for i in range(12)]
    # print("Array {}".format(power_array))
    gamma_rate = ""
    epsilon_rate = ""

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    i = 0
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            for bit in line.rstrip():
                if bit == '1':
                    # add 1 to the field
                    power_array[i] += 1
                else:
                    # subtract 1 from the field
                    power_array[i] -= 1
                # print("Bit {}".format(bit))
                i +=1
            # print("Array {}".format(power_array))
            i = 0
        for digit in power_array:
            if int(digit) > 0:
                gamma_rate += "1"
                epsilon_rate += "0"
            else:
                gamma_rate += "0"
                epsilon_rate += "1"
        binary = gamma_rate
        gamma_decimal = 0
        for digit in binary:
            gamma_decimal = gamma_decimal*2 + int(digit)
        print("Gamma {} - Decimal {}".format(binary, gamma_decimal))
        binary = epsilon_rate
        epsilon_decimal = 0
        for digit in binary:
            epsilon_decimal = epsilon_decimal*2 + int(digit)
        print("Epsilon {} - Decimal {}".format(binary, epsilon_decimal))
    
    print("Result {}".format(gamma_decimal * epsilon_decimal))

if __name__ == '__main__':
    main()