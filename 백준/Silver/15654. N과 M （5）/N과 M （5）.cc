#include <iostream>
#include <algorithm>
using namespace std;

int n,m;
int arr[10];
int arr2[10];
bool isused[10];

void func(int k){ //k는 더이상 몇번째 자리수가 아닌 수열의 인덱스이다
    if(k==m){
        for(int i = 0 ; i < k ; i++){
            cout << arr2[i] << ' ';
        }
        cout << '\n';
        return;
    }

    for(int i = 0 ; i < n ; i++){
        if(!isused[i]){
            arr2[k] = arr[i];
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
    for(int i = 0 ; i < n ; i++){
        cin >> arr[i];
    }
    sort(arr, arr+n);
    func(0);

}