#include<stdio.h>
int main()
{
	int a=1,n,b,c=0,rem;
	printf("Enter: ");
	scanf("%d",&n);
	b=n;
	while(n>0)
	{
		rem=n%10;
		while(rem>=1)
		{
			a=a*rem;
			rem--;
		}
		c=c+a;
		a=1;
		n=n/10;
	}
	if(b==c)
	printf("STRONG NUMBER");
	else
	printf("NOT A STRONG NUMBER");
	return 0;
}
