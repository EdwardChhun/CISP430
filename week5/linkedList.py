class Node: #a node of a linked list

    def __init__(self, node_data): #create new node
        self._data = node_data
        self._next = None

    def get_data(self): #getter for data
        return self._data

    def set_data(self, node_data): #setter for data
        self._data = node_data

    data = property(get_data, set_data) #encapsulation for data
    
    def get_next(self): #getter for next
        return self._next

    def set_next(self, node_next): #setter for next
        self._next = node_next

    next = property(get_next, set_next) #encapsulation for next
    
    def __str__(self): #overloads string operator
        return str(self._data)


class LinkedList():
    """Linked List class implementation"""

    def __init__(self): #Create a linked list
        self._head = None
        self._count = 0

    def is_empty(self): #Is the list empty?
        return self._head is None

    def size(self): #Size of the list
        return self._count

    def __len__(self): #Size of the list
        return self._count

    def __str__(self): #List as a stringE
        list_str = "["
        current = self._head

        while current:
            list_str += str(current)
            if current.next:
                list_str += ", "
            current = current.next
        list_str += "]"
        return list_str

    def add(self, value): #Add a new node
        new_node = Node(value)
        new_node.set_next(self._head)
        self._head = new_node
        self._count += 1 

    def append(self, value):
        new_node = Node(value)
        if not self._head:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._count += 1
            
        
    def remove(self, value): #Remove a node with a specific value
        curr = self._head
        prev = None
        while curr:
            if curr.data == value:
                if prev is None:
                    self._head = curr.next
                else:
                    prev.next = curr.next
                self._count -= 1
                return
            prev = curr
            curr == curr.next
        raise ValueError(f"{value} is not in the list")

    def search(self, value): #Search for a node with a specific value
        curr = self._head
        while curr:
            if curr.data == value:
                return True
            curr = curr.next
        return False

class CircularList(LinkedList):
    def __init__(self): #Create an Circular linked list"""
        LinkedList.__init__(self)
        self._tail=None

    def add(self, value): #Add a new node
        new_node = Node(value)
        new_node.set_next(self._head)
        self._head = new_node
        
        #add code here to deal with the tail
        curr = self._head
        for _ in range(self._count):
            curr = curr.next
        self._tail = curr
        self._tail.next = self._head
        
        self._count = self._count + 1

    def __str__(self): #overload string operator
        cur=self._head
        list_str="["
        #you'll probably want to change the kind of loop
        for _ in range(self._count):
            list_str += str(cur)
            if cur.next and (cur.next != self._head):
                list_str += ", "
            cur = cur.next
        list_str += "]"
        return list_str


if __name__=="__main__":
    linkedlist = LinkedList()
    #add your LinkedList test code here
    linkedlist.add(17)
    linkedlist.add(38)
    linkedlist.append(77)
    linkedlist.search(38)
    linkedlist.remove(38)
    linkedlist.search(77)
    print(linkedlist)
    my_list = CircularList()
    print("Edward Chhun")
    my_list.add(31)
    my_list.add(29)
    my_list.add(23)
    my_list.add(19)
    my_list.add(17)
    my_list.add(13)
    print(my_list.size())
    print(my_list)