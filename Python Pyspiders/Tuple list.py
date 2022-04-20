#it is more storage effecient and according to the situation immutability is also useful

#2

a= 10,
print(type(a))

#3

a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
#print( c = (*a , *b))

#4

t = [1, 2, 3, 4, ["hai", "hello", 23], "python"]
#t[4][0][-1] = 'y' #it shows error because string is an immutable value
print(t)


#5
t[1:3] = ["hai", 10]
print(t)

#6

a = [1, 2, 3]
b = [4, 5, 6]
print([a, b])
print((a, b))

