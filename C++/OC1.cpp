#include <iostream>
#include <string>

using namespace std;

int main() {
    cout << "가위 바위 보 게임을 합니다. 가위, 바위, 보 중에서 입력하세요." << endl;
    cout << "로미오>>";
    string romio;
    getline(cin,romio);
    cout << "줄리엣>>";
    string juliet;
    getline(cin,juliet);

    if (romio == juliet) {
        cout << "비겼습니다." <<endl;
    }
    else if (romio == "가위"){
        if (juliet == "바위") {
            cout << "줄리엣이 이겼습니다.";
        }
        else if (juliet == "보") {
            cout << "로미오가 이겼습니다.";
        }
    }
        else if (romio == "바위"){
        if (juliet == "보") {
            cout << "줄리엣이 이겼습니다.";
        }
        else if (juliet == "가위") {
            cout << "로미오가 이겼습니다.";
        }
    else if (romio == "보"){
        if (juliet == "가위") {
            cout << "줄리엣이 이겼습니다.";
        }
        else if (juliet == "바위") {
            cout << "로미오가 이겼습니다.";
        }
    }
    }
    

}