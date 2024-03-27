#Doubly Linked List in Python
class Node:
    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_Node = Node(data)

        if not self.head:
            self.head = new_Node
            return
        else:
            added_Node = self.head

        while added_Node.next:
            added_Node = added_Node.next

        added_Node.next = new_Node
        new_Node.previous = added_Node

    def print_List(self):
        current_Node = self.head

        if current_Node is Node:
            print("Null")
            return

        while current_Node:
            if current_Node.previous is None:
                print("Null", end=" <--> ")
            
            else: 
                print(current_Node.previous.data, end=" <--> ")
            
            print(current_Node.data, end=" <--> ")
            current_Node = current_Node.next

        print("Null")

        # Displaying the HEAD and the TAIL Node
        print(f"Head: {self.head.data}")
        print(f"Tail: {current_Node}")

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)

dll.print_List()