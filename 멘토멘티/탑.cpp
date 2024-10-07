#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n =0;
    cin >> n;
    cout << "n의 값은 :"<<n;
    vector<int> tops(n);
    for(int i=0;i<n;i++){
        cin >> tops[i];
        cout << "tops"<<i << "의 값은" << tops[i];
    } 
    bool flag = true; 
    int A=0;
    int B=0;
    vector<int> ans(n);
    ans[0] = 0;
    while (flag){
        cout <<"while문 들어옴";
        if (A == B) {
            B++;
            cout<< "B를 더했습니다.";
        }
        while(tops[A] > tops[B]){
            B++;
        }
        int htop=tops[A+1];
        int loc_top = A;
        for(int i=A+1;i<B-A;i++){
            if (htop < tops[i]){
                htop = tops[i];
                loc_top = i;
            }
            if (htop == tops[i]){
                ans[i] = tops[A];
            }
            else if (tops[i] < htop){
                ans[i] = loc_top;
            }
            if( i == n-1){
                break;
                flag = false;
            }
        }
        A= B;
        if (A == n-1){
            break;
        }
    }

    
    for(int i=0;i<n;i++){
        cout<< ans[i] << " ";
    }
}