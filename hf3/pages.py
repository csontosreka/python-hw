#!/usr/bin/env python3


def main():
    print_pages = []
    pages = input("Adja meg a nyomtatandó oldalakat: ")
    pages = pages.split()
    for p in pages:
        p = p.rstrip(',')
        if len(p) == 1:
            print_pages.append(int(p))

        else:
            string = str(p)
            start = int(p[0])
            end = int(p[2]) + 1
            for n in range(start, end):
                print_pages.append(n)

    print("Kinyomtatott oldalak: {}".format(print_pages))


if __name__ == "__main__":
    main()
