#include <iostream>
#include <stack>
#include <queue>

using namespace std;

#define MAX_VALUE 1001

int map[MAX_VALUE][MAX_VALUE];
bool visited[MAX_VALUE];
bool visited2[MAX_VALUE];
int N, M, V; //input

void dfs(int v){
    
    stack<int> s;
    s.push(v);
    
    while(!s.empty()){
        int cnt = s.top();
        s.pop();
        if(!visited[cnt]){
            visited[cnt] = true;
            cout << cnt << ' ';            
            
            for(int i=N; 0<i; i--){
                if(map[cnt][i] == 1 && !visited[i]){
                    s.push(i);
                }
            } // end for

        }
    }
    
    cout << endl;
    
}

void bfs(int v){
    queue<int> q;
    q.push(v);
    visited2[v] = true;
    
    
    while(!q.empty()){
        int cnt = q.front();
        q.pop();
        cout << cnt << ' ';
        
        for(int i=1; i<=N; i++){
            if(map[cnt][i] == 1 && !visited2[i]){
                visited2[i] = true;
                q.push(i);
            }
        } // end for
    }
    
}

int main()
{
   
   int x, y; //input map data
   cin >> N >> M >> V;
   
   for(int i=0; i<M; i++){
       cin >> x >> y;
       map[x][y] = map[y][x] = 1;
   }
   
   dfs(V);
   bfs(V);
   
   
   return 0;
}
