class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def createLinkedList(self, arr):
        start = self.head
        n = len(arr)

        temp = start
        i = 0

        while(i < n):
            newNode = Node(arr[i])
            # the first node
            if i == 0:
                start = newNode
                temp = start
            # Not first node    
            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next   # always point to the last node
            i += 1

        self.head = start
        self.tail = temp
        

    def printList(self):
        temp = self.head
        linkedList = ""
        while (temp):
            linkedList += (str(temp.data)+ " ")
            temp = temp.next
            
        print(linkedList)

    def countList(self):
        temp = self.head
        count = 0
        while (temp is not None):
            temp = temp.next
            count += 1
        return count


    def insertAtLocation(self, vaule, index):
        temp = self.head
        count = self.countList()

        # index is 6, count is 5, vaild
        # index is 7, count is 5, invaild
        if count + 1 < index:
            return self.head
        
        newNode = Node(vaule)

        # if index is Head node
        if index == 1:
            newNode.next = temp    # original head(temp) become second
            temp.prev = newNode    # original head(temp).prev point to Head(newNode)
            self.head = newNode    # newNode become Head
            return self.head
        # if index is tail
        if index == count + 1:
            while(temp.next is not None):
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
            self.tail = newNode
            return self.head
        else:
            curr_index = 1
            while((curr_index + 1) != index):
                temp = temp.next
                curr_index += 1
            temp_next = temp.next

            temp.next = newNode
            newNode.prev = temp

            newNode.next = temp_next
            temp_next.prev = newNode

            return self.head
    
    def deleteAtLocation(self, index):
        temp = self.head
        count = self.countList()

        # index is out of bound
        if count < index:
            return self.head
        
        # delete Head node
        if index == 1:
            temp = temp.next
            self.head = temp
            return self.head

        # delete Tail node
        if index == count:
            # go to tail
            while(temp.next.next is not None):
                temp = temp.next
            temp.next = None
            self.tail = temp
            return self.head

        else:
            curr_index = 1
            while((curr_index + 1) != index):
                temp = temp.next
                curr_index += 1

            pre_node = temp
            delete_node = temp.next
            next_node = delete_node.next

            pre_node.next = next_node
            next_node.prev = pre_node

            return self.head

            








arr = [1,2,3,4,5,6]
DLlist = DoubleLinkedList()
DLlist.createLinkedList(arr)
DLlist.printList()
DLlist.insertAtLocation(9,2)
DLlist.printList()
DLlist.deleteAtLocation(2)
DLlist.printList()