#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<string> croatia_alpha = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    string str;
    cin >> str;
    int count = 0;

    for (string ca : croatia_alpha){
        size_t pos;
        while(string::npos !=  (pos = str.find(ca))){
            str.replace(pos, ca.length(), "#");
        }
    }

    cout << str.length();

    return 0;
}