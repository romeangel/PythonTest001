a = [1,2,3,4,5,6]
b = [7,8,9,10]
c = a.insert(0,b)
a.extend(b)
print(a)

a[1:3]=b
print(a,b)



a.pop(0)
print(a)

s = a.clear
print(s)

a[1]=999
print(a)

a[6:7]=[11,22,33,44,55]
print(a)