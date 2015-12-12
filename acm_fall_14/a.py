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
    case += 1
    i = i_()
    bs = bin(i)[2:]
    bs = map(lambda x: x=='1', bs[::-1])
    tot = sum((2**n) * (n+1) for n in range(len(bs)))
    big = 2**len(bs) - 1
    delta = len(bs) * (big-i)
    tot -= delta
    print "Case %d: %d" % (case, tot)