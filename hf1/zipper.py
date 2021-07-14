#!/usr/bin/env python3

def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = list(range(ord('a'), ord('z') + 1))
    # ha a codes range objektum marad, akkor is ugyanazt az eredményt kapom

    for t in list(zip(chars, codes)):
        print(t)


if __name__ == "__main__":
    main()
