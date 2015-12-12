import math
buffer = []

def i_(line=False):
    global buffer
    if line:
        return map(int, raw_input().split())
    if not buffer:
        try:
            input = raw_input()
        except:
            exit()
        if not input:
            exit()
        buffer = input.split()
    return int(buffer.pop(0))


def choose(n, k):
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))

n = i_()
casee = 1
for case in range(n):
    n, k = i_(), i_()
    print 'Case %d: %d' % (casee, choose(n, n + 1 - k))
    casee = casee + 1
