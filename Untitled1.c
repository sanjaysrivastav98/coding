#include<stdio.h>
#include<math.h>

int main(){
    int s ;
    scanf("%d",&s);
    int inp[s];
    int i=0;
    for (i=0;i<s;i++){
        scanf("%d",&inp[i]);
        if(inp[i]<1 ||inp[i]>1000000000)
                i-=1;
    }
    int noz,n;
    for(i=0;i<s;i++){
        n=1;
        noz=0;
        while((inp[i]/pow(5,n))!=0){
            noz+=inp[i]/pow(5,n);
            n+=1;
        }
        printf("%d\n",noz);
    }
    return 0;


}
