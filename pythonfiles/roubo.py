# class A:
#     def a(self):
#         return 'a'

# class B:
#     def a(self):
#         return 'b'
# class C(B,A):
#     pass

# o=C()
# print(o)

# class Class:
#     def __init__(self):
#         pass



# class A:
#     def __init__(self,v):
#         self.__a=v+1
# a=A(0)
# print(a.__a)

# class Ex(Exception):
#     def __init__(self,msg):
#         Exception.__init__(self,msg+msg)
#         self.args=(msg,)
# try:
#     raise Ex('ex')
# except Ex as e:
#     print(e)
# except Exception as e:
#     print(e)

# class A:
#     def __init__(self):
#         self.a=1
# class B(A):
#     def __init__(self):
#         A.__init__()
#         self.b=2



# try:
#     raise Exception(1,2,3)
# except Exception as e:
#     print(len(e.args))

# class I:
#     def __init__(self):
#         self.s='abc'
#         self.i=0

#         def __iter__(self):
#             return self
        
#         def __next__(self):
#             if self.i==len(self.s):
#                 raise StopIteration
#             v=self.s[self.i]
#             self.i+=1
#             return v
# for x in I():
#     print(x,end='')

# class A:
#     def __init__(self,v=1):
#         self.v = v
#     def set(self,v):
#         self.v=v
#         return v
# a=A()
# print(a.set(a.v+1))

# class A:
#     def __init__(self):
#         pass
# a=A(1)
# print(hasattr(a,'A'))
