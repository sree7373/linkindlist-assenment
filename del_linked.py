class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def addatstart(self,newData):
        newNode = node(newData)
        newNode.next = self.head
        self.head = newNode

    def deleting(self, removeKey):
        head = self.head
        if head:
            if head.data == removeKey:
                self.head = head.nexthead = None
                return
            
            while head is not None:
                if head.data == removeKey:
                    break
                prev = head
                head = head.next

            if head == None:
                return
            
            prev.next = head.next
            head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data )
            temp = temp.next

linked_list = LinkedList()
linked_list.addatstart("honeycake")
linked_list.addatstart("chocklate")
linked_list.addatstart("butterscoch")
linked_list.addatstart("vennila")


#print("linked list before deletion: ")
#linked_list.display()

linked_list .deleting("honeycake")

#print("linked list after deletion: ")
#linked_list.display()