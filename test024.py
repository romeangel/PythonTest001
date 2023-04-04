#集合的第一用创建方式，集合是没有value的字典，是无序的

s = {2,3,4,5,5,6,7,7}

print(s)

#第二种创建方式，使用set()

s1 = set(range(6))

print(s1,type(s1))

s2 = set([1,2,3,4,5,6666,6666,6666])

print(s2)

s3 = set((1,44,44,2,3,4,77,77,55))

print(s3)

print(set('Python'))

#定义空集合
s7 = set()
#不可以使用｛｝直接定义，否则会变为dict

