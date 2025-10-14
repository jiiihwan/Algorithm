#include <bits/stdc++.h>
using namespace std;

int n;
long long a[100005];

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for(int i = 0 ; i < n ; i++)
        cin >> a[i];
    sort(a, a+n); //일단 오름차순으로 정렬시킨다

    int cnt = 0;
    long long mxval = - (1ll -62) - 1; // -2의 62승 보다 -1 낮은걸로 설정, 그리고 long long으로 설정한다
    int mxcnt = 0;
    
    for(int i = 0 ; i < n ; i++){
        if(i == 0 || a[i-1] == a[i]){ //시작일때랑 업데이트할때 똑같은숫자가 안나오면
            cnt++;
        }
        else{
            if(cnt > mxcnt){ //업데이트 하다가 카운트가 mxcnt 넘어가면 업데이트
                mxcnt = cnt; 
                mxval = a[i-1];
            }
            cnt = 1; //카운트 초기화
        }
    }
    if(cnt > mxcnt) //마지막 수 예외상황 처리
        mxval = a[n-1];
    
    cout << mxval;
}