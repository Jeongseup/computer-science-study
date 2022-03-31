"""
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
"""
"""
input)
	3
	29
	38
	12
	57
	74
	40
	85
	61
	
"""

if __name__ == '__main__':
	nums = []

	for _ in range(9):
		temp_num = int(input())
		nums.append((temp_num))
	
	# 초기화
	max_index, max_value = 0, 0
	for index, value in enumerate(nums):
		# print(index, value)
		if value > max_value:
			max_value = value
			max_index = index

	print(max_value)
	print(max_index  + 1)

