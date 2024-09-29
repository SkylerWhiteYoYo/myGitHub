#include <iostream>
using namespace std;
#include "Calculator.h"
#include "Adder.h"

void Calculator :: run() {
    cout << "두수를 입력하세요>>";
    int a=0,b=0;
    cin >> a >> b;
    Adder adder(a,b);
    cout << adder.process();

}