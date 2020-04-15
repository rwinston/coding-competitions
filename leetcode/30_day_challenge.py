# Day 15
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1]*len(nums)
        r = [1]*len(nums)
        q = [1]*len(nums)
        for i in range(len(nums)):
            p[i] = 1 if i==0 else nums[i-1]*p[i-1]
            r[i] = 1 if i==0 else nums[len(nums)-i]*r[i-1]
        
        for i in range(len(nums)):
            q[i] = r[len(nums)-(i+1)]*p[i]
            
        return(q)
        
 
 # Day 14
 class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        tmp=s
        for st in shift:
            i=st[0]
            if i==0:# left
                sh = st[1] % (len(s))
                tmp=tmp[sh:]+tmp[:sh]
            elif i==1:
                sh = st[1] % (len(s))
                tmp=tmp[-sh:]+tmp[:-sh]
        return(tmp)

# Day 13
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=[None]*(2*len(nums)+1)
        nums = [b if b==1 else -1 for b in nums]
        count=0
        maxrun=0
        for i,num in enumerate(nums):
            count=count+num
            if count==0:
                maxrun=max(i+1,maxrun)
            elif n[count] is None:
                n[count]=i
            else:
                maxrun=max(maxrun,i-n[count])
        return(maxrun)
                
# Day 12
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones = sorted(stones)
            rem = stones[-1]-stones[-2]
            stones = stones[:-2]
            if rem > 0:
                stones.append(rem)
            
        return(stones[0] if len(stones)>0 else 0)

# Day 11

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left = self.maxpath(root.left)
        right = self.maxpath(root.right)

        ldia = self.diameterOfBinaryTree(root.left)
        rdia = self.diameterOfBinaryTree(root.right)


        return max(left+right, max(ldia, rdia))
        
    def maxpath(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return 1+max(self.maxpath(node.left),self.maxpath(node.right))
   
# Day 10
class MinStack:
   
    def __init__(self):
    head = tail = 0
    stack = [None]*10000    

    def push(self, x: int) -> None:
        self.stack[self.tail]=x
        self.tail=self.tail+1

    def pop(self) -> None:
        item = self.stack[self.tail]
        self.tail=self.tail-1
        return(item)
        

    def top(self) -> int:
        return(self.stack[self.tail-1])

    def getMin(self) -> int:
        #print('stack=%s,head=%s,tail=%s' % (self.stack, self.head, self.tail))
        m = self.stack[self.head]
        for x in range(self.head,self.tail):
            if self.stack[x] < m:
                m = self.stack[x]
        return(m)

# Day 9
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return (self.f(S)==self.f(T))
    
    def f(self, S : str) -> str:
        out = [None]*200
        i = 0
        for char in S:
            if char=='#':
                i=max(i-1,0)
            else:
                out[i]=char
                i=i+1
        return ''.join(out[:i])

# Day 8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        i=0
        nodes=[]
        while ptr is not None:
            nodes.append(ptr)
            ptr=ptr.next
            i=i+1
        
        return(nodes[int(i/2.0)])
        
        
# Day 7
class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        i = 0
        for num in arr:
            if (num+1) in s:
                i=i+1
        return(i)
        
# Day 6
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            s = ''.join(sorted(word))
            anagrams[s].append(word)
        return anagrams.values()
        
# Day 5
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
               return sum(max(prices[i]-prices[i-1], 0) for i in range(1, len(prices)))

# Day 4
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i,num in enumerate(nums):
            if (num==0):
                for j in range(i+1,len(nums)):
                    if (nums[j]!=0):
                        tmp=nums[i]
                        nums[i]=nums[j]
                        nums[j]=tmp
                        break
                        
# Day 3
class Solution(object):
   def isHappy(self,n):
       i = 1
       num = n
       while i < 100:
            digits = [int(x) for x in str(num)]
            num = sum([x**2 for x in digits])
            if (num==1):
                return(True)
            i=i+1
       return(False)
        

# Day 2
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = set()
        for num in nums:
            if num in m:            
                m.remove(num)
            else:
                m.add(num)
        return m.pop()
                
# Day 1
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        def max_subarray(numbers):
        best_sum = 0  # or: float('-inf')
        """
        
        best_sum = float('-inf')
        current_sum = 0
        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum
        

        


