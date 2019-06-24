import random
l1=[0]*10
s=''
while(len(s)<=3):
    k=random.randint(0,9)
    if str(k) not in s:
        s=s+str(k)
print(s)
l2=[]
for i in s:
    l2.append(int(i))

print(l2)
for i in l2:
    l1[i]=1
print(l1)
count=0
bulls=0
while(bulls!=4):
    bulls=0
    cows=0
    a=input("Guess another no : ")
    l=list(a)
    count+=1
    for i in range(4):
        if(int(l[i])==l2[i]):
            bulls+=1
    for i in a:
        if int(i) in l2:
            cows+=1
    cows=cows-bulls
    print("bulls :",bulls,"\n","cows : ",cows)
if(bulls==4):
    print("you won !")
