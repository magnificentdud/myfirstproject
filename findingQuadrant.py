while True:
    x = int(input("enter x: "))
    y = int(input("enter y"))
if x < 100 and x > -100 and y < 100 and y > -100 and x!=0 and y!= 0:
    stop
print ("ERROR: NUMBERS OUT OF RANGE")
if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y < 0:
    print(3)
elif x < 0 and y > 0:
    print(2)

