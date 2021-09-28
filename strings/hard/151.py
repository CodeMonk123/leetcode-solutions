class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = list(s.strip(' '))
        word_list.reverse()
        start = 0
        end = 1
        while True:
            if end == len(word_list) or word_list[end] == ' ':
                i, j = start, end - 1
                while i < j:
                    word_list[i], word_list[j] = word_list[j], word_list[i]
                    i += 1
                    j -= 1
                start = end + 1
                if start >= len(word_list):
                    break
                while word_list[start] == ' ':
                    word_list.pop(start)
                end = start + 1
            else:
                end = end + 1
                if end > len(word_list):
                    break

        return ''.join(word_list)


solution = Solution()
print(solution.reverseWords(s="the   sky is blue   "))
