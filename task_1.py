class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def from_list(self, values):
        self.head = None
        for value in values:
            self.append(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev


def insertion_sort_linked_list(linked_list):
    if not linked_list.head or not linked_list.head.next:
        return

    sorted_list = ListNode(0)  
    current = linked_list.head

    while current:
        prev_node = sorted_list
        next_node = sorted_list.next

        while next_node:
            if next_node.value > current.value:
                break
            prev_node = next_node
            next_node = next_node.next

        temp = current.next
        current.next = next_node
        prev_node.next = current
        current = temp

    linked_list.head = sorted_list.next


def merge_sorted_linked_lists(list1, list2):
    dummy = ListNode(0)
    tail = dummy

    l1 = list1.head
    l2 = list2.head

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list



list1 = LinkedList()
list1.from_list([4, 2, 1])
list2 = LinkedList()
list2.from_list([5, 3, 2])


reverse_linked_list(list1)
print("Реверсований список:")
list1.print_list()


insertion_sort_linked_list(list1)
print("Відсортований список:")
list1.print_list()


sorted_list1 = LinkedList()
sorted_list1.from_list([1, 2, 4])
sorted_list2 = LinkedList()
sorted_list2.from_list([2, 3, 5])

merged_list = merge_sorted_linked_lists(sorted_list1, sorted_list2)
print("Об'єднаний відсортований список:")
merged_list.print_list()

