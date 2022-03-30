def solution(s: str) -> str:
	def expand(left: int, right: int) -> str:
		# index 끝이 아니면서 양 끝이 같은지 확인
		while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
			left -= 1
			right += 1

		return s[(left + 1):(right - 1)]

	# 속도 향상 : 1개로 구성된 스트링이나 자체작 팰린드롬인 경우
	if len(s) < 2 or s == s[::-1]:
		return s

	result = ''
	for i in range(0, len(s) - 1):
		result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

	return result


if __name__ == '__main__':
	input = 'babad'

	result = solution(input)
	print(result)
