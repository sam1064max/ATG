/*C program to demonstrate the working of do...while statement*/
#include <stdio.h>
int main(){
   int sum=0,num;
   do             /* Codes inside the body of do...while loops are at least executed once. */
   {                                    
        printf("Enter a number\n");
        //scanf("%d",&num);
	klee_make_symbolic(&num, sizeof &num, "num");
        sum+=num;      
   }
   while(num!=0);
   printf("sum=%d",sum);
return 0;
}
