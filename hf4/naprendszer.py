#!/usr/bin/env python3

def my_func(lst):
    return lst[-1]


def main():
    letters = ['j', 's', 'u', 'n']
    f = open('corpus.txt', 'r')
    for line in f:
        indexes = []
        line = line.lower().rstrip('\n')
        for c in letters:
            index = line.find(c)
            if index != -1:
                indexes.append((c, index))
            else:
                continue
            
        if len(indexes) == 4:
            sorted(indexes, key=my_func)
            indexes_only = [i[1] for i in indexes]
            sorted_indexes = sorted(indexes_only)
            if indexes_only == sorted_indexes:
                line = line.split(',')
                print(line[0])
            

    f.close()


if __name__ == "__main__":
    main()
