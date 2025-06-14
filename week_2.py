class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

 #Adds a node to the end of the list.
    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        
#Prints the linked list.
    def print_list(self):
        
        curr = self.head
        if not curr:
            print("List is empty.")
            return
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")
        
#Deletes the nth node from the linked list (1-based index).
    def delete_nth_node(self, n):
        if not self.head:
            print("Error: Cannot delete from an empty list.")
            return

        if n <= 0:
            print("Error: Invalid index. Index must be 1 or greater.")
            return

        try:
            if n == 1:
                del_val = self.head.data
                self.head = self.head.next
                print(f"Deleted node")
                return

            curr = self.head
            for _ in range(n - 2):
                if not curr.next:
                    raise IndexError("Index out of range.")
                curr = curr.next

            if not curr.next:
                raise IndexError("Index out of range.")

            del_val = curr.next.data
            curr.next = curr.next.next
            print(f"Deleted node")
            
        except IndexError as e:
            print("Error:", e)


# main function
if __name__ == "__main__":
    ll = LinkedList()

    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Initial list:")
    ll.print_list()

    ll.delete_nth_node(2)   # Valid
    ll.print_list()

    ll.delete_nth_node(5)   # Out of range
    ll.delete_nth_node(0)   # Invalid
    empty_ll = LinkedList()
    empty_ll.delete_nth_node(1)  # Empty list
