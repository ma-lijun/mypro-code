# 1 　获取身高和体重的

height = input("请输入身高(kg)：")
weight = input("请输入体重(cm)：")
h = int(height)/100
w = int(weight)
# ２　计算ＢＩＭ值
bim = w/(h*h) #int(weight)/((int(height)/100) ^ 2)
print(bim)

# ３　判断标准并输出
if bim < 18.5:
    print("低于１８．５：过轻")
elif bim < 25:
    print("正常")
elif bim < 28:
    print("过重")
elif bim < 32:
    print("肥胖")
else:
    print("严重肥胖")