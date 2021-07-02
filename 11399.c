#include<stdio.h>

int main(){
    int n, t; // input temp
    int array[1000] = {};
    int sum = 0; // result
    scanf("%d", &n);
    
    // save
    for(int i=0; i<n; i++){
        scanf("%d", &t);
        array[i] = t;
    }
    
    // sort
    for(int i=0; i<n-1; i++){
        for(int j=0; j<n-i-1; j++){
            if(array[j] > array[j+1]){
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    

    }
        
    for(int i=0; i<n; i++){
        sum = sum + (array[i]*(n-i));
    }
    
    printf("%d", sum);
}
