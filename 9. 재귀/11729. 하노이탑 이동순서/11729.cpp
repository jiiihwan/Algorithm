#include <iostream>
using namespace std;

void func(int a, int b, int n){
    //base condition
    if(n==1){
        cout << a << ' ' << b << '\n';
        return;
    }
    
    func(a, 6-a-b, n-1);
    cout << a << ' ' << b << '\n';
    func(6-a-b, b, n-1);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int K;
    cin >> K;
    cout << (1<<K) - 1 << '\n';
    func(1,3,K);
}