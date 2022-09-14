def creare_lista():
    n=int(input('Introdu numarul de elemente: '))
    lista=[]
    for i in range(n):
        el=eval(input('elementul '+str(i)+' este '))
        if str:
            print("Doar elemente integer")
            break
        lista.append(el)
    return lista
print(creare_lista())
