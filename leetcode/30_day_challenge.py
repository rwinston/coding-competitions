# May 11
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
            visited = {}
            def paint(i,j,color):
                image[i][j]=newColor
                if (i,j) in visited:
                    return
                visited[(i,j)]=True
                if i>0 and image[i-1][j]==color:
                    paint(i-1,j,color)
                if i<len(image)-1 and image[i+1][j]==color:
                    paint(i+1,j,color)
                if j>0 and image[i][j-1]==color:
                    paint(i,j-1,color)
                if j<len(image[0])-1 and image[i][j+1]==color:
                    paint(i,j+1,color)
               
                
            paint(sr,sc,image[sr][sc])
            return(image)
                    
                
# May 10
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trustMap = defaultdict(list)
        trustCount = defaultdict(int)
        for t in trust:
            trustMap[t[0]].append(t[1])
            if not t[1] in trustMap:
                trustMap[t[1]] = []
            trustCount[t[1]]+=1
            
        
        if len(trustMap)==0 and N==1:
            return(N)
        
        for kv in trustCount.items():
            if kv[1]==len(trustMap.keys())-1 and len(trustMap[kv[0]])==0:
                return kv[0]
        
        return -1
    
    
# May 9
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return(True)
        guess=int(num/2)
        for i in range(1,100):
            newguess = 0.5*(guess+num/guess)
            if int(newguess)*int(newguess)==num:
                return(True)
            guess=newguess
        return(False)

# May day 8
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (len(coordinates)==2):
            return(True)
        
        distances = []
        for i in range(1,len(coordinates)):
            rise=(coordinates[i][1]-coordinates[0][1])
            run=(coordinates[i][0]-coordinates[0][0])
            if run==0:
                return(False)
            d = rise/run
            distances.append(d)
                
        for i in range(1, len(distances)):
            if distances[i]!=distances[i-1]:
                return(False)
        
        return(True)

# May day 7
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def findLevel(root:TreeNode, v, level):
            if root is None:
                return -1
            
            if (root.val==v):
                return(level)
            
            l = findLevel(root.right, v, level+1)    
            
            if l !=-1:    
                return l
            
            return findLevel(root.left, v, level+1)
        
        def findParent(root:TreeNode, v, p):
            if root is None:
                return -1
            
            if (root.val==v):
                return(p)
            
            p = findParent(root.right, v, root.val)    
            
            if p !=-1:    
                return p            
            return findParent(root.left, v, root.val)    
        
        
       
        return (findLevel(root, x, -1)==findLevel(root, y, -1)) and (findParent(root, x, -1)!=findParent(root, y, -1))
    
# May Day 6
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lim = floor(len(nums)/2)
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
            if map[num]>lim:
                return(num)
            
                
# May Day 5
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = OrderedDict()
        d = []
        for i,char in enumerate(s):
            if not char in m:
                m[char]=i
            else:
                d.append(char)
              
        for c in d:
            if c in m:
                del m[c]
                
        return -1 if len(m)==0 else m.popitem(False)[1]

# May Day 4
class Solution:
    def findComplement(self, num: int) -> int:
        t = int(num)
        ans = int(0)
        i = int(0)
        while t>0:
            ans += (1-(t&0x1))*(2**i)
            t >>= 1
            i += 1 
        
        return(ans)
            
        
  
    

        
        
            
        
# Day 21
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = defaultdict(int)
        map[0]=1
        result=0
        sum=0
        
        for n in nums:
            sum += n
            if sum-k in map:
                result += map[sum-k]
            map[sum] = map[sum]+1            
        
        return(result)
        
        
# Day 20
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i<len(preorder) and  preorder[i] < root.val:
            i+=1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
                

# Day 19
class Solution:
       def search(self, nums: List[int], target: int) -> int:
        def helper(l,r):
            if l > r:
                return -1
            m = (r+l)//2
            if nums[m] == target:
                return m
            if nums[l] <= target < nums[m] or (nums[m] <= nums[r]  and not nums[m] < target <= nums[r]):
                return helper(l,m-1)
            else: 
                return helper(m+1, r)
        return helper(0,len(nums)-1)
       
        

#Day 18
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 0 or grid is None:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if r==0 and c==0: # We just want to skip the top-left corner of the grid
                    continue
                if r-1<0: # Cases for elements in top row
                    grid[r][c] = grid[r][c] + grid[r][c-1]  
                elif c-1<0: # Cases for elements in leftmost column
                    grid[r][c] = grid[r][c] + grid[r-1][c]  
                else: # Normal cell
                    grid[r][c] = grid[r][c] + min(grid[r-1][c], grid[r][c-1])               
        
        return grid[rows-1][cols-1] # We have got the minimum path accumaled at the bottom-right corner, just return this

# Day 17
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        land = []
        
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if grid[i][j]=='1':
                    islands = islands+1
                    land.append((i,j))
                    while land:
                        coord = land.pop()
                        
                        x=coord[0]
                        y=coord[1]
                       
                        grid[x][y] = '0'
                        
                        if x>0 and grid[x-1][y]!='0':
                            land.append((x-1,y))
                        if x<len(grid)-1 and grid[x+1][y]!='0':
                            land.append((x+1,y))
                        if y>0 and grid[x][y-1]!='0':
                            land.append((x,y-1))
                        if y<len(grid[0])-1 and grid[x][y+1]!='0':
                            land.append((x,y+1))
                        
                        
                
        return(islands)
    


# Day 16


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
        

        


