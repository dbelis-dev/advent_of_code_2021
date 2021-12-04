import sys
import os
import array
from ordered_set import OrderedSet

def main():
    draws_filepath = './input_file-draws'
    boards_filepath = './input_file-boards'
    draws_array = array.array('i',[])
    cols = 5
    rows = 5
    boards = 100
    board_array = [[[0 for i in range(cols)] for j in range(rows)] for k in range(boards)]
    board_mark_array = [[[0 for i in range(cols + 1)] for j in range(rows + 1)] for k in range(boards)]
    winning_boards = OrderedSet()

    if not os.path.isfile(draws_filepath):
        print("File path {} does not exist. Exiting...".format(draws_filepath))
        sys.exit()
    if not os.path.isfile(boards_filepath):
        print("File path {} does not exist. Exiting...".format(boards_filepath))
        sys.exit()

    read_draws_array_in(draws_filepath, draws_array)
    read_board_array_in(boards_filepath, board_array)

    for num in draws_array:
        # print("Number {}".format(num))
        mark_draw_number_in_array(num, board_array, board_mark_array, boards, rows, cols)
        find_bingo_line(board_array, board_mark_array, boards, rows, cols, winning_boards, num)

    print("Last Board {} - Last Result {}".format(last_board, last_result))

def mark_draw_number_in_array(number, array, mark_array, boards, rows, cols):
    for board in range(boards):
        for row in range(rows):
            for col in range(cols):
                if number == array[board][row][col]:
                    mark_array[board][row][col] = 1
                    mark_array[board][rows][col] += 1
                    mark_array[board][row][cols] += 1 

def find_bingo_line(array, mark_array, boards, rows, cols, winning_boards, number):
    # global bingo_board
    global last_board
    global last_result
    found = False
    for board in range(boards):
        for row in range(rows):
            for col in range(cols):
                if mark_array[board][rows][col] == 5:
                    if board not in winning_boards:
                        winning_boards.add(board)
                        last_board = board
                        last_result = number * sum_unmarked(array, mark_array, board, rows, cols)

            if mark_array[board][row][cols] == 5:
                if board not in winning_boards:
                    winning_boards.add(board)
                    last_board = board
                    last_result = number * sum_unmarked(array, mark_array, board, rows, cols)

def sum_unmarked(array, mark_array, board, rows, cols):
    sum = 0
    for row in range(rows):
        for col in range(cols):
            if mark_array[board][row][col] == 0:
                sum += array[board][row][col]
    return sum

def read_draws_array_in(filepath, array):
    with open(filepath, 'r') as fp:
       for value in fp.read().split(','):
           array.append(int(value))

def read_board_array_in(filepath, array):
    board = 0
    with open(filepath, 'r') as fp:
        row = 0
        for line in fp.readlines():
            line = line.strip()
            col = 0
            if line == "":
                board += 1
                row = -1
                pass
            for value in line.split(' '):
                if value != "":
                    array[board][row][col] = int(value)
                    col += 1
            row += 1

if __name__ == '__main__':
    main()