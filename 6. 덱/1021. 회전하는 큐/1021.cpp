#include <iostream>
#include <deque>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N,M,count = 0;
    cin >> N;
    
    deque<int> dq,ans,temp;
    for(int i = 1 ; i <= N ; i++){
        dq.push_back(i);
    }

    cin >> M;
    for(int i = 0 ; i < M ; i++){
        int x;
        cin >> x;
        ans.push_back(x);
    }

    for(int i : ans){
        int j = 0;
        while(i != dq.at(j)){
            j++;
        }
        while(i != dq.front()){ //i가 front에 올때까지
            if(j<=dq.size()/2){ //size의 절반이하면 2번 수행
                dq.push_back(dq.front());
                dq.pop_front();
                count++;
            }
            else{ //이상이면 1번수행해서 front에 오게 함
                dq.push_front(dq.back());
                dq.pop_back();
                count++;
            }
        }
        //temp.push_back(dq.front()); 
        dq.pop_front(); //front에 있으면 pop
    }
    
    /*
    for(int a : temp){
        cout << a << " ";
    }
    cout << "\n";
    */

    cout << count;
}