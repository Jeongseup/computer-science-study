def solution(progresses, speeds):
	Q = []
	for temp_progress, temp_speed in zip(progresses, speeds):
		temp_due_time = -1 * ((temp_progress - 100) // temp_speed)

		# 먼저 빈 배열이라면 바로 push : [progress, 1]
		if not Q:
			Q.append([temp_due_time, 1])
			# print(Q)
			continue
		# 빈 배열이 아닌 경우, 이전 배열의 due date 확인
		else:
			current_due_time = Q[-1][0]
			# print(current_due_time, Q[-1])
			# 다음 작업이 이전 작업보다 빨리 끝나는 경우 count 증가
			if current_due_time >= temp_due_time:
				Q[-1][1] += 1
			# print(Q)
			else:
				Q.append([temp_due_time, 1])

	return [q[1] for q in Q]

if __name__ == "__main__":
	test_progresses = [93, 30, 55]
	test_speeds = [1, 30, 5]

	print(solution(test_progresses, test_speeds))
