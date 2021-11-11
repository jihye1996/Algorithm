import java.util.*;
import java.awt.*;

public class Main {
    static String [][] map;
    static boolean [][] visit;
    
    static int [] diry ={-1,0,1,0}; //상 우 하 좌
    static int [] dirx ={0,1,0,-1};
    
    public static int bfs(int x, int y, String color, int n, int m){
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(x, y));
        int cnt =1;
        visit[x][y] = true;
        
        while(!q.isEmpty()){
            
            Point cp = q.poll();
            for(int i=0; i<4; i++){
                int nx = cp.x+dirx[i];
                int ny = cp.y+diry[i];
                if(nx>=0 && nx<m && ny>=0 && ny<n){
                    if(!visit[nx][ny] && color.equals(map[nx][ny])){
                        q.add(new Point(nx,ny));
                        visit[nx][ny] = true;
                        cnt++;
                    }
                }
            }
        }
        
        return cnt;
        
    }
    
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        map = new String[M][N];
        visit = new boolean[M][N];
        
        for(int i = 0; i<M; i++){
            String line = sc.next();
            for(int j =0; j<N; j++){
                map[i][j] = line.substring(j,j+1);
            }
        }
        int w = 0;
        int b = 0;

        for(int i = 0; i<M; i++){
            for(int j =0; j<N; j++){
                if(map[i][j].equals("W") && !visit[i][j]){
                    int num = bfs(i, j, "W", N, M);
                    w += num*num;
                }else if(map[i][j].equals("B") && !visit[i][j]){
                    int num = bfs(i, j, "B", N, M);
                    b += num*num;
                }
            }
        }
        
        System.out.println(w+" "+b);
    }
}
