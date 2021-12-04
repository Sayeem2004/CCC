class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

    @property
    def value(self):
        return str(self.data);

class Stack:
    def __init__(self):
        self.head = None;
        self.size = 0;

    def push(self, value):
        new_node = Node(value);
        new_node.next = self.head;
        self.head = new_node;
        self.size+=1;

    def pop(self):
        if self.size == 0:
            return None;
        else:
            temp = self.head.value;
            self.head = self.head.next;
            return temp;

    def __str__(self):
        result = [];
        current = self.head;
        while (current):
            result.append(current.value);
            current = current.next;
        return " -> ".join(result);

if __name__ == "__main__":
    s = Stack();
    for i in range(10):
        s.push(i);
    print(s);
    print(s.pop());
    print(s);
    s.push(17);
    print(s);
