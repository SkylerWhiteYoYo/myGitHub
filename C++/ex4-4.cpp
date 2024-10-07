#include <iostream>
using namespace std;

class Circle{
    int radius;
public:
    Circle() {radius =1;}
    Circle(int r) {radius = r;}
    void setRadius(int r) {radius = r;}
    double getArea();
};

double Circle::getArea() {
    return radius*radius*3.14;
}
int main()  {
    Circle circles[2][3];
    int j = 1;
    for(int i=0;i<2;i++) {
        for(int k=0;k<3;k++){
            circles[i][k].setRadius(j);
            j++;
        }
    }
    for(int i=0;i<2;i++) {
        for(int k=0;k<3;k++){
            cout << "원"<<i<<"-"<<k<<"의 면적은 " << circles[i][k].getArea()<<"입니다." << endl;
        }
    }

}