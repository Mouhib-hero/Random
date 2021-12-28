#import re
tab = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
tab2 = []
count=0
chaine=input('type the encrypted string: ')
char = " "
#indices = [i.start() for i in re.finditer(char, chaine)]
indices = [i for i, c in enumerate(chaine) if c == char]
chaine = chaine.replace(" ","")
print(chaine)
print(indices)
chaine2=""
a=0
for i in range(26):
    if (i==0):
        continue
    for j in range(26):
        if(i+j<26):
            tab2.append(tab[i+j])
            count=0
        else:
            tab2.append(tab[count])
            count=count+1
    for j in range(len(chaine)):
        chaine2=chaine2+tab[tab2.index(chaine[j].upper())]
    print(tab2)
    tab2=[]
    #print(chaine2)
    #chaine2=""
    for i in range(len(indices)):
        chaine2=chaine2[:indices[i]]+" "+chaine2[indices[i]:]
    print(chaine2)
    chaine2=""
