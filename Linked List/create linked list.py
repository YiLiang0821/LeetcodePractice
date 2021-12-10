#Can not random access, only sequential access(head->tail)
# Ref: https://lovedrinkcafe.com/python-single-linked-list/
#create node, data for info; next point to next node
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        return


# start linked list 
class SingalLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        

    # insert the data to the specific index
    def insert(self, index, data):
        if self.head == None:
            print('empty list')
        if not (1 <= index <= len(self)):
            print('{0} is out of range'.index)
        elif index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            # start from head
            cur_index = 1 
            new_node = Node(data)
            current_node = self.head
            while (cur_index + 1) != index :
                current_node = current_node.next
                cur_index += 1
            new_node.next = current_node.next
            current_node.next = new_node
        return
            


    # append on last
    def append(self, data):
        new_node = Node(data)

        # link list is empty new node is the first node
        if self.head == None :
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    
    # delete from tail
    def deleteNode(self):
        if self.head == None:
            return print('empty list')
        else:
            if self.head == self.tail: #only one node
                self.head = None
                self.tail = None
            else:
                current = self.head #從頭(current)走到最後
                while current.next != None:
                    self.tail = current #把tail 跟著current node走
                    current = current.next
                self.tail.next = None #找到最後一個點(self.tail.next)的前一個點(current = self.tail)
        return        


    def delete_by_index(self, index):
        if self.head == None:
            print('This is empty list, no need to delete')
        # one node only
        if index == 1 and len(self) == 1:
            self.head = None
            self.tail = None
        # delete head
        elif index == 1 and len(self) > 1 :
            self.head = self.head.next
        elif index > 1 and index < len(self):
            cur_index = 1
            cur_node = self.head
            while cur_index +1 != index:
                prev_node = cur_node
                cur_node = cur_node.next
                cur_index += 1
            prev_node.next = cur_node.next
        #last node
        elif index == len(self):
            cur_index = 1
            cur_node = self.head
            while cur_index +1 != index:
                prev_node = cur_node
                cur_node = cur_node.next
                cur_index += 1
            prev_node.next = None
            self.tail = prev_node
        else:
            print('index: {0} is out of range')



    def reverse(self):
        prev = None
        while self.head:
            current = self.head         #從頭開始
            self.head = self.head.next
            current.next = prev
            prev = current
        self.head = current
        self.tail = self.head
        return

    def print_nodes(self):
        if not self.head:
            print(self.head)
        node = self.head
        while node:
            end = "->" if node.next else "\n"
            print(node.data, end=end)
            node = node.next
    

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node != None:
            length += 1
            current_node = current_node.next
        return length


# instance of linked list            
l = SingalLinkedList()
l.append(10)
l.append(20)
l.append(30)
l.insert(2,5)
l.append(40)
l.deleteNode()
l.print_nodes()
l.append(50)
l.delete_by_index(2)
l.print_nodes()
#l.deleteNode()
#l.print_nodes()
#l.reverse()
#l.print_nodes()


