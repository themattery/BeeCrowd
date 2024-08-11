#include <stdio.h>
#include <iostream>
#include <iomanip>

using namespace std;
 
int main() {
 
    int numFunc, horasTrab;
    double valorHora, salario;
    cin >> numFunc >> horasTrab >> valorHora;
    salario = valorHora * horasTrab;
    cout << "NUMBER = " << numFunc << endl << "SALARY = U$ " << fixed << setprecision(2) << salario << endl;
 
    return 0;
}
