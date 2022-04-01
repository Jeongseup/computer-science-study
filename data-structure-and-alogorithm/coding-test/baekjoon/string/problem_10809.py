"""
baekjoon
"""

if __name__ == '__main__':
	# 입력받고
	string = input()

	# 초기화 해서
	alphabet_dict = {}
	for i in range(97, 97 + 26):
		alphabet_dict[chr(i)] = -1


	for i, word in enumerate(string):
		if alphabet_dict[word] == -1:
			alphabet_dict[word] = i
		# sum += int(word)

	answer = ''
	for value in alphabet_dict.values():
		answer += str(value) + " "

	print(answer[:-1])