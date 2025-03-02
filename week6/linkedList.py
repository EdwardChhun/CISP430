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

    def __init__(self):
        """Create a linked list"""
        self._head = None
        self._count = 0

    def is_empty(self):
        """Is the list empty"""
        return self._head is None

    def size(self):
        """Size of the list"""
        return self._count

    def __len__(self):
        """Size of the list"""
        return self._count

    def __str__(self):
        """List as a string"""
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
        self._count = self._count + 1

    def append(self, value):
        curr=self._head
        new_node = Node(value)
        if curr is None:
            self._head=new_node
        else:
            while curr.next:
                curr=curr.next
            curr.next=new_node
        self._count += 1
        
    def remove(self, value): #Remove a node with a specific value
        current = self._head
        prev = None

        while current:
            if current.data == value:
                if prev is None:
                    self._head = current.next
                else:
                    prev.next = current.next
                self._count = self._count - 1
                return
            prev = current
            current = current.next
        raise ValueError(f"{value} is not in the list")

    def search(self, value): #Search for a node with a specific value
        current = self._head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

class CircularList(LinkedList):
    def __init__(self): #Create an Circular linked list"""
        LinkedList.__init__(self)
        self._tail=None

    def add(self, value): #Add a new node
        new_node = Node(value)
        new_node.set_next(self._head)
        self._head = new_node
        if self._count==0:
            self._tail=new_node
        else:
            self._tail.set_next(self._head)
        self._count = self._count + 1

    def __str__(self): #overload string operator
        cur=self._head
        outStr=""
        for i in range(self._count):
            outStr+=str(cur)+" "
            cur=cur.get_next()
        return outStr

def circular_linked_list_way(numElves):
    linkedList=CircularList()
    for i in range(numElves,0,-1):
        linkedList.add(i)
    #tail=linkedList._head
    #while tail.next:
    #    tail=tail.next
    print(linkedList)
    #tail.next=linkedList._head
    cur=linkedList._head
    safetyCnt=0
    while len(linkedList)>1:
        #cur.set_next(cur.get_next().get_next())
        cur.next=cur.next.next
        linkedList._count-=1
        cur=cur.next
    return cur.get_data()

if __name__=="__main__":
    my_list = LinkedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    my_list.append(19)
    print(my_list.size())
    print(my_list)
    #print(circular_linked_list_way(5))
    my_list = CircularList()
    print("my name")
    my_list.add(31)
    my_list.add(29)
    my_list.add(23)
    my_list.add(19)
    my_list.add(17)
    my_list.add(13)
    print(my_list.size())
    print(my_list)