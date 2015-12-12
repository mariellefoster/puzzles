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

case = 1
while True:
    n = i_()
    t = i_()
    jobs = map(int, raw_input().split())
    count = len(jobs)
    while jobs and t >= jobs[0]:
        t -= jobs.pop(0)
    print 'Case %d: %d' % (case, count - len(jobs))
    case += 1
