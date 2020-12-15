def read_input():
	with open('day_2_data.txt', 'r') as file:
		data = file.read().replace('\n', ',')
	return data

def convertStringtoList(string_data):
	li = list(string_data.split(','))
	return li

def convertsubstringstosublist(string_list):
	new_set = {sub.replace(':', '').replace(' ', ',') for sub in string_list}
	final_list = []
	for substring in new_set:
		substring = list(substring.split(','))
		final_list.append(substring)
	return final_list

def limitations(string_list):
	for substring in string_list:
		newsubstring = list(substring[0].split('-'))
		substring[0] = newsubstring
	return string_list

# first num = at least has it; second num = at most has it
def check_validity_partONE(list_set):
	valid = []
	for set in list_set:
		if set[2].count(set[1]) >= int(set[0][0]) and set[2].count(set[1]) <= int(set[0][1]):
			valid.append(True)
		else:
			valid.append(False)
	return valid

# exactly one of the positions matches the letter
def check_validity_partTWO(list_set):
	valid = []
	for set in list_set:
		pos1 = int(set[0][0])-1
		pos2 = int(set[0][1])-1
		if set[2][pos1] == set[1] and set[2][pos2] == set[1]:
			valid.append(False)
		elif set[2][pos1] != set[1] and set[2][pos2] != set[1]:
			valid.append(False)
		else:
			valid.append(True)
	return valid

def main():
	text_string = read_input()
	string_list = convertStringtoList(text_string)
	listwithinlist = convertsubstringstosublist(string_list)
	list_ = limitations(listwithinlist)
	# passwords = check_validity_partONE(list_)
	passwords = check_validity_partTWO(list_)
	counter = 0
	for valid in passwords:
		if valid is True:
			counter = counter + 1
		else:
			pass
	print(counter)

if __name__ == "__main__":
	main()

