'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''Using memoization'''
        def dfs_path(matrix, i, j, cache):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return 0 
            
            # key = '%d_%d' % (i, j)
            #if key in cache:
            #    return cache[key]
            if cache[i][j] != -1:
                return cache[i][j]
            
            left, right = i - 1, i + 1 
            up, down = j + 1, j - 1 
            
            path_1, path_2, path_3, path_4 = -1, -1, -1, -1 
            current = matrix[i][j] 
            if left >= 0 and matrix[left][j] > current:
                path_1 = 1 + dfs_path(matrix, left, j, cache)
            
            if right < len(matrix) and matrix[right][j] > current:
                path_2 = 1 + dfs_path(matrix, right, j, cache)
            
            if down >= 0 and matrix[i][down] > current:
                path_3 = 1 + dfs_path(matrix, i, down, cache)
            
            if up < len(matrix[0]) and matrix[i][up] > current:
                path_4 = 1 + dfs_path(matrix, i, up, cache)
            
            max_ = max(path_1, path_2, path_3, path_4, 1)  # 1 is for current
            cache[i][j] = max_
            return max_
        
        cache = [[-1 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        longest_path = 0 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest_path = max(longest_path, dfs_path(matrix, i, j, cache))
        
        return longest_path

    ##################
    # Using loop 
    # in directions
    ##################

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''DFS + memoization'''
        
        def in_matrix(r, c):
            if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]):
                return False 
            return True
        
        def find_path(i, j):
            # check memory
            if self.mem[i][j] != -1:
                return self.mem[i][j]
            
            current = matrix[i][j]
           
            # create list to hold values for paths
            paths = [0] * 4
            
            for index, direction in enumerate(directions):
                i_off, j_off = direction
                new_i, new_j = i + i_off, j + j_off
                
                if in_matrix(new_i, new_j) and matrix[new_i][new_j] > current:
                    paths[index] = find_path(new_i, new_j)
            
            ans = max(paths) + 1
            # update memory
            self.mem[i][j] = ans
            return ans
    
    
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        max_path = 0
        
        # setup memory for holding longest path for particular index
        self.mem = []
        for i in range(len(matrix)):
            self.mem.append([-1] * len(matrix[0]))
   
        # call DFS for all indexes
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                path = find_path(i, j)
                max_path = max(max_path, path)
        
        return max_path
            
