while true:
    h = int(input("H: "))
    m = int(input("M: "))
    if m > 59 or h > 23:

if m > 44:
    print (h, m-45)

elif m <= 44 and h >= 1:
    print (h-1, m+15)


else: 
    print (23, m+15)
