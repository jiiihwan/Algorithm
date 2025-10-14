#include <bits/stdc++.h>
using namespace std;

int d[1000001];
int n;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    for(int i = 2 ; i <= n ; i++){
        d[i] = d[i-1] + 1; //일단 할수있는 뺄셈으로 초기화
        if(i % 2 == 0)
            d[i] = min(d[i], d[i/2] + 1); //2로 나눠질때가 더 작으면 그렇게 한다
        if(i % 3 == 0)
            d[i] = min(d[i], d[i/3] + 1); //3으로 나눠질때가 더 작으면
    }


    cout << d[n];
}