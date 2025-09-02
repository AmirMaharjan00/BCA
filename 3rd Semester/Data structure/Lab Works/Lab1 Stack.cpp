//stack implementation of stack
#include<stdio.h>
#include<conio.h>
#define MAX 5
int a[MAX], top=-1;
void push();
void pop();
void disp();
int main(){
	int ch;
	printf("1: push or insert\n");
	printf("2: pop or delete\n");
	printf("3: display\n");
	printf("4: End program\n");
	while (1){
		printf("\nEnter choice: ");
		scanf("%d", &ch);
		switch (ch){
			case 1:{
					push();
					break;
				}
				case 2:{
					pop();
					break;
				}
				case 3:{
					disp();
					break;
				}
				default:{
					printf("Wrong Choice");
				}
		}
	}
}
void push(){
	int data;
	if (top == MAX -1)
		printf("\nOver flow of stack");
	else
	printf("Enter element to push:");
	scanf("%d", &data);
	top++;
	a[top]=data;
}
void pop(){
	if (top == -1)
	 printf("Stack is empty");
	else
		printf("Popped element : %d", a[top]);
		top --;
}
void disp(){
	int i;
	if (top>=0){
		printf("Elements:\n");
		for (i=top; i>=0; i--)
		printf("%d\n", a[i]);
	}
	else
		printf("The stack is empty");   
}
