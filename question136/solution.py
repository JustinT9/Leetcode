# using bitwise xoR to solve the problem 

# xor of the same two bits return 0 
# xor of 0 and another number returns that number 
# the idea is to xor all of the bits to find a unique number 
# and use that number to return it 
def singleNumber2(self, nums):
    res = 0
    # traverse through nums to bitwise XOR them 
    for num in nums:
        res ^= num
    # returns unique number
    return res