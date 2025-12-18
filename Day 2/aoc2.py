# --- Day 2: Gift Shop ---
# You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

# As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

# As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

# They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

# 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124
# (The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

# The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

# Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

# None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

# Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

# 11-22 has two invalid IDs, 11 and 22.
# 95-115 has one invalid ID, 99.
# 998-1012 has one invalid ID, 1010.
# 1188511880-1188511890 has one invalid ID, 1188511885.
# 222220-222224 has one invalid ID, 222222.
# 1698522-1698528 contains no invalid IDs.
# 446443-446449 has one invalid ID, 446446.
# 38593856-38593862 has one invalid ID, 38593859.
# The rest of the ranges contain no invalid IDs.
# Adding up all the invalid IDs in this example produces 1227775554.

# What do you get if you add up all of the invalid IDs?

# --- Part Two ---
# The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

# Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

# From the same example as before:

# 11-22 still has two invalid IDs, 11 and 22.
# 95-115 now has two invalid IDs, 99 and 111.
# 998-1012 now has two invalid IDs, 999 and 1010.
# 1188511880-1188511890 still has one invalid ID, 1188511885.
# 222220-222224 still has one invalid ID, 222222.
# 1698522-1698528 still contains no invalid IDs.
# 446443-446449 still has one invalid ID, 446446.
# 38593856-38593862 still has one invalid ID, 38593859.
# 565653-565659 now has one invalid ID, 565656.
# 824824821-824824827 now has one invalid ID, 824824824.
# 2121212118-2121212124 now has one invalid ID, 2121212121.
# Adding up all the invalid IDs in this example produces 4174379265.

# What do you get if you add up all of the invalid IDs using these new rules?

import time

def main():
    start_time = time.perf_counter()
    sum1 = 0
    sum2 = 0
    file = open("input2.txt","r")
    content = file.read().strip().split(",")
    for num_range in content:
        int_range = convert_range_to_int(num_range)
        sums = check_range(int_range)
        sum1 += sums[0]
        sum2 += sums[1]
    end_time = time.perf_counter()
    print(f"Part 1: {sum1}")
    print(f"Part 2: {sum2}")
    print(f"Time: {end_time-start_time}")

def convert_range_to_int(str_range:str) -> list:
    str_range = str_range.split("-")
    return [int(x) for x in str_range]

def check_range(int_range:list) -> list:
    range_sum1 = 0
    range_sum2 = 0
    for x in range(int_range[0],int_range[1]+1):
        str_x = str(x)
        l = len(str_x)
        
        #part 1
        if l % 2 == 0:  #if even
            low = x%(10**(l//2))
            high = low*(10**(l//2))
            if x == high + low:
                range_sum1 += x

        #part 2
        for i in range(l//2):
            if l % (i+1) == 0:
                sub_string = str_x[:i+1]
                repeats = False
                for j in range(i+1,l-i+1,i+1):
                    if sub_string != str_x[j:j+i+1]:
                        break
                    elif j == l-i-1:
                        repeats = True
            if repeats:
                range_sum2 += x
                break

        
    return [range_sum1,range_sum2]
        
    
main()

# t = [1188511880,1188511890]
# print(check_range(t))