import re
from collections import Counter
from typing import List


def solution(paragraph: str, banned: List[str]) -> str:
	# data cleaning
	words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

	# 카운터 객체에 넣기
	counts = Counter(words)
	print(f'most common is {counts.most_common(1)}')
	return counts.most_common(1)[0][0]

if __name__ == '__main__':
	paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
	banned = ["hit"]

	result = solution(paragraph, banned)
	print(result)
