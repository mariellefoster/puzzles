buffer = []

def i_(line=False):
    global buffer
    if line:
        return map(int, raw_input().split())
    if not buffer:
        buffer = raw_input().split()
    return int(buffer.pop(0))

def s_(line=False):
    global buffer
    if line:
        return raw_input().split()
    if not buffer:
        buffer = raw_input().split()
    return buffer.pop(0)

def i_end_nul(fn):
    while True:
        try:
            fn(i_())
        except EOFError as e:
            break

def i_end_0(fn):
    while True:
        i = i_()
        if i == 0:
            break
        fn(i)

def s_end_nul(fn):
    while True:
        try:
            fn(s_())
        except EOFError as e:
            break

def s_end_str(fn, str_):
    while True:
        s = s_()
        if s == str_:
            break
        fn(s)


def main(i):
    print int(i)+1

s_end_nul(main)
