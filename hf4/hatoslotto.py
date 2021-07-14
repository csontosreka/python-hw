#!/usr/bin/env python3

import random

def multiply(lst) :
     
    result = 1
    for x in lst:
         result = result * x
    return result


def main():
    result_sum = 90
    result_multiply = 996300

    sum_nums = 0
    multi_nums = 1
    nums = []

    while (sum_nums != result_sum or multi_nums != result_multiply):
        nums = []
        for n in range(1, 6+1):
            nums.append(random.randint(1, 45+1))
            
        sum_nums = sum(nums)
        multi_nums = multiply(nums)
        

    print("A hatoslottó nyerőszámai: {}".format(sorted(nums)))


if __name__ == "__main__":
    main()
