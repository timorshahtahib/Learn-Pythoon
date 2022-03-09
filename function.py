
from unittest import result


def sayhello():
    print("hi")   


sayhello()


# 0,1,1,2,3,5,8,13 ......
def fib(n):
    
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
        
    return result

    
    
print(fib(100))