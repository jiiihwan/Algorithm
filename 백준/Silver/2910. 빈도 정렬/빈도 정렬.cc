#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second



bool cmp(const pair<int,int>& a, const pair<int,int>& b){
    return a.Y > b.Y;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N,C;
    cin >> N >> C;
    vector<pair<int,int>> arr; //{num,cnt}
    for(int i = 0 ; i < N ; i++){
        int x;
        cin >> x;
        bool check = false;

        for(auto &a : arr){ //arr검사
            if(a.X == x){ //만약 숫자가 이전에 있었다면
                check = true;
                a.Y++; //카운트숫자를 늘린다
                break;
            }
        }

        if(!check) //숫자가 없던 경우에만
            arr.push_back({x,1}); //초기값은 1
    }

    stable_sort(arr.begin(), arr.end(), cmp);


    for(auto i : arr){
        while(i.Y--) //그냥 카운트 개수만큼 출력한다
            cout << i.X << ' '; 
    }

}

