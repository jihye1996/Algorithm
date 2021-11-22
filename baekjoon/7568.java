import java.util.*;
import java.io.*;

public class Main {
    
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int[][] ps= new int[N][2];
        int[] scores = new int[N];
        
        for(int i=0;i<N;i++ ) {
            st= new StringTokenizer(br.readLine());
            for(int j=0;j<2;j++) {
                ps[i][j]=Integer.parseInt(st.nextToken()); 
            }  
        }

        for(int i=0;i<N;i++ ) {
            for(int j=i+1;j<N;j++) {
                scores[i]++;
                scores[j]++;
                
                if(ps[i][0]>ps[j][0] && ps[i][1]>ps[j][1]) scores[j]--;
                else if(ps[i][0]<ps[j][0] && ps[i][1]<ps[j][1]) scores[i]--;
                
            }  
        }
        
        for(int i=0;i<N;i++ ) {
            System.out.println(N-scores[i]);
        }


    }
}
