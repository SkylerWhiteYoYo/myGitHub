#include <iostream>
using namespace std;



int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int pos =0;
    int pointer =1;
    bool flag = false;
    int n = 0;
    cin >> n;
    int arr[200001];
    int num;
    int cur =1;
    int wanted_arr[200001];
    bool ans[400002];
    int tick=0;
    for(int i = 0; i<n;i++){
        cin >>num;
        while(pointer<=num){
            arr[pos++] = pointer++;
            ans[tick++]=true;
        }
        if (pointer >num){
            wanted_arr[i] = arr[pos-1];
            pos--;
            ans[tick++]=false;
        }
        if (wanted_arr[i] != num){
            flag = true;
            cout << "NO";
            break;
        }
        
    }
    if (not flag){
        for(int i=0 ;i<2*n;i++){
            if (ans[i])
                cout << "+" <<"\n";
           else cout << "-"<<"\n";
    }
    }
}

