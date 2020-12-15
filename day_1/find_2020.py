from itertools import combinations 

def read_input():
	with open('day_1_data.txt', 'r') as file:
		data = file.read().replace('\n', ',')
	return data

def convertStringtoInt(string_data):
	li = list(string_data.split(','))
	for i in range(len(li)):
		li[i] = int(li[i])
	return li

def iteration_sum(nums, int_li, K):
	return [pair for pair in combinations(int_li, nums) if sum(pair) == K]

def multiply_pair(x, y):
	return x*y

def multiply_three(x, y, z):
	return x*y*z

def main():
	text_string = read_input()
	int_list = convertStringtoInt(text_string)
	#pairs = iteration_sum(2, int_list, 2020)
	triple = iteration_sum(3, int_list, 2020)
	#result1 = multiply_pair(pairs[0][0], pairs[0][1])
	#print(result)
	result2 = multiply_three(triple[0][0], triple[0][1], triple[0][2])
	print(result2)

if __name__ == "__main__":
	main()
