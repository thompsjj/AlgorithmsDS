import sys
import math

def largest_number(a):
    
    def cmp_to_key(mycmp):
        class K(object):
            def __init__(self, obj, *args):
                self.obj = obj
            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0
            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0
            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0
            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0
            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0
            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0
        return K
    
    def compare(a, b):
        strAB = str(a)+str(b)
        strBA = str(b)+str(a)
        if int(strAB) < int(strBA):
            return 1
        elif int(strAB) == int(strBA):
            return 0
        else:
            return -1
    
    return int(''.join(sorted(a, key =cmp_to_key(compare))))
    
input = sys.stdin.read()
data = input.split()
a = data[1:]
print(largest_number(a))