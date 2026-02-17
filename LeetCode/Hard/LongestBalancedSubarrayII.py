"""
You are given an integer array nums.

A is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.


Example 1:

Input: nums = [2,5,4,3]
Output: 4

Explanation:

    The longest balanced subarray is [2, 5, 4, 3].
    It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.

Example 2:

Input: nums = [3,2,2,5,4]
Output: 5

Explanation:

    The longest balanced subarray is [3, 2, 2, 5, 4].
    It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.

Example 3:

Input: nums = [1,2,3,2]
Output: 3

Explanation:

    The longest balanced subarray is [2, 3, 2].
    It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.


Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 105

"""
class SegmentTree:
    def __init__(self, size):
        self.n = size
        # Stores max balance value in the range
        self.tree = [0] * (4 * size)
        # Lazy propagation for range updates
        self.lazy = [0] * (4 * size)

    def _push(self, v):
        if self.lazy[v] != 0:
            self.tree[2*v] += self.lazy[v]
            self.lazy[2*v] += self.lazy[v]
            self.tree[2*v+1] += self.lazy[v]
            self.lazy[2*v+1] += self.lazy[v]
            self.lazy[v] = 0

    def update(self, v, tl, tr, l, r, add):
        if l > r:
            return
        if l == tl and r == tr:
            self.tree[v] += add
            self.lazy[v] += add
        else:
            self._push(v)
            tm = (tl + tr) // 2
            self.update(2*v, tl, tm, l, min(r, tm), add)
            self.update(2*v+1, tm+1, tr, max(l, tm+1), r, add)
            self.tree[v] = max(self.tree[2*v], self.tree[2*v+1])

    def find_first_zero(self, v, tl, tr, target):
        # Specific logic to find the furthest index where balance is 0
        if self.tree[v] < target:
            return -1
        if tl == tr:
            return tl
        self._push(v)
        tm = (tl + tr) // 2
        res = self.find_first_zero(2*v+1, tm+1, tr, target)
        if res == -1:
            res = self.find_first_zero(2*v, tl, tm, target)
        return res

class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        next_occurrence = {}
        next_pos = [n] * n
    
        # Precompute next occurrences of each number
        last_seen = {}
        for i in range(n - 1, -1, -1):
            if nums[i] in last_seen:
                next_pos[i] = last_seen[nums[i]]
            last_seen[nums[i]] = i
        
        st = SegmentTree(n)
        max_len = 0
    
        # Process the array
        # Logic: balance = (distinct_even - distinct_odd)
        # Use Segment Tree to track balance across ranges
        for i in range(n - 1, -1, -1):
            val = 1 if nums[i] % 2 == 0 else -1
            # Update range from current index to next occurrence of same number
            st.update(1, 0, n-1, i, next_pos[i] - 1, val)
        
            # Find furthest index where balance relative to i is 0
            idx = st.find_first_zero(1, 0, n-1, 0)
            if idx != -1:
                max_len = max(max_len, idx - i + 1)
            
        return max_len


solution = Solution()
# print(solution.longestBalanced([2,5,4,3]))
print(solution.longestBalanced([3,2,2,5,4]))
# print(solution.longestBalanced([1,2,3,2]))