#include <iostream>
using namespace std;

int N;

void bar(string str, int cnt){
    for(int i = 0 ; i < cnt ; i++)
        cout << "____";
    cout << str;
}

void solve(int cnt){
    bar("\"����Լ��� ������?\n", cnt);
    if(cnt == N)
        bar("\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"\n", cnt);
    else{
        bar("\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���.\n", cnt);
        bar("���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���.\n", cnt);
        bar("���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"\n", cnt);
        solve(cnt+1);
    }
    bar("��� �亯�Ͽ���.\n", cnt);

}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    cout << "��� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������.\n";
    solve(0);
}