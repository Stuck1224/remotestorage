#include <stdio.h>
#include <stdlib.h>

struct Node
{
int data;
struct Node* next;

};

struct Node* head;


void Insert(int data)
{
struct Node* temp1 = (struct Node*)malloc(sizeof(struct Node));
temp1->data = data;
temp1->next = NULL;

if (head==NULL)
{head = temp1;
return ;}
struct Node* temp2;
temp2 = head;
while(temp2!=NULL)
	temp2 =temp2 ->next;
temp2->next=temp1;

}


void Delete(int n)
{
struct Node* temp1 = head;
for(int i=0;i<n-2;i++)
	temp1 = temp1 ->next;
struct Node* temp2;

temp2= temp1->next;
temp1->next = temp2->next;
free(temp2);

}







void Print()
{
struct Node* temp;
temp= head;
while(temp!=NULL)
{
	temp = temp->next;
	if(temp!=NULL)
	printf("  %d",temp->data);
}
printf("\n");


}



int main()
{
head = NULL;

Insert(4);
Print();

Insert(13);

Print();
Insert(8);

Print();
Insert(9);
Print();
Delete(3);
Print();
return 0;
}
