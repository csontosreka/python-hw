#!/usr/bin/env python3

import random


def shuffled(li: list) -> list:
    shuffled_li = li
    random.shuffle(shuffled_li)
    return shuffled_li


def main():
    li = [1, 2, 3, 4, 5]
    print("Eredeti lista: {}".format(li))
    print("Összekevert lista: {}".format(shuffled(li)))


if __name__ == "__main__":
    main()
