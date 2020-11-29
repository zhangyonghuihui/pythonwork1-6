w= eval(input("请输入预设的数"))
g,n=0,0
while g!=w:
    g=eval(input("请猜数"))
    if g<w:
        print("猜小了")
        n+=1
    if g>w:
        print("猜大了")
        n+=1
    if g==w:
        print("猜对了")
        n+=1
        print("猜了{}次".format(n))
