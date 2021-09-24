from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_total = 0
        fruit_a, fruit_b = fruits[0], fruits[0]
        num_a = 0
        num_b = 0

        for i, fruit in enumerate(fruits):
            if fruit == fruit_a:
                num_a += 1
            elif fruit != fruit_a and fruit_a == fruit_b:
                fruit_b = fruit
                num_b += 1
            elif fruit == fruit_b:
                num_b += 1
            max_total = max(max_total, num_a + num_b)
            # print('a[{}], num_a = {}'.format(fruit_a, num_a))
            # print('b[{}], num_b = {}'.format(fruit_b, num_b))

            if fruit != fruit_a and fruit != fruit_b:
                if fruits[i - 1] == fruit_b:
                    fruit_a = fruit_b
                fruit_b = fruit
                num_b = 1
                num_a = 0

                # print('a[{}], num_a = {}'.format(fruit_a, num_a))
                for j in range(i - 1, -1, -1):
                    if fruits[j] == fruit_a:
                        num_a += 1
                    else:
                        break
                # print('a[{}], num_a = {}'.format(fruit_a, num_a))
                # print('b[{}], num_b = {}'.format(fruit_b, num_b))
                max_total = max(max_total, num_a + num_b)

        return max_total


solution = Solution()
print(solution.totalFruit([0, 1, 0, 2]))
print(solution.totalFruit([0, 1, 2, 2]))
print(solution.totalFruit([1, 2, 3, 2, 2]))
print(solution.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
