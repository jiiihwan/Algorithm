    #include <bits/stdc++.h>
    using namespace std;

    //0-based
    int main(void){
        ios::sync_with_stdio(0);
        cin.tie(0);

        int n;
        cin >> n;
        int A[n];
        int D[n];
        for(int i = 0 ; i < n ; i++){
            cin >> A[i];
        }
        D[0] = A[0]; //초기값
        for(int i = 1 ; i < n ; i++){
            D[i] = max(0, D[i-1]) + A[i]; //i번째까지의 합 들어있는 배열 채우는데, 0보다 크면 새로시작
        }

        cout << *max_element(D, D+n); //0-based이고 n번째는 포함안하니까 n+1이 아니라 n으로 쓰면된다.
    }

