def formul(x):
    s=0
    for i in range(0,(x+1),2):
        s+=0.5**i
    return s
print(formul(8))
