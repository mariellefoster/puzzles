buffer = []

def i_():
    global buffer
    while not buffer:
        try:
            input_ = raw_input()
        except:
            exit()
        buffer = input_.split()
    return int(buffer.pop(0))

case = 0
while True:
    cons = i_()
    case += 1
    j1 = [(i_(), i) for i in range(cons)]
    j2 = [(i_(), i) for i in range(cons)]
    s1 = sorted(j1, reverse=True, key=lambda x: x[0])
    s2 = sorted(j2, reverse=True, key=lambda x: x[0])
    printed = False
    i = 0
    while i < cons:
        if s1[i][1] != s2[i][1]:
            print 'Case %d: %d' % (case, i+1)
            printed = True
            break
        i += 1
    if not printed:
        print 'Case %d: agree' % case
