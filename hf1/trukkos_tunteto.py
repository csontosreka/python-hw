#!/usr/bin/env python3

def binaryToString(binary):
    return ''.join([chr(int(x, 2)) for x in binary])


def main():

    binaryCode = []
    f = open('tunteto.txt', 'r')
    for line in f:
        line = line.rstrip('\n')
        binaryCode.append(line)
    f.close()

    
    appleCode = []
    f2 = open('apple.txt', 'r')
    for line in f2:
        line = line.rstrip('\n')
        appleCode.append(line)
    f2.close()
    
    result = binaryToString(binaryCode)
    result2 = binaryToString(appleCode)

    print("Trükkös tüntető titkos üzenete: \n   {}".format(result))
    print("-" * 40)
    print("Apple titkos üzenete: \n   {}".format(result2))

if __name__ == "__main__":
    main()
