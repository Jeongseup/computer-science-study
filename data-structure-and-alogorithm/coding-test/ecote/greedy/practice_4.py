"""
공포도 모험가 문제

"""
from typing import List

def better_solution(input_list: List[int]) -> None:
	# 정렬
	input_list.sort()


	result = 0 # 총 그룹수
	count = 0 # 현재 그룹에 포함된 모험가 수

	for i in input_list:
		count += 1 # 현재 그룹에 모험가 포함
		if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면?
			result += 1
			count = 0

	print(result)

def solution(input_list: List[int]) -> None:
	input_list.sort()
	print(input_list)
	count = 0

	while True:
		# 몇 명씩  짜를 건지
		temp_group_num = input_list.pop()

		# 자기를 포함하니까 자기를 제외하고 나머지를 뒤에서 부터 가져온다.
		# 그럼 그 전까지만 남겠지?
		input_list = input_list[: -(temp_group_num - 1)]
		count += 1

		if input_list[-1] >= len(input_list):
			break

	if input_list[-1] == len(input_list):
		count += 1

	print(count)


if __name__ == '__main__':
	N = 5
	input = [2, 3, 1, 2, 2]

	better_solution(input)
