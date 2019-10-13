f=iter(open("family.ged").readlines())
name='GIVN'
surn='SURN'
sex='SEX'
n=[]
f=[]
s=[]
for line in f:
    if name in line:
        n.append(line[5:])
    elif surn in line:
        f.append(line[:5])
    elif sex in line:
        s.append(line[:4])
#f.close()
print(n)





            