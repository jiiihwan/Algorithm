#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> v;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    while(n--){ //일단 벡터에 다 넣는데 뒤집어서 넣음
        string s;
        cin >> s;

        reverse(s.begin(), s.end());
        long long a = stoll(s);

        v.push_back(a);
    }

    sort(v.begin(), v.end());
    for(auto a : v)
        cout << a << '\n';
}