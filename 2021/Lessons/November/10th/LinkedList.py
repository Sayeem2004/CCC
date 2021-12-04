class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

    @property
    def value(self):
        return str(self.data);

class LinkList:
    def __init__(self):
        self.head = None;
        self.size = 0;

    def insert(self, data):
        new_node = Node(data);
        if self.head is None:
            self.head = new_node;
        else:
            current = self.head;
            while (current.next):
                current = current.next;
            current.next = new_node;
        self.size+=1;

    def __str__(self):
        result = [];
        current = self.head;
        while (current):
            result.append(current.value);
            current = current.next;
        return " -> ".join(result);

    def __len__(self):
            return self.size;

    def __getitem__(self, index):
        if self.size < index:
            return None;
        if index < 0:
            index = self.size + index;
        current = self.head;
        for i in range(index):
            current = current.next;
        return current.value;

    def removeAt(self, index):
        if self.size < index:
            return None;
        if index < 0:
            index = self.size + index;
        current = self.head;
        for i in range(index-1):
            current = current.next;
        temp = current.next;
        current.next = current.next.next;
        self.size -= 1;
        return temp;

if __name__ == "__main__":
    s = LinkList();
    s.insert(5);
    s.insert(7);
    s.insert(10);
    s.insert(9);
    print(s);
    print(len(s));
    print(s[1]);
    s.removeAt(2);
    print(s[2]);
