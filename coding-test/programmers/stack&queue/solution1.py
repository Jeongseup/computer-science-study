def solution(progresses, speeds):
	Q = []
	for p, s in zip(progresses, speeds):
		# 현재 큐가 비었거나, 해당 배열의 첫 번째 값보다 작은 경우 push
		# tip) 음수로 나누면, 몫에 나머지가 있는 경우 +1 을 더함
		if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
			Q.append([-((p - 100) // s), 1])
		else:
			Q[-1][1] += 1
	return [q[1] for q in Q]


if __name__ == "__main__":
	test_progresses = [93, 30, 55]
	test_speeds = [1, 30, 5]

	Q = []
	for p, s in zip(test_progresses, test_speeds):
		if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
			Q.append([-((p - 100) // s), 1])
			print(Q)
		else:
			Q[-1][1] += 1

	print([q[1] for q in Q])
	# print(solution(test_progresses, test_speeds))
