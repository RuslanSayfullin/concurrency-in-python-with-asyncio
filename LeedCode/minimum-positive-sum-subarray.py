from typing import List
import math
import collections


"""Вам дан массив целых чисел nums и два целых числа l и r. 
Ваша задача — найти минимальную сумму элементов подмассива, размер которого находится в диапазоне от l до r (включительно), и сумма которых больше 0.
Верните минимальную сумму элементов такого подмассива. Если такого подмассива не существует, верните -1.
Подмассив — это непрерывная непустая последовательность элементов внутри массива.
"""


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        
        # Вычисляем префиксные суммы
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        result = math.inf
        
        # Используем deque для поддержки минимума в окне
        dq = collections.deque()
        
        # Рассматриваем все возможные длины от l до r
        for length in range(l, r + 1):
            dq.clear()
            
            # Перебираем возможные правые границы подмассива
            for i in range(length, n + 1):
                # Добавляем в deque индекс начала подмассива
                start_idx = i - length
                
                # Поддерживаем deque в порядке возрастания префиксных сумм
                while dq and prefix[dq[-1]] >= prefix[start_idx]:
                    dq.pop()
                
                dq.append(start_idx)
                
                # Удаляем устаревшие индексы
                if dq[0] < i - length:
                    dq.popleft()
                
                # Вычисляем сумму подмассива
                if dq:
                    current_sum = prefix[i] - prefix[dq[0]]
                    if current_sum > 0:
                        result = min(result, current_sum)
        
        return result if result != math.inf else -1

nums = [3, -2, 1, 4]
l = 2
r = 3

example = Solution()
result = example.minimumSumSubarray(nums, l, r)

nums = [-2, 2, -3, 1]
l = 2
r = 3
result2 = example.minimumSumSubarray(nums, l, r)


nums = [1, 2, 3, 4]
l = 2
r = 4
result3 = example.minimumSumSubarray(nums, l, r)

print(result, result2, result3)
