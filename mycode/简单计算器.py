# 1 获取输入的信息
summ =0
num1 = input("输入第一个数字并回车：")
n1 = int(num1)
signal = input("输入运算符：")
num2 = input("输入第二个数字字并回车：")
n2 = int(num2)
# ２　判断运算符计算
if signal == "+":
    summ = n1 + n2
    print("%d+%d=%d " % (n1, n2, summ))
elif signal== "-":
    summ = n1 -n2
    print("%d-%d=%d " % (n1, n2, summ))
elif signal== "*":
    summ = n1 *n2
    print("%d*%d=%d " % (n1, n2, summ))

elif signal== "/":
    summ = n1 /n2
    print("%d/%d=%d " % (n1, n2, summ))
else:
    print("输入有错误！")
