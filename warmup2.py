#Warmup-2

def string_times(str, n):
#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
    return str*n

def front_times(str, n):
#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
    front = str[:3]
    return front*n

def string_splosion(str):
#Given a non-empty string like "Code" return a string like "CCoCodCode".
word =""
   for i in range(len(str)):
       word= word+str[:i+1]
   return word
   #This one, I needed help with. My original code was longer than it needed to be

def last2(str):
#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring). 
    if len(str) <2:
        return 0

    str2 = str[-2:]
    count=0
    
    for i in range(len(str)-2):
        new = str[i:i+2]
        if new == str2:
            count+=1
    #This code did not yield the result I expected, and I still need to go back and work on it


def array_count9(nums):
#Given an array of ints, return the number of 9's in the array. 
    count = 0
    for i in nums:
       if i == 9:
           count+=1
    return count
  
def string_match(a, b):
#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings. 
   a_or_b = min(len(a),len(b))
   count = 0
   
   for i in range(a_or_b-1):
       new_a = a[i:i+2]
       new_b = b[i:i+2]
       if new_a == new_b:
           count+=1
   return count
#Some difficulty here at first too, but referring to previous exercises helped.
