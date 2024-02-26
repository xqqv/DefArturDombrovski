from DefArturDombrovski import*
from random import*

a=[]
b=[]

for i in range(5):
    a.append(randint(-20,20))
for i in range (1,4):
    arv=int(input(f" {i}. arv "))
    b.append(arv)
print(a)
print(b)
print()
suurim_element(a,b)

a=randint(-10,10)
print("Esineme arv=",a)
b=float(input("Teine arv:"))
kor=Korrutis(a,b,5.5)
print("Tulemus:",kor)
kor=korrutis(a,b,10)
print(f"Tulemus: {b}*{a}*{b}*10=",kor)
 