#include<stdio.h>
#include<math.h>
int main()
{
	int n,b=0,x=0,a,rem;
	printf("ENTER: ");
	scanf("%d",&n);
	a=n;
	while(n>0)
	{
		n=n/10;
		x++;
	}
	n=a;
	while(n>0)
	{
		rem=n%10;
		b=b+pow(rem,x);
		n=n/10;
	}
	if(a==b)
	printf("ARMSTRONG NUMBER.");
	else
	printf("NOT AN ARMSTRONG NUMBER.");
	return 0;
}
