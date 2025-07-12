#include <bits/stdc++.h>
using namespace std;


int Y,M,atime[10000];
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> atime[i];
    }

    for(int i = 0 ; i < N ; i++){
        Y += ((atime[i] / 30) + 1) * 10;
        M += ((atime[i] / 60) + 1) * 15;
    }
    
    if (Y>M){
        cout << "M " << M; 
    }
    else if(Y<M){
        cout << "Y " << Y;
    }
    else
        cout << "Y M " << Y;
}