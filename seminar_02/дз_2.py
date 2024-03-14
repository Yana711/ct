import copy

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack():
    def __init__(self):
        self.head = Node("head")
     
    def __str__(self):
        cur = self.head.next
        out = ''
        sep = '→'
        while cur != None:
            out += f"{cur.value}{sep}"
            cur = cur.next
        out = out[:-1]
        return out    
        
        
    def push(self, value):
        new_element = Node(value)
        new_element.next = self.head.next
        self.head.next = new_element
        
        
    def pop(self):
        tmp = self.head.next.value
        self.head.next = self.head.next.next
        return tmp
        

class PersistentStack(Stack):
    def __init__(self):
        self.backups = []
        self.d=[]
        super().__init__()
        
    def backup(self, val):
        tmp = val
        self.backups.append(tmp)
        self.d.append(copy.copy(self.backups))
     

     
    def get_backup(self, i):
        return self.d[i]

        
    def push(self, value):
        self.backup(value)
        super().push(value)
        
    def pop(self, value):
        self.backup()
        return super().pop()
    

s=PersistentStack()
for i in range(5):
    s.push(i) 
print(f"Stack: {s}")  

print(f"Backups:")
for i in range(5):
    presi=s.get_backup(i)
    out = ''
    sep = '→'
    for i in range(0, len(presi)):
        out += f"{presi[i]}{sep}"
    out = out[:-1]
    print(out)
    

