for i in range(1,51):
    if i % 5 != 0:
        continue
    print(i,end='\t')
print()



for i in range(5):
    for j in range(1,51):
        if j % 2 == 0:
            break
            #continue
        print(j,end="\t")
    print()