from QueueByTwoStacks import  Queue2Stacks
from SinglyLinkedList.SinglyLinkedList import *
from SinglyLinkedList.Node import *
from DoublyLinkedList.DoublyLinkedList import *
from DoublyLinkedList.DoublyLinkedListNode import *
def main():
########## testing single linked list
    single_linked_list=SingleyLinkedList(Node(1))
    single_linked_list.add_node(Node(2))
    single_linked_list.add_node(Node(3))
    single_linked_list.add_node(Node(4))
   # single_linked_list.print()
   # print(single_linked_list.tail.get_value())
   # print(single_linked_list.cycle_check())
   # single_linked_list.tail.next_node=single_linked_list.tail
   # print(single_linked_list.cycle_check())
   # single_linked_list.reverse_list()
    #single_linked_list.print()
    print(single_linked_list.nth_to_last_node(1))
    single_linked_list.print()
    print(single_linked_list.nth_to_last_node(3))

###########

########### testing double linked list
  # double_linked_list=DoublyLinkedList(DoublyLinkedListNode(1))
  # double_linked_list.add_node(DoublyLinkedListNode(2))
  # double_linked_list.add_node(DoublyLinkedListNode(3))
  # print(double_linked_list.tail.prev_node.prev_node.get_value())
###########
if __name__ == '__main__':
    main()