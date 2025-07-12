#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long A,B,C;
    cin >> A >> B;
    if(B > A)
        C = B - A - 1;
    else if (A > B){
        swap(A,B); 
        C = B - A - 1;
    }
    else
        C = 0;
    cout << C << "\n";
    for(long long i = 0 ; i < C ; i++ ){
        cout << ++A << " ";
    }
}