#include <iostream>

using namespace std;

int main() {

  int valor;
  int n100, n50, n20, n10, n5, n2, n1;
  cin >> valor;
  n100 = valor/100;
  valor = valor%100;
  n50 = valor/50;
  valor = valor%50;
  n20 = valor/20;
  valor = valor%20;
  n10 = valor/10;
  valor = valor%10;
  n5 = valor/5;
  valor = valor%5;
  n2 = valor/2;
  valor = valor%2;
  n1 = valor/1;
  valor = valor%1;
  int valorTotal = n100*100 + n50*50 + n20*20 + n10*10 + n5*5 + n2*2 + n1;
  cout << valorTotal << endl;
  cout << n100 << " nota(s) de R$ 100,00" << endl;
  cout << n50 << " nota(s) de R$ 50,00" << endl;
  cout << n20 << " nota(s) de R$ 20,00" << endl;
  cout << n10 << " nota(s) de R$ 10,00" << endl;
  cout << n5 << " nota(s) de R$ 5,00" << endl;
  cout << n2 << " nota(s) de R$ 2,00" << endl;
  cout << n1 << " nota(s) de R$ 1,00" << endl;
  
  return 0;
}