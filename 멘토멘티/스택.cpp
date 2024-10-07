#include <iostream>
#include <string>

using namespace std;

const int MX = 1000005;
int dat[MX];
int pos = 0;

void push(int x) {
    dat[pos++] = x;
}


void pop() {
    if (pos == 0)
        cout << -1 << endl;
    else {cout << dat[pos-1]<<endl;
    pos--;}
}
void top() {
    if (pos == 0)
        cout << -1 << endl;
    else cout<< dat[pos-1]<<endl;
}
void empty() {
    if(pos == 0)
        cout << 1<<endl;
    else cout << 0 << endl;
}
void size() {
    cout << pos<<endl;
}
int main() { 
    int n;
    string input;
    int x=0;
    cin >> n;
    cin.ignore();
    for (int i=0;i<n;i++){
        getline(cin,input);

        if(input == "top")
            top();
        else if (input == "empty")
            empty();
        else if (input == "size")
            size();
        else if (input == "pop")
            pop();
        else{
            x = stoi(input.substr(5));
            push(x);
        }

    }
}
