#!/usr/bin/env python3

import palindrom as pl


def binary(n: int) -> str:
    return bin(n).replace("0b", "")


def main():
    result = 0
    for n in range(1, 1000000):
        if pl.is_palindrom(str(n)) and pl.is_palindrom(binary(n)):
            result += n

    print(result)

if __name__ == "__main__":
    main()
