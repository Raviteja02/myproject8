x = 100;
print (x)
print (id (x)) #we cant modify the values of immutable objects

x = 200;
print (x)
print (id(x))

y = 100;   #we can't create two immutable objects with same data.
print (y)

print (id(y))  #the address of the object already created will be pointed to the  new variable.


z = [10,20,30]
print (z)
print (type(z))
print (id(z))

z[1] =40
print (z)
print (id(z))  #we can modify the values or elements of the mutable objects.

a =[10,40,30]
print (a)
print (id(a)) #we can create two mutable objects with same data or elements.

