import sys
import os
import array

def main():
    filepath = './input_file'
    input_array = []
    position = 0
    depth = 0

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            for value in line.split(' '):
                input_array.append(value.rstrip())

    i = 0
    while i < len(input_array):
        opcode = input_array[i]
        if opcode == "down":
            depth += int(input_array[i+1])
        if opcode == "up":
            depth -= int(input_array[i+1])
        if opcode == "forward":
            position += int(input_array[i+1])
        i += 2

    print("Position: {} - Depth {} - Result {}".format(position, depth, position * depth))

if __name__ == '__main__':
    main()
