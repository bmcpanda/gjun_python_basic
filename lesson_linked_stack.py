class StackNode:
    def __init__(self, value):
        self.value = value
        self.next_pointer = None


class LinkedStack:
    def __init__(self):
        self.top = None
        self.stack_size = 0
    
    def push(self, value):
        if self.top == None:
            self.top = StackNode(value)
        else:
            new_node = StackNode(value)
            new_node.next_pointer = self.top # 連結
            self.top = new_node
        self.stack_size += 1

    def pop(self):
        if self.top == None:
            return None
        else:
            node = self.top
            self.top = self.top.next_pointer
            self.stack_size -= 1
            return node.value

    def peek(self):
        if self.top == None:
            return None
        else:
            return self.top.value

    def size(self):
        # O(1)
        return self.stack_size
        

    def trace_overall(self):
        trace_node = self.top
        while trace_node:
            print(f"|{trace_node.value:4}|")
            trace_node = trace_node.next_pointer
        print("-" * 6)

class LinkedStackByList:
    def __init__(self):
        self.stack = list()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1] if len(self.stack) > 0 else None
    
    def size(self):
        return len(self.stack)
    
    def trace_overall(self):
        print(self.stack)

if __name__ == '__main__':
    linked_stack = LinkedStack()
    linked_stack.push(1)
    linked_stack.push(2)
    linked_stack.push(4)
    linked_stack.push(6)
    linked_stack.trace_overall()
    print("pop: ", linked_stack.pop())
    print("pop: ", linked_stack.pop())
    print("pop: ", linked_stack.pop())
    print("pop: ", linked_stack.pop())
    