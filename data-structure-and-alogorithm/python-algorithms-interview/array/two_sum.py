from typing import List


def solution(nums: List[int], target: int) -> List[int]:
	for i in range(len(nums)):
		# print(f'nums[i] is {nums[i]}')
		for j in range(i + 1, len(nums)):
			# print(nums[j])
			if nums[i] + nums[j] == target:
				return [i, j]

def better_solution(nums, target):
	nums_map = {}

	for i, num in enumerate(nums):
		# print(num)
		if (target - num) in nums_map:
			return [nums_map[target - num], i]

		nums_map[num] = i
	print(nums_map)

if __name__ == '__main__':
	print('main')

	nums = [2, 7, 11, 15]
	target = 9

	result = solution(nums, target)
	print(result)