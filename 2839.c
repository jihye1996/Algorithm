#include<stdio.h>

int main(){
    int a, b, n, t; // 5kg 자루, 3kg 자루, input, temp
    scanf("%d", &n);
        
    t=n%5;
    a=n/5;
        
    while(t<=n){
        
        if(t%3 != 0){
            t+=5;
            a--;
            
            if(a==-1){
                printf("%d", a);
                break;
            }
        }else{
            b=t/3;
            printf("%d", a+b);
            break;
        }
    } 
}
