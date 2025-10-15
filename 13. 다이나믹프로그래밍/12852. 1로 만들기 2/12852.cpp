#include <bits/stdc++.h>
using namespace std;

int d[1000001];
int pre[1000001];

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for(int i = 2 ; i <= n ; i++){
        d[i] = d[i-1] + 1; //일단 할수있는 뺄셈으로 초기화
        pre[i] = i - 1;
        if(i % 2 == 0 && d[i] > d[i/2] + 1){
            d[i] = d[i/2] + 1; //2로 나눠질때가 더 작으면 그렇게 한다
            pre[i] = i/2;
        }
        if(i % 3 == 0 && d[i] < d[i/3] + 1){
            d[i] = d[i/3] + 1; //3으로 나눠질때가 더 작으면
            pre[i] = i/3;
        }
    }

    cout << d[n] << '\n';
    int cur = n;
    while(true){
        cout << cur << ' ';
        if(cur = 1)
            break;
        cur = pre[cur];
    }
}