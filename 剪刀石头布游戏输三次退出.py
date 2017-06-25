import random
# i = 1
# while i <= 10:
j = 0
while True:
    # 1 提示并获取用户输入
    player = int(input("请输入您的选择　０剪刀　１石头　2布:"))
    computer = random.randint(0, 2)
    # ２　判断输赢
    # 2.1　你赢了
    if (player == 0 and computer == 3)\
            or(player == 1 and computer == 0) or (player == 2 and computer ==1):
        print("恭喜你，　你赢了。。。。。。。。。。。")
    # ２．２　　平局
    elif player == computer:
        print("平局")
    # ２．３　你输了
    else:
        j += 1
        print("不好意思你输了。。。。。。。。。。")
        if j == 3:
            print("你已经输了三次，再输怕你哭，游戏结束了。。。。。")
            break
    # i += 1

