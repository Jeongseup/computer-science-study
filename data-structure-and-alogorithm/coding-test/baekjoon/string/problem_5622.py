"""
input)
UNUCIC

"""
# 데이터를 받고
input_string = input()

telephone_dict = {'A': 2, 'B': 2, 'C': 2,
				  'D': 3, 'E': 3, 'F': 3,
				  'G': 4, 'H': 4, 'I': 4,
				  'J': 5, 'K': 5, 'L': 5,
				  'M': 6, 'N': 6, 'O': 6,
				  'P': 7, 'Q': 7, 'R': 7, 'S': 7,
				  'T': 8, 'U': 8, 'V': 8,
				  'W': 9, 'X': 9, 'Y': 9, 'Z': 9}

answer = len(input_string)
for word in input_string:
	answer += telephone_dict[word]

print(answer)
