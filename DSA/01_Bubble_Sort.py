def display(list):
    print(list)

def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if(arr[j]>=arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    display(arr)

if __name__ == '__main__':
    lis1=[]
    a=int(input("Enter how many Numbers you want to add in list: "))
    for i in range(a):
        n=int(input(f"{i+1} >> "))
        lis1.append(n)
    bubbleSort(lis1)