#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;
#define X first
#define Y second

int n,m;
int board[51][51];
int ans = 0;
vector<pair<int,int>> chicken;
vector<pair<int,int>> house;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < n ; j++){
            cin >> board[i][j];
            if(board[i][j] == 1)
                house.push_back({i,j});
            if(board[i][j] == 2)
                chicken.push_back({i,j});
        }
    }
    
    vector<int> brute(chicken.size(), 1); //치킨 사이즈 만큼 1 채우기
    fill(brute.begin(), brute.begin() + chicken.size() - m , 0); // 뺄 치킨집개수 남기고 0으로 채우기

    int ans = 9999999;
    do{
        int dist = 0;
        for(auto h : house){
            int tmp = 9999999;
            for(int i = 0 ; i < chicken.size() ; i++){
                if(brute[i] == 0)
                    continue;
                tmp = min(tmp, abs(chicken[i].X - h.X) + abs(chicken[i].Y - h.Y));
            }
            dist += tmp;
        }
        ans = min(ans, dist);
    }while(next_permutation(brute.begin(), brute.end()));

    cout << ans;
}

/*
최대 M개 치킨집을 고르면서
치킨거리가 가장 작게 나오는 경우 찾기
*/