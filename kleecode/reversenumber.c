#include <stdio.h>
int main(int argc, char *argv[])
{
  int n, reverse=0, rem;
  printf("Enter an integer: ");
  klee_make_symbolic(&n, sizeof n, "n");
  while(n!=0)
  {
     rem=n%10;
     reverse=reverse*10+rem;
     n/=10;
  }
  printf("Reversed Number = %d",reverse);
  return 0;
}
