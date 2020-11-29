def isPrime(a):
    a= input("请输入")
    b=list("0123456789")
    c=0
    for i in a:
        if i in b:
            c+=1
    if c==len(b):
        print("有异常")
            
        
