def hansu(input_num: int):
	# 100보다 작으면 모두 한수
	if input_num < 100:
		return 1

	string_num = str(input_num)

	for i, word in enumerate(string_num):
		# 포인터가 끝이면 종료
		if i == (len(string_num) - 1):
			break

		diff = int(string_num[i]) - int(string_num[i + 1])
		if i == 0:
			CONST_DIFF = diff
			continue

		# print(f'{CONST_DIFF} <-> 다음 {diff}')
		if CONST_DIFF != diff:
			# print('종료')
			return 0

	# print('한수!')
	return 1


n = int(input())
answer = 0

for num in range(1, n + 1):
	# print(hansu(num))
	answer += hansu(num)

print(answer)

