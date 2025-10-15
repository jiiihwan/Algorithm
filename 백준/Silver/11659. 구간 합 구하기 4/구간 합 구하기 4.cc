#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N,M;
    cin >> N >> M;
    int A[N]; //수 담을 곳
    int D[N]; //1부터 i번째 수까지의 합을 담을곳
    D[0] = 0;
    D[1] = 1;
    for(int i = 1 ; i <= N ; i++){
        cin >> A[i];
        D[i] = D[i-1] + A[i];
    }

    while(M--){
        int i,j;
        cin >> i >> j;
        int result = D[j] - D[i-1];
        cout << result << '\n';
    }
}