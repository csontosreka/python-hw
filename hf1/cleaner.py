#!/usr/bin/env python3


def main():

    
    f = open('string1.py', 'r')
    f2 = open('string1_clean.py', 'w')
    
    for line in f:
        line = line.rstrip('\n')
        if line == '#!/usr/bin/env python3':
            f2.write(line + '\n')
            
        if line.startswith('#') or line.startswith('    #'):
            continue

        else:    
            f2.write(line + '\n')

    f.close()
    f2.close()

if __name__ == "__main__":
    main()
