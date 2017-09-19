# 1 判断密码是否正确

# passwd = input("输入密码：")
# # ２密码不正确（输错3次退出程序）
# if passwd != "10010":
#     i = 1
#     while i <= 3:
#         passwd = input("密码错误，请重新输入密码：")
#         if passwd == "10010":
#             print("密码正确。。。。。。。")
#             break
#         i += 1
#     print("密码不正确，程序结束。。。。")
# else:
#     print("密码正确。。。。。。。")

# ３正确 非常有趣的小程序　　　　在研究

i =1
while i<=3:
    passwd = input("输入密码：")
    if passwd == "10010":
        print("密码正确，干活")
    else:
        i += 1
        print("密码错误，请重新输入。。。。。。。。。")
while i>3:
    print("错误三次，明天再试")
    break



