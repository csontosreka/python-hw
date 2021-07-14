#!/usr/bin/env python3

from enum import Enum, auto


class Hangrend(Enum):
    MAGAS = auto()
    MELY = auto()
    VEGYES = auto()
    SEMMILYEN = auto()


MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'


def hangrend(words):
    
    for word in words:
        magas = 0
        mely = 0
        for ch in word:
            if (ch in MELY_MGHK):
                mely += 1
            elif (ch in MAGAS_MGHK):
                magas += 1
    
        if (magas != 0 and mely == 0):
            print("{}: {}".format(word, Hangrend.MAGAS.name))
            
        elif (magas == 0 and mely != 0):
            print("{}: {}".format(word, Hangrend.MELY.name))

        elif (magas != 0 and mely != 0):
            print("{}: {}".format(word, Hangrend.VEGYES.name))
        else:
            print("{}: {}".format(word, Hangrend.SEMMILYEN.name))


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pfffffff"]
    hangrend(words)
    
    
    

if __name__ == "__main__":    
    main()
