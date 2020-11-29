w= input("请输入文本")
g= "1234567890"
k="qwertyuiopasdfghjklzxcvbnQWERTYUIOPASDFGHJKLZXCVBN"
m=" "
mm=0
gg=0
kk=0
zs=0
qt=0
for i in w:
    for l in g:
        if i== l:
            gg+=1
    
    for q in k:
        if q==i:
            kk+=1
    if i==m:
        mm+=1
    
    zs+=1
qt=zs-gg-kk-mm
print ("数字个数为：{}。字母个数为：{}。空格个数为：{}。其他字符个数为{}。".format(gg,kk,mm,qt))
