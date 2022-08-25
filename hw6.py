def get_list() -> list:
      return list(range(0, 1_000_000, 2))

class Solution:
      def find_target(self, list, target):
          n = len(list)
          low = 0
          high = n - 1
          while low <= high:
              mid = (high + low) // 2
              guess = list[mid]
              if guess == target:
                  return mid
              elif guess > target:
                  high = mid - 1
              else:
                  low = mid + 1

          return target



lol = Solution()
print(lol.find_target(list=get_list(), target=245560))

file = open('binary_search.txt', 'w', encoding='UTF-8')
file.write("Что такое бинарный поиск?\n"
           "Зачем он нужен?\n"
           "Принцип работы бинарного поиска?")

