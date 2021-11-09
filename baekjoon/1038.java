import java.util.*;

public class Main{

     public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();
        
        if(N<=10){
            System.out.println(N);
        }else if(N>1022){
            System.out.println("-1");
        }else{
            ArrayList<Integer> array = new ArrayList<>();
            
            Collections.sort(array);
            System.out.println(array.get(N));
        }
    }
    
    private static void descedning_number(){
        
    }  
}
