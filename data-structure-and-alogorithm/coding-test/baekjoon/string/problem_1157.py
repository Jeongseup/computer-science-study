

"""
input)
Mississipi

"""
from collections import Counter

if __name__ == '__main__':
	# 입력받고
	input_string = input()

	counter = Counter(input_string.lower())

	# 한 문자만 연속되었다면 아래처럼 출력
	if len(counter) == 1:
		print(counter.most_common(1)[0][0].upper())
	else:
		most_one = counter.most_common(2)[0]
		most_two = counter.most_common(2)[1]

		if most_one[1] == most_two[1]:
			print('?')
		else:
			print(most_one[0].upper())


