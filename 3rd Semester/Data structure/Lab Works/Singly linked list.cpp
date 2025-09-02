#include<stdio.h>
#include<conio.h>
#include<malloc.h>
#include<process.h>
struct node
{
	int info;
	struct node *next;
};
typedef struct node NodeType;
NodeType *head;

void insert_atfirst(int);
void insert_givenposition(int);
void insert_atend(int);
void delet_first();
void delet_last();
void delet_nthnode();
void info_sum();
void count_nodes();
int main()
{
	int choice;
	int item;
	do
	{
		printf("\nMenu for program:");
		printf("1: insert first\n2: insert at given position\n3: insert at last\n4: Delete first node\n5: Delete last node\n6: delete nth node\n7: count nodes\n8: Display items\n9: exit\n");
		printf("Enter your choice : ");
		scanf("%d", &choice);
		switch(choice)
		{
			case 1:
				printf("Enter item to be inserted");
				scanf("%d", &item);
				insert_atfirst(item);
				break;
			case 2:
				printf("Enter item to be inserted");
				scanf("%d", &item);
				insert_givenposition(item);
				break;
			case 3:
				printf("Enter item to be inserted");
				scanf("%d", &item);
				insert_atend(item);
				break;
			case 4:
				delet_first();
				break;
			case 5:
				delet_last();
				break;
			case 6:
				delet_nthnode();
				break;
			case 7:
				info_sum();
				break;
			case 8:
				count_nodes();
				break;
			case 9:
				exit(1);
				break;
			default: 	
				printf("You have entered invalid choice");
				break;	
		}
	}while(choice<10);
	getch();
}
