# 1 　判断ｉ的行号
i=0
    # １．１　当ｉ=< 5: 打印ｉ个星星
while i<5:
    str=" "*(5-i)+"*"*(2*i+1)
    # print("-"*(5-i)+"*"*(2*i+1)))
    # print("*"*i)
    print(str)
    print("\n")
    i+=1
    # １．２　当ｉ>5:打印１０－ｉ个星星
while 10>i>=5:
    str = (" "*(i-5)+"*"*(10-((i-5)*2+1)))
    # print("-"*(i-5)+"*"*(10-i))
    # print("*"*(10-i))
    print(str)
    print("\n")
    i+=1
