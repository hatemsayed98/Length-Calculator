wrd=input("enter word: ")
a=0
e=0
i=0
u=0
o=0
for l in range(len(wrd)):
    letter=wrd[l]
    if letter=='a':
        a=a+1
    if letter== 'A':
        a=a+1
    if letter== 'e':
        e=e+1
    if letter=='E':
        e=e+1
    if letter=='i':
        i+=i
    if letter=='I':
        i=i+1
    if letter=='o':
        o=o+1
    if letter=='O':
        o=o+1
    if letter=='u':
        u=u+1
    if letter=='U':
        u=u+1
print("number of a: ",a)        
print("number of e: ",e)
print("number of i: ",i)
print("number of o: ",o)
print("number of u: ",u)
print("number of vowels: ",a+e+i+o+u)
