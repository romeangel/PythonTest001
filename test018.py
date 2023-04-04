i =[1,2,35564,4,5,9,11,555,12]
print(i,id(i))

i.sort()
print(i,id(i))

i.sort(reverse=True)
print(i)

i.sort(reverse=False)
print(i)


i =[1,2,35564,4,5,9,11,555,12] 
print('原列表',i)
new_i = sorted(i)
print(i)
print(new_i)


