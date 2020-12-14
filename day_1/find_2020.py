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

def iteration_sum(int_li, K):
	return [pair for pair in combinations(int_li, 2) if sum(pair) == K]

def multiply_pair(x, y):
	return x*y

def main():
	text_string = read_input()
	int_list = convertStringtoInt(text_string)
	pairs = iteration_sum(int_list, 2020)
	result = multiply_pair(pairs[0][0], pairs[0][1])
	print(result)

if __name__ == "__main__":
	main()

