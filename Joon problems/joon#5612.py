r_time = int(input())
initial_c = int(input())

max_cars = initial_c
for i in range(r_time):
    in_c, out_c = map(int, input().split())
    initial_c = initial_c + in_c - out_c 
    if initial_c < 0:
        max_cars = 0
        print(0)
        exit()

    if max_cars < initial_c:

        max_cars = initial_c
print(max_cars)