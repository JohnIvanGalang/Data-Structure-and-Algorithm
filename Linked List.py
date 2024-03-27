class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        new_Node = Node(data)  # For creating a Node

        if not self.head:
            self.head = new_Node  # Assigns the HEAD to the first Node
            return
        
        last_Node = self.head  # NEW VARIABLE 

        while last_Node.next:
            last_Node = last_Node.next
        
        last_Node.next = new_Node  # Assigns the the TAIL to the last Node


    def print_List(self):  # For displaying the list
        current_Node = self.head

        while current_Node:
            print(current_Node.data, end="  -->  ")
            current_Node = current_Node.next
        print("Null")

        # Displaying the HEAD and the TAIL Node
        print(f"Head: {self.head.data}")
        print(f"Tail: {current_Node}")


my_List = LinkedList()
my_List.append(3)
my_List.append(7)
my_List.append(8)
my_List.append(2)

my_List.print_List()