"""
비효율적인 방법만 생각나서 바로 답을 찾아봄..
input)
ljes=njak

"""
# 데이터를 받고
input_string = input()

# 크로아티아 문자를 추가한 set 문자 만들기
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for word in croatia:
	input_string = input_string.replace(word, '*')

print(len(input_string))
