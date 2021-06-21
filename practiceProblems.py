import sympy as sympy

#Problem 1
counter = 0
for i in range(1000):
    if i % 3 == 0:
        counter += i
    elif i % 5 == 0:
        counter += i
print (counter)

#Problem 2
term1 = 1
term2 = 2
term3 = 0
counter2 = 3
j = 0
while term1 < 55:
    term3 = term1 + term2
    #print ('term3 is now', term3)
    term1 = term2
    term2 = term3
    if term3 % 2 == 0:
        counter2 += term3
    term3 = 0
print (counter2)

#Problem 3
num = 3388
largest = 0
#600851475143
#print(sympy.isprime(30))
for l in range(1,3388):
    if (num % l == 0) and (sympy.isprime(l)):
        largest = l
print(largest)