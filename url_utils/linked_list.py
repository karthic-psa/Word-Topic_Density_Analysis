class Node:

    # Constructor to initialize the node object
    def __init__(self, data, word):
        self.data = data
        self.value = word
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def sortedInsert(self, new_node):

        # Special case for the empty linked list
        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        # Special case for head at end
        elif self.head.data <= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else:

            # Locate the node before the point of insertion
            current = self.head
            while (current.next is not None and
                   current.next.data > new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node

    # Function to insert a new node at the beginning
    def push(self, new_data, new_word):
        new_node = Node(new_data, new_word)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        temp_arr = []
        cnt = 0
        while (temp) and cnt < 9:
            temp_arr.append(temp.value)
            # print temp.value, temp.data
            temp = temp.next
            cnt += 1
        print(temp_arr)