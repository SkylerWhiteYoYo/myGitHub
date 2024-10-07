#include <iostream>
using namespace std;

int main() {
    int a[10];
    for (int i =0;i<10;i++) {
        cin >> a[i];
    }
    int mod[42];
    for (int i=0;i<42;i++)
        mod[i] =0;
    for (int i=0;i<10;i++){
        mod[a[i]%42] = 1;
    }
    int count = 0;
    for (int i=0;i<42;i++) {
        if(mod[i] == 1)
            count++;
    }
    cout << count;

}