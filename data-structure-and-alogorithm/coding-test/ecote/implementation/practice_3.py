input = 'a1'

x, y = int(ord(input[0]) - 96), int(input[1])

move_type = [
	# 위
	(-2, -1),
	(-2, +1),
	# 아래
	(+2, -1),
	(+2, +1),
	# 왼쪽
	(+1, -2),
	(-1, -2),
	# 오른쪽
	(+1, +2),
	(-1, +2),
]

count = 0
for temp_p in move_type:
	# print(temp_p)
	# 옮겨보고
	nx = x + temp_p[0]
	ny = y + temp_p[1]

	# 안에 있으면 count 증가
	if 1 <= nx <= 8 and 1 <= ny <= 8:
		count += 1

print(count)