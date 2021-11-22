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
