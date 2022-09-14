n=int(input("Introdu n: "))
m=int(input("Introdu m: "))
if n>m:
    def factorial(x):
        fact=1
        for i in range(1,x+1):
            fact*=i
        return int(fact)
    C=factorial(n)/(factorial(m)*factorial(n-m))
    print(C)
elif n==m:
    print('0')
else:
    print('nu exisa combinatii posibile')
