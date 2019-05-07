
# coding: utf-8

# In[29]:


import math
# K-Way Merge Sort Algorithm (Iterative merge)

# Input array to be sorted
numbersToBeSorted = [10,20,45,899,1,2,4567,85,967,123,12,15,17,1,6,967,44,78988,444,23,459,8,7,65,18]

def kWayMergeSort(numbersToBeSorted):
    # If the length of the array is 1, SORTED
    sortLen1(numbersToBeSorted)
    print("Original List of numbers before Merge Sort:")
    print(numbersToBeSorted)
    # Split the array in to k-arrays
    k=10
    print("K value: ")
    print(k)
    n=len(numbersToBeSorted)
    numOfArrays=n/k
    y=math.ceil(numOfArrays)
    #print(y)
    # Create y arrays of size k
    kArray = [[[] for i in range(k)] for j in range(y)]
    #print(kArray) # Before insert
    putValuesIntoKArray(kArray,y)
    # Print k-array
    printAfterkArraySplit(kArray,y)
    #Sort each k-array
    sortEachkArray(kArray,y,n)
    # Using Iterative merge, merge k-arrays in to one big array and 2-way sort
    sArray=iterativeMerge2way(kArray,n,k)
    print("Sorted list:")
    print(sArray)

def printAfterkArraySplit(kArray,y):
    print("K-Arrays before sort: ")
    i=0
    while i<y:
        print(kArray[i])
        i=i+1
    
def sortEachkArray(kArray,y,n):
    print("Sorting k-Arrays using quicksort: ")
    h=0
    while h<y:
        k=0
        for i in kArray[h]:
            if type(i) is int:
                k=k+1
        # Quicksort algorithm 
        quickSort(kArray[h],0,k-1)
        print(kArray[h])
        h=h+1
        
def partition(arr, low, high):
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
    for j in range(low , high): 
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
            # increment index of smaller element 
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )

def quickSort(arr, low, high):
    if low < high: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)
    
def iterativeMerge2way(kArray,n,k):
    print("Iterative merging on the sorted arrays 2-way sort:")
    sortedArray = [[] for i in range(n)]
    l=0
    for i in range(0,len(kArray)):
        for j in range(0,len(kArray[i])):
            if type(kArray[i][j]) is int:
                sortedArray[l]=kArray[i][j]
                l=l+1
        if i>0:
            print("Details...Iterative Merging... before sort: ")
            print(sortedArray)
            quickSort(sortedArray,0,l-1)
            print("After merged sort:")
            print(sortedArray)
    return sortedArray


def putValuesIntoKArray(kArray,y):
    # Store the array values in to the k-array
    v=0
    i=0
    while(i<len(numbersToBeSorted)):
        # stored it k-times and the last one the remaining elements
        if v!=y:
            for j in range(0,len(kArray[v])):
                if i!=len(numbersToBeSorted):
                    kArray[v][j]=numbersToBeSorted[i]
                    i=i+1
            v=v+1
    return kArray

def sortLen1(numbersToBeSorted):
    # If the length of the array is 1, SORTED
    if len(numbersToBeSorted)==1:
        print("Already Sorted!")
        print(numbersToBeSorted)

kWayMergeSort(numbersToBeSorted)

