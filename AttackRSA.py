import math

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

def expM(a,b, n): #a = base, b = exponente, n = módulo
    if b == 1: 
        return mod(a,n)
    Nb = b//2
    res = expM(a,Nb,n)
    if b % 2: 
        return mod(res*res*a, n)
    return mod(res**2, n)

def Mypow (a,b):
    cont = 0
    res = 1
    while (cont < b):
        res = res * a
        cont = cont +1
    return res

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

def factorizator (n):
    for i in range (2, int(math.sqrt(n))):
        while (mod(n,i) == 0):
            nro1 = i
            break
    nro2 = n//nro1
    return (nro1,nro2)
    
def attack1 (c,e,n):
    (p,q) = factorizator(n)
    phi = (p-1)*(q-1)
    d = invMul(e,phi)

    m = expM(c,d,n)
    return m

def attack2(c1,c2,e1,e2,n):
    
    if (euclides(e1,e2) == 1):
        (d,x,y) = ext(e1,e2)
    
        if (euclides(c2,n) == 1):
            cI = invMul(c2,n)
            x = invMul(x,e2);

            if (y<0):
                m = mod(Mypow(c1,x) * Mypow(cI,-y),n)#teniendo Y negativo
                return m
            else:
                m = mod(Mypow(c1,-x) * Mypow(cI,y),n)
                return m
        else:
            return 0
    else:
        return 0

print(factorizator(999630013489))
print("C: ",expM(100000000001,65537,999630013489))
print("M: ",attack1(747120213790,65537,999630013489))
print(attack2(35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544,35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184,7,11,35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667))