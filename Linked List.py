class Node:
    def _init_(self,data=None):
        self.data=data
        self.next=None
        SLL.SinglyLinkedList
class SinglyLinkedList:
    def _init_(self):
        self.first=None
    def insertFirst(self.data):
        temp=node(data)
        temp.next=self.first 
        self.first=temp
    def removeFirst(self):
        if(self.first==None):
           print("list is empty")
        else:    
           cur=self.first
           self.first=self.first.next
           print("the deleted item is",cur.data)
    def display(self):
        if(self.first==None):
           print("list is empty")
           return
        cur=self.first
        while cur:
           print(cur.data, end=" ")
           cur=cur.next
        print()
    def search(self,item):
        if self.first is None:
           print("list is empty")
           return
        cur=self.first
        while cur is not None:
           if cur.data==item:
              print("item is not present in the Linked list")
              return
           cur=cur.next
        print("item is not present in the Linkedlist")
SLL=SinglyLinkedList()
while True:
    ch=int(input("\nEnter your choice: 1-insert 2-delete 3-search 4-display 5-exit:"))
    if ch == 1:
       item=input("Enter element to insert")  
       SLL.insertFirst(item)
       SLL.display()
    elif ch == 2:
       SLL.removeFirst()
       SLL.display()
    elif ch == 3:
       item=input("enter element to search:")
       SLL.search(item)
    elif ch == 4 :
       SLL.display()
    elif ch == 5:
       break
    else:
       print("invalid choice, try again!")   