buffer = []
def i_():
    global buffer
    while not buffer:
        try:
            buffer = raw_input().split()
        except:
            exit()
    return int(buffer.pop(0))

def is_valid_preorder(t):
    if len(t) <= 1:
        return True
    mid, rest = t[0], t[1:]
    left = []
    right = []
    i = 0
    while i < len(rest):
        if rest[i] > mid:
            break
        left.append(rest[i])
        i += 1
    while i < len(rest):
        if rest[i] < mid:
            return False
        right.append(rest[i])
        i += 1
    return is_valid_preorder(left) and is_valid_preorder(right)\




case = 1
while True:
    t = []
    while True:
        i = i_()
        if i < 0:
            break
        t.append(i)
    ans = is_valid_preorder(t)
    print 'Case %d: %s' % (case, 'yes' if ans else 'no')
    case += 1
