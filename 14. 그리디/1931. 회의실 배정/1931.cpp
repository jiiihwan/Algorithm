#include <bits/stdc++.h>
using namespace std;

pair<int,int> s[100001]; // {end, start}, 정렬조건

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    for(int i = 0 ; i < n ; i++){
        cin >> s[i].second >> s[i].first;
    }
    sort(s, s+n);

    int ans=0;
    int t=0;

    for(auto i : s){
        if(i.second >= t){
            ans++;
            t = i.first;
        }
    }

    cout << ans;
}