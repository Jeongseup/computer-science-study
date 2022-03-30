# N = input('시각을 입력하세요')
N = 5
count = 0
for hour in range(0, N + 1):
	# print(h)
	for min in range(60):
		# print(hour, min)
		for sec in range(60):
			temp_time = f'{hour}:{min}:{sec}'
			if '3' in temp_time:
				count += 1

print(count)