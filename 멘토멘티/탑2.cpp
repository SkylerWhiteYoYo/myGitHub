#include <iostream>
#include <utility>
#include <vector>
#include <stack>

using namespace std;

int main() {
    int n = 0;
    cin>>n;
    vector<pair<int,int>> tops;
    for(int i=0;i<n;i++){
        int h;
        cin>>h;
        tops.push_back(make_pair(h,i));
    }
    stack<pair<int,int>> s;
    s.push(make_pair(tops[0].first,tops[0].second));
    vector<int> ans;
    for(int i=0;i<n;i++){
        if(s.top().first<tops[i].first){
            ans.push_back(0);
            s.push(make_pair(tops[i].first,tops[i].second));
        }
        else {
            ans.push_back(s.top().second);
        }
    }
    for (int i=0;i<n;i++)
        cout<< ans[i]<< " ";

}