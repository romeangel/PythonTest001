s = set()
s.add(80)
print(s)
s.update({200,300,400})
print(s)
s.update([2,3,4,5])
print(s)
s.update((11,22,33))
print(s)


s.remove(200)
print(s)

s.pop()
print(s)
s.clear()
print(s)