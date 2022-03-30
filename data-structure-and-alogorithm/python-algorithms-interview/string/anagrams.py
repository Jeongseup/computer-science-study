"""
음.. 내 생각에는 이거 defaultdict를 하나 선언하면서 있으면 거기에 추가하는 형식으로 할 것 같은데?

아님.. 이거 정렬 한번시켜서? 처리
"""
from collections import defaultdict
from typing import List


def solution(input: List[str]) -> List[List[str]]:
	anagrams = defaultdict(list)

	for word in input:
		# 정렬하여 딕셔러니에 추가
		anagrams[''.join(sorted(word))].append(word)

	return anagrams.values()


if __name__ == '__main__':
	input = ["eat", "tea", "tan", "ate", "nat", "bat"]
	result = solution(input)
	print(result)
