def insertionSort(arr):
    for n, i in enumerate(arr[1:], 1):
        for nk, ik in enumerate(arr[:n]):
            if ik > i: 
                arr.insert(nk, arr.pop(n))
                break
        print('Round', n, arr)            

 
inp = list(map(int, input("Enter list for number: ").split(",")))
print("Before sort:", inp)
insertionSort(inp)
print("After sort:", inp)