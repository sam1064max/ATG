#include <stdio.h>
int main()
{
    int n, count;
    unsigned long long int factorial=1;         
    printf("Enter an integer: ");
    klee_make_symbolic(&n, sizeof n, "n");
    if ( n< 0)
        printf("Error!!! Factorial of negative number doesn't exist.");
    else
    {
       for(count=1;count<=n;++count)    /* for loop terminates if count>n */
       {
          factorial*=count;              /* factorial=factorial*count */
       }
    printf("Factorial = %lu",factorial);
    }
    return 0;
}
