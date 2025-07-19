#include <iostream>
#include <stack>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int count = 0;
    int sum = 0;
    stack<int> st;
    string s;
    cin >> s;
    for(char c : s){
        if(c == '('){
            st.push(c);
            count++;
        }
        else{ //닫는 괄호가 들어오면
            if(!st.empty() && st.top() == '('){ //이전 게 여는 괄호일때
                //st.pop();
                count--;
                sum += count;
                st.push(c);
            }
            else{ //이전게 닫는 괄호일때
                st.push(c);
                count--;
                sum++;
            }
        }
    }

    cout << sum;
}