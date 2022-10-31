#include <stdio.h>

int main()
{
    int n1, n2;
    scanf("%d %d", &n1, &n2);
    int n3 = (n2%10)*n1;
    int n4 = (n2/10%10)*n1;
    int n5 = (n2/100)*n1;
    
    printf("%d\n", n3);
    printf("%d\n", n4);
    printf("%d\n", n5);
    printf("%d\n", n1*n2);
    
    return 0;
}