"""
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
"""
import re


def solution(new_id):
	# 1단계
	new_id = new_id.lower()

	# 2단계
	available_dict = create_dict()
	print(available_dict)

	for word in new_id:
		# print(new_id, word)
		if word not in available_dict:
			# print(word)
			new_id = new_id.replace(word, '')

	print(new_id)
	# 3단계
	while '..' in new_id:
		print('test')
		new_id = new_id.replace('..', '.')

	# 4 단계
	if new_id and new_id[0] == '.':
		new_id = new_id[1:]

	if new_id and new_id[-1] == '.':
		new_id = new_id[:-1]

	print(new_id)
	# 5 단계
	if not new_id:
		new_id = 'a'

	# 6 단계
	if len(new_id) > 15:
		new_id = new_id[:15]
		# print(new_id)
		# print(len(new_id))

		if new_id[-1] == '.':
			new_id = new_id[:-1]

	if len(new_id) <= 2:
		while len(new_id) < 3:
			new_id = new_id + new_id[-1]

	return new_id


def create_dict():
	available_dict = set()

	for i in range(97, 97 + 26):
		available_dict.add(chr(i))

	for i in range(0, 10):
		available_dict.add(str(i))

	available_dict.add('-')
	available_dict.add('_')
	available_dict.add('.')

	return available_dict


input_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(input_id))
# 6 18 26 틀림

def better_solution(new_id):
	# 1
	new_id = new_id.lower()
	# 2
	new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
	new_id = re.sub('\.+', '.', new_id)
	new_id = re.sub('^[.]|[.]$', '', new_id)
	new_id = 'a' if len(new_id) == 0 else new_id[:15]
	new_id = re.sub('[.]$', '', new_id)
	# 마지막응은 쫌...
	new_id = new_id if len(new_id) > 2 else new_id + "".join(new_id[-1] for i in range(3 - len(new_id)))

	return new_id
