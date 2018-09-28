#include <stdio.h>
#include <math.h>

int main()
{
    int T, x1, y1, x2, y2, n, cx, cy, r;
    int planet[3];
    int inout=0;
    double distance1, distance2;
    _Bool circle1=0, circle2=0;
    
    scanf("%d", &T);
    
    for(int i=0; i<T; i++){
        
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        
        scanf("%d", &n);
        
        for(int j=0; j<n; j++){
            scanf("%d %d %d", &cx, &cy, &r);
            planet[0]=cx;
            planet[1]=cy;
            planet[2]=r;
            
            //중점과 거리 < r => inout++
            distance1 = sqrt(pow((planet[0]-x1),2)+pow((planet[1]-y1),2));
            distance2 = sqrt(pow((planet[0]-x2),2)+pow((planet[1]-y2),2));
            
            if(distance1<planet[2]){
                circle1 = 1;
            } else{
                circle1 = 0;
            }
            
            if(distance2<planet[2]){
                circle2 = 1;
            }else{
                circle2=0;
            }
            
            //출발점과 도착점이 하나의 원에 있을 경우, 둘 다 원 밖에 있을 경우 플러스 하지 않는다.
            //출발점과 도착점이 다른 원에 있을 경우에 ++
            if(circle1^circle2){
                inout++;
            }
            
        }
        printf("%d\n", inout);
        inout=0;
    }

    return 0;
}
