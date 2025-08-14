

def monkey_climb(feet, high, low):
    current_climb = 0
    count = 1

    while current_climb <= feet:
        current_climb += high
        if current_climb >= feet:
            break
        count += 1
        current_climb -= low


    # current_climb += 3
    return count

print(monkey_climb(5,3, 2))


