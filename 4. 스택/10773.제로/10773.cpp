#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int K,n,ans=0;
    cin >> K;

    stack<int> s;
    for(int i = 0 ; i < K ; i++){
        cin >> n;
        if(n != 0)
            s.push(n);
        else
            s.pop();
    }
    int size = s.size();
    
    //순회하면서 top 을 ans에 계속더해주고 pop으로 뺀다
    for(int i = 0 ; i < size ; i++){
        if(!s.empty()){
            ans+=s.top();
            s.pop();
        }
    }

    cout << ans;

}