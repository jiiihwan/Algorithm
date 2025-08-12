#include <iostream>
#include <algorithm>
using namespace std;

int n;
int arr[13];
int num[13];

void func(int k){
    if(k==6){
        for(int i = 0 ; i < k ; i++)
            cout << num[arr[i]] << ' ';
        cout << '\n';
        return;
    }
    int st = 0;
    if(k!=0)
        st = arr[k-1] + 1; // 시작할 인덱스는 이전 인덱스보다 1보다 큰 곳
    for(int i = st ; i < n ; i++){
        arr[k] = i;
        func(k+1);
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    while(1){
        cin >> n;
        if(n==0)
            return 0;
        for(int i = 0 ; i < n ; i++)
            cin >> num[i];
        sort(num,num+n);
        func(0);
        cout << '\n';
    }

}