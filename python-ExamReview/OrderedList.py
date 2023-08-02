from Node import *

class OrderedList:
    def __init__(self):
        self.head = None # a Node object

    def search(self, item): # returns the index of the item in the node list starting at 1; -1 if not found
        index = 1
        current = self.head
        while current != None:
            if current.getData() == item:
                return index
            index += 1
            current = current.getNext()
        return -1

    # def search(self, item):
    #     # searches and returns node with corresponding key
    #     current = self.head
    #     found = False
    #     stop = False
    #     found_node = None
    #     while (current is not None) and not found and not stop:
    #         if current.getData() == item:
    #             found = True
    #             found_node = current
    #         else:
    #             if current.getData() > item:
    #                 stop = True
    #             else:
    #                 current = current.getNext()
    #
    #     return found_node

    def add(self, item):
        # adds a node with key and data to the list
        current = self.head
        previous = None
        stop = False
        while (current is not None) and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    # def remove(self, item):
    #     index = self.search(item)     # returns the index the item is in the list
    #     if index == -1: return        # if the item doesnt exist: return
    #
    #     current = self.head           # current node becomes head
    #
    #     if index == 1:                # if the node to be removed is the head: make the head the next node and return
    #         self.head = current.getNext()
    #         return
    #
    #     while index > 2:              # move the current node to before the one to be removed
    #         current = current.getNext()
    #         index -= 1
    #
    #     current.setNext(None)
    #     current = current.getNext()   # current becomes the node to be removed
    #     after = current.getNext()     # after becomes the node after current (if there is one, None if not)
    #     while after is not None:
    #         current.setNext(after)    # previous sets the next node to that after the one to be removed
    #         current = after
    #         after = after.getNext()

    def remove(self, item):
        current = self.head
        previous = self.head
        if self.head == None: return               # if there is no ordered list do nothing
        if current.getData() == item:              # if you want to remove the head
            self.head = current.getNext()
            return
        while (current is not None):               # find the node and change its predecessor's link to its successor node
            if current.getData() == item:
                previous.setNext(current.getNext())
                return
            else:
                previous = current
                current = current.getNext()

    def reverseOrder(self):
        current = self.head
        previous = Node(current.getData())
        current = (current.getNext())
        while current is not None:
            next = current.getNext()
            current.setNext(previous)
            previous = current
            current = next

        self.head = previous





    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def __str__(self):
        print_list=""
        current = self.head
        while current is not None:
            node_print="[item:{}]".format(current.getData())
            print_list += node_print
            print_list += "->"
            current = current.next

        print_list +="None"

        return str(print_list)

# class OrderedList:
#     def __init__(self):
#         self.head = None
#
#     def insert(self, item, current=self.head):
#         if current is None:
#             self.head = Node(item)
#
#         elif item > current.getData():
#             if current.getNext() is not None:
#                 if current.getNext().getNext() is not None:
#                     if
#                 self.insert(item, current.getNet())
#             else:
#                 temp = Node(item)
#                 current.setNext(temp)
#         else:
#
#
#     def search(selfself, item):
#         if self.head is None:
#             return -1
#         elif item == self.head.getData():
#             return 0
#         else:
#             count = 1
#             current = self.head.getNext()
#             while current != None:
#                 if current.getData() == item:
#                     return count
#                 count += 1
#                 current = current.getNext()
#
#
#
#     def remove(self, item):
#         index = self.search(item)
#         if index == -1:
#             return
#         current = self.head
#         while index >= 0 and current is not None:
#             current.getNext()
#             index -= 1
