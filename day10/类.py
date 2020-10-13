# class Person():
#     def __init__(self,name,age):
#         self.names=name
#         self.ages=age
#         #print(self)
#
#         #print(id(self))
#
#
#
# p1=Person("yuan",28)
# p2=Person("yuan",28)
# print(id(p1))
# print(id(p2))

class Cal(object):

    @staticmethod
    def add(x,y):
        print(x,y)
        return x+y
    @staticmethod
    def mul(x,y):
        print(x*y)

c = Cal()
sum = c.add(1,3)
print(sum)
print(Cal.add(1,3))