//Queue implementation using array
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#define max 5
int q[max], front = 0, rear = -1;
void enqueue ();
void dequeue ();
void display();
int main()
{
	int ch;
	printf("Pick your choice: \n");
	printf("\n1: Enqueue or Insert\n2: Dequeue or Delete\n3: Display\n4: End the program\n ");
	while(1)
	{
		printf("\nEnter your choice : ");
		scanf("%d", &ch);
		switch(ch)
		{
			case 1:
				enqueue();
				break;
			case 2:
				dequeue();
				break;
			case 3:
				display();
				break;
			case 4:
				exit(1);
			default:
				printf("You have entered invalid choice.");
				
		}
	}
}
void enqueue()
{
	int data;
	if (rear == max-1)
	{
		printf("Queue is overflow. Overflow!!");
	}
	else
	{
		if(front==-1)
		{
			front = 0;
		}
		printf("Enter the element to insert: ");
		scanf("%d", &data);
		rear ++;
		q[rear]=data;
	}
}
void dequeue()
{
	if (front == -1 || front > rear)
	{
		printf("\nThe stack is empty. Underflow!!");
	}
	else
	{
		printf("\nDequeue: %d", q[front]);
		front++;
	}
}
void display()
{
	int i;
	if (front == -1)
	{
		printf("\nQueue is Empty");
	}
	else
	{
		printf("Elements:");
		for(i=front; i<=rear; i++)
		{
			printf("\n%d", q[i]);
		}
	}
}
