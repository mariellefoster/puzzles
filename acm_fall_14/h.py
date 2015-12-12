buffer = []
def i_():
    global buffer
    while not buffer:
        try:
            buffer = raw_input().split()
        except:
            exit()
    return int(buffer.pop(0))

import math

def cont_fraction(x, lst):
    mod = x[0]%x[1]
    whole = (x[0]-mod) / x[1]
    lst.append(whole)
    if mod == 0:
        return
    x = (x[1], x[0] - (whole * x[1]))
    cont_fraction(x, lst)
    
def rec_num(lst):
    lst = lst[::-1]
    b = (lst[0], 1)
    for i in range(1, len(lst)):
        a = (lst[i], 1)
        b = ((a[0]*b[0] + a[1]*b[1]), a[1]*b[0])
    return b
    
case = 1
while True:
    len1, len2 = i_(), i_()
    rec1 = [i_() for _ in xrange(len1)]
    rec2 = [i_() for _ in xrange(len2)]


    a = rec_num(rec1)
    b = rec_num(rec2)

    add = ((a[0]*b[1] + a[1]*b[0]), a[1]*b[1])
    sub = ((a[0]*b[1] - a[1]*b[0]), a[1]*b[1])
    mult = (a[0]*b[0], a[1]*b[1])
    div = (a[0]*b[1], a[1]*b[0])

#    exit()
    nums = [add, sub, mult, div]
    #nums = [mult]
    
    print 'Case %d:' % (case)
    case = case + 1

    for num in nums:
        lst = []
        cont_fraction(num, lst)
        print ' '.join(map(str, lst))

