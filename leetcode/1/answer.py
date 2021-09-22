class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        iterator = 0
        setnum = []
        temp = []
        zero = False
        for i in range (len(nums)):
            #print(nums[i])
            #print(temp)
            #print(setnum)
            if(nums[i]==1 and zero==False):
                temp.append(nums[i])
                #print(str(i) + " nums[i]==1 and zero==False")
            elif(nums[i]==1 and zero==True):
                zero = False
                temp = []
                temp.append(nums[i])
                #print(str(i) + " nums[i]==1 and zero==True")
            elif(nums[i]==0 and zero==False):
                zero = True
                setnum.append(len(temp))
                #print(str(i) + " nums[i]==0 and zero==False")
            else:
                #print(str(i) + " nums[i]==0 and zero==True")
                continue
        setnum.append(len(temp))
        return max(setnum)