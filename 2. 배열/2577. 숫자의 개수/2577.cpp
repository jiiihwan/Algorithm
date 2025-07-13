#include <bits/stdc++.h>
using namespace std;

int A,B,C,res,ans[10];

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> A >> B >> C;
    res = A*B*C;

    int num[15];
    fill(num, num+10, -1);
    string a = to_string(res);

    for (char c : a) {
        ans[c - '0']++; // 각 숫자에 해당하는 인덱스 증가
    }

    /*
    for(int i = 0; i < 10 ; i++){
        cout << ans[i] << "\n";
    }
    */

    for (int i : ans) {
        cout << i << '\n';
    }   


}