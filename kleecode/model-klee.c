#include <stdio.h>
#include <math.h>

int prime(int n){
  int i, flag=1;
  for(i=2;i<=n/2;++i)
  {
      if(n%i==0)
      {
          flag=0;
          break;
      }
  }
  return flag;
}

int even(int n){
  if(n%2==0)
    return 1;
  else
    return 0;
}

int squr(int n){
  int i, flag=0;
  for(i=1;i<=sqrt(n);++i)
  {
      if(n==i*i)
      {
          flag=1;
          break;
      }
  }
  return flag;
}

int main(int argc, char *argv[])
{
  int n, i, f1,f2,f3;
  //scanf("%d",&n);
  klee_make_symbolic(&n, sizeof n, "n");
  f1 = prime(n);
  f2 = even(n);
  f3 = squr(n);
  if(f1){
    if(f2){
      if(f3)
        printf("%d is a prime, even and squre number.\n",n);
      else
        printf("%d is a prime, even and not squre number.\n",n);
    }
    else{
      if(f3)
        printf("%d is a prime, odd and squre number.\n",n);
      else
        printf("%d is a prime, odd and not squre number.\n",n);
    }
  }
  else{
    if(f2){
      if(f3)
        printf("%d is a composite, even and squre number.\n",n);
      else
        printf("%d is a composite, even and not squre number.\n",n);
    }
    else{
      if(f3)
        printf("%d is a composite, odd and squre number.\n",n);
      else
        printf("%d is a composite, odd and not squre number.\n",n);
    }
  }
  return 0;
}
