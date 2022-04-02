"""
input)
3
happy
new
year

"""


def solution(string: str) -> bool:
	is_group = True

	temp_word = ''
	word_dict = set()

	for word in string:
		# 그리고.. 이전 문자랑 현재 문자랑 같으면 continue
		if temp_word == word:
			temp_word = word
			continue
		else:
			if word in word_dict:
				return False

			# 일단 처음이면 set에 add
			word_dict.add(word)

			# 이전 단어를 저장
			temp_word = word

	return is_group


if __name__ == '__main__':
	# 데이터를 받고
	N = int(input())

	count = 0

	for _ in range(N):
		input_string = input()
		# print(solution(input_string))
		if solution(input_string) is True:
			count += 1

	print(count)
