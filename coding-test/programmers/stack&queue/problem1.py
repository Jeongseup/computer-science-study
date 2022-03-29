from collections import deque
from typing import List


def solution(progresses, speeds):
	due_time_list = create_due_time(progresses, speeds)
	schedule_list = create_schedule(due_time_list)
	print(schedule_list)
	answer = []
	for i in range(len(schedule_list)):
		answer.append(len(schedule_list[i]))

	return answer


def create_due_time(progresses: List[int], speeds: List[int]) -> List[int]:
	progress_queue = deque(progresses)
	speed_queue = deque(speeds)

	# due date list init
	due_date = []
	for _ in range(len(progress_queue)):
		# 임시 작업과 스피드
		temp_progress = progress_queue.popleft()
		temp_speed = speed_queue.popleft()

		temp_due_date, remainder = divmod((100 - temp_progress), temp_speed)
		# print(temp_due_date, remainder)

		if remainder > 0:
			temp_due_date += 1

		# print(temp_due_date)
		due_date.append(temp_due_date)

	return due_date


def create_schedule(due_time_list: List[int]) -> List[int]:
	# init
	due_time_queue = deque(due_time_list)
	answer = []

	for _ in range(len(due_time_queue)):
		temp_date = due_time_queue.popleft()
		# print([temp_date])

		# 빈 배열인 상태라면 바로 push
		if len(answer) == 0:
			answer.append([temp_date])

		# 빈 배열이 아닌경우
		else:
			# 바로 직전의 배열의 최댓값과 현재 due date 비교
			if max(answer[-1]) >= temp_date:
				answer[-1].append(temp_date)
			else:
				answer.append([temp_date])

	return answer


if __name__ == "__main__":
	test_progresses = [93, 30, 55]
	test_speeds = [1, 30, 5]

	print(solution(test_progresses, test_speeds))
