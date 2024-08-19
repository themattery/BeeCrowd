#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int tempo, vel;
  cin >> tempo >> vel;
  double distancia = tempo * vel;
  double litros = distancia / 12.0;
  cout << fixed << setprecision(3) << litros << endl;
  return 0;
}