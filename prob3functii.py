a,b=int(input('Introdu prima fractie: ')),int(input())
c,d=int(input('Introdu a doua fractie: ')),int(input())
def adunare(x,y,n,m):
    i=(x*m)+(n*y)
    j=y*m
    return (i,j)
def inmultire(x,y,n,m):
    i=x*n
    j=y*m
    return i,j
print(a,'/',b,'+',c,'/',d,'=',adunare(a,b,c,d))
print(a,'/',b,'*',c,'/',d,'=',inmultire(a,b,c,d))
