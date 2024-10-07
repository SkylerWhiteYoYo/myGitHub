#include <iostream>

using namespace std;

int k =0;
int pos =0;
int jh =0;
int arr[100001];
int sum =0;

int main() { 
    cin >> k;

    for(int i =0; i<k;i++){
        cin >> jh;
        if (jh==0)
            pos--;
        else arr[pos++] = jh;
    }
    for(int i =0;i<pos;i++){
        sum += arr[i];
    }
    cout << sum;


}