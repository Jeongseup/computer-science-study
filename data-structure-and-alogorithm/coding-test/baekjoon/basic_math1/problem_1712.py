"""
input)
1000 70 170

"""
import math

def solution(A: int, B: int, C: int ) -> int:
	# C * x = A + B * x
	# A = (C - B) * x

	# for x in range(1, sys.maxsize):
	X = A // (C - B)


	return X + 1

if __name__ == '__main__':
	# 데이터를 받고
	A, B, C = map(int, input().split())

	# 손익 분기가 생기려면 C가 B보다 커야함
	if C > B:
		answer = solution(A, B, C)
	else:
		answer = -1

	print(answer)
