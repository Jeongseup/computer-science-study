input_string = '02984'


def solution(input_string: str) -> int:
	num_list = list(input_string)

	init_num = int(num_list[0])
	print('start', init_num)
	for i in range(1, len(num_list)):
		temp_num = int(num_list[i])
		# print(temp_num)
		if temp_num > 2:
			init_num *= temp_num
		else:
			init_num += temp_num

	print(init_num)



solution(input_string)
