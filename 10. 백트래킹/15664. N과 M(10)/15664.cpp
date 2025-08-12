#include <iostream>
#include <algorithm>
using namespace std;

int n,m;
int arr[10];
int num[10];

void func(int k, int st){
    if(k==m){
        for(int i = 0 ; i < m ; i++)
            cout << arr[i] << ' ';
        cout << '\n';
        return;
    }
    
    int tmp=0;
    for(int i = st ; i < n ; i++){
        if(tmp != num[i]){
            arr[k] = num[i]; //k번째의 인덱스를 고르는 거니까 arr에 i번째 인덱스를 담는다
            tmp = arr[k];
            func(k+1, i+1); //이전 단계에서 어디까지 골랐는지를 다음 재귀로 넘겨줘야하니까 이걸 인자에 포함시켜서 전달한다.
        }

    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for(int i = 0 ; i < n ; i++) 
        cin >> num[i];
    sort(num, num+n);
    func(0,0);
}