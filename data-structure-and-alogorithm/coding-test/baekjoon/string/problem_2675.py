"""
input)
2
3 ABC
5 /HTP

"""

def solution(R: int, S: str) -> str:
	# 음.. 입력을 받은 걸

	answer = ''
	for word in S:
		answer += word * R

	return answer
if __name__ == '__main__':
	# 입력받고
	T = int(input())

	for _ in range(T):
		R, S = input().split()
		# print(type(R))
		# print(type(S))
		answer = solution(int(R), S)
		print(answer)

