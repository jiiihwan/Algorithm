#include <iostream>
#include <stack>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    
    while(1){
        string s;
        stack<int> st;
        bool isValid = true;
        
        getline(cin, s);
        if(s==".")
            break;

        for(char a : s){
            if(a=='(' || a == '['){
                st.push(a);
            }
            else if(a == ')'){
                if(st.empty() || st.top() != '('){
                    isValid = false;
                    break;
                }
                else if(st.top() == '('){
                    st.pop();
                }
            }
            else if(a == ']'){
                if(st.empty() || st.top() != '['){
                    isValid = false;
                    break;
                }
                else if(st.top() == '['){
                    st.pop();
                }
            }            
        }

        if(!st.empty()){
            isValid = false; 
        }

        if(isValid == false)
            cout << "no\n";
        else 
            cout << "yes\n";
    }
}