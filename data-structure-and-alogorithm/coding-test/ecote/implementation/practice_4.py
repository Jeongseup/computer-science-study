"""
문자열 재정렬

1. 알파벳은 오름차순 정렬 후 출력
2. 이어서 모든 숫자를 더한 값 출력
"""


def solution(input_string: str) -> None:
	words, digits = [], []

	for ch in input_string:
		if ch.isdigit():
			digits.append(int(ch))
		else:
			words.append(ch)

	print(''.join(sorted(words)) + str(sum(digits)))


def better_solution(input_string: str) -> None:
	words = []
	sum = 0

	for ch in input_string:
		if ch.isdigit():
			sum += int(ch)
		else:
			words.append(ch)
	# 정렬
	words.sort()
	if sum != 0:
		words.append(str(sum))

	print(''.join(words))



if __name__ == '__main__':
	test = 'K1KA5CB7'
	better_solution(test)