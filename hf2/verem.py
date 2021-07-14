#!/usr/bin/env python3

class Verem:
    def __init__(self):
        self.data = []

    def ures(self):
        if len(self.data) != 0:
            return False
        else:
            return True
        
    def betesz(self, value):
        self.data.append(value)

    def meret(self):
        return len(self.data)

    def kivesz(self):
        if self.ures():
            return "Hiba! A verem üres."
        else:
            return self.data.pop()

    def __str__(self):
        return str(self.data).rstrip(']')


class Sor:
    def __init__(self):
        self.data = []

    def ures(self):
        if len(self.data) != 0:
            return False
        else:
            return True
        
    def betesz(self, value):
        self.data.append(value)

    def meret(self):
        return len(self.data)

    def kivesz(self):
        if self.ures():
            return "Hiba! A sor üres."
        else:
            first = self.data[0]
            self.data.remove(self.data[0])
            return first

    def __str__(self):
        return str(self.data).rstrip(']')

def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

    print(40 * '-')

    s = Sor()      # üres verem létrehozása
    print(s)         # [
    print(s.ures())  # True
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)         
    print(s.meret()) 
    print(s.ures())  
    x = s.kivesz()
    print(x)         
    print(s)         
    s.kivesz()
    s.kivesz()       
    x = s.kivesz()
    print(x) 
    

if __name__ == "__main__":
    main()
