a = 0
""" while a < 4:
    pwd = input("请输入密码：")
    if pwd == 123456:
        print("密码输入正确")
        break
    elif a < 3:
        print('密码输入错误，请重新输入')
        a = a + 1
    else:
        print('错误次数太多，密码锁定')
        a = a + 1 """


while a < 3:
    pwd = input("请输入密码：")
    if pwd == "123456":
        print('密码输入正确')
        break
    elif a < 2:
        print('密码输入错误，请重新输入，错误3次将锁定')
        a = a + 1
    else:
        print('错误次数太多，密码锁定')
        break
    
