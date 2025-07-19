#include <iostream>
#include <stack>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, count = 0;
    cin >> N;
    while(N--){
        stack<int> st;
        bool isValid = true;
        string s;
        cin >> s;
        for(char c : s){
            if(!st.empty() && st.top() == c){
                st.pop();
                continue;
            }
            
            st.push(c);
        } 

        if(!st.empty())
            isValid = false;
        
        if(isValid)
            count++;
    }

    cout << count;
}