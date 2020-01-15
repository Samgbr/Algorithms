
# coding: utf-8

# In[31]:


#IMC test
def solution(N, artifacts, searched):
    dict={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
    table = [[[] for i in range(N)] for j in range(N)]
    #print(table)
    putartifact(N,artifacts,table,dict)
    searchartifact(N,searched,table,dict)
    return table


def putartifact(N,artifacts,table,dict):
    mylist=[]
    charlist=[]
    numlist=[]
    adjlist = artifacts.split(',')
    #print(adjlist)
    for i in range(len(adjlist)):
        mylist.append(adjlist[i].split())
    #print(mylist)
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            str=mylist[i][j]
            ch=str[-1:]
            charlist.append(ch)
            ch=str[:-1]
            numlist.append(int(ch)-1)
    for i in range(len(charlist)):
        table[numlist[i]][dict[charlist[i]]]=1
    print(table)

def searchartifact(N,searched,table,dict):
    srchlist=[]
    charlist=[]
    numlist=[]
    srchlist = searched.split()
    #print(srchlist)
    for i in range(len(srchlist)):
        str1=srchlist[i]
        cr=str1[-1:]
        charlist.append(cr)
        cr=str1[:-1]
        numlist.append(int(cr)-1)
    for i in range(len(charlist)):
        if table[numlist[i]][dict[charlist[i]]]==1:
            #print("found")
            table[numlist[i]][dict[charlist[i]]]="X"
        else: table[numlist[i]][dict[charlist[i]]]=0
    #print(table)
        
    
solution(4,"1B 2C,2D 4D","2B 2D 3D 4D 4A")


# In[32]:


# Binary Gap
def solution(N):
    str=""
    max=0
    str=bin(N)
    print(str)
    arr=[]
    for i in range(len(str)):
        if str[i] == "1":
            arr.append(i)
    print(arr)
    for i in range(len(arr)-1):
        diff = arr[i+1]-arr[i]
        print(diff)
        if diff > 1 and diff-1 > max:
            max=diff-1
    return max

solution(647)

