class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next

    def insertationatstart(self,newdata):         # adding the data in starting
        newdata=node(newdata)
        newdata.next=self.head
        self.head=newdata

    def insertationat_end(self,newdata):         # adding data at end
        newdata=node(newdata)
        if self.head==None:
            self.head=newdata
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = newdata

    def inseratatmiddle(self,middlenode,newdata):    # adding data in middleof the values
      if middlenode is  None:
         print('mainted node is node')
         return
      newnode=node(newdata)
      newnode.next=middlenode.next
      middlenode.next=newnode

    def linkedlist_deleting(self, del_data):         # deleting data data in linkedlist
      head = self.head
      if head:
        if head.data == del_data:
            self.head = head.nexthead = None
            return
        while head is not None:
                if head.data == del_data:
                    break
                prev = head
                head = head.next
        if head == None:
                return
        prev.next = head.next
        head = None
linkedlist=linkedlist()  # obj call
linkedlist.head=node("T S Reddy") # data 
second=node("Dinesh")
third=node("fazzu")

linkedlist.head.next=second   
second.next=third
linkedlist.insertationatstart("Asif")
linkedlist.insertationat_end("Prakesh")
linkedlist.inseratatmiddle(linkedlist.head.next,'V G S')
linkedlist.linkedlist_deleting('T S Reddy')
linkedlist.display()
