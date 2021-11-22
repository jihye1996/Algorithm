import java.util.*;
import java.io.*;

public class Main {
    static int N = 0;
    static int MIN = 101;
    static int MAX = 0;
    static int MAX_SPACE = 0;
    static int[][] maps;
    static boolean[][] visited;
    
    static void DFS(int height, int x, int y){
        
        visited[x][y] = true;
        
        if(x-1>=0 && !visited[x-1][y] && maps[x-1][y]>height)
            DFS(height, x-1, y);

        if(x+1<N && !visited[x+1][y] && maps[x+1][y]>height)
            DFS(height, x+1, y);
            
        if(y-1>=0 && !visited[x][y-1] && maps[x][y-1]>height)
            DFS(height, x, y-1);
            
        if(y+1<N && !visited[x][y+1] && maps[x][y+1]>height)
            DFS(height, x, y+1);
    }
    
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        maps = new int[N][N];
        
        for(int i=0;i<N;i++ ) {
            for(int j=0; j<N; j++){
                maps[i][j] = sc.nextInt();
                if(MIN>maps[i][j]) MIN = maps[i][j];
                if(MAX<maps[i][j]) MAX = maps[i][j];
            }
        }

        sc.close();
        
        for(int k=MIN-1; k<MAX; k++) {
            visited = new boolean[N][N];
            int count = 0;
            
            //dfs
            for(int i=0;i<N;i++) {
                for(int j=0; j<N; j++){
                    if(!visited[i][j] && maps[i][j]>k){
                        DFS(k, i, j);
                        count++;
                    }
                }// end for
            }//end for for
            
            if(MAX_SPACE<count) MAX_SPACE = count;

        }
        
        System.out.println(MAX_SPACE);

    }
}
