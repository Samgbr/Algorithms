
# coding: utf-8

# In[15]:


# Resolution Implementation on Conjunctive Normal Form (CNF)
# An input formula (in the form of f=C1^C2^C3^C4... in conjunctive normal form(CNF) and each Ci is a clause)
# The literals are represented using small letters
f="(aV~bVcV~dVy)^(~aVbVeVrV~h)^(~cVdV~eVhV~rV~y)" # Unsatisfiable
#f="(aV~bVcV~dVy)^(~aVbVeVrV~h)^(~cVdV~eVhV~r)" # Satisfiable
# Do Resolution on f by merging Ci and Ci+1 and remove literals that are same (a negation with the not negation) a,~a
def readFormula(f):
    indexList=[]
    for i in range(0,len(f)):
        if f[i]=="(" or f[i]==")":
            indexList.append(i)
    #print(indexList)
    print("Original CNF Formula")
    print(f)
    checkBraceErrors(indexList)
    checkANDBTWNClauses(indexList)
    checkORInsideClause(indexList)
    #Merge clauses (2-clauses at a time) in to one clause
    merformula = mergeClauses(indexList)
    print("Merged formula")
    print(merformula)
    #Remove same literals (a,~a), ~ represents the negation of a literal
    result=removeLiterals(merformula)
    print("Removing same literals with negations formula: Resolution")
    print(result)
    unsatisfiable(result)

# Unsatisiable check
def unsatisfiable(result):
    if len(result)<3:
        print("UNSATISFIABLE")

# Checks if braces are correct in f
def checkBraceErrors(indexList):
    if len(indexList)%2!=0:
        raise Exception("ERROR IN FORMULA")

# Check ^ is in between CNF clauses in f
def checkANDBTWNClauses(indexList):
    i=1
    while i<len(indexList)-1:
        if "^" not in f[indexList[i]+1]:
            raise Exception("ERROR IN FORMULA")
        i=i+2
    
# Check for clause errors 
def checkORInsideClause(indexList):
    c=0
    for i in range(0,len(indexList)-1):
        if (indexList[i+1]-indexList[i])>2:
            #Count the literals inside the clause
            j=indexList[i]+1
            k=indexList[i+1]
            literalCounter=0
            orCounter=0
            while j<k:
                if (f[j]>='a' or f[j]<='z') and f[j]!="~" and not f[j]=="V":
                    literalCounter=literalCounter+1
                if "V" in f[j]:
                    orCounter=orCounter+1
                j=j+1
            c=orCounter+1
            if c!=literalCounter:
                raise Exception("ERROR IN FORMULA")
                
# Merge the original clause in to one clause
def mergeClauses(indexList):
    g="("
    for i in range(0,len(indexList)-1):
        if (indexList[i+1]-indexList[i])>2:
            j=indexList[i]+1
            k=indexList[i+1]
            literalCounter=0
            orCounter=0
            while j<k:
                if (f[j]>='a' or f[j]<='z') and f[j]!="~" and not f[j]=="V":
                    g+=f[j]+"V"
                elif "~" in f[j]:
                    g+=f[j]
                j=j+1
    l=list(g)
    del l[len(l)-1]
    g="".join(l)
    g+=")"
    return g

# Remove same literals (b, ~b)
def removeLiterals(merformula):
    index=[]
    g=""
    for i in range(0,len(merformula)-1):
        if merformula[i]>='a' and merformula[i]<='z':
            for j in range(i+1,len(merformula)-1):
                if merformula[i]==merformula[j]:
                    if merformula[i-1]=="~" and merformula[j-1]!="~":
                        index.append(i)
                        index.append(i-1)
                        index.append(j)
                    elif merformula[j-1]=="~" and merformula[i-1]!="~":
                        index.append(i)
                        index.append(j)
                        index.append(j-1)                 
    index.sort()
    for k in range(0,len(merformula)):
        if k not in index:
            if merformula[k]>='a' and merformula[k]<='z':
                g+=merformula[k]+"V"
            elif merformula[k]=="(" or merformula[k]==")":
                g+=merformula[k]
    li=list(g)
    if li[1]!=')':
        del li[len(li)-2]
        g="".join(li)
    if len(g)>2:
        print("SATISFIABLE")
    return g

readFormula(f)

