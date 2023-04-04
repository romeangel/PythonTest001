s1 = {10,20,30,40}
s2 = {20,30,40,50,60}

print(s1.intersection(s2))
print(s1 & s2)   #intersection()与  &是等价的交集操作

# 并集操作

print(s1.union(s2))
print(s1 | s2)

# 差集操作
print(s1.difference(s2))
print(s1-s2)
print(s2-s1)
# 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)


