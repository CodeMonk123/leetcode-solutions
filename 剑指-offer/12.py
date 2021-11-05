# -*- coding: utf-8 -*-
# @Date    : 2021-11-05 11:01:05
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy


class Solution:
    def __init__(self) -> None:
        self.used = set()

    def dfs(self, board:List[List[str]], x, y, word:str) -> bool:
        if len(word) == 0:
            return True
        candidates = [(x-1, y), (x+1,y), (x, y-1), (x,y+1)]

        for (i,j) in candidates:
            if i >=0 and i < len(board):
                if j >= 0 and j < len(board[0]):
                    if (i,j) not in self.used and board[i][j] == word[0]:
                        self.used.add((i,j))
                        exist = self.dfs(board, i, j, word[1:])
                        self.used.remove((i,j))
                        if exist:
                            return True

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.used = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    self.used.add((i,j))
                    exist = self.dfs(board, i, j, word[1:])
                    self.used.remove((i,j))
                    if exist:
                        return True
        
        return False

solution = Solution()
print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))