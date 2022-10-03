def selectionSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    print("Selection sort is Completed..!")

def display(arr,n):
    for i in range(n):
        print(f"Index {i} -> {arr[i]}")

n=int(input("Enter the no. of elements: "))
arr=[]
for i in range(n):
    temp=int(input(f"Element {i+1} >> "))
    arr.append(temp)
selectionSort(arr)
display(arr,n)

