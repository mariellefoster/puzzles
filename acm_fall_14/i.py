buffer = []

def i_():
    global buffer
    while not buffer:
        try:
            buffer = raw_input().split()
        except:
            exit()
    return buffer.pop(0)

case = 1
while True:
    n = int(i_())
    d = {i: set() for i in range(40)}
    for i in xrange(n):
        w = i_().strip()
        d[len(w)].add(tuple(sorted(list(w))))
    m = int(i_())
    
    print 'Case %d:' % case
    case += 1
    
    for i in xrange(m):
        top, bottom = i_(), i_()
        top, bottom = tuple(sorted(list(top))), tuple(sorted(list(bottom)))
        if any(x not in bottom for x in top):
            print 'no'
            continue
        candidates = [bottom]
        size = len(bottom)
        opts = []
        while size != len(top):
            for c in candidates:
                opts += [tuple(c[:i] + c[i + 1:]) for i in xrange(len(c))]
            size -= 1
            opts = filter(lambda opt: opt in d[size], opts)
            opts = list(set(opts))
            candidates = filter(lambda opt: all(x in opt for x in top), opts)
            opts = []
        print ('yes' if top in candidates else 'no')
