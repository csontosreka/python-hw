#!/usr/bin/env python3

def parentheses(example):

    openP = ["[","{","("]
    closeP = ["]","}",")"]
  
    checked = []
    
    for c in example:
        if c in openP:
            checked.append(c)
        elif c in closeP:
            p = closeP.index(c)
            if ((len(checked) > 0) and (openP[p] == checked[len(checked)-1])):
                checked.pop()
            else:
                break
            
    if len(checked) == 0:
        print("{} = True".format(example))
    else:
        print("{} = False".format(example))
        

def main():
    ex1 = "((5+3)*2+1)"
    ex2 = "{[(3+1)+2]+}"
    ex3 = "(3+{1-1)}"
    ex4 = "[1+1]+(2*2)-{3/3}"
    ex5 = "(({[(((1)-2)+3)-3]/3}-3)"

    parentheses(ex1)
    parentheses(ex2)
    parentheses(ex3)
    parentheses(ex4)
    parentheses(ex5)
    

if __name__ == "__main__":
    main()
