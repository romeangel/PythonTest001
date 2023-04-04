#coding:utf-8
name = 'xxx'
age = 20
print(type(name),type(age))

print("我叫" + name + "今年" + str(age) + '岁')

print(type(str(age)))

a = 10
b = '3.14'
c = False
d = 1.1
e = 2.2
print(int(d)+int(e))
print(type(b),type(c))
print(type(str(c)))
print(int(c),type(int(c)))


print(float(c),type(float(c)))
print(float(a))
print(float(b))


name = input('请输入你的名字：')
if str.isalpha(name) == 1:
    print('录入成功')
    age = input('请输入你的年龄：')
    if str.isdigit(age) == 1:
        print('录入成功')
        birth = input('请输入你的生日：')
        if str.isalnum(birth) == 1:
            print('录入成功，结束录入')
        else:
            print('录入失败，重新录入')
    else:
        print('请输入数字')
else:
    print('请输入文字')



def input_message_name(name):
    name = input('请输入你的名字：')
    if str.isalpha(name) == 1:
        print('录入成功')
    else:
        print('输入错误，重新输入，请输入文字')

def input_message_age(age):
    age = input('请输入你的年龄：')
    if str.isdigit(age) == 1:
        print('录入成功')
    else:
        print('输入错误，重新输入，请输入数字')

def input_message_birth(birth):
    birth = input('请输入你的生日：')
    if str.isalnum(birth) == 1:
        print('录入成功，结束录入')
    else:
        print('录入失败，重新录入，请输入正确生日')

