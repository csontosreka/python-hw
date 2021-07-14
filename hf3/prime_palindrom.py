#!/usr/bin/env python3

import prime as pr
import palindrom as pl


def is_palindrom_and_prime(n: int) -> int: 
    while (pr.is_prime(n) and pl.is_palindrom(str(n))) != True:
         n += 1

    return n     

 
def main():
    n1 = 31
    n2 = 130
    n3 = 131
    n4 = 1977

    print("{} esetén: {}".format(n1, is_palindrom_and_prime(n1)))
    print("{} esetén: {}".format(n2, is_palindrom_and_prime(n2)))
    print("{} esetén: {}".format(n3, is_palindrom_and_prime(n3)))
    print("{} esetén: {}".format(n4, is_palindrom_and_prime(n4)))


if __name__ == "__main__":
    main()
