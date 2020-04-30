'''
A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, 
or null if it does not point to any node.


Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        def get_node(node):
            if not node:
                return None

            # if already seen - don't create new
            if node in self.visited:
                return self.visited[node]

            # create new - updated old -> new map and return
            self.visited[node] = Node(node.val)
            return self.visited[node]

        if not head:
            return None

        old = head
        new_ = Node(old.val)  # create new head 
        self.visited[old] = new_  # update old -> new map

        # clone all the nodes in list
        while old:
            new_.random = get_node(old.random)
            new_.next = get_node(old.next)

            old = old.next  # move forward
            new_ = new_.next  

        return self.visited[head]

