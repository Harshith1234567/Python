#1


#print(~10)
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names.append(['netflix', 'walmart', 'kroger'])
print(names)
names.extend(['netflix', 'walmart', 'kroger'])
print(names)

#2


a=names.pop(0)
print(a)
print(names)

a=names.remove("google")
print(a)
print(names)

#3
n=['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
n.sort(reverse=True)
print(n)

#4

names.sort(key= len)
print(names)

#5

names.sort(reverse = True, key = len)
print(names)
#help('list')

#6

s = "Hi welcome to python"
l=list(s)
print(l)



s = "Hi welcome to python"
l=s.split()
print(l)

#7

#to make a copy of all data in antother location

#8

#.copy is used to make a shallow copy where nested list data is not stored in a different space 