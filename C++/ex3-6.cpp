#include <iostream>
using namespace std;

class Rectangle {
public:
    bool isSquare() ;
    int width, height;
    Rectangle();
    Rectangle(int a);
    Rectangle(int a, int b);
};

Rectangle :: Rectangle() : Rectangle(1,1) {}
Rectangle :: Rectangle(int a) : Rectangle(a, a) {}
Rectangle :: Rectangle(int a, int b) {
    width = a;
    height = b;
}
 bool Rectangle :: isSquare() {
    if (width == height) return true;
    else return false;
 }

 int main() {
    Rectangle rect1;
    Rectangle rect2(3,5);
    Rectangle rect3(3);

    if (rect1.isSquare()) { cout << "rect1은 정사각형이다."<<endl;}
    if (rect2.isSquare()) { cout << "rect2는 정사각형이다."<<endl;}
    if (rect3.isSquare()) { cout << "rect3은 정사각형이다."<<endl;}
    
 }
