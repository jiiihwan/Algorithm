#include <iostream>
#include <utility> //pair
#include <stack>
#include <vector>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    stack<pair<int,int>> st,temp;
    vector<int> ans;

    cin >> n;
    for(int i = 1 ; i <= n ; i++){
        int x;
        cin >> x;
        st.push({i,x});
    }

    while (!st.empty()){
        temp.push(st.top());
        st.pop();
        
        if(st.empty())
            break;

        if(!temp.empty() && temp.top().second < st.top().second){
            ans.push_back(st.top().first);
            temp.pop();
        }
        else{
            while(!temp.empty() && temp.top().second > st.top().second){
                ans.push_back(st.top().first);
                temp.pop();
            }
        }
    }
    while(!temp.empty()){
        ans.push_back(0);
        temp.pop();
    }
    
    for(int a : ans){
        cout << a;
    }

}
