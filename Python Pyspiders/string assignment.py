"""
#1

a="hai welcome to python"
a=a.replace(" ",",")
print(a)

print("\n")
print("\n")
print("\n")

#2 function
def chec(b):
    if len(b)==0:
        return True
    else:
        return False



print(chec(""))
print(chec("hi"))
print(chec("hai welcome to python"))

#3
print("\n")
print("\n")
print("\n")

c="hai welcome to python"
if c.count("python"):
    print(True)
else:
    print(False)

#4
print("\n")
print("\n")

print("1234".isdigit())
print("hello1234".isdigit())

#5

print("\n")
print("\n")


d="hello world"
print(d[::-1])


#6

#s="abc"
#s[1]="g"

#7

s="www.python.org"
print(s.strip("w.org"))

#8

print("python".index("o"))


#9

print("she sells sea shells near the sea shore".count("s"))





"""

#11
msg="hi hello how are you why are you here"

#print(msg.replace("hi hello how are","hey who are"))



#msg="hi hello how are you why are you here"
#print(msg.split(" ",3)[1:])


#print(msg.split("are"))

#not possible to extract 'how are you' from msg using strip method
print(msg.strip('hielo'))



#print((msg.title()).replace(" ","#"))














"""
#12

a="123"
b="456"
c=a+b
print(c)


#13
print("india\n"*10)


#14

q="I Love my country"
q=q[::-1]
print(q.replace("o","@"))

#15
c="truth or dare".count("r")
i=0
for j in range(c): 
    print("truth or dare".index("r",i+1,len("truth or dare")))
    

    print("truth or dare".find("r",i+1,len("truth or dare")))
    i="truth or dare".index("r",i+1,len("truth or dare"))



#10



print("msg".find("a"))

print("msg".index("a"))



"""
#