# --- Day 3: Lobby ---
# You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all offline.

# "Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."

# You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."

# "But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

# There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their joltage rating, a value from 1 to 9. You make a note of their joltage ratings (your puzzle input). For example:

# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

# You'll need to find the largest possible joltage each bank can produce. In the above example:

# In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
# In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
# In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
# In 818181911112111, the largest joltage you can produce is 92.
# The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

# There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?

import time

def main():
    start_time = time.perf_counter()
    total1 = 0
    total2 = 0
    file = open("input3.txt","r")
    for line in file:
        line = line.strip()
        #convert string to a list of digits
        digits = [int(digit) for digit in line]
        #get the largest battery
        total1 += max_battery(digits)
        total2 += max_battery12(digits)
    
    end_time = time.perf_counter()

    print(f"Part 1: {total1}")
    print(f"Part 2: {total2}")
    print(f"Time: {end_time-start_time}")

def max_battery(digits:list) -> int:
    front = 1
    front_index = 0
    for i in range(len(digits)-1):
        if digits[i] == 9:
            front = 9
            front_index = i
            break
        elif digits[i] > front:
            front = digits[i]
            front_index = i
    
    back = 1
    for j in range(front_index+1,len(digits)):
        if digits[j] == 9:
            back = 9
            break
        elif digits[j] > back:
            back = digits[j]
    
    return front*10 + back

def max_battery12(digits:list) -> int:
    max_dig = list()
    k = 0
    for j in range(12):
            #make a new spot in the list
        max_dig.append(1)
        for i in range(k,len(digits)-(11-j)):
            if digits[i] == 9:
                max_dig[j] = 9
                k = i+1
                break
            elif digits[i] > max_dig[j]:
                max_dig[j] = digits[i]
                k = i+1
                
    max_str = "".join(map(str,max_dig))
    
    return int(max_str)

main()