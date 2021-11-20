import random

def mod (a, b):
    q = a//b
    r = a - b*q
    r = r + (r < 0) * b
    return r

def euclides (a, b):
    if (mod(a,b) == 0):
	    return b
    else:
	    return euclides(b, mod(a,b));

def ext (a,b):
    if (mod(a,b) == 0):
        return (b,0,1)
    else:
        (d, xP, yP) = ext(b, mod(a,b))
        (x,y) = (yP, xP-a//b*yP)
        return (d,x,y)

def invMul (a, n):
    (d,xP,iP) = ext(a,n)
    if d == 1:
        return mod(xP, n)
    else:
        return a," no tine inv, mul. mod ",n

def isprime (a):
    if a < 1:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True      

def getPrime ():
    nro = random.randint(2,100)
    while(isprime(nro) == False):
        nro = nro + random.randint(2,100)
    return nro

def expM(a,b, n): #a = base, b = exponente, n = módulo
    if b == 1: 
        return mod(a,n)
    Nb = b//2
    res = expM(a,Nb,n)
    if b % 2: 
        return mod(res*res*a, n)
    return mod(res**2, n)

def Generator ():
    #p = getPrime() #obtener p
    #q = getPrime() #obtener q

    print("Ingrese el valor de p: ")
    p = int(input())
    while (isprime(p) == False):
        print("Ingrese un valor PRIMO para p: ")
        p = int(input())
    
    print("Ingrese el valor de p: ")
    q = int(input())
    while(isprime(q) == False):
        print("Ingrese un valor PRIMO para q: ")
        q = int(input())

    while (p == q): #verificar si p != q, caso contrario, cambiar valor de p
        print("Ingrese un valor PRIMO para p, diferente de q: ")
        p = int(input())
        #p = getPrime()

    print("p: ",p)
    print("q: ",q)
    
    n = p * q #calcular n
    print("n: ",n)
    phin = (p-1)*(q-1) #calcular phi de n
    print("Phi: ",phin)

    e = getPrime() #obtener e
    while (e <= 2 or e >= n-1 or euclides(e,phin) != 1): #verificar que: 2<e<n-1
        e = getPrime()
    print("e: ",e)

    d = invMul(e,phin) #calcular d
    print("d: ",d)

    return (n,e,d)

def cipher (msj):
    (n,e,d) = Generator()
    
    alf = "abcdefghijklmnopqrstuvwxyz1234567890"
    m = alf.index(msj)
    print("Mensaje a cifrar: ",msj," m: ",m)

    c = expM(m,e,n)
    print("C: ",c)

    return (n,e,d,c)

def decipher (n,e,d,c):
    
    alf = "abcdefghijklmnopqrstuvwxyz1234567890"
    
    m = expM(c,d,n)
    if (m>len(alf)):
        m = mod(m,len(alf))
    msj = alf[m]
    print("Mensaje descifrado: ",msj," m: ",m)
    
    return (m,msj)

(N,E,D,C) = cipher("r")
decipher(N,E,D,C)