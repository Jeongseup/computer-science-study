from collections import defaultdict
"""
input)
39
40
41
42
43
44
82
83
84
85

"""
if __name__ == '__main__':

	# 두 수를 받아서 % 42 한 값을
	# dict에 저장
	# key 개수 출력

	remainder = set()

	for _ in range(10):
		# int(input())
		remainder.add(int(input()) % 42)

	print(len(remainder))
