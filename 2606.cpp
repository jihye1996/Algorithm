#include <iostream>
#include <stack>

using namespace std;

#define MAX 101

int map[MAX][MAX];
bool visited[MAX];  
int N, M;

void dfs(int n){
    
    int cnt = 0;
    stack<int> s;
    s.push(n);
    visited[n] = true;
    
    while(!s.empty()){
        int c = s.top();
        s.pop();
        
        for(int i=1; i<=N; i++){
            if(!visited[i] && map[c][i]==1){
                visited[i] = true;
                s.push(i);
                cnt++;
            }
        }
    }
    
    cout << cnt;
    
}

int main()
{
    
    int x, y;
    cin >> N >> M;
    
    for(int i=0; i<M; i++){
        cin >> x >> y;
        map[x][y] = 1;
        map[y][x] = 1;
    }
    
    
    dfs(1);
    
    return 0;
}
