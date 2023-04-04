money = 10000
s = int(input('请输入取款金额：'))

if money >= s:
    money = money - s
    print("取款成功，当前余额为：",money)
else:
    print("余额不足，余额为：",money)
