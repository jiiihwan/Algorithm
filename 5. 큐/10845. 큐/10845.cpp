#include <iostream>
#include <queue>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, x;
    string A;
    queue<int> Q;
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> A;
        
        if(A=="push"){
            cin >> x;
            Q.push(x);
            //cout << x << "\n";
        }
        else if(A=="pop"){
            if(Q.empty())
                cout << "-1"<< "\n";
            else{
                cout << Q.front() << "\n";
                Q.pop();
            }
        }
        else if(A=="size")
            cout << Q.size() << "\n";
        else if(A=="empty")
            if(Q.empty())
                cout << "1" << "\n";
            else
                cout << "0"<< "\n";
        else if(A=="front"){
            if(Q.empty())
                cout << "-1" << "\n";
            else{
                cout << Q.front() << "\n";
            }
        }
        else if(A=="back"){
            if(Q.empty())
                cout << "-1"<< "\n";
            else{
                cout << Q.back() << "\n";
            }
        }
        
    }
}