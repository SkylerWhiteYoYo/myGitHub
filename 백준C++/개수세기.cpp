#include <iostream>
using namespace std;

int main() {
    int n = 0;
    cin >> n;
    int *arr = new int[n];
    if (!arr) {
        cout << "메모리 배정 실패!"<<endl;
        return 0;
    }
    for (int i = 0; i<n ; i++){
        cin >> arr[i];
    }
    int v =0;
    cin >> v ;
    int count = 0;
    for (int i=0;i<n;i++){
        if (v == arr[i]){
            count += 1; 
        }
    }
    cout << count<<endl;

    delete [] arr;
}
