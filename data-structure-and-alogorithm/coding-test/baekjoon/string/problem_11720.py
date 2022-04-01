"""
input)
5
54321

"""
if __name__ == '__main__':
	n = input()
	string_num = input()

	sum = 0

	for word in string_num:
		sum += int(word)

	print(sum)