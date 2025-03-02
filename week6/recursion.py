import linkedList
from linkedList import Node

def write(linkedList):
    print("List :",end=' ')
    writeSub(linkedList._head);
    print("")

def writeSub (node):
    if (node is not None):
        writeSub(node.next)
        print(node.data,end='')


def insertEnd (linkedList,newDataItem):
    insertEndSub(linkedList._head,newDataItem)

def insertEndSub (node,newDataItem):
    if (node.next is not None):
       insertEndSub(node.next,newDataItem);    # Continue searching for
    else:                                      # end of list
       newNode = linkedList.Node(newDataItem)   # Create new node
       node.next=newNode                        # Add to end of list
       
def aAfterb(linkedList):
    aAfterbSub(linkedList._head)

def aAfterbSub(node):#this is the recursive function
    if node is None:
        return
    
    if (node._data == "b"):
        # Insert an "a" after "b"
        new_node = Node("a")
        new_node.next = node.next 
        node.next = new_node
        aAfterbSub(new_node.next)
    else:
        aAfterbSub(node.next)

if __name__=="__main__":
    #part 1:
    my_list = linkedList.LinkedList()
    my_list.add('c')
    my_list.add('b')
    my_list.add('a')
    write(my_list)
    insertEnd(my_list,'!')
    write(my_list)
    #part 2:
    text=input("Enter a list of characters:")
    testList=linkedList.LinkedList()
    for ch in text:
        testList.append(ch)
    write(testList)
    insertEnd(testList,'?')
    write(testList)
    aAfterb(testList)
    print(testList)