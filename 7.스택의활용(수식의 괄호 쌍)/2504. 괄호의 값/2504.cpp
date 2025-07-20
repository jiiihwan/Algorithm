/*
1. 올바른 괄호쌍인지 검사
    1.1. 여는 괄호가 들어오면 st에 추가
        a. top이 여는 괄호거나 비어있으면 +연산이라는건가?
    1.2. 닫는 괄호가 들어오면?
        a. top 이 여는 괄호면 올바른 괄호 -> pop
        b. top 이 닫는 괄호면 잘못된 괄호
        c. top 이 비어있으면 잘못된 괄호
    1.3. 스택이 비어있지않으면 잘못된 괄호
2. 
3. 잘못된 괄호는 ans=0
*/

#include <iostream>
#include <stack>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    int ans;    
    stack<int> st;
    bool isValid = true;
    cin >> s;

    for(char c : s){
        if(c == '(' || c == '['){ //여는 괄호가 들어왔을때
            st.push(c);

        }
        else if(c == ')'){ //닫는 괄호가 들어왔을때
            if(st.empty() || st.top() != '('){ //잘못된 경우
                isValid = false;
                break;
            }
            else if(!st.empty() && st.top() != ')'){ //숫자일때
                while(st.top() != '('){
                    st.pop();
                }
            }
            else if(!st.empty())
            st.pop();
                
        }
        else{ // 문자일때

        }
    }


    if(isValid==false)
        ans = 0; 
    cout << ans;
}