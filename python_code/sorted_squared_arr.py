# Question

# You are given an array of Integers in which each subsequent value is not less than
#  the previous value. Write a function that takes this array as an input and returns a 
# new array with the squares of each number sorted in ascending order.


# You can solve this question in multiple ways.

# Think about the following -

# 1.What would be the brute force way of solving this question ? 
# What would be the Time and Space complexity of this approach?

# 2.Is there a better way to solve this with a more optimum Time complexity than 
# the Brute force way ? 

def sorted_squared(array):
    #write code here.make sure to return desired array
    squared_arr = []
    for element in array:
        squared_arr.append(element*element)
        
    sorted_array = sorted(squared_arr)
    return sorted_array
    
print(sorted_squared([-4,-2,0,1,2]))