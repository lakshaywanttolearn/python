#\\\\\LIST\\\\ mutable ,[]

a=[10]   
print(type(a)) #single element list

#it contains any kind of datatype in it
b=[50,20,30,"nice",True,78.2,20] 

#negative indexing and positive indexing 
print(b[0],b[-1])
#DIFFERENCE reassining is allowed in list BUT NOT IN TUPLE 
b[0]=20 
print(b)

#functions
c = [10,40,20,30,20]
print(sum(c))#gives sum
print(max(c))#gives max
print(min(c))#gives min
print(len(b))#gives length
print(sorted(c))#gives sorted list of tuple
print(sorted(c,reverse=True))#gives sorted list of tuple

#methods
print(c.count(20))#count how many times it occurs
print(c.index(20))#gives index   
c.sort()#it sorted the orignal list all above fun and method are no changing in the orignal list
print(c)

#\\\\\\\ADD NEW VALUES
b.append("hello")#add a value at the end of list
print(b)
c.insert(3,99)#insert in between insert(pos,val)
print(c)
b.extend(c)#all c element got attached at the end of b
print(b)

#\\\\\\\deletion
b.pop(4)#delete the element present at that position pop(pos)if no pos then remove last element
print(b)
b.remove("hello")#delete the element in the brackets if present multiple times it deleted who found the first
print(b)
del b[0]#delete the thing after del
print(b)
