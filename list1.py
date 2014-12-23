#List-1

def first_last6(nums):
#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more. 
    for i in [nums[0],nums[-1]]:
        if i == 6:
            return True
    else:
        return False
#A shorter way to do this appears to be "return 6 in [nums[0],nums[-1]]"

def same_first_last(nums):
#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal. 
    if (len(nums)>=1) and ([nums[0]]==[nums[-1]]):
        return True
    else:
        return False

def make_pi():
#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}. 
   pi = 3,1,4
   return list(pi)
#This could also very easily just be "return [3,1,4]

def common_end(a, b):
#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more. 
    if ([a[0]] == [b[0]] or [a[-1]]==[b[-1]]) and (len(a)>=1 and len(b)>=1):
        return True
    else:
        return False
  
def sum3(nums):
#Given an array of ints length 3, return the sum of all the elements. 
    return nums[0]+nums[1]+nums[2]

def rotate_left3(nums):
#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}. 
    return [nums[1]]+[nums[2]]+[nums[0]]
  
  

    
