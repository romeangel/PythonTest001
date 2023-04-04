a = [ i * 2 for i in range(1,11)]
print(a)

scroes = {'张三':100,'李四':98,'王五':60}

so = dict(name = 'jack',age = 20)

print(scroes,'你的名字：',so['name'],so['age'])

print(so.get("name"))
print(so.get("王二麻子",0))
#so.clear()
so["王二麻子"] = 0
print(so)

print(type(so.keys()))

print(so.keys())

#print(list(so.keys()))

print(list(so.items()),type(so.items()))


for i in so:
    print(i,so[i])