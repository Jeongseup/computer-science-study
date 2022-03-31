"""
input)
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX

"""


def solution(input_string: str) -> int:
	score = 0
	stack = []

	for word in input_string:
		if word == 'O':
			stack.append(word)
			score += len(stack)
		else:  # word is 'X'
			stack = []

	return score


if __name__ == '__main__':
	# 점수를 구하는데
	# 연속된 O의 개수에 따라 점수가 매겨진다.
	# O가 들어오면 stack에 넣고, 그 len을 점수로 count한다.
	# 만약 X가 들어온다면? 배열을 []로 초기화

	N = int(input())

	for _ in range(N):
		test_string = input()
		print(solution(test_string))
