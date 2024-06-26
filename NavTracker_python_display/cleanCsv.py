import csv,tqdm,os

my_file_name = "some.csv"
cleaned_file = "cleansome.csv"
remove_words = [";"]

with open(my_file_name, 'r', newline='\n') as infile, open(cleaned_file, 'w',newline='\n') as outfile:
	writer = csv.writer(outfile)
	for line in csv.reader(infile, delimiter=';'):
		if not any(remove_word in line for remove_word in remove_words):
			writer.writerow(line)
