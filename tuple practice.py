my_tuple = ()
print(my_tuple)

my_tuple = (1, "hello", [4,5,6],(1,2,3))
print(my_tuple)
#packing
my_tuple = 3,1.1, "hi"
print(my_tuple)
#unpacking
a, b, c = my_tuple
print(a)
print(b)
print(c)

x = ("hello")
print(type(x))
#if only 1 in tuple, type is string
my_tuple = ('p','r','o','g','r',1,2[3,4])
print(my_tuple[-2:])

my_tuple = ('p','r','o','g','r',1,2[3,4])
my_tuple[7][0] = 5

