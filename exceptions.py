import io


def sum(a,b):
    assert(type(a) is int and type(b) is int),"numbers must be integer"
    assert(a>=0 and b>=0), "argumnets must be  positive"
    return a+b



# print(sum(1,0))


# try:
#      print(sum(1,12))
 
# except AssertionError as error:
#     print("assertion error",error)
# except:
#   print('An exception occurred')



# try :
#     x=10
#     if x<12:
#         raise Exception("some ting wrong")
# except Exception as ex:
#     print("rese exception ", ex)
    
    
    
try:
      fn=open('text.txt','r')

except FileNotFoundError as fn:
      print(fn)
except IOError as io_e:
        print(io_e)
else:
        print("file opened")
        fn.close()
        
        
      