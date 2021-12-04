import sys
import os
import array

def main():
    draws_filepath = './input_file-draws'
    boards_filepath = './input_file-boards'
    draws_array = array.array('i',[])
    cols = 5
    rows = 5
    boards = 100
    board_array = [[[0 for i in range(cols)] for j in range(rows)] for k in range(boards)]
    board_mark_array = [[[0 for i in range(cols + 1)] for j in range(rows + 1)] for k in range(boards)]

    if not os.path.isfile(draws_filepath):
        print("File path {} does not exist. Exiting...".format(draws_filepath))
        sys.exit()
    if not os.path.isfile(boards_filepath):
        print("File path {} does not exist. Exiting...".format(boards_filepath))
        sys.exit()

    read_draws_array_in(draws_filepath, draws_array)
    read_board_array_in(boards_filepath, board_array)

    for num in draws_array:
        mark_draw_number_in_array(num, board_array, board_mark_array, boards, rows, cols)
        if find_bingo_line(board_mark_array, boards, rows, cols):
            sum = sum_unmarked(board_array, board_mark_array, bingo_board, rows, cols)
            print("Result {}".format(sum * num))
            break

def mark_draw_number_in_array(number, array, mark_array, boards, rows, cols):
    for board in range(boards):
        for row in range(rows):
            for col in range(cols):
                if number == array[board][row][col]:
                    mark_array[board][row][col] = 1
                    mark_array[board][rows][col] += 1
                    mark_array[board][row][cols] += 1 

def find_bingo_line(mark_array, boards, rows, cols):
    global bingo_board
    for board in range(boards):
        for row in range(rows):
            for col in range(cols):
                if mark_array[board][rows][col] == 5:
                    print("Winning Board {} - Col {}".format(board+1, col+1))
                    bingo_board = board
                    return board
            if mark_array[board][row][cols] == 5:
                print("Winning Board {} - Row {}".format(board+1, row+1))
                bingo_board = board
                return board

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