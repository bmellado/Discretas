#include <bits/stdc++.h>
using namespace std;
string abecedario = "abcdefghijklmnñopqrstuvwxyz";

int factorial(int n){
    if(n==0){
        return 1;
    }
    return n* factorial(n-1);
}

int posArreglo(char caracter){
    for(int i=0;i<abecedario.length();i++){
        if(abecedario[i]==caracter){
            return i;
        }
    }
}
int esEntero(float x){
    int y = x;
    if(x-y >0){
        return 0;
    }
    else
        return 1;
}

int main(){
    string palabra;

    float A[abecedario.length()]; //Arreglo que guarda cuantos pares hay de cada letra
    for(int i =0; i<abecedario.length();i++){
        A[i]=0;
    }
    cout << "Ingrese palabra: ";
    cin >> palabra;
    int largo = palabra.length();
    if(largo % 2 == 0){//La palabra tiene cantidad par de elementos
        for(int i =0;i<largo;i++){
            A[posArreglo(palabra[i])]+=0.5;
        }
        for(int i = 0; i<abecedario.length(); i++){
            if(!esEntero(A[i])){//Si no tiene cantidad par de letras
                cout<<"Permutaciones palindromo: " <<0<< endl;
                return 0;
            }
        }
        int n=largo/2;
        int permutaciones = factorial(n);
        for(int i = 0; i<abecedario.length(); i++){
            permutaciones /= factorial((int)A[i]);
        }
        cout<<"Permutaciones palindromo: " <<permutaciones<< endl;
    }
    else{//La palabra tiene cantidad impar de elementos
        for(int i =0;i<largo;i++){
            A[posArreglo(palabra[i])]+=0.5;
        }
        int cola = 0;
        for(int i = 0; i<abecedario.length(); i++){
            if(!esEntero(A[i])){//Si no tiene cantidad par de letras
                cola +=1;
                if(cola > 1){
                    cout<<"Permutaciones palindromo: " <<0<< endl;
                    return 0;
                }
            }

        }
        int n = (largo-1)/2;
        int permutaciones = factorial(n);
        for(int i = 0; i<abecedario.length(); i++){
            permutaciones /= factorial((int)A[i]);
        }
        cout<<"Permutaciones palindromo: " <<permutaciones<< endl;
    }



return 0;}
