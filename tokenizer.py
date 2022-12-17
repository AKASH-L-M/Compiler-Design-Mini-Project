import re
output = []
def isValidDelimiter(ch):
    if( ch == ' ' or ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == ',' or ch == ';' or ch == '>' or ch == '<' or ch == '=' or ch == '(' or ch == ')' or ch == '[' or ch == ']'):
        return True
    else:
        return False
    
def isValidOperator(ch):
    if(ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '>' or ch == '<' or ch == '='):
        return True
    else:
        return False
    """regex = '^[+-/\*><=]$()\{\}[]'
    print(str)
    if(re.search(regex, str)):
        return True
    else:
        return False"""
    
def isvalidIdentifier(str):
    """if(str[0] == '0' or str[0] == '1' or str[0] == '2' or str[0] == '3' or str[0] == '4' or str[0] == '5' or str[0] == '6' or str[0] == '7' or str[0] == '8' or str[0] == '9' or isValidDelimiter(str[0]) == True):
        return False
    else:
        return True"""
    regex = '^[A-Za-z_][A-Za-z0-9_]*'
    if(re.search(regex, str)):
        return True
    else:
        return False

def isValidKeyword(str):
    lst = ["if", "else", "while", "break", "begin", "end", "printf", "int", "main"]
    if str in lst:
        return True
    else:
        return False

def isValidInteger(str):
    return bool(re.search(r"^\d+$", str))

def isRealNumber(str):
    return bool(re.search(r"^\d+\.\d+$", str))

def isRealNumber(str):
    return bool(re.search(r"^\d+\.\d+$", str))

def takeSub(str, left, right):
    return str[left:right]
    """print(str)
    lst = list(str)
    newlst = []
    for i in range(left, right+1):
        newlst.append(lst[i])
    #sub[right-left+1] = '\0'
    return str(lst)"""

def detectTokens(str):
    left = 0
    right = 0
    length = len(str)
    
    # print(length)
    try:
        while (right<= length and left <= right):
            #print(left)
            if isValidDelimiter(str[right])==False :
                right=right+1
                
            if (isValidDelimiter(str[right])==True and left == right):
                if (isValidOperator(str[right]) ==True):
                    print(("|     Operator : "+ '\t'+ sub + '\t' + "|").expandtabs(10))
                    output.append(str[right])
                if str[right]==")" or str[right]=="(" or str[right] == '+' or str[right] == '-' or str[right] == '*' or str[right] == '/' or str[right] == ',' or str[right] == ';':
                   # print("Here ", str[right])
                    output.append(str[right])
                right=right+1
                left = right
            elif (isValidDelimiter(str[right]) == True and left != right or (right == length and left != right)):
                sub =  takeSub(str, left, right)
                # print("sub",sub)
                # right=right+1
                if isValidKeyword(sub)==True:
                    print(("|     Keyword :"+ '\t'+ sub + '\t' + "|").expandtabs(10))
                    output.append(sub)
                elif isValidInteger(sub) == True:
                    print(("|     Integer :"+ '\t'+ sub + '\t' + "|").expandtabs(10))
                    output.append(sub)
                elif (isRealNumber(sub) == True):
                    print(("|     Real Number : "+ '\t'+ sub + '\t' + "|").expandtabs(10))
                    output.append(sub)
                elif (isvalidIdentifier(sub) == True and isValidDelimiter(str[right - 1]) == False):
                    print(("|     Identifier : "+ '\t'+ sub + '\t' + "|").expandtabs(10))
                    for i in range(len(sub)):
                        output.append(sub[i])
                elif (isvalidIdentifier(sub) == False and isValidDelimiter(str[right - 1]) == False):
                    print(("Invalid Identifier : "+ '\t'+ sub + '\t' + "|").expandtabs(10))
                    output.append(sub)
                left = right
                
            
    except:
        print(("|     keyword : "+ '\t'+ "end" + '\t' + "|").expandtabs(10))
        output.append("end")
        
f  = open("InputProg.txt", "r")   
str = f.readline()

print("\n\n````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
print("CODE : ", str)
print("````````````````````````````````````````````````````````````````````````````````````````````````````````````````")

print("All Tokens are :")
try:
    detectTokens(str)
except :
    pass

def listToString(instr):
    emptystr=""
    for ele in instr:
        emptystr += ele
        emptystr += " "
    return emptystr

temp =listToString(output)

print("````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
print(listToString(output))
print("````````````````````````````````````````````````````````````````````````````````````````````````````````````````")

f2 = open("intermediate.txt", "w")
f2.write(temp)
                