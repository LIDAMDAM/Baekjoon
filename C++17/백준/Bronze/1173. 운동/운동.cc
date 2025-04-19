#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, m, M, T, R, X, count = 0, totalTime = 0;
    cin >> N >> m >> M >> T >> R;
    X = m;
    for(;count!=N;){
        if (m+T > M){
            totalTime = -1;
            break;
        }
        else if (X+T <= M){
            X += T;
            totalTime++;
            count++;
        }
        else{
            if(X-R<m){
                X = m;
                totalTime++;
            }
            else{
                X -= R;
                totalTime++;
            }
        }
    }

    cout << totalTime;

    return 0;
}