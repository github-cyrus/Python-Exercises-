# class Person:
#       def __init__(self,name,age):
#             self.name = name
#             self.age = age

# x = lambda a : a + 10
# print(x(5))

def myfun(n):
      return lambda a : a * n 

mydoubler =  myfun(5)

print(mydoubler(40))