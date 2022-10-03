class parent:
    a=0
    b=0
    c=0
    def __init__(self,a,b,c):
        self.a=a        
        self.b=b        
        self.c=c        
    def display(self):
        print(f'{self.a},{self.b},{self.c}')

a=parent(12,24,48)
a.display()