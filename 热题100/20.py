# -*- coding: utf-8 -*-
# @Date    : 2021-11-29 10:27:36
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        st.append(s[0])
        for i in range(1, len(s)):
            if s[i] == ')':
                if len(st) == 0 or st[-1] != '(':
                    return False
                else:
                    st.pop()
            elif  s[i] == ']':
                if len(st) == 0 or st[-1] != '[':
                    return False
                else:
                    st.pop()
            elif  s[i] == '}':
                if len(st) == 0 or st[-1] != '{':
                    return False
                else:
                    st.pop()
            else:
                st.append(s[i])
        
        return len(st)==0