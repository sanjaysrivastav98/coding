#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isPalindrome(int *b,int n){
	int i=0;
	if(n==1){
		return 1;
	}
	else if(n==2){
		return b[0]==b[1];
	}
	if(b[0]==b[n-1]){
		int *c=(int*)malloc((n-2)*sizeof(int));
		return isPalindrome(c,n-2);
	}
	return 0;
}



int main(){
	int T;
	scanf("%d",&T);
	int a[T];
	int **b = (int**)malloc(T*sizeof(int*));
	int i=0,j=0;
	for(i=0;i<T;i++){
		scanf("%d",&a[i]);
		b[i]=(int*)malloc(a[i]*sizeof(int));
		for(j=0;j<a[i];j++){
			scanf("%d",&b[i][j]);
		}
	}
	int result[T];
	for(i=0;i<T;i++){
		if(isPalindrome(b[i],a[i]) && b[i][(a[i]-1)/2]==7){	
			for(j=1;j<(a[i]-1)/2;j++){
				if(b[i][j]-b[i][j-1]==0 || b[i][j]-b[i][j-1]==1){
					result[i]=1;
				}
				else{
					result[i]=0;
					break;
				}

			}
			
		}
		if(result[i]==1)
			printf("yes\n");
		else
			printf("no\n");
	}

}

