def display(list):
    print(list)

def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    display(arr)

if __name__ == '__main__':
    lis1=[]
    a=int(input("Enter how many Numbers you want to add in list: "))
    for i in range(a):
        n=int(input(f"{i+1} >> "))
        lis1.append(n)
    insertionSort(lis1)
