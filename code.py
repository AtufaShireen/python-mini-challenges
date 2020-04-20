# --------------

def palindrome(num):
    if num<9:
        return num+1
    elif num==9:
        return num+2
    x=[int(i) for i in str(num)]     
    mid=(len(x)//2)-1   
    if len(x)%2==0:
        if x[mid]>=x[mid+1]:
            x[mid+1:]=x[mid::-1]
            return int(''.join(str(p) for p in x))
        else:
            x[mid]+=1
            x[mid+1:]=x[mid::-1]
            return int(''.join(str(p) for p in x))

    elif len(x)%2!=0:
        mid=len(x)//2
        if x[mid-1]>=x[mid+1]:
            x[mid+1:]=x[mid-1::-1]
            return int(''.join(str(p) for p in x))
        else:
            x[mid]+=1
            x[mid+1:]=x[mid-1::-1]
            return (int(''.join(str(p) for p in x)))
print(palindrome(8))


# --------------
def a_scramble(str_1,str_2):
  str_1=str_1.replace(" ","").lower()
  str_2=str_2.replace(" ","").lower()
  x=list(str_1)
  y=list(str_2)
  for i in y:
    if i not in x:
      return False
    else:
      x.remove(i)
  return True
  


# --------------
# python program to check if x is a perfect square 
import math 
  
# A utility function that returns true if x is perfect square 
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibinacci Number, else false 
def check_fib(num): 
  
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return isPerfectSquare(5*num*num + 4) or isPerfectSquare(5*num*num - 4)


# --------------
import itertools as it
def compress(word):
    o=''
    for k,g in it.groupby(word.lower()):
        o+=k+str(len(list(g)))
    return o


# --------------
#Code starts here
def k_distinct(string,k):
    p=set(string.lower())
    print(p)
    if len(p)==k:
        return True
    else:
        return False


