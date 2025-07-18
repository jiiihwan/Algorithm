#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

void parse(string& tmp, deque<int>& d){
  int cur = 0;
  for(int i = 1; i+1 < tmp.size(); i++)
  {
    if(tmp[i] == ','){
      d.push_back(cur);
      cur = 0;
    }
    else{
      cur = 10 * cur + (tmp[i] - '0');
    }
  }
  if(cur != 0)
    d.push_back(cur);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    while(T--){
        string p,arr; 
        int n;
        deque<int> dq;

        cin >> p; //RDD
        cin >> n; //4
        cin >> arr;
        parse(arr, dq);

        for(char a : p){ //RDD
            if(a == 'R'){ //Reverse
                if(!dq.empty())
                    reverse(dq.begin(), dq.end());
            }
            else{ //Delete first
                if(!dq.empty()){
                    dq.pop_front();
                }
                else{
                    cout << "error\n";
                    break;
                }
            }
        }

        int size = dq.size();
        if(!dq.empty())
            cout << "[";
        for(int i=0 ; i < size ; i++){
            cout << dq.front();
            if(dq.size()!=1){
                cout << ",";
                dq.pop_front();
            }
        }
        if(!dq.empty())
            cout << "]\n";
            

    }
}