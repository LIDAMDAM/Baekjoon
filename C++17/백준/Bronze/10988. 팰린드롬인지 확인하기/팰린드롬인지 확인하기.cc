#include <iostream>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string str;
    cin >> str;
    int ans = 1;

    int front = 0, back = str.size()-1;
    while(front < back){
        if(str[front] != str[back]){
            ans = 0;
            break;
        }
        else{
            front++;
            back--;
        }
    }

    cout << ans;

    return 0;
}