from cgi import print_arguments


a = 0
while a < 3:
    name = input('请输入你的名字：')
    if str.isalpha(name) == 1:
        print('录入成功')
        break
    else:
        a = a + 1
        if a == 3:
            print("输入次数过多")
        else:
            print('输入错误，重新输入，请输入文字')

a = 0
while a < 3:
    age = input('请输入你的年龄：')
    if str.isdigit(age) == 1:
        print('录入成功')
        break
    else:
        a = a + 1
        if a == 3:
            print("输入次数过多")
        else:
            print('输入错误，重新输入，请输入数字')        
        

a = 0
while a < 3:
    birth = input('请输入你的生日：')
    if str.isalnum(birth) == 1:
        print('录入成功')
        break
    else:
        a = a + 1
        if a == 3:
            print("输入次数过多")
        else:
            print('录入失败，重新录入，请输入正确生日')
        


print(name)
print(age)
print(birth)