tempstr = input("请输入体重：")
while tempstr[-1] not in ['n','N']:
    if tempstr [-1] in ['￥']:
        C = (eval(tempstr[0:-1])/6)
        print("转换后是{:.2f}$".format(C))
    elif tempstr [-1] in ['$']:
        F=6*eval(tempstr[0:-1])
        print("转换后是{:.2f}￥".format(F))
    else:
        print("输入格式错误")
    tempstr = input ("请输入:")
