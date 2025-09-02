//Program Code of Implementation of Stack.
#include<stdio.h>
#include<conio.h>
void push();
void pop();
void display();
int tos=-1,stack[5],max=5;
 main()
{
int ch;
top:
printf("\nInput the choice");
printf("\n1 to PUSH data in the stack");
printf("\n2 to POP the data from the stack");
printf("\n3 to display data");
printf("\n4 to exit");
scanf("%d",&ch);
switch(ch)
{
case 1:
push();
goto top;
case 2:
pop();
goto top;
case 3:
display();
goto top;
case 4:

default:
printf("\nInvalid input");
goto top;
}
getch();
}
void push()
{
int data;
if(tos==max-1)
{
printf("\nOVERFLOW!!!!");
}
else
{
tos=tos+1;printf("Input the data to push onto stack:");
scanf("%d",&data);
stack[tos]=data;
printf("\n%d is pushed onto stack",data);
}
}
void pop()
{
if(tos==-1)
{
printf("\nUNDERFLOW!!!!");
}else
{
printf("\nPopped data=%d",stack[tos]);
tos=tos-1;
}
}
void display()
{
int i;if(tos==-1)
{
printf("\nThe stack is empty.");
}else
{
printf("\nThe elements of the stack are:");
for(i=0;i<=tos;i++)
{
printf("%d\t",stack[i]);
}
}
}

