def tempconvert (valuestr):
    if valuestr [-1] in ['￥',]:
        C = (eval(valuestr[0:-1])/6)
        print("兑换后是{:.2f}美元".format(C))
    elif valuestr [-1] in ['$',]:
        F=eval(valuestr[0:-1])*6
        print("兑换后是{:.2f}元".format(F))
    else:
        print("输入格式错误")
tempstr = input ("请输入带有符号的钱数:")
tempconvert(tempstr)

