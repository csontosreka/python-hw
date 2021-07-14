#!/usr/bin/env python3

class Sor:
    v1 = []
    v2 = []

    def append(self, value):
        self.v1.append(value)

    def popleft(self):
        if self.is_empty():
            return "Hiba! A sor üres."
        else:
            self.v1 = self.v1[::-1]
            left = self.v1.pop()
            for v in self.v1[:len(self.v1)+1]:
                self.v2.append(v)
                self.v1.remove(v)
            self.v2 = self.v2[::-1]
            for v in self.v2[:len(self.v2)+1]:
                self.v1.append(v)
                self.v2.remove(v)
            
            return left
    
    def is_empty(self):
        if len(self.v1) != 0:
            return False
        else:
            return True

    def size(self):
        return len(self.v1)

    def __str__(self):
        return str(self.v1)
    

def main():
    s = Sor()
    print("Sor tartalma: {}".format(s))
    print("Üres-e? -> {}".format(s.is_empty()))
    s.append(1)
    s.append(2)
    s.append(3)
    s.append(4)
    print("Sor tartalma: {}".format(s))
    print("Üres-e? -> {}".format(s.is_empty()))
    print("Mérete: {}".format(s.size()))
    x = s.popleft()
    print("Kivett elem: {}".format(x))
    print("Sor tartalma: {}".format(s))
    x = s.popleft()
    print("Kivett elem: {}".format(x))
    print("Sor tartalma: {}".format(s))
    s.popleft()
    s.popleft()
    print("Sor tartalma: {}".format(s))
    print("Üres-e? -> {}".format(s.is_empty()))


if __name__ == "__main__":
    main()
