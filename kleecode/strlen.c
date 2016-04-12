#include <stdio.h>
int main()
{
    char s[1000],i;
    printf("Enter a string: ");
    //scanf("%s",s);
    klee_make_symbolic(s, sizeof s, "s");
    for(i=0; s[i]!='\0'; ++i);
    printf("Length of string: %d",i);
    return 0;
}
