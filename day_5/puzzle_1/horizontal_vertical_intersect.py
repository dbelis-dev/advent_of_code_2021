import sys
import os
import pprint

def main():
    pp = pprint.PrettyPrinter(indent=4)
    filepath = './input_file'
    input_array = []
    count_intersect = 0

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            for value in line.split(' -> '):
                input_array.append(value.rstrip())
                
    ### Find maximum coords in input
    findMaxXY(input_array)
    ### Create blank board to the maximum values
    board_size_x = max_x + 1
    board_size_y = max_y + 1
    board_array = [[0 for i in range(board_size_x)] for i in range(board_size_y)]

    for src_, dest_ in zip(input_array[::2], input_array[1::2]):
        src_x,src_y = (int(coord) for coord in src_.split(','))
        dest_x,dest_y = (int(coord) for coord in dest_.split(','))
        ### Vertical lines
        if src_x == dest_x:
            if src_y > dest_y:
                step = -1
            else:
                step = 1
            for y_ in range(src_y, dest_y+step, step):
                board_array[y_][src_x] += 1
        ### Horizontal lines
        if src_y == dest_y:
            if src_x > dest_x:
                step = -1
            else:
                step = 1
            for x_ in range(src_x, dest_x+step, step):
                board_array[src_y][x_] += 1
    ### Count all intersecting points
    for i in range(board_size_x):
        for k in range(board_size_y):
            count_intersect += board_array[i][k] > 1

    print("================================================================")
    print(">> Intersecting Points: {}".format(count_intersect))

def findMaxXY(array):
    global max_x
    global max_y
    max_x = 0
    max_y = 0
    for src_, dest_ in zip(array[::2], array[1::2]):
        src_x,src_y = (int(coord) for coord in src_.split(','))
        dest_x,dest_y = (int(coord) for coord in dest_.split(','))
        if src_x > max_x:
            max_x = src_x
        if dest_x > max_x:
            max_x = dest_x
        if src_y > max_y:
            max_y = src_y
        if dest_y > max_y:
            max_y = dest_y
    print("MaxX: {} - MaxY: {}".format(max_x, max_y))

if __name__ == '__main__':
    main()