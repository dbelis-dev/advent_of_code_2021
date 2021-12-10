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
    corrupted_queue = queue.Queue()

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()


    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            delim_queue = queue.LifoQueue()
            get_chunk(delim_queue, corrupted_queue, line.rstrip())

    print("================================================================")
    print("Result: {}".format(calculate_corrupted(corrupted_queue)))


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

def get_chunk(delim_queue, corrupted_queue, line):
    delim_queue.put(line[0])
    for i in range(1, len(line)):
        current_delim = delim_queue.get()
        if line[i] == '{' or line[i] == '[' or line[i] == '(' or line[i] == '<':
            delim_queue.put(current_delim)
            delim_queue.put(line[i])
            continue
        if end_delim(current_delim) != line[i]:
            corrupted_queue.put(line[i])
            break
        if delim_queue.empty():
            break

if __name__ == '__main__':
    main()