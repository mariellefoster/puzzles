import re

def i_():
    imp = re.sub(r'\s+', ' ', raw_input())
    imp = imp.strip().split()
    imp = [] if imp == [''] else imp
    return map(int, imp)

def t(lo, hi, l):
    stack = [(lo, hi)]
    while len(stack) > 0:
        run = stack.pop(0)
        x = tree(run[0], run[1], l)
        if isinstance(x, bool):
            if not x:
                return False
        else:
            stack += x
    return True

def tree(lo, hi, l):
    if lo >= hi-1:
        return True
    root = l[lo]
    i = 1
    while lo+i < hi:
        if l[lo+i] < root:
            i += 1
        else:
            break
    j = i
    while lo+j < hi:
        if l[lo+j] <= root:
            return False
        j += 1
    return [(lo+1, lo+i), (lo+i, hi)]

case = 0
while True:
    case += 1
    try:
        l = []
        while True:
            l += i_()
            if len(l)==0:
                continue
            if l[-1] < 0:
                l = l[:-1]
                break
        yes = t(0, len(l), l)
        yes = "yes" if yes else "no"
        print "Case %d: %s" % (case, yes)
    except EOFError as e:
        break
