"""
pseudo code
배열 데이터를 역순으로 정렬하는 방법은?
절반의 데이터들을 바꿔버린다.

for i in range(n // 2):
	a[i] 와 a[n - i -1] 의 값을 교환
"""

from typing import MutableSequence


def reverse_array(a: MutableSequence) -> None:
	"""뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
	n = len(a)
	for i in range(n // 2):
		a[i], a[n - i - 1] = a[n - i - 1], a[i]


if __name__ == '__main__':
	print('배열 원소를 역순으로 졍렬합니다.')
	data = list(map(int, input().split()))
	reverse_array(data)
	print(data)
