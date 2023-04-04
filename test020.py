from multiprocessing.sharedctypes import Value


items = ['Girls','Boys','Peoples']
prices = [1,2,3,4]

s = {key.upper():value for key,value in zip(items,prices)}
print(s)