#include <stdio.h>
int even(int n){
  if(n%2==0)
    return 1;
  else
    return 0;
}
int main()
{
  int n;
  scanf("%d",&n);
  if(even(n))
    printf("%d is a even.\n",n);
  else
    printf("%d is a odd.\n",n);
  return 0;
}