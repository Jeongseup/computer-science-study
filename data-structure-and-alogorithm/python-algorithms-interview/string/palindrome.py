import collections
import re
from typing import Deque


def solution(s: str) -> bool:
	strs = []

	# 문자열 분해
	for char in s:
		if char.isalnum():
			strs.append(char.lower())

	# 팰린드롬 여부 확인
	while len(strs) > 1:
		# 앞 뒤에서 pop한 게 같지 않담녀
		if strs.pop(0) != strs.pop():
			return False

	return True

def better_solution(s: str) -> bool:
	# 자료형 데크 선언
	strs: Deque = collections.deque()

	for char in s:
		if char.isalnum():
			strs.append(char.lower())

	while len(strs) > 1:
		if strs.popleft() != strs.pop():
			return False

	return True

def better_solution2(s: str) -> bool:
	# 슬라이싱 이용
	s = s.lower()
	# 정규식으로 불필요한 문자 필터링
	s = re.sub('[^a-z0-9]', '', s)

	return s == s[::-1]


if __name__ == '__main__':
	test_s = 'raca a car'
	print(solution(test_s))
