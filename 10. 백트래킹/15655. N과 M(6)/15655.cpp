#include <iostream>
#include <algorithm>
using namespace std;

int n,m;
int num[10]; //수열의 숫자가 들어있는 배열. sort로 오름차순으로 정리한다
int arr[10]; //출력할 숫자가 들어있는 배열. 여기는 인덱스 번호 순서를 저장한다.

void func(int k){
    if(k==m){
        for(int i = 0 ; i < m ; i++)
            cout << num[arr[i]] << ' '; //출력할 숫자를 arr수열에 저장된 인덱스 순서대로 출력한다.
        cout << '\n';
        return; //return 빠뜨리지말기
    }
    int st = 0;
    if(k!=0)
        st = arr[k-1] + 1; // 시작할 인덱스는 이전 인덱스보다 1보다 큰 곳
    for(int i = st ; i < n ; i++){
        arr[k] = i; //k번째 인덱스에 num에 해당하는 인덱스 저장
        func(k+1); 
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for(int i = 0 ; i < n ; i++)
        cin >> num[i];
    sort(num, num+n);
    func(0);
}