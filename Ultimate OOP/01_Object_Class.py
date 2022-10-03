class parent:
    def display(self,val):
        print('Display method of class parent')
        print(f'Value in Display -> {val}')

p1=parent()
p2=parent()

parent.display(p1,100)
parent.display(p2,200)

p1.display(300)
p1.display(400)

# a=4
# print(a.bit_length())