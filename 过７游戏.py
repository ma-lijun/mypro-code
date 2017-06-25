# 1 获取输入数字
# number=int(input("输入一个１００以内的数字："))
# ２　判断数字
# if number%7 or number%10:
#     print()
# # ３　打印结果
# else:
#     print(number)

i=100
# while 实现循环打印
while i>=0:
    # if (not(i%10)%7 and (i/7)):
    #     print(i)
    # 判断数字不是７的倍数
    if i%7:
        # 判断数字不含有７
        if (i%10-7):
            # 判断十位数是否为７
            if (i//10)!=7:
                print(i)

    i-=1
