def isNum(n):
    ls=[1,2,3,4,5,6,7,8,9,0,".","i",]
    for i in n:
        if i  not in ls:
            print("不是整数浮点数复数")
            break
        else:
            print("是整数浮点数复数")
num=input("请输入：")
isNum(num)
