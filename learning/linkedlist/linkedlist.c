#include <stdlib.h>
#include <stdio.h>

typedef struct LinkedListStruct{
    int data;
    struct LinkedListStruct *next;
}LinkedListStruct;

LinkedListStruct* add(LinkedListStruct* head, int data)
{
    // 普通にmalloc
    LinkedListStruct *obj = (LinkedListStruct *)malloc(sizeof(LinkedListStruct));
    if(obj == NULL){
        fprintf(stderr,"malloc failed\n");
        exit(1);
    }
    
    // Data storage 
    obj-> next = NULL ;
    obj->data = data;
    
    
    // The last tail explore 
    if (head == NULL ){
         return obj;
    }else{
        LinkedListStruct *ptr = head;
        while(ptr->next != NULL){
            ptr = ptr->next;
        }
        ptr->next = obj;
        return head;
    }
}

int count(LinkedListStruct *ptr, int data)
{
    int c = 0;
    while(ptr != NULL){
        if(ptr->data == data){
            c += 1;
        }
        ptr = ptr->next;
    }
    return c;
}


int main(void){
    // テスト用
    LinkedListStruct*head = NULL;
    
    head = add(head,1);
    head = add(head,2);
    head = add(head,3);
    head = add(head,1);
    head = add(head,2);
    head = add(head,1);
    
    printf("1:%d\n",count(head,1));
    printf("2:%d\n",count(head,2));
    printf("3:%d\n",count(head,3));
    
    printf("\n");
    LinkedListStruct*ptr = head;
    while(ptr != NULL){
        printf("%d, ", ptr->data);
        ptr = ptr->next;
    }
    printf("\n");
}
