# -*- coding: utf-8 -*-
# @Date    : 2021-11-07 15:32:44
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(' ')
        words = []
        current_word = []
        for ch in s:
            if ch == ' ':
                if len(current_word) > 0:
                    words.append(''.join(current_word))
                    current_word = []
                else:
                    continue
            else:
                current_word.append(ch)
        words.append(''.join(current_word))

        words.reverse()
        return ' '.join(words)