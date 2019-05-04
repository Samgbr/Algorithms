
# coding: utf-8
# W is the input string as stated on Problem 3.12 and % is the blank symbol
w = "#10#3#80#4#13%"
print("Input String w: " + w)
def ElementDistinctProblem( w ):
    str = w
	
	# 1 step - check if len(w) is one and only has blank symbol, ACCEPT
    if len(w)==1 and '%' in w:
        return "ACCEPT"	
		
    # Check if w last string is not % blank string REJECT
    if '%' not in w[-1]:
        return "REJECT"
    # Check if there exists # before % REJECT
    if '#' in w[-2]:
        return "REJECT"    
    # Remove the blank string before split
    if '%' in str[-1]:
        str = str[:-1]
    # Put w Xi values to a list to compare values later
    wlist = str.split('#')
    # Remove the first empty string while split is done
    wlist.pop(0)
    # print(wlist)
    # Count the number of # in w to do step 2-4
    hashcounter=0
    for x in w:
        if '#' in x:
            hashcounter += 1
    # print(hashcounter)
    # print(len(wlist))
    # Check if w is not in proper format REJECT
    if hashcounter != len(wlist):
        return "REJECT"
    
    # 2 Step - if next symbol is # move to the right otherwise REJECT
    if '#' not in w[:1]:
        return "REJECT"
    # Move to the right next # not present before % ACCEPT
    if hashcounter == 1:
        return "ACCEPT"
    # Step 3 and 4 - By Zig-zag compare the two strings, and no # mark is before % then all strings have been compared and ACCEPT 
    # If they are equal REJECT 
    for i in range(len(wlist)):
        j=i+1
        while j < len(wlist):
            if wlist[i] == wlist[j]:
                return "REJECT"
            j=j+1
    return "ACCEPT"
print(ElementDistinctProblem(w))

