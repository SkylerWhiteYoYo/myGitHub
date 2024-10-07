#include <iostream>
using namespace std;
int main() {
    int *p = new int[5];
    if (!p) {
        cout<< "메모리 실패!";
        return 0;
    }
    for (int i = 0 ; i < 5 ; i++){
        cout << i+1 << "번째 정수를 입력하세요>>";
        cin >> p[i];
    }
    int max = p[0];
    for (int i = 1; i<5; i++){
        if (max < p[i]) {
            max = p[i];
        }
    }
    cout << "제일 큰 수는 '" << max << "' 입니다.";

    delete [] p;
}