#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cctype>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int max_alpha_index = 0, max_alpha_num = 0;
    char ans;
    string str;
    vector<int> alpha(26, 0);
    cin >> str;

    for (int i = 0; i<size(str); i++){
        str[i] = toupper(str[i]);
        alpha[str[i]-'A'] += 1;
    }

    for (int i = 0; i<26; i++){
        if (alpha[i] != 0){
            if (alpha[i] > max_alpha_num){
                max_alpha_index = i;
                max_alpha_num = alpha[i];
                ans = '0';
            }
            else if (alpha[i] == max_alpha_num){
                ans = '?';
            }
        }
    }

    if (ans == '?'){
        cout << "?";
    }
    else {
        ans = max_alpha_index+'A';
        cout << ans;
    }

    return 0;
}