"""
백준 10818번 문제 : 최소 최대

explain
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

input
5
20 10 35 30 7

output
7 35
"""

def solution(num_list):
	if len(num_list) == 1:
		return num_list[0], num_list[0]
	else:
		return min(num_list), max(num_list)


n = input()
num_list = list(map(int, input().split()))
min, max = solution(num_list)

print(min, max)
