import sys
import os
import pprint
import queue

def end_delim(i):
    switcher={
            '{':'}',
            '[':']',
            '(':')',
            '<':'>'
            }
    return switcher.get(i,"Invalid delimiter")

def main():
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    filepath = './input_file'
    delim_queue = queue.LifoQueue()
    total = 0
    sum_array= []

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            chunk_pos = 0
            delim_queue = queue.LifoQueue()
            while True:
                chunk_pos = get_chunk(delim_queue, line.rstrip(), chunk_pos)
                if chunk_pos == 0:
                    break
                if chunk_pos == -1:
                    delim_queue = queue.LifoQueue() 
                    break
            if chunk_pos == 0:
                total = calculate_incomplete(delim_queue)
                sum_array.append(total)

    print("================================================================")
    find_middle_score(sum_array)


def find_middle_score(sum_array):
    sum_array.sort()
    middle = int(len(sum_array) / 2)
    print("Result: {}".format(sum_array[middle]))

def calculate_incomplete(delim_queue):
    sum = 0
    for i in range(len(delim_queue.queue)):
        delim = delim_queue.get()
        sum *= 5
        if delim == '(':
            sum += 1
        if delim == '[':
            sum += 2
        if delim == '{':
            sum += 3
        if delim == '<':
            sum += 4
    return sum

def calculate_corrupted(corrupted_queue):
    sum = 0
    for i in range(len(corrupted_queue.queue)):
        delim = corrupted_queue.get()
        if delim == ')':
            sum += 3
        if delim == ']':
            sum += 57
        if delim == '}':
            sum += 1197
        if delim == '>':
            sum += 25137
    return sum

def get_chunk(delim_queue, line, start):
    delim_queue.put(line[start])
    for i in range(start + 1, len(line)):
        current_delim = delim_queue.get()
        if line[i] == '{' or line[i] == '[' or line[i] == '(' or line[i] == '<':
            delim_queue.put(current_delim)
            delim_queue.put(line[i])
            continue
        if end_delim(current_delim) != line[i]:
            break
        if delim_queue.empty():
            return i + 1
    if i != len(line) - 1:
        return -1
    else:
        return 0

if __name__ == '__main__':
    main()