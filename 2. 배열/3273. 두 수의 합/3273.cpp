#include <bits/stdc++.h>
using namespace std;

int a[100001];
bool occur[2000001];

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,x,count=0;
    cin >> n;
    for(int i = 0 ; i < n ; i++){
        cin >> a[i];
    }
    cin >> x;

    for(int i = 0 ; i < n ; i++){
        if(x-a[i] > 0 && occur[x-a[i]]) //x-a[i] 가 양수여야지 인덱스 조건에 맞기 때문. x보다 a[i]가 
            count++;
        occur[a[i]] = true;
    }
    
    cout << count;
}