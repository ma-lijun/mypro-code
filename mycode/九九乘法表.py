# 1 行循环
i = 1
while i <= 9:
    # 2 内层循环
    j = 1
    while j <= i:
        print("%d*%d=%d \t" % (j, i, j*i), end="")
        j += 1

    print("")
    i += 1
