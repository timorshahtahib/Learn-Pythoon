def sum(a,b):
    assert(type(a) is int and type(b) is int),"numbers must be integer"
    assert(a>=0 and b>=0), "argumnets must be  positive"
    return a+b



# print(sum(1,0))


try:
     print(sum(1,12))
 
except AssertionError as error:
    print("assertion error",error)
except:
  print('An exception occurred')