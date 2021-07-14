#!/usr/bin/env python3


def main():
    
    results = []
    
    p = open('day02.txt', 'r')
    for line in p:
        line = line.rstrip('\n')
        lsline = line.split()
        lsline = [int(n) for n in lsline]
        res = max(lsline) - min(lsline)
        results.append(res)
        
    p.close()
    print(sum(results))


if __name__ == "__main__":
    main()
