import pprint

x_min_target = 240
x_max_target = 292
y_min_target = -90
y_max_target = -57
x_current_pos = 0
y_current_pos = 0
step_array = []
x_inc = 0
y_inc = 0

def main():
    global step_array
    global x_inc, y_inc
    global x_current_pos, y_current_pos
    global pp
    pp = pprint.PrettyPrinter(indent=4)

    for i in range(x_max_target):
        for j in range(abs(y_min_target)):
            x_current_pos = i
            y_current_pos = j
            x_inc = i
            y_inc = j
            max_y = 0
            for k in range(200):
                calc_next_step()

                if max_y < y_current_pos:
                    max_y = y_current_pos

                if step_within_target(x_current_pos, y_current_pos):
                    step_array.append(max_y)
                    break
                if x_current_pos > x_max_target and y_current_pos < y_min_target:
                    break

    max_y = 0
    for i in range(len(step_array)):
        if max_y < step_array[i]:
            max_y = step_array[i]
    
    print("================================================================")
    print("Result: {}".format(max_y))

def calc_next_step():
    global x_inc, y_inc
    global x_current_pos, y_current_pos
    if x_current_pos > 1 and x_inc != 0:
        x_inc -= 1
    elif x_current_pos < 1 and x_inc != 0:
        x_inc += 1
    y_inc -= 1
    x_current_pos += x_inc
    y_current_pos += y_inc

### Check whether the current step coords
### are within the target area
def step_within_target(x_, y_):
    if x_ >= x_min_target and y_ >= y_min_target and x_ <= x_max_target and y_ <= y_max_target:
        return True


if __name__ == '__main__':
    main()