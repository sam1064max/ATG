#include <stdio.h>
int main(int argc, char *argv[])
{
  int n,count=0;
  printf("Enter an integer: ");
  klee_make_symbolic(&n, sizeof n, "n");
  while(n!=0)
  {
      n/=10;             /* n=n/10 */
      ++count;
  }
  printf("Number of digits: %d",count);
}
