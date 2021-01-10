# # # from abc import ABC, abstractmethod
# # # class A(ABC):
# # #     @abstractmethod
# # #     def get(self):
# # #         pass
# # # class B(A):
# # #     def set(self):
# # #         return 'B'
# # #
# # # b=B()
# # # print(b.set())
# #
# # a=[1,2]
# # b=[x**2 for x in a if x<2]
# # print(b)
#
# a=lambda x: lambda y: x+y
# print(a(3)(5))

from operator import add, sub
d={'add':add, 'sub':sub}
print(d.get('mul',add)(5,4))
print(d.get('mul',sub)(5,4))
print(d)