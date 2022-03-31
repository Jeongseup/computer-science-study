"""
input)
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

"""
from typing import List
from statistics import mean

if __name__ == '__main__':

	C = int(input())

	for _ in range(C):
		nums = list(map(int, input().split()))

		avg = mean(nums[1:])
		count = 0

		for score in nums[1:]:
			if score > avg:
				count += 1

		rate = count / nums[0] * 100

		print(f'{rate:.3f}%')
