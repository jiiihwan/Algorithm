#include <iostream>
using namespace std;

int n,m;
int arr[10];
bool isused[10];

void func(int k){ // k = 몇번째 숫자를 고르고 있는가?
    if(k==m){ //m개의 숫자를 골랐으니 출력
        for(int i = 0 ; i < m ; i++)
            cout << arr[i] << ' ';
        cout << '\n';
        return;
    }

    for(int i = 1; i <= n; i++){
        if(!isused[i]){
            arr[k] = i;
            isused[i] = 1;
            func(k+1);
            isused[i] = 0;
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    func(0);
}