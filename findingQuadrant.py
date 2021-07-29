x = int(input())
-100 <= x <= 100, x != 0

y = int(input())
-100 <= y <= 100, y != 0

if x > 0 and y > 0:
    print(1)
if x > 0 and y<0:
    print(4)
if x < 0 and y < 0:
    print(3)
if x < 0 and y > 0:
    print(2)
