d = input("请输入你的名字：")
if len(d) == 0:
    print("请输入内容")
elif str.isdigit(d) != 1:
    print("请输入有效内容")
else:
    print('输入完毕')