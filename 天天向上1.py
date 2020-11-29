def p(df):
    p  = 1.0
    for i in range(365):
        if i %7 in[6,0]:
            p = p*(1-0.01)
        else:
            p = p*(1+df)
    return p
df=0.01
while (p(df)<37.78):
    df+=0.001
print("努力参数：{:.3f}".format(df))
