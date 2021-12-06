# -*- coding: utf-8 -*-
# @Date    : 2021-12-05 20:40:30
# @Author  : CodeMonk123

from typing import List, Set
from typing import Dict, Tuple
import copy

class Solution:
    def dfs(self, board:List[List[str]], used:Set, current:str, word:str, x:int, y:int, m:int, n:int)->bool:
        if current == word:
            return True
        target = word[len(current)]
        candidates = []
        if x > 0:
            candidates.append((x-1, y))
        if x < m-1:
            candidates.append((x+1,y))
        if y > 0:
            candidates.append((x,y-1))
        if y < n-1:
            candidates.append((x,y+1))
        for candidate in candidates:
            if candidate not in used and board[candidate[0]][candidate[1]] == target:
                used.add(candidate)
                if self.dfs(board, used, current + target, word, candidate[0], candidate[1], m ,n):
                    return True
                used.remove(candidate)
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        start = []
        used = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start.append((i,j))
        for (i,j) in start:
            used.add((i,j))
            if self.dfs(board, used, word[0], word, i, j, m, n):
                return True
            used.remove((i,j))
        return False