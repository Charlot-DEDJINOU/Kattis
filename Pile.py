class Pile :

    def __init__(self) :
        self.items = []

    def push(self, item) :
        self.items.insert(0,item)

    def pop(self) :
        if self.items :
            head = self.items[0]
            return self.items.remove(head)
        
    def top(self) :
        if self.items :
            return self.items[0]
    
    def diplay(self) :
        print(*self.items)