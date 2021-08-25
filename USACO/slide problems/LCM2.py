x = int(input())
y = int(input())

def GCD(x,y):
    while(y):
        x, y=y, x%y
    return x

def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return result
print(LCM(x,y))


