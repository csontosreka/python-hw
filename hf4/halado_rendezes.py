#!/usr/bin/env python3

def my_func1(t):
    return t[-1]


def my_func2(user):
    return int(user.split(":")[0])


def my_func3(m):
    return m[1]


def main():
    data = [ 
        (1,'Albany','NY',162692),
        (3,'Allegany','NY',11986),
        (121,'Wyoming','NY',8722),
        (123,'Yates','NY',5094)
    ]
    print(data)
    print(sorted(data, key = my_func1))
    print(sorted(data, key = lambda t: t[-1]))
    print("-" * 40)

    lst = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print(lst)
    print(sorted(lst, key = my_func2, reverse = True))
    print(sorted(lst, key = lambda user: int(user.split(":")[0]), reverse = True))
    print("-" * 40)

    li=[ [2,6],[1,3],[5,4] ]
    print(li)
    print(sorted(li, key = my_func3))
    print(sorted(li, key = lambda m: m[1]))

    

if __name__ == "__main__":
    main()
