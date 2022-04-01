"""
input)
734 893

"""
#
string_num1, string_num2 = input().split()
num1, num2 = int(string_num1[::-1]), int(string_num2[::-1])
# print(num1, num2)

if num1 > num2:
	print(num1)
else:
	print(num2)
