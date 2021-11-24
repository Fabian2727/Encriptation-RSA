# RSA

En el archivo RSA_nros.py se encuentra el programa de cifrado RSA para enteros. Dicho programa está conformado por las siguientes funciones
- Primero realizamos el import random, ya que nos será útil más adelante
Las funciones son:
- mod: Calcula a mod b
- euclides: Calcula el gcd(a,b)
- ext: El cual retorna los valores de a, x, b, y, d (gcd de a y b) en la expresión lineal ax + by = d
- inMul: El cual retorna la inversa multiplicativa del entero a en módulo n
- isPrime: Verifica si un número es primo o no
- getPrime: Mediante la función random generará un entero, el cual será verificado si es primo o no con la función isPrime, en caso no fuese primo, se genera un número nuevamente y se suma al número anterior, así hasta que la suma sea un número primo
- expM: Calcula la exponenciación modular de a elevado a b en mod n
- Generator: Pide ingresar por teclado los valores de p y q, se verifica si estos son primos con la función isPrime, y en caso sean iguales, se pide que se ingrese el valor de p nuevamente.
- cipher: Con los valores de p y q obtenidos de la función Generator, se calcular n=p*q, phin = (p-1)*(q-1), e (un número random entre 2 a n-1), d (inversa de e en mod phin). Y se cifra el mensaje con la operación de exponenciación modular c = m^e mod n. Y se retornan lo valores de n,e,d,c
- decipher: Con los valores obtenidos de la función cipher se descifra el mensaje c, mediante la operación m = c^d mod n 
========================================================================

En el archivo AttackRSA.py se encuentran los métodos de ataque al cifrado RSA. Dichas funciones de ataque son:
- attack1: La cual calcula m mediante la operación m = c^1/e
- attack2: Verifica si el gcd de e1 y e2 es 1 (si son coprimos). En caso sea así, procede a verificar que c2 y n sean coprimos para calcular la inversa de c2. Tras esto se calcula m mediante la operación m = (c1^x * c2'^-y) mod n
- Las potenciaciones requeridas en attack2 son muy grandes, por lo que se genera un overflow, para evitar dicho problema se creó la función Mypow. Dicha función realiza lo mismo que la función pow convencional, con la excepción de no convertir los valores a tipo float, esto permite evitar dicho overflow.
