#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wej-wyj.py

def main(args):
    a = input("podaj swoje imię: ")
    b = input("podaj swoje nazwisko: ")
    
    print("Witaj", a, b,)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
