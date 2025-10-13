#include <bits/stdc++.h>
using namespace std;

int n;
string st;
vector<string> v;

bool cmp(string& a, string& b){
    int lena = a.size();
    int lenb = b.size();
    int suma = 0, sumb = 0;

    if(lena != lenb)
        return lena < lenb; //a가 b보다 먼저올때가 true, 그러니 짧은 것이 먼저올때가 true이므로 lena가 더 작을때를 반환한다.

    for(int i = 0 ; i < lena ; i++){
        if(isdigit(a[i]))
            suma += a[i] - '0'; //문자형태 숫자로 바꾸기
    }
    for(int i = 0 ; i < lenb ; i++){
        if(isdigit(b[i]))
            sumb += b[i] - '0'; //문자형태 숫자로 바꾸기
    }
    if(suma == sumb)
        return a < b; //사전순. 사전순은 문자가 작은대로
    else
        return suma < sumb; //작은합을 가지는게 먼저
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for(int i = 0 ; i < n ; i++){
        cin >> st;
        v.push_back(st);
    }

    sort(v.begin(), v.end(), cmp);
    for(auto i : v)
        cout << i << '\n';
}