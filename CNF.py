
# coding: utf-8

# In[74]:


# This CKY Algorithm uses dynamic programming using tabulation and data filled from bottom up
w = "baaba" # Input string for the first grammar
#w="abababa" # Input string for palindrome
# Let us give the grammar in CNF and store it in a dictionary

# Tested and works

# The most common grammar for testing cnf
grammar = {
    "S": ["AB","BC"],
    "A": ["BA","a"],
    "B": ["CC","b"],
    "C": ["AB","a"]
}
'''
# Palindrome grammar
grammar= {
    "S": ["AA","BB","a","b","AT"],
    "U": ["AT","BW","AA","BB","a","b"],
    "T": ["UA"],
    "W": ["UB"],
    "A": ["a"],
    "B": ["b"]
}

# Balanced Parenthesis grammar
w="()()"  # Input string for balanced parenthesis
grammar = {
    "S":["SC","LA","LR"],
    "C":["LR","LA"],
    "A":["SR"],
    "L":["("],
    "R":[")"]
}
'''
def parser(grammar, w):
    #Empty grammar S->e
    if len(grammar)==1 and grammar[rule] == "S" and rule == "e":
            return "ACCEPT"
    printGrammar(grammar)
    print("Input String")
    print(w)
    print("Derivations list on each level")
    cky(grammar, list(w))

def printGrammar(grammar):
    print("A Grammar in Chomsky Normal Form to be Tested: ")
    for rule in grammar:
        str1=""
        for rhsRule in grammar[rule]:
            str1+=rhsRule+"|"
        str1=str1[:-1]
        print(rule + "->" + str1)

def cky(grammar, input):
    n = len(input)
    table = [[[] for i in range(n)] for j in range(n)]
    
    print("Level0 table fill: ")
    level0Fill(grammar,n,input,table)
    
    level1Fill(grammar,n,table)
    
    level2AndAboveFill(grammar,n,table)
    print("Cky Table:")
    print(table)
    scheck=list(table[0][0])
    if "S" in scheck:
        print("ACCEPT")

def level0Fill(grammar,n,input,table):
    # Check for length 1 and the time complexity is O(n^2)
    i=0
    j=0
    temp=""
    str=""
    visited=False
    for value in input:
        for rule in grammar:
            if value in grammar[rule]:
                if visited:
                    temp=str
                str=rule
                visited=True
        table[n-1][j]=temp+str
        str=""
        temp=""
        j=j+1
    print(table[n-1])

def level1Fill(grammar,n,table):
    # Check for length 2 and time complexity is O(n^3) = O(n) * O(n^2) from cartesianProductionsAndResult
    k=0
    x=0
    w=0
    strlen=2
    strArr=[]
    # O(n) loop mentioned above
    for r in range(n-1):
        x=0
        strArr=[]
        while x < strlen:
            strArr.append(table[n-1][r+x])
            x=x+1
        result = cartesianProductionsAndResult(strArr, grammar,w,table,n)
        table[n-2][w]=result
        #print(result)
        w=w+1
    print("Level1 table fill:")
    print(table[n-2])

def level2AndAboveFill(grammar,n,table):
    # Check for length 3 and above.
    l=2
    y=n-1
    f=0
    x=0
    while l<=y:
        #print(l)
        k=l
        j=0
        rlist=[]
        cartProd1=[]
        #loop here for length change
        while k<n:
            i=n-l
            c=n-1
            r=k
            result1=""
            while i<n:
                cartProd1.append(table[i][j])
                cartProd1.append(table[c][r])
                result1 = cartesianProductionsAndResult(cartProd1,grammar,w,table,n)
                #print(cartProd1)
                rlist.append(result1)
                i=i+1
                c=c-1
                r=r-1
                cartProd1.clear()
            k=k+1
            j=j+1
            #print(rlist)
            if l==2:
                str2 = commonDervationFilter(rlist,l)
                insertTableLevel2(table,str2,l,x,n)
                x=x+1
            if l>=3:
                str = commonDervationFilter(rlist,l)
                insert(table,str,l,f,n)
                f=f+1
                #print(str)
            rlist.clear()
        l=l+1 
        f=0

def insert(table,str,l,f,n):
    table[n-l-1][f]=str

# Concatenate the result and remove duplicates
def commonDervationFilter(rlist,l):
    st=""
    ct=""
    g=0
    a=[]
    while g<len(rlist):
        st=""
        h=0
        while h<l:
            st+=rlist[g]
            g=g+1
            h=h+1
        a.append(st)
        #print(a)
    for rule in grammar:
        for ii in a:
            if rule in ii:
                ct+=rule
    #print(ct)
    return ct

# Time Complexity is O(n^2)
def cartesianProductionsAndResult(arr, grammar,w,table,n):
    concatseplist=[]
    cprod=[]
    sRule=""
    seplist=[]
    first=False
    second=False  
    # The two array values are only one letter rule, add to a list for cartesian product before check on the grammar  
    if len(arr[0])==1 and len(arr[1])==1:
        cprod.append(arr[0]+arr[1])
    elif len(arr[0])>2:
        #print("First rule has morethan one variable")
        arList=[]
        seplist=list(arr[0])
        for i in seplist:
            concatseplist.append(i) 
        if len(arr[1])>1:
            arrList=list(arr[1])
            for i in arrList:
                for j in concatseplist:
                    cprod.append(i+j)               
        elif len(arr[1])==1:
            z=arr[1]
            for i in concatseplist:
                cprod.append(z+i)
        #print(arr)
    elif len(arr[1])>2:
        arrList=[]
        #print("Second rule has morethan one variable")
        seplist=list(arr[1])
        for i in seplist:
            concatseplist.append(i) 
        if len(arr[0])>1:
            arrList=list(arr[0])
            for i in arrList:
                for j in concatseplist:
                    cprod.append(i+j)
        elif len(arr[0])==1:
            s=arr[0]
            for i in concatseplist:
                cprod.append(s+i)
        #print(cprod)
    # If the letter rules are are in the form (BC,B) or (B,BC) do cartesian product
    if len(arr[0])==1:
        first=True
    elif len(arr[1])==1:
        second=True
    for c in arr:
        if len(c)==1:
            sRule=c
        elif len(c)==2:
            seplist=list(c)
            concatseplist.append(seplist[0])
            concatseplist.append(seplist[1])            
    if len(concatseplist)==2:
        for v in concatseplist:
            if second == True:
                cprod.append((v+sRule).strip())
            else:
                #print(sRule)
                if "S" in v:
                    cprod.append((v+sRule).strip())
                else:
                    cprod.append((sRule+v).strip())
    elif len(concatseplist)==4:
        for e in range(0,2):
            for c in range(2,len(concatseplist)):
                cprod.append(concatseplist[e]+concatseplist[c])
    #print(cprod)
    # Check if all derivations exist or not
    t=0
    found=""
    for cp in cprod:
        for rule in grammar:
            if cp in grammar[rule]:
                found+=rule
    #print(found)
    return found

# Time Complexity is O(n)
def insertTableLevel2(table,str2,p,x,n):
    table[n-(p+1)][x]=str2
        
parser(grammar, w)

