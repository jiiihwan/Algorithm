#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,count=0;
    cin >> n;
    int arr[n],num[n];
    vector<string> ans;
    stack<int> s;
    for(int i = 0 ; i < n ; i++){
        cin >> arr[i];
        num[i] = i+1;
    }

    int i = 0, j = 0;
    while(count < n){
        if(!s.empty() && (s.top() == arr[i])){
            s.pop();
            //cout << "-" << "\n";
            ans.push_back("-");
            count++;
            i++;

        }
        else if((j == n) && s.top() != arr[i]){
            //cout << "NO";
            ans.clear();
            ans.push_back("NO");
            break;
        }
        else{
            s.push(num[j]);
            //cout << "+" << "\n";
            ans.push_back("+");
            j++;
        }
    }

    for(string a : ans){
        cout << a << "\n";
    }



}