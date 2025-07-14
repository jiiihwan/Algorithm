#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    for(int i = 0 ; i < N ; i++){
        string word;
        list<char> password;
        auto it = password.end();

        cin >> word;
        for(char j : word){
            if(j == '<'){
                if(it != password.begin())
                    it--;
            }
            else if(j == '>'){
                if(it != password.end())
                    it++;
            }   
            else if(j == '-'){
                if(!password.empty() && it != password.begin()){
                    it = password.erase(--it);
                }
            }
            else{
                password.insert(it,j);
            }
        }

        for(char k : password){
            cout << k;
        }
        cout << '\n';
    }


}