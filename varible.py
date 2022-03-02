x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# casting
print('casting')

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#end casting

#Many Values to Multiple Variables
print('Many Values to Multiple Variables')
a,b,c,d=1,2,3,4
print(a)
print(b)
print(c)
print(d)



#One Value to Multiple Variables
print('One Value to Multiple Variables')

a=b=c=d=2

print(a)
print(b)
print(c)
print(d)




#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

frutes=['apple','banan','orange']
x,y,z=frutes
print(x)
print(y)
print(z)




#  global varible


print('global varioble')


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print(x)
