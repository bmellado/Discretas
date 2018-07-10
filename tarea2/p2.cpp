#include <bits/stdc++.h>
using namespace std;
int main(){
    string combinacion1;
    string combinacion2 = "";
    cout << "Ingrese una combinacion de cara o sello de largo 3, Ejemplo css:" << endl;
    cin >> combinacion1;
    if(combinacion1.length()==3){
        combinacion2 += combinacion1[2];
        combinacion2 += combinacion1[0];
        combinacion2 += combinacion1[1];
        cout <<"La secuencia del segundo jugador es: "<< combinacion2;
    }
    else
        cout << "Ingrese combinacion correcta";





return 0;}
