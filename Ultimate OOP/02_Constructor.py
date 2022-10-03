class parent:
    def __init__(self,val1,val2):
        self.value1=val1
        self.value2=val2

    def sum(self):
        return f'Sum = {self.value1+self.value2}'

p1=parent(10,20)
print(p1.sum())