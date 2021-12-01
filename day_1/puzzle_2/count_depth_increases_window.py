import sys
import os
import queue


def main():
    filepath = './input_file'
    counter = 0
    previous_window_sum = 0
    current_window_sum = 0
    window_q = queue.Queue(3)

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath) as fp:
        for depth in fp:
            window_q.put(int(depth))
            current_window_sum += int(depth)

            if window_q.full():
                if current_window_sum > previous_window_sum:
                    counter += 1                
                previous_window_sum = current_window_sum
                old_depth = window_q.get(1)
                current_window_sum -= old_depth
                

    print("Number of increaces: {}".format(counter-1))

if __name__ == '__main__':
    main()
