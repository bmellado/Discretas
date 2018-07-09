### P1 ###
import sys


def esLetra(c):
    for i in range(len(abecedario)):
        if (c == abecedario[i]):
            return True
    return False

def esNumero(c):
    for i in range(len(numeros)):
        if (c == numeros[i]):
            return True
    return False

while(True):
    palabra = input()
    if(palabra==""):
        break
    largo = len(palabra)
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    numeros = "1234567890"
    suma = "+"
    producto = "*"
    pIzq = "("
    pDer = ")"
    esArit = True
    parentesis = [0,0] #parentesis[0] = cantidad de pIzq, parentesis[1] = cantidad de pDer
    pasos = []
    digitos = 0


    for i in range(largo):
        if(i==0):
            if (palabra[i] == suma):
                esArit = False
            if (palabra[i] == producto):
                esArit = False
        if(i != largo-1):
            if(esLetra(palabra[i])):
                if(palabra[i+1]==suma or palabra[i+1]==producto or palabra[i+1]==pDer):
                    pasos.append("b")
                    continue
                else:
                    esArit=False
                    break
            if(palabra[i]==suma):
                if(esLetra(palabra[i+1]) or esNumero(palabra[i+1]) or palabra[i+1]==pIzq):
                    pasos.append("d")
                    continue
                else:
                    esArit = False
                    break
            if(palabra[i]==producto):
                if (esLetra(palabra[i + 1]) or esNumero(palabra[i + 1]) or palabra[i + 1] == pIzq):
                    pasos.append("e")
                    continue
                else:
                    esArit = False
                    break
            if(esNumero(palabra[i])):
                if(palabra[i+1]==suma or palabra[i+1]==producto or palabra[i+1]==pDer):
                    pasos.append("a")
                    continue
                elif(esNumero(palabra[i+1])):
                    continue
                else:
                    esArit = False
                    break
            if(palabra[i]==pIzq):
                parentesis[0]+=1
                if(esLetra(palabra[i+1]) or esNumero(palabra[i+1]) or palabra[i + 1] == pIzq):
                    continue
                else:
                    esArit = False
                    break
            if(palabra[i]==pDer):
                parentesis[1]+=1
                if (parentesis[1] > parentesis[0]):
                    esArit = False
                    break
                if(palabra[i+1]==suma or palabra[i+1]==producto or palabra[i+1]==pDer):
                    pasos.append("c")
                    continue
                else:
                    esArit = False
                    break

        else: #i == largo-1
            if (esNumero(palabra[i])):
                pasos.append("a")
            if(esLetra(palabra[i])):
                pasos.append("b")
            if (palabra[i] == suma):
                esArit = False
            if (palabra[i] == producto):
                esArit = False
            if (palabra[i] == pIzq):
                parentesis[0] += 1
            if (palabra[i] == pDer):
                parentesis[1] += 1
            if(parentesis[0]!=parentesis[1]):
                esArit = False

    if(esArit):
        for i in range(len(pasos)):
            if not(i==len(pasos)-1):
                print(pasos[i],end=",")
            else:
                print(pasos[i])
    else:
        print("NO")








