def isPrime():
    a= input("请输入")
    b=list("0123456789")
    c=0
    d=0
    for i in a:
        if i in b:
            c+=1
    if c==len(a):
        print("有异常")  
        e= eval(a)
        for i in range(e+1):
            for j in range(e+1):
                if i *j==e :
                    d+=1
        if d==2:
            print("true")
        else:
            print("false")
    else:
        print("输入内容非整数")
        

        
 
