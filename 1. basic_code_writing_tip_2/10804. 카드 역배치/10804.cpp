#include <bits/stdc++.h>
using namespace std;

int a, b;
int card[21];

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    for(int i = 1 ; i < 21 ; i++){
        card[i] = i;
    }
    for(int i = 1; i<11 ; i++){
        cin >> a >> b;
        reverse(card+a,card+b+1); //0번부터니까 b+1 해야 b번까지다.
    }

    for(int i = 1 ; i < 21 ; i++){
        cout << card[i] << " ";
    }

}