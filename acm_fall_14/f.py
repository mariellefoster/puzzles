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



A = {}
for k in xrange(1, 16):
    A[(1, k)] = k
for n in xrange(2, 31):
    A[(n, 0)] = 0
for n in xrange(2, 31):
    for k in xrange(1, 16):
        A[(n, k)] = A[(n, k - 1)] + A[(n - 1, k)]



#memo = {}
def sums(n, k):
    if n == 0:
        return 1
    return A[(n, k)]
#    if k == 1:
#        return 1
#    global memo
#    '''number of ways to pick k ordered nonnegative ints that sum to n'''
#    if (n, k) in memo: 
#        return memo[(n,k)]
#    return sum([
#        sums(n - i, k - 1)
#        for i in range(n + 1)
#    ])


def equal_ratings(ratings):
    if not ratings:
        return 0
    n = len(ratings)
    if n == 1:
        return 1
    total = sum(ratings)
    return sum([
        sums(total - i, n - 1)
        for i in range(ratings[0])
    ]) + equal_ratings(ratings[1:])


case = 1
while True:
    n = i_()
    if not n:
        break
    ratings = [i_() for _ in range(n)]
    total = sum(ratings)
    ans = sum([
        sums(a_total, n) for a_total in range(total)])
    ans += equal_ratings(ratings)
    print 'Case %d: %d' % (case, ans)
    case = case + 1
