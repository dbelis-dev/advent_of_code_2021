import sys
import os
import pprint
import queue

row = []
cave_array = []
path_q = queue.LifoQueue()
max_x = 0
max_y = 0

def main():
    global pp
    global max_x, max_y
    pp = pprint.PrettyPrinter(indent=4)
    filepath = './input_file-example'

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ### Read the input into an array of integers
    read_array_in_template(filepath)
    max_x = len(cave_array[0])
    max_y = len(cave_array)

    ## Add starting point
    ## increase by 10 to make 'added'
    path_q.put(cave_array[0][0])
    cave_array[0][0] += 10

    print_array(cave_array)
    print(path_q.queue)

    check_adjacent(3, 0, 0)
    # check_adjacent(1, 0, 1)
    # check_adjacent(2, 0, 2)
    # check_adjacent(1, 1, 2)
    # check_adjacent(3, 1, 1)
    # check_adjacent(1, 1, 0)

    print("================================================================")
    # print("Result: {}".format(max-min))


def find_min_path():
    print()

def check_adjacent(risk, x, y):
    print(x, y)
    min = 10
    left = True
    right = True
    up = True
    down = True
    min_x = 0
    min_y = 0
    if x == 0:
        left = False
    if y == 0:
        up = False
    if x == len(cave_array[0]) -1:
        right = False
    if y == len(cave_array) - 1:
        down = False
    print(left, right, up, down)
    if left:
        print("Checking LEFT {},{}".format(x - 1, y))
        if cave_array[y][x - 1] > 10:
            print(" This is already ADDED")
        elif cave_array[y][x - 1] <= min:
            min = cave_array[y][x - 1]
            min_x = x-1
            min_y = y
            # path_q.put(cave_array[y][x - 1])
            # check_adjacent(cave_array[y][x - 1], x - 1, y)
    if right:
        print("Checking RIGHT {},{}".format(x + 1, y))
        if cave_array[y][x + 1] > 10:
            print(" This is already ADDED")
        elif cave_array[y][x + 1] <= min:
            min = cave_array[y][x + 1]
            min_x = x+1
            min_y = y
            # path_q.put(cave_array[y][x + 1])
            # check_adjacent(cave_array[y][x + 1], x + 1, y)
    if up:
        print("Checking UP {},{}".format(x, y - 1))
        if cave_array[y - 1][x] > 10:
            print(" This is already ADDED")
        elif cave_array[y - 1][x] <= min:
            min = cave_array[y - 1][x]
            min_x = x
            min_y = y-1
            # path_q.put(cave_array[y - 1][x])
            # check_adjacent(cave_array[y - 1][x], x, y - 1)
    if down:
        print("Checking DOWN {},{}".format(x, y + 1))
        if cave_array[y + 1][x] > 10:
            print(" This is already ADDED")
        elif cave_array[y + 1][x] <= min:
            min = cave_array[y + 1][x]
            min_x = x
            min_y = y+1
            # path_q.put(cave_array[y + 1][x])
            # check_adjacent(cave_array[y + 1][x], x, y + 1)
    
    if cave_array[min_y][min_x] > 10:
        return
    print("Min neighbour: {} - {},{}".format(min, min_x, min_y))
    path_q.put(cave_array[min_y][min_x])
    cave_array[min_y][min_x] += 10
    print(path_q.queue)

    if min_x == max_x and min_y == max_y:
        return
    check_adjacent(cave_array[min_y][min_x], min_x, min_y)
    # if cave_array[y][x] > 10:
    #     pass



### Iterate over the lines in the file
def read_array_in_template(filepath):
    global initial_template
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            line = line.rstrip()
            row = []
            for char in line:
                row.append(int(char))
            cave_array.append(row)

### Pretty-print the array
def print_array(array):
    for i in array:
        for j in i:
            print(j, end=' ')
        print()


if __name__ == '__main__':
    main()