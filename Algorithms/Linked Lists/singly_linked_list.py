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
        # Catering for possibility of an empty linked list
        if self.head is None:
            # If there's no head value, it implies that it’s an empty linked list and there’s nothing there
            self.head = new_node
            return
        # In the case of a non empty linked list
        last_node = self.head  # We set the head to last_node
        while last_node.next:  # Moving through the linked list as long as last_node.next doesn't point to None
            last_node = last_node.next
        # Setting the value of the last node to the newly created node after we break out of the loop
        last_node.next = new_node

    def prepend(self, data):
        # The prepend method will insert an element at the beginning of the linked list
        new_node = Node(data)

        # Setting the next value of the new node to the current head in the List
        new_node.next = self.head
        self.head = new_node  # Making the newly created node head of the list

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            # we need to check if the node to be inserted after is in the linked list or not.
            #  If it’s not in the linked list, we’ll return
            print("Previous node is not in the list")
            return

        new_node = Node(data)

        # Set the next value of the new node to the next value of the previous node
        new_node.next = prev_node.next
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

        # Case of Deleting Node Other Than the Head
        prev = None  # This will keep track of the previous node of the node to be deleted
        while cur_node and cur_node.data != key:  # will run until cur_node becomes None
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:  # check whether or not it’s because of cur_node being None
            return

        # if cur_node is not None and its data matches with the key
        # Set the previous nodes next to the value of the target nodes next
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        # Delete a node at a given position
        # Cases:
        # 1. Node to be deleted is at position 0
        # 2. Node to be deleted is not at position 0
        if self.head:  # check if the linked list is an empty list or not
            cur_node = self.head

            if pos == 0:  # If the position refers to the head, we set the head to the next node and delete the current head
                self.head = cur_node.next
                cur_node = None
                return

            # Deleting at a position other than the head
            prev = None
            count = 0
            # The while loop will terminate if cur_node becomes None or
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
        if node is None:  # Checking if the we've reached the end of the list
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        # Swapping the position of two nodes in a linked list
        if key_1 == key_2:
            return

        def swap_nodes(self, key_1, key_2):
            if key_1 == key_2:
                return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        # Reversing a linked list iteratively
        prev = None
        cur = self.head
        while cur: # Runs until cur is not equal to None
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print("Original List")
llist.print_list()


llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print_list()

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node")
llist.print_list()

llist.swap_nodes("D", "B")
print("Swapping nodes D and B where key_2 is head node")
llist.print_list()

llist.swap_nodes("C", "C")
print("Swapping nodes C and C where both keys are same")
llist.print_list()


llist.reverse_iterative()
llist.print_list()