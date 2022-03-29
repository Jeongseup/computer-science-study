"""
explanation)
10 진수의 정숫값을 입력받아 2~16 진수로 변환하여 출력하기
"""


def card_conv(x: int, r: int) -> str:
	"""정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

	d = ''
	dchar = '0123456789ABCDEFGHJKMNOP'

	while x > 0:
		d += dchar[x % r]
		x = x // r

	# 역순으로 전환
	return d[::-1]


if __name__ == '__main__':
	origin_num = int(input())
	cd = int(input())

	print(f'{cd}진수로 {card_conv(origin_num, cd)}입니다.')
