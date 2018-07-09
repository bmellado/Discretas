##P4##
j = input("Ingresar n: ")
n= int(j)
matriz = []
for i in range(2**n):
    matriz.append([])
    for j in range(2**n):
        matriz[i].append(0)

for i in range(2**n):
    for j in range(2**n):
        if(i%2!=0):
            if(j%2!=0):
                matriz[i][j]=1
        if(i%2==0):
            if(j%2==0):
                matriz[i][j]=1


for i in range(2**n):
    for j in range(2**n):
        if not(j==2**n-1):
            print(matriz[i][j],end = " ")
        else:
            print(matriz[i][j])

