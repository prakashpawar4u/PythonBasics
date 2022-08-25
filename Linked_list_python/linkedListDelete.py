#Node Class
class Node:
    #Function to initialize the node object
    def __init__(self, data):
        self.data = data #assign data
        self.next = None #Initialize next as null


class LinkedList:
    #Function to initialize the head
    def __init__(self):
        self.head = None

    #Function to insert a new node at the begining
    def push(self,new_data):
        #1 & 2 Allocate the node & put in the data
        new_node = Node(new_data)

        #3 Make next of the new Node as head
        new_node.next = self.head

        #4 Move the head to poin to new node
        self.head = new_node



    #Inserts a new node after the given prev node. This method is defined inside LinkedList class shown above

    def insertAfter(self, prev_node, new_data):

        #1 check if the given prev node exists
        if prev_node is None:
            print("The given previous node must be in Linked List")

        #2 Create new node & put in the data
        new_node = Node(new_data)

        #3 make the next of the newnode as next of the prev_node
        new_node.next = prev_node.next

        #4 make next of the prev node as new_node
        prev_node.next = new_node



    # Append at the end of the linked list
    # 1Create a new node
    # 2. Put in the data
    # 3. Set next as None
    def append(self, new_data):
        new_node = Node(new_data)

        #4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return
        #5 Else traverse till the last node
        last = self.head
        while(last.next):
            last = last.next

        #6 Change the next of last node
        last.next = new_node

    def deleteNode(self,key):
        #store the head node
        temp = self.head

        #if the head node itself hotds the key





    def printList(self):
        temp= self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    # Start with the empty list
    llist = LinkedList()

    # Insert 6.  So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)


    print('Created linked list is:')
    llist.printList()





