s = {10,20,30,40}

s1 = {40,30,20,10}
print(s == s1)  #True


s1 = {10,20,30,40}
s2 = {10,20,30,40,50,60,70}
s3 = {10,50,70,90}
#issubset判断是否为子集
print(s1.issubset(s2))
print(s3.issubset(s2))
#issuperset判断是否为超集
print(s2.issuperset(s1))
print(s3.issuperset(s2))
#isdisjoint判断是否没有交集

s4 = {1,2,3,4}
print(s4.isdisjoint(s1))
print(s1.isdisjoint(s2))