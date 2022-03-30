"""
N에서 1을 빼거나
N을 K로 나누거나
"""

n = 25
k = 5

def better_solution(n:int, k:int) -> None:
	count = 0
	while True:
		# n이 k로 나누어 떨어지는 수가 될때까지 뺀다.
		target = (n // k) * k
		count += (n -target)
		n = target

		# n보다 k가 작을 때? 반복문을 탈출한다.
		if n < k:
			break

		# k로 나눈다.
		n //= k
		count += 1

	# 마지막으로 남은 수에 대해 1씩 뺀다.
	count += (n - 1)
	print(count)

def solution(n: int, k: int) -> None:
	count = 0

	while True:
		# 	# n이 나눠진다면 나눠버림.
		if (n % k) == 0:
			n //= k
			count += 1
		# 나눠지지 않으면 -1
		else:
			if n == 1:
				break

			n -= 1
			count += 1

	print(count)


