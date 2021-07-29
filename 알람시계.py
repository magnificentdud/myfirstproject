h = int(input("H: "))
m = int(input("M: "))
if m > 59 or h > 23:
    break

if m > 44:
    print (h, m-45)
    else m<45:
        print (h-1, 60-m)
