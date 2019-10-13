f="family.ged"
p="prolog.pl"
file=open(f,"r")
lines=file.readlines()
file.close()
n=[]
f=[]
s=[]
ind=[]
person=""
for line in lines:
    if 'GIVN' in line:
        n.append(line[7:-1])
    elif 'SURN' in line:
        f.append(line[7:-1])
    elif 'SEX' in line:
        s.append(line[6:-1])
    elif 'INDI' in line:
        ind.append(line[4:-7])
file=open(p,"a")
i=0
while i < len(n):
    person = n[i] +" "+ f[i]
    if s[i]=="M":
        file.write("male("+person+").\n")
    i+=1
i=0
while i < len(n):
    person = n[i] +" "+ f[i]
    if s[i]=="F":
        file.write("female("+person+").\n")
    i+=1
fams = []
husb = ""
wife = ""
child = []
for line in lines:
    word = line.split(' ')
    if word[1] == "HUSB":
        husb = line[9:-2]
    if word[1] == "WIFE":
        wife = line[9:-2]
    if word[1] == "CHIL":
        child.append(line[9:-2])
    if (len(word) > 2 and word[2] == "FAM\n" and (husb != '' or wife != '')):
        fams.append([husb, wife, child])
        husb = ''
        wife = ''
        child = []

def conv(person):
    i=0
    while ind[i] != person:
        i+=1
    person = n[i]+" "+f[i]
    return person
fam=[]
for fam in fams:
    if fam[0] != '':
        for child in fam[2]:
            file.write("child(" + conv(child) + ", " + conv(fam[0]) + ").\n")
for fam in fams:
    if fam[1] != '':
        for child in fam[2]:
            file.write("child(" + conv(child) + ", " + conv(fam[1]) + ").\n")
file.close()