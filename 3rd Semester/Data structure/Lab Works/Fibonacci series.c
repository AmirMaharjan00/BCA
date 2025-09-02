#include<stdio.h>
#include<conio.h>
void main()
{
	int n,i;
	int fibo(int k);
	printf("Enter the number: ");
	scanf("%d", &n);
	printf("The fibonacci series of the given number is : %d\n", n);
	for ( i =1; i<=n; i++)
		printf("%d\n", fibo(i));
		getch();
}
	int fibo(int k)
	{
		if (k == 1 || k == 2)
			return 1;
		else
			return fibo(k-1)+fibo(k-2);
	}

