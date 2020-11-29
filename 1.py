from math import sqrt
def getNum():
    nums = []
    iNumStr = input("请输入数字(回车退出):")
    while iNumStr != "":    #死循环判断为空退出，不为空就继续输入并添加到列表里
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出):")
    return nums
getNum()
def mean (numbers):
    s=0.0
    for num in numbers:
        s=s+m
    return s/len (numbers)
def dev (numbers, mean):
    sdev=0.0
    for num in numbers:
        sedv=sedv+(num-mean)**2
    return sqrt(sedv/len(numbers)-1)
def median(numbers):
    new=sorted(numbers)
    size= len(numbers)
    if size %2==0:
        med=(new[size//2-1]+new[size//2])/2
    else:
        med=new[size//2]
    return med
n= getNum()
m=mean(n)
print("平均数{} 标准差{:.2} 中位数 {} ".format(m,\
                                      dev(n,m),median(n)))
