class node:
    def __init__(self,val):
        self.val=val
        self.next=None
        

a= node(1)
b= node(2)
c= node(3)
a.next=b
b.next=c
head=a
print(head.val)

def printlist(head):
    curr=head
    while curr!=None:
        print(curr.val,end=" ")
        curr=curr.next




def insertatbeginning(head,val):
    newnode=node(val)
    newnode.next=head
    return newnode

head=insertatbeginning(head,0)


def insertatend(head,val):
    newnode=node(val)
    if head==None:
        return newnode
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newnode
    return head

head=insertatend(head,4)


def insertatposition(head,pos,val):
    newnode=node(val)
    if pos==0:
        newnode.next=head
        return newnode
    curr=head
    for i in range(pos-1):
        if curr==None:
            return head
        curr=curr.next
    if curr==None:
        return head
    newnode.next=curr.next
    curr.next=newnode
    return head

head=insertatposition(head,2,10)
printlist(head)