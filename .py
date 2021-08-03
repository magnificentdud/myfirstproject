#lists

my_list = [1, "hello", [1,2,3]]
print (my_list)

#accessing
print (my_list[1][4])
print (my_list[-2][-1])

#slicing
my_list = ['a','b','c','d','e','x','y','z']
print (my_list[5:9])


odd = [2,4,6,8]
odd[0]=1
print[odd]
print (odd)
odd[1:4] = [3,5,7]
#appending
odd.append(9)
#extending
odd.extend([11,13])
#concatenating
#not change og list
odd= [1,3,5]
print(odd + [5,7,9])
print(odd)
print(["a"]*3)


#append, extend, contact
#insert() method..
odd = [1,9]
odd.insert(1,3)
print(odd)
print(odd)
odd[2:2] = [5,7]
print(odd)



#deleting removing

my_list = ['p','r','o','b','l','e','m']

del my_list[2]
print(my_list)
del my_list[1:5]
print(my_list)



#removing
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
print(my_list)


#pop
my_list = ['p','r','o','b','l','e','m']
print(my_list.pop())


#clear
my_list = ['p','r','o','b','l','e','m']
my_list.clear()
print(my_list)
