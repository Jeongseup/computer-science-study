from typing import List


def solution(input_string: List[str]) -> List[str]:
	left_index, right_index = 0, len(input_string) - 1
	# 같아지면 종료된다.
	while left_index < right_index:
		input_string[left_index], input_string[right_index] = input_string[right_index], input_string[left_index]
		left_index += 1
		right_index -= 1
	# print(input_string)
	return input_string


def solution2(input_string: List[str]) -> str:
	input_string.reverse()
	return input_string


def simple_solution(input_string: str) -> str:
	return input_string[::-1]


if __name__ == '__main__':
	input = ['h', 'e', 'l', 'l', 'o']
	result = solution2(input)

	print(result)
