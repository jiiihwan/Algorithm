#include <bits/stdc++.h>
using namespace std;

string str;
string explode;
stack<char> st;
stack<int> save;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> str >> explode;
    int len = str.length();
    int exp_len = explode.length();

    int j = 0; //explode문자열 순환용
    for(int i = 0 ; i < len ; i++){
        st.push(str[i]);
        if(!st.empty() && st.top() == explode[j]){
            if(j == exp_len - 1){ //폭발 문자를 만족하면
                for(int i = 0 ; i < exp_len ; i++){
                    st.pop();
                }
                if(!save.empty()){
                    j = save.top();
                    save.pop(); 
                }
                else
                    j = 0;
                if(!st.empty() && st.top() == explode[j]) //pop한 뒤 남아있는 것에 대한 비교 
                    j++;
                continue;
            }
            j++; //맞았으면 j++
        }
        else{
            if(j > 0) //하나라도 맞았으면 일단 저장
                save.push(j);
            j = 0; //안 맞았으면 j초기화
            if(st.top() == explode[j]) //그리고 다시 확인
                j++;
        }
    }

    char ans[st.size()];
    if(!st.empty()){
        for(int i = st.size() - 1 ; i >= 0 ; i--){
            ans[i] = st.top();
            st.pop();
        }
        for(auto c : ans)
            cout << c;
    }
    else{
        cout << "FRULA";
    }
}