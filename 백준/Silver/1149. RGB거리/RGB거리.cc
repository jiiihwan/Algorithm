#include <bits/stdc++.h>
using namespace std;

int D[1001][3]; //0=R, 1=G, 2=B

int R[1001];
int G[1001];
int B[1001];

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    for(int i = 1 ; i <= N ; i++){
        cin >> R[i] >> G[i] >> B[i];
    }

    D[1][0] = R[1];
    D[1][1] = G[1];
    D[1][2] = B[1];

    for(int i = 1 ; i <= N ; i++){
        D[i][0] = min(D[i-1][1], D[i-1][2]) + R[i];
        D[i][1] = min(D[i-1][2], D[i-1][0]) + G[i];
        D[i][2] = min(D[i-1][0], D[i-1][1]) + B[i];
    }

    cout << min({D[N][0], D[N][1], D[N][2]});
}