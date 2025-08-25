#include <iostream>

using namespace std;

int gear[4][8];
int area[3][2];
int K,num,dir,score = 0;
int a=2, b=6, c=6, d=6;

bool is_area_different(int n){
    if(n==3)
        n--;
    if(area[n][0] != area[n][1])
        return true;
}



void clockwise_spin(int n){    
    switch(n){
        case 0:
            if(a == 0)
                a = 7;
            area[0][0] = gear[0][--a];
        case 1:
            if(b == 0)
                b = 7;
            area[0][1] = gear[0][--b];
            area[1][0] = (area[0][1] + 4)  % 8;
        case 2:
            if(c == 0)
                c = 7;
            area[0][2] = gear[0][--c];
            area[2][0] = (area[0][2] + 4)  % 8;
        case 3:
            if(d == 0)
                d = 7;
            area[2][1] = gear[3][--d];
    }
}

void counter_clockwise_spin(int n){
    switch(n){
        case 0:
            if(a == 7)
                a = 0;
            area[0][0] = gear[0][++a];
        case 1:
            if(b == 7)
                b = 0;
            area[0][1] = gear[0][++b];
            area[1][0] = (area[0][1] + 4)  % 8;
        case 2:
            if(c == 7)
                c = 0;
            area[0][2] = gear[0][++c];
            area[2][0] = (area[0][2] + 4)  % 8;
        case 3:
            if(d == 7)
                d = 0;
            area[2][1] = gear[3][++d];
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    for(int i = 0 ; i < 4 ; i++){
        for(int j = 0 ; j < 8; j++){
            char c;
            cin >> c;
            gear[i][j] = c -'0';
        }
    }
    
    cin >> K;
    while(K--){
        cin >> num >> dir;
        num--;

        //n번 바퀴의 양끝에 있는 area확인
        //다르다면 n번 바퀴 돌리기
        //확인안한 area돌리기
        //area확인
        //다르면 반대로 돌린다

        
    }

    cout << score;
}

/*
톱니를 돌릴때 돌리는 거 옆 톱니 동작) 붙어있는게 다른경우
-옆에 있는게 같이돌아감
-같은 경우는 안돌아감

봐야할 부분은 3곳
*/