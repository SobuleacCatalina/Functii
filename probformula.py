n=int(input("Introdu n: "))
def formul(x):
    s=0
    for i in range(x+1):
        s=s+((1/2)**i)
    return s
print(formul(n))