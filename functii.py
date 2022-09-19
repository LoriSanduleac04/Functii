n=int(input('n=  '))
m=int(input('m=  '))

def suma(n,m):                               #Suma numerelor;
    S=n+m
    return S

print("Suma numerelor este ",suma(n,m))

def produs(n,m):                             #Produsul numerelor;
    P=n*m
    return P

print("Produsul numerelor este ",produs(n,m))

def media(n,m):                              #Media aritmetica a numerelor;
    MA=(n+m)/2
    return MA

print("Media aritmetica a numerelor este ",media(n,m))

def divizor(n, m):                           #Cel mai mare divizor comun;
    if(m == 0):
        return n
    else:
        return divizor(m, n % m)

print("Cel mai mare divizor comun este ", divizor(n,m) )

def multiplu(n,m):                           #Cel mai mic multiplu comun;
    multiplu = (n*m)/divizor(n,m)
    return multiplu

print("Cel mai mic multiplu comun este ", multiplu(n,m))

def minim(n,m):                              #Numarul minim;
    if n>m:
        minim=m
    if m>n:
        minim=n
    if m==n:
        minim="sunt egale"
    return minim

print("Numarul minim este ", minim(n,m))

def maxim(n,m):                              #Numarul maxim;
    if n>m:
        maxim=n
    if m>n:
        maxim=m
    if m==n:
        maxim="sunt egale"
    return maxim

print("Numarul maxim este ", maxim(n,m))
    
def suma():                                 #Suma numerelor in formatul a + b=c, dacà a si b reprezintà numerele citite;
    a=int(input('a=  '))
    b=int(input('b=  '))
    c=a+b
    print(a,"+",b,"=", c)

c=suma()

def produs():                               #Produsul numerelor in formatul a *b=c, dacà a si b reprezintà numerele citite;
    a=int(input('a=  '))
    b=int(input('b=  '))
    c=a*b
    print(a,"*",b,"=", c)

c=produs()

def toti_divizorii(n,m):                     #Toti divizorii comuni;
    div=[]
    print("Toti divizorii comuni al lui ",n,"si",m,"sunt: ")
    for i in range(1,min(n,m)+1):
        if n%i == m%i == 0:
            div.append(i)
    return div

print(toti_divizorii(n,m))

lista_multipli=[]
def multipli_comuni(n,m):                      #Cinci multipli comuni;
    h=n*m
    for i in range(5):
        lista_multipli.append(h)
        h=h*2
multipli_comuni(n,m)
print("Cinci multipli comuni sunt: ", lista_multipli[0:5])

a=list(map(int, str(n)))
b=list(map(int, str(m))) 

def cifre_com(a, b):                          #Cifrele care se contin in ambele numere;
    return set(a).intersection(b)
  
print("Cifrele care se contin in ambele numere sunt: ", cifre_com(a, b))

d=[]
def diferenta(a, b):                          #Cifrele care sunt in primul numar si nu sunt in al doilea numar;
    for element in a:
        if element not in b:
            d.append(element)
    return d
  
print("Care sunt in primul numar si nu sunt in al doilea numar sunt: ", diferenta(a, b))

def prietene(n):                              #Va afisa mesajul PRIETENE, dacà numerele sunt prietene. Douà numere se numesc prietene, dacà numärul de divizori este acelasi.
    k=0
    for i in range(1,n+1):
        if n% i==0:
            k+=1
    return k
if prietene(m)==prietene(n):
    print("PRIETENE")
else:
        print("NU SUNT PRIETENE")