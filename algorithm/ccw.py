# input
# 1 1
# 5 5
# 7 3
# output
# -1

# input
# 1 1
# 3 3
# 5 5
# ouput
# 0

# input
# 1 1
# 7 3
# 5 5
# output
# 1

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

res = ccw(x1, y1, x2, y2, x3, y3)
if res > 0:
    print(1)
elif res == 0:
    print(0)
else:
    print(-1)
