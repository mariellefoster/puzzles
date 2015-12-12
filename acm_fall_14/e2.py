import math
buffer = []

def i_():
    global buffer
    if not buffer:
        try:
            buffer = raw_input().split()
        except:
            exit()
    return int(buffer.pop(0))


def f_():
    global buffer
    if not buffer:
        try:
            buffer = raw_input().split()
        except:
            exit()
    return float(buffer.pop(0))


def reorder_vertices(v):
    bottom = [x for x in v if x[1] == 0]
    left, right = tuple(sorted(bottom))
    v.reverse()
    left_i = v.index(left)
    new_v = [v[(i + left_i) % len(v)] for i in xrange(len(v))]
#    return new_v, ((left[0] + right[0]) / 2.0, 0)
    return new_v


#def area_from_vertices(v, midpoint):
#    total_area = 0
#    last_vert = (v[0][0] - midpoint[0], v[0][1])
#    i = 1
#    while i < len(v):
#        curr_vert = (v[i][0] - midpoint[0], v[i][1])
#        total_area += abs((last_vert[0] * curr_vert[1] - last_vert[1] * curr_vert[0])/ 2.0)
#        last_vert = curr_vert
#        i += 1
#    return total_area


def max_y_from_vertices(v):
    return max(v, key=lambda x: x[1])[1]

def interpolate_x(lower, upper, y):
    slope = (upper[0] - lower[0]) / float((upper[1] - lower[1]))
    return lower[0] + slope * (y - lower[1])


def width_of_tank(left_wall, right_wall, y):
    l_pt_i = 0
    while left_wall[l_pt_i][1] < y:
        l_pt_i += 1
    r_pt_i = 0
    while right_wall[r_pt_i][1] < y:
        r_pt_i += 1
    l_x = interpolate_x(left_wall[l_pt_i - 1], left_wall[l_pt_i], y)
    r_x = interpolate_x(right_wall[r_pt_i - 1], right_wall[r_pt_i], y)
    return r_x - l_x


case = 1
while True:
    n = i_()
    b, l = f_(), f_()
    v = [(i_(), i_()) for _ in xrange(n)]
    v = reorder_vertices(v)

    # "Amount of area" beying poured into the polygon
    area_amt = l / b / 10  # in m^2
    
    # Find y of top edge
    max_y = max_y_from_vertices(v)
    
    # Find index of upper left and right vertices
    upper_left_i = 0
    while v[upper_left_i][1] != max_y:
        upper_left_i += 1
    upper_right_i = upper_left_i + 1
    
    # Find the vertices that make up each wall
    left_wall = v[:upper_right_i]
    right_wall = v[upper_right_i:]
    right_wall.reverse()
    
#    print left_wall
#    print right_wall
#    print 'hi', width_of_tank(left_wall, right_wall, 5)
    
    max_y = max_y / 100.
    
    left_i = 0
    right_i = 0
    y = 0.0
    amt = 0.0
    while y < max_y and amt < area_amt:
        if (left_wall[left_i + 1][1] < right_wall[right_i + 1][1]):
            left_i += 1
            new_y = left_wall[left_i][1] / 100.
        else:
            right_i += 1
            new_y = right_wall[right_i][1] / 100.
        
        height = new_y - y
        w2 = width_of_tank(left_wall, right_wall, new_y * 100) / 100.
        w1 = width_of_tank(left_wall, right_wall, y * 100) / 100.
        width = (w2 + w1) / 2.0
        
        if (amt + width * height <= area_amt):
            amt += width * height
            y = new_y
        else:
            s = (w2 - w1) / (new_y - y)
            a = area_amt - amt
            dy = ( -w1 + math.sqrt(w1 ** 2 + 2 * s * a) ) / 2
            y += dy
            break
    
    
    
    
#    step = max_y / 10000000.0
#    y = 0
#    amt = 0
#    while amt < area_amt and y < max_y:
#        w = width_of_tank(left_wall, right_wall, y * 100) / 100.
#        amt += w * step
#        y += step
#    print y, max_y



    print 'Case %d: %.04f' % (case, y * 100)
    case += 1
    
    
    
#    v, midpoint = reorder_vertices(v)
#    area = area_from_vertices(v, midpoint)
#    print area
#    ans = l / (area * b)
#    print 'Case %d: %.04f' % (case, ans)
#    case += 1
