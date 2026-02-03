"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

Constraints:
    1 <= numRows <= 30

"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            # Start each new row with 1
            row = [1]
            # Calculate inner values by summing adjacent elements from the previous row
            if i > 0:
                last_row = triangle[-1]
                for j in range(len(last_row) - 1):
                    row.append(last_row[j] + last_row[j+1])
            # End each new row with 1
            if i > 0:
                row.append(1)
            triangle.append(row)
        return triangle
    

solution = Solution()

print(solution.generate(5))
print(solution.generate(1))
print(solution.generate(6))

pascal_math_data = solution.generate(7)
for row in pascal_math_data:
    print(" ".join(map(str, row)).center(20))
