"""
Linked List Class
Classes:
    1. Node
    2. Linked List
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        # Method for printing out all members of the list
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self, data):
        # Adding a node to the end of the linked list
        new_node = Node(data)
        #Catering for possibility of an empty linked list
        if self.head is None:
            #If there's no head value, it implies that it’s an empty linked list and there’s nothing there
            self.head = new_node
            return
        # In the case of a non empty linked list
        last_node = self.head # We set the head to last_node 
        while last_node.next: # Moving through the linked list as long as last_node.next doesn't point to None
            last_node = last_node.next
        # Setting the value of the last node to the newly created node after we break out of the loop
        last_node.next = new_node

    def prepend(self, data):
        #The prepend method will insert an element at the beginning of the linked list
        new_node = Node(data)

        new_node.next = self.head #Setting the next value of the new node to the current head in the List
        self.head = new_node  # Making the newly created node head of the list

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            # we need to check if the node to be inserted after is in the linked list or not.
            #  If it’s not in the linked list, we’ll return
            print("Previous node is not in the list")
            return
        
        new_node = Node(data)

        new_node.next = prev_node.next # Set the next value of the new node to the next value of the previous node
        prev_node.next = new_node

    def delete_node(self, key):
        # Deleting a node in a linked list (2 cases: 1. Node to be deleted is head, 
        # 2. Node to be deleted is not head)

        # Case of deleting head
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        #Case of Deleting Node Other Than the Head
        prev = None #This will keep track of the previous node of the node to be deleted
        while cur_node and cur_node.data != key: #will run until cur_node becomes None      
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None: # check whether or not it’s because of cur_node being None
            return

        # if cur_node is not None and its data matches with the key
        prev.next = cur_node.next # Set the previous nodes next to the value of the target nodes next
        cur_node = None

    def delete_node_at_pos(self, pos):
        # Delete a node at a given position
        # Cases: 
        # 1. Node to be deleted is at position 0
        # 2. Node to be deleted is not at position 0
        if self.head: #check if the linked list is an empty list or not
            cur_node = self.head

            if pos == 0: # If the position refers to the head, we set the head to the next node and delete the current head
                self.head = cur_node.next
                cur_node = None
                return

            # Deleting at a position other than the head
            prev = None
            count = 0
            #The while loop will terminate if cur_node becomes None or 
            # count becomes equal to pos which will imply that cur_node
            #  will be the node that we want to delete.
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    def len_iterative(self):
        # Counting the number of nodes using the iterative approach
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def len_recursive(self, node):
        # Recursive approach of counting nodes
        if node is None: #Checking if the we've reached the end of the list
            return 0
        return 1 + self.len_recursive(node.next)


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.print_list()

if not (llist.delete_node("E")):
    print("E not found in the linked list")

llist.print_list()
print("Iterative count of nodes: " ,llist.len_iterative())

print("Recursive count of nodes: " ,llist.len_iterative())
