"""
공포도 모험가 문제

"""
from typing import List


def solution(N: int, plan: List[chr]) -> None:
	# 동 북 서 남
	move = {
		'R': (1, 0),
		'L': (-1, 0),
		'U': (0, -1),
		'D': (0, 1)
	}

	x, y = 1, 1
	for temp_plan in plan:
		print(x, y, end=" ")
		dx = x + move[temp_plan][0]
		dy = y + move[temp_plan][1]

		if 1 <= dx <= N and 1 <= dy <= N:
			x = dx
			y = dy
			print(f'MOVE TO "{temp_plan}"', end=" ")
			print(x, y)
		else:
			print()

	print(x, y)


def better_solution(N: int, plan: List[chr]) -> None:
	move_types = ['L', 'R', 'U', 'D']

	# L R U D 일반적인 X,Y랑 반대로 생각한다.
	# x = row, y = column
	dx = [0, 0, -1, 1]
	dy = [-1, 1, 0, 0]

	# 초기화
	x, y = 1, 1
	# 이동 계획 확인하기
	for temp_p in plan:
		for i in range(len(move_types)):
			if temp_p == move_types[i]:
				next_x = x + dx[i]
				next_y = y + dy[i]

		# 만약 공간을 벗어나면?
		if next_x < 1 or next_y < 1 or next_x > N or next_y > N:
			# for 문 생략
			continue

		x, y = next_x, next_y

	print(x, y)

if __name__ == '__main__':
	N = 5
	plan = ['R', 'R', 'R', 'U', 'D', 'D']

	better_solution(N, plan)
