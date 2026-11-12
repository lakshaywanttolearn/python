#\\\\\TUPLE\\\\ immutable ,()

a=50,   #same as a=(50,) and a=(50) it considred as int datatype
print(type(a)) #single element tuple

#it contains any kind of datatype in it
b=(10,20,30,"hello",False,42.2,40) 

#negative indexing and positive indexing 
print(b[0],b[-1])
#but reassining is not allowed in tuple 
#b[0]=20 gives error

#functions
c = (10,40,50,30,50)
print(sum(c))#gives sum
print(max(c))#gives max
print(min(c))#gives min
print(len(b))#gives length
print(sorted(c))#gives sorted list of tuple
print(sorted(c,reverse=True))#gives sorted reversed list of tuple

#methods
print(c.count(50))#count how many times it occurs
print(c.index(50))#gives index   

#tuples can be concatinted and dublicated
print(b+c)
print(c*2)

#treversing of tuple
for num in c:
    print(num)

for i in range(len(b)):
    print(b[i])
