from typing import List

def func(x):
	return x.split()[1], x.split()[0]

def solution(input_logs: List[str]) -> List[str]:
	# 빈 리스트 만들어 문자끼리 숫자끼리 모음
	letters, digits = [], []

	for log in input_logs:
		if log.split()[1].isdigit():
			digits.append(log)
		else:
			letters.append(log)

	# 2개의 키를 람다 표현식으로 정렬
	# letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
	letters.sort(key=func)
	return letters + digits

if __name__ == '__main__':
	logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
	result = solution(logs)

	print(result)