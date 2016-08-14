import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number")
args = parser.parse_args()


def sum_three_five(number):

	number = int(number)
	total = 0

	for i in range(0, number):
		if i % 3 == 0 or i % 5 == 0:
			total += i
			
	print(total)		
	

sum_three_five(args.number)

