import pprint

player_count = 2
player_position = [[0 for j in range(2)] for i in range(player_count)]
dice_adv = 3
dice_start = 1
dice_counter = 0

def main():
    global player_position
    global pp
    pp = pprint.PrettyPrinter(indent=4)

    ## Puzzle input
    player_position[0][0] = 2
    player_position[1][0] = 7
    
    reached_target = True
    ## Loop until sum is gt than 1000
    while reached_target:
        for j in range(2):
            ## Player j
            sum = roll_next_dice(dice_start) + player_position[j][0]
            if sum > 10:
                sum = sum % 10
                if sum == 0:
                    sum = 10
            player_position[j][0] = sum
            player_position[j][1] += sum
            if player_position[j][1] >= 1000:
                reached_target = False
                break

    pp.pprint(player_position)

    print("================================================================")
    print("Result: {} - {}".format(dice_counter*player_position[0][1], dice_counter*player_position[1][1]))

def roll_next_dice(start):
    global dice_counter, dice_start
    dice_sum = 0
    roll_counter = 0
    for i in range(start, start + dice_adv):
        ## if dice reached 100, break
        if i > 100:
            start = 0
            break
        dice_sum += i
        roll_counter += 1
    ## if dice reached 100, roll-over to 1
    if start == 0:
        start = 1
        for i in range(start, start + dice_adv - roll_counter):
            dice_sum += i
        start = start - roll_counter
    dice_counter += dice_adv
    dice_start = start + dice_adv
    return dice_sum

if __name__ == '__main__':
    main()