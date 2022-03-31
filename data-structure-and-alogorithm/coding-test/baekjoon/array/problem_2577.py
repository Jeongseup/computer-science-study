"""
input)
150
266
427

"""
if __name__ == '__main__':

	nums_counter = [0] * 10
	multiple = 1

	for _ in range(3):
		multiple *= int(input())

	for chr_index in str(multiple):
		nums_counter[int(chr_index)] += 1
		# print(word)

	for answer in nums_counter:
		print(answer)


