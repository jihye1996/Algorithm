import java.util.*;

public class Main {

    static int MAX_VALUE = 10001;
    
	public static void main(String[] args) {
        boolean[] flags = new boolean[MAX_VALUE];
        
        for(int i=1; i<MAX_VALUE; i++){
            int t = i;
            
            while(true){
               String str = String.valueOf(i);
                int sum = i;
                for (int j = 0; j < str.length(); j++) {
    			    sum += str.charAt(j) - '0';
    		    } 
    		    
    		    if(sum>=MAX_VALUE || flags[sum]) break;
    		    
    		    flags[sum] = true;
    		    t = sum;
            }
        }
		
		for (int i = 1; i <MAX_VALUE; i++) {
			if(!flags[i]) System.out.println(i); 
		}
	}

}
