#include <bits/stdc++.h>
using namespace std;

int triangle[501][501];
int D[501][501];

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    //1-based index
    for(int i = 1 ; i <= n ; i++)
        for(int j = 1 ; j <= i ; j++)
            cin >> triangle[i][j];
        
    D[1][1] = triangle[1][1];

    for(int i = 1 ; i <= n ; i++)
        for(int j = 1 ; j <= i ; j++)
            D[i][j] = max(D[i-1][j-1], D[i-1][j]) + triangle[i][j];
    
    cout << *max_element(D[n]+1, D[n]+n+1); //
}
