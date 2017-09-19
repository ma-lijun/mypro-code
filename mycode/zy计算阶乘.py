# 获取要计算的阶乘值
i = int(input("请输入要计算的阶乘数字："))
jie = 1
while i > 0:
    jie *= i
    i -= 1
print("%d的阶乘是：%d" % (i, jie))
