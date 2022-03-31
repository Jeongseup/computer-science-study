from collections import defaultdict
"""
input)
4
1 100 100 100

"""
if __name__ == '__main__':

	# 평균을 구하고
	# 그냥 그 값을
	# 평균 / MAX * 100 하면 되지 않을까?

	N = int(input())
	scores = list(map(int, input().split()))

	M = max(scores)
	average = sum(scores) / len(scores)

	adjusted_average = average / M * 100
	print(adjusted_average)
