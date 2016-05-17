
def Newton(n,m):
    r = 1
    for i in range(1, m+1):
        r = r * (n + 1 - i)/i
    return r


def Pascal(n):
    triangle=[]
    for i in range(n):
        l = []
        for k in range(i+1):
            l.append(Newton(i,k))
        triangle.append(l)

    return triangle


def LotOfHash(n):
    for t in Pascal(n):
        print "".join([ "#" if i % 2 != 0 else " " for i in t])


def PowerModulo(a, b, n):
    return a**b % n


# def Intersect(a, b):
#     x1, y1, r1 = a
#     x2, y2, r2 = b
#     x,y = 0,0


